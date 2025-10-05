# DPY公式サイト DB定義書

## 概要
本サイトで使用する主なテーブル設計を記載します。

## テーブル一覧
- lives（ライブ情報）
- discs（ディスコグラフィー）
- news（ニュース）
- gallery（ギャラリー）

---

### lives（ライブ情報）
|項目名|型|制約|説明|
|---|---|---|---|
|id|INTEGER|PRIMARY KEY|ライブID|
|date|DATE|NOT NULL|開催日|
|title|TEXT|NOT NULL|タイトル|
|venue|TEXT|NOT NULL|会場|
|description|TEXT||詳細|
|created_at|TIMESTAMP|NOT NULL|登録日時|

### discs（ディスコグラフィー）
|項目名|型|制約|説明|
|---|---|---|---|
|id|INTEGER|PRIMARY KEY|音源ID|
|title|TEXT|NOT NULL|タイトル|
|release_date|DATE||リリース日|
|type|TEXT|NOT NULL|種別（CD/配信/動画等）|
|link|TEXT||配信・動画リンク|
|created_at|TIMESTAMP|NOT NULL|登録日時|

### news（ニュース）
|項目名|型|制約|説明|
|---|---|---|---|
|id|INTEGER|PRIMARY KEY|ニュースID|
|title|TEXT|NOT NULL|タイトル|
|body|TEXT|NOT NULL|本文|
|published_at|DATE|NOT NULL|公開日|
|created_at|TIMESTAMP|NOT NULL|登録日時|

### gallery（ギャラリー）
|項目名|型|制約|説明|
|---|---|---|---|
|id|INTEGER|PRIMARY KEY|ギャラリーID|
|type|TEXT|NOT NULL|種別（写真/動画）|
|title|TEXT||タイトル|
|url|TEXT|NOT NULL|ファイルURL|
|created_at|TIMESTAMP|NOT NULL|登録日時|

## ER図イメージ
- 各テーブルは基本的に独立（外部キーなし）
- 必要に応じて関連付けを追加
