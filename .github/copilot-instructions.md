# Copilot Instructions - DPY Official Website

## プロジェクト概要
ギタリスト「DPY」の公式サイト。詳細は`README.md`参照。

## 技術スタック
- **Backend**: FastAPI (Python 3.13) + MongoDB (Beanie ODM)
- **Frontend**: Vue 3 + TypeScript + Vite + Tailwind CSS
- **Container**: Docker Compose

## コーディング規約

### Python (Backend)
- 型ヒント必須（`from typing import`活用）
- async/await使用（Beanie ODM、FastAPI）
- Linter: ruff, black, isort
- Pydanticモデルでバリデーション
- APIエンドポイントは`app/api.py`に集約

### TypeScript (Frontend)
- Composition API使用（`<script setup lang="ts">`）
- 型定義は`src/types/`に配置
- Linter: ESLint, Prettier
- コンポーネントはPascalCase

## ディレクトリ構造
```
backend/app/     # FastAPIアプリ (main.py, api.py, db.py, models.py)
frontend/src/    # Vueアプリ (components/, types/)
doc/             # 設計書 (requirements.md, db_schema.md, screens/)
```

## 重要な参照先
- **DB設計**: `doc/db_schema.md` (MongoDB コレクション定義)
- **要件**: `doc/requirements.md`
- **画面仕様**: `doc/screens/` 配下
- **環境構築**: `README.md`

## コード生成時の注意
- MongoDB ObjectIdは`from beanie import PydanticObjectId`
- 既存のモデル(`app/models.py`)を参照
- エラーハンドリングは`app/main.py`のハンドラー参照
- 既存APIルート(`app/api.py`)との整合性確認
- Vue componentsは既存構造(`components/layout/`, `components/cards/`等)に従う
