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
├─ infra/            # Dockerfile, docker-compose.yml, k8s など
├─ docs/             # 要件定義書、設計書、運用ドキュメント
└─ README.md
```

---

## 技術スタック

- Backend: Python 3.13、FastAPI
- ASGI サーバ: Uvicorn
- ORM / DB: SQLAlchemy / SQLModel / asyncpg + PostgreSQL
- Migrations: Alembic
- Frontend: Vue 3 + TypeScript
- Build: Vite
- Styling: Tailwind CSS
- Container: Docker / docker-compose
- Tests: pytest（バックエンド）、Vitest（フロントエンド）
- Lint/Format: ruff/black/isort（Python）、ESLint/Prettier（TS）
- CI: GitHub Actions

---

## 開発環境 / 起動方法

メモ: `frontend` と `backend` の雛形を追加した後に、具体的な起動手順（クイックスタート）を README に追記します。

---

## マイグレーション

メモ: マイグレーションには Alembic を使います。マイグレーションの初期化・実行手順は backend の雛形を作成後に記載します。

---

## CI / CD（検討中）

- 推奨ワークフロー（GitHub Actions 例）:
  - pull request / push: lint → build → test（フロント/バック両方。テストは将来追加）
  - main/release ブランチ: イメージビルド → コンテナレジストリへプッシュ → デプロイ（本番環境）
  - セキュリティスキャンや依存関係のアラートを組み込むと安全性が向上します。

テンプレートは `.github/workflows/` に雛形を置き、CI の段階的強化（テスト追加、E2E、コードカバレッジ）を進めていきます。

---

## デプロイ

メモ: 本番デプロイはコンテナイメージを用いて行います。詳細なクラウド選定・インフラ構成（例: GCP, AWS, Fly.io, DigitalOcean）は要件確定後に決定します。
