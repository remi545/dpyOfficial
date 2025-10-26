from dotenv import load_dotenv

load_dotenv()

import os
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from contextlib import asynccontextmanager

from .db import init_db, close_db
from .api import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield
    await close_db()


app = FastAPI(
    lifespan=lifespan,
    title="DPY Official API",
    description="ギタリスト「DPY」の公式サイトAPI",
    version="1.0.0",
)

# APIルーターを登録（/apiプレフィックス）
app.include_router(router)

# 静的ファイルディレクトリのパス
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "static"))


# === 例外ハンドラー ===
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    """HTTPエラー処理: APIは通常のエラーレスポンス、それ以外はVue Routerにフォールバック"""
    # API呼び出しの404エラーは通常のJSONエラーを返す
    if request.url.path.startswith("/api"):
        return JSONResponse(
            status_code=exc.status_code,
            content={"error": exc.detail, "code": exc.status_code},
        )
    
    # Vue Router対応: 404の場合はindex.htmlを返す
    if exc.status_code == 404 and os.path.isdir(static_dir):
        index_path = os.path.join(static_dir, "index.html")
        if os.path.isfile(index_path):
            return FileResponse(index_path)
    
    # その他のHTTPエラー
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail, "code": exc.status_code},
    )


@app.exception_handler(Exception)
async def internal_exception_handler(request: Request, exc: Exception):
    """内部エラー処理"""
    return JSONResponse(
        status_code=500,
        content={"error": "Internal Server Error", "code": 500},
    )


# === 静的ファイル配信 ===
# assetsフォルダは直接配信
if os.path.isdir(static_dir):
    assets_dir = os.path.join(static_dir, "assets")
    if os.path.isdir(assets_dir):
        app.mount("/assets", StaticFiles(directory=assets_dir), name="assets")


# Vue Routerのフォールバック: 全ての非APIルートをindex.htmlへ
@app.get("/{full_path:path}")
async def spa_fallback(full_path: str):
    """
    SPAフォールバック: 
    - /api/* は404エラー（未定義のAPIエンドポイント）
    - 実在する静的ファイルはFileResponseで配信
    - それ以外はindex.htmlを返す（Vue Routerに委譲）
    """
    # API呼び出しは404エラー
    if full_path.startswith("api/") or full_path == "api":
        raise StarletteHTTPException(status_code=404, detail="API endpoint not found")
    
    # 静的ファイルの直接配信を試みる
    if os.path.isdir(static_dir):
        file_path = os.path.join(static_dir, full_path)
        if os.path.isfile(file_path):
            return FileResponse(file_path)
        
        # index.htmlへフォールバック（Vue Router用）
        index_path = os.path.join(static_dir, "index.html")
        if os.path.isfile(index_path):
            return FileResponse(index_path)
    
    # 静的ファイルが存在しない場合は404
    raise StarletteHTTPException(status_code=404, detail="Not Found")

# --- デバッグ用: main.pyを直接実行した場合にサーバー起動 ---
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
