from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.api.routes import router
from app.core.config import get_settings, BASE_DIR
from app.core.logging import configure_logging
from app.services.audit import init_db
import logging

logger = logging.getLogger(__name__)


configure_logging()
settings = get_settings()
init_db()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Render free has no persistent disk: rebuild the FAISS index on boot
    # when it is missing (costs 1 tiny embedding call for the sample KB).
    try:
        index_file = Path(settings.faiss_index_dir) / "index.faiss"
        if not index_file.exists():
            from app.core.keypool import google_keys

            if google_keys():
                from app.services.ingestion import load_file, chunk_documents
                from app.rag.vectorstore import add_documents

                docs = []
                for path in Path(settings.sample_kb_dir).iterdir():
                    if path.is_file():
                        docs.extend(load_file(path))
                add_documents(chunk_documents(docs))
                logger.info("Boot ingest complete: FAISS index rebuilt")
            else:
                logger.warning("No GOOGLE_API_KEYS set - skipping boot ingest")
    except Exception as exc:
        logger.warning("Boot ingest failed (app still serving): %s", exc)
    yield


app = FastAPI(title=settings.app_name, version="1.0.0", lifespan=lifespan)

app.include_router(router)
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request, "app_name": settings.app_name},
    )
