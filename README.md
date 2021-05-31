# 企画書

## メンバー
- [s19003 上原功也](https://github.com/s19003/Graduation_Task.git)
- [n20006 金城岳見](https://github.com/n20006/GraduationTask)
- [n20010 佐谷公紀](https://github.com/n20010/GraduationTask)

## 現状分析
- コロナ情勢化でイベント、個人の配信が増えている
    - 配信画面にコメントを流して視聴者を盛り上げられないか
    - ローカルで直接ソースコードを触るのは技術的に難しい、
        ターゲット毎に違うサービスを使わないといけないのはレイアウトの調整面で不向き


## 企画の目的
- Youtube,Twitch,Twitter等に寄せられるコメントを配信画面に流して視聴者の満足度をより高めたい
- これだけで複数のプラットフォームからコメントを取得,htmlソースを生成できるwebアプリケーションを制作

### 実装したい機能
- 本アプリで生成したコメントをOBSにhtmlソースでインプットできる
- ユーザーが選んだプラットフォームからイベント、配信に関するコメントを取得できる
- コメントの頭に取得元のプラットフォームのロゴを載せる
- 取得したコメントのレイアウトをプリセットから選べる
- ユーザーのアカウントにお気に入りのプリセットを登録できる



### スケジュール
- 6月 企画確定、各自勉強
- 7~8月 プロトタイプ制作、機能テスト、バックエンド環境構築
- 9~10月 レイアウト実装、結合テスト
- 11~12月 最終チェック、プレゼン完成


## 企画の具体的な環境
- バックエンドは各メンバーで異なる言語で作成し、完成後にそれぞれの速度を比較する
  (比較用サイト: [GTmetrix](https://gtmetrix.com/))
- 各バックエンドでコメントを取得、整形後フロントにJsonデータを送る
- フロントはHTML&CSS, Javasript(担当:s19003上原功也)で作成されたものを
  それぞれ各バックエンドに合わせて修正して利用。デザインや機能は統一する。

### node.js兼フロント担当
[s19003 上原功也](https://github.com/s19003/Graduation_Task.git)
#### 環境
- node.js
- AWS

### AWSLambda担当
[n20006 金城岳見](https://github.com/n20006/GraduationTask)  
#### 環境
- AWSLambda
- python3

### Ruby on rails担当
[n20010 佐谷公紀](https://github.com/n20010/GraduationTask)
#### 環境
- Ruby on rails6
- AWS


### 必要機能(関数レベル)
- select-platform 使うプラットフォームを選ぶ
- get-twitter-comment twitterのコメントを取得する
- get-youtube-comment youtubeのコメントを取得する
- get-twitch-comment twitchのコメントを取得する
- select-layout 流すコメントのレイアウトを選ぶ

