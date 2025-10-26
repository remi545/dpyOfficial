# DPY公式サイト DB定義書

## 概要
本サイトで使用する主なコレクション設計を記載します。
データベース: **MongoDB**

## コレクション一覧
- lives（ライブ情報）
- discs（ディスコグラフィー）
- news（ニュース）
- gallery（ギャラリー）

---

### lives（ライブ情報）
MongoDBコレクション: `lives`

|フィールド名|型|必須|説明|
|---|---|---|---|
|_id|ObjectId|自動|ライブID（MongoDB自動生成）|
|date|Date|○|開催日|
|title|String|○|タイトル|
|venue|String|○|会場|
|description|String||詳細|
|created_at|Date|○|登録日時|

**インデックス:**
- `date` (降順) - 日付での検索・ソート用
- `created_at` (降順) - 最新情報取得用

---

### discs（ディスコグラフィー）
MongoDBコレクション: `discs`

|フィールド名|型|必須|説明|
|---|---|---|---|
|_id|ObjectId|自動|音源ID（MongoDB自動生成）|
|title|String|○|タイトル|
|release_date|Date||リリース日|
|type|String|○|種別（CD/配信/動画等）|
|link|String||配信・動画リンク|
|created_at|Date|○|登録日時|

**インデックス:**
- `release_date` (降順) - リリース日での検索・ソート用
- `type` - 種別でのフィルタリング用

---

### news（ニュース）
MongoDBコレクション: `news`

|フィールド名|型|必須|説明|
|---|---|---|---|
|_id|ObjectId|自動|ニュースID（MongoDB自動生成）|
|title|String|○|タイトル|
|body|String|○|本文|
|published_at|Date|○|公開日|
|created_at|Date|○|登録日時|

**インデックス:**
- `published_at` (降順) - 公開日での検索・ソート用
- `created_at` (降順) - 最新情報取得用

---

### gallery（ギャラリー）
MongoDBコレクション: `gallery`

|フィールド名|型|必須|説明|
|---|---|---|---|
|_id|ObjectId|自動|ギャラリーID（MongoDB自動生成）|
|type|String|○|種別（写真/動画）|
|title|String||タイトル|
|url|String|○|ファイルURL|
|created_at|Date|○|登録日時|

**インデックス:**
- `type` - 種別でのフィルタリング用
- `created_at` (降順) - 最新情報取得用

---

## データモデリングの特徴

### MongoDB利用の利点
- **スキーマレス**: 必要に応じてフィールドを追加可能
- **ドキュメント指向**: JSONライクな構造で直感的
- **スケーラビリティ**: 水平スケーリングに対応
- **柔軟なクエリ**: 複雑な検索条件に対応

### 設計方針
- 各コレクションは基本的に独立（リレーションなし）
- 必要に応じて埋め込みドキュメントまたは参照を使用
- `_id`フィールドはMongoDBが自動生成するObjectId
- 日付型は`Date`型を使用（ISO 8601形式）
- インデックスは実際のクエリパターンに応じて最適化

---

## 移行メモ

### PostgreSQLからの主な変更点
1. **PRIMARY KEY** → `_id` (ObjectId)
2. **INTEGER型のID** → ObjectId（12バイトの一意識別子）
3. **DATE/TIMESTAMP** → Date型
4. **NOT NULL制約** → Pydanticモデルで必須フィールド定義
5. **外部キー** → なし（元々独立テーブルのため影響なし）

### データ型マッピング
| PostgreSQL | MongoDB |
|---|---|
| INTEGER (id) | ObjectId (_id) |
| TEXT | String |
| DATE | Date |
| TIMESTAMP | Date |
