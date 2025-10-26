# Public Assets

このディレクトリにはビルド時にルートにコピーされる静的ファイルを配置します。

## OGP画像について

`ogp-image.jpg` を配置してください。

### 推奨サイズと仕様
- **サイズ**: 1200 x 630 px
- **フォーマット**: JPG, PNG
- **ファイルサイズ**: 1MB以下推奨
- **内容**: DPYのロゴ、アーティスト写真、またはブランドイメージ

### 画像の配置方法
1. 1200x630pxの画像を用意
2. このディレクトリに `ogp-image.jpg` として保存
3. ビルドコマンドを実行（`npm run build`）

**注意**: 現在 `ogp-image.svg` がプレースホルダーとして配置されていますが、DiscordやTwitterなどのSNSはJPG/PNG形式を推奨しています。実際の `ogp-image.jpg` を用意して置き換えてください。

### その他の推奨ファイル
- `favicon.svg` または `favicon.ico`: サイトのファビコン
- `robots.txt`: 検索エンジン向けの指示ファイル

## 参考
- [Open Graph Protocol](https://ogp.me/)
- [Twitter Cards](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards)
