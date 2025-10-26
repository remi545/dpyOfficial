# DPY Official Website

ギタリスト「DPY」の公式サイト用リポジトリです。コンテンツ公開、イベント情報、ディスコグラフィ、問い合わせ機能などを提供することを目的としたフルスタック Web アプリケーションを想定します。

## リポジトリ構成

```
/
├─ backend/          # FastAPI アプリケーション
│  ├─ app/
│  ├─ migrations/    # Alembic 等のマイグレーション定義
│  └─ requirements.txt
├─ frontend/         # Vue 3 + TypeScript (Vite)
│  ├─ src/
│  └─ package.json
├─ docs/             # 要件定義書、設計書、運用ドキュメント
└─ README.md
```

---

## 技術スタック

- Backend: Python 3.13、FastAPI
- ASGI サーバ: Uvicorn
- DB/ODM: MongoDB + Beanie（PyMongo Async API対応 ODM）
- Frontend: Vue 3 + TypeScript
- Build: Vite
- Styling: Tailwind CSS
- Container: Docker / docker-compose
- Tests: pytest（バックエンド）、Vitest（フロントエンド）
- Lint/Format: ruff/black/isort（Python）、ESLint/Prettier（TS）
- CI: GitHub Actions

---

## 開発環境 / 起動方法

### 必要なアプリ・ツール

- Python 3.13 以上（バックエンド用）
- Node.js 18 以上（フロントエンド用）
- npm（Node.jsに同梱）
- Docker / Docker Compose（コンテナ実行・開発用）
- VS Code（推奨IDE）
- Git（バージョン管理）

各アプリは公式サイトからインストールしてください。
VS Code には Python, ESLint, Prettier などの拡張機能を導入すると便利です。

### backend の仮想環境 (venv) 作成・実行手順（Windows）

1. backend ディレクトリに移動
2. venv を作成
3. VS Code 右下に「このフォルダーの仮想環境を有効化しますか？」と表示されたら「はい」を押す
4. 依存パッケージをインストール
5. FastAPI サーバを起動

```powershell
cd backend
python -m venv .venv
# （VS Code右下のメッセージで「はい」を押して仮想環境を有効化）
pip install -r requirements.txt
```

この手順で `.venv` 仮想環境が backend ディレクトリ内に作成され、依存パッケージ（fastapi, uvicorn など）がインストールされます。
APIサーバの起動は VS Code の launch.json を使ってください。
F5キーまたは「実行とデバッグ」→「FastAPI: Uvicorn (reload)」で起動できます。


### frontend の起動・デバッグ手順（Windows）

1. frontend ディレクトリに移動
2. 依存パッケージをインストール
3. 開発サーバを起動
4. ブラウザで http://localhost:5173 を開く

```powershell
cd frontend
npm install
npm run dev
```

VS Code でデバッグする場合は、
- 「実行とデバッグ」→「Vite: Dev Server」などのタスクを利用
- ソースマップ対応でブレークポイント可能

※初回は `npm install` で依存パッケージ（vue, vite, tailwindcss など）を必ずインストールしてください。

---

## CI / CD（検討中）

- 推奨ワークフロー（GitHub Actions 例）:
  - pull request / push: lint → build → test（フロント/バック両方。テストは将来追加）
  - main/release ブランチ: イメージビルド → コンテナレジストリへプッシュ → デプロイ（本番環境）
  - セキュリティスキャンや依存関係のアラートを組み込むと安全性が向上します。

テンプレートは `.github/workflows/` に雛形を置き、CI の段階的強化（テスト追加、E2E、コードカバレッジ）を進めていきます。

---

## デプロイ

メモ: 本番デプロイはルート直下のDockerfile/docker-compose.ymlを用いたコンテナイメージで行います。　　
詳細なクラウド選定・インフラ構成（例: GCP, AWS, Fly.io, DigitalOcean）は要件確定後に決定します。
