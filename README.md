# 企画書

## メンバー
- [s19003 上原功也](https://github.com/s19003/Graduation_Task.git)
- [n20006 金城岳見](https://github.com/n20006/GraduationTask)
- [n20010 佐谷公紀](https://github.com/n20010/GraduationTask)

## 現状分析
コロナ情勢化でイベント、個人の配信が増えている
 →  コメントを画面に流してもっと盛り上げたい
 →  技術的に難しい、ターゲット毎に違うサービスを使わないといけないのは面倒

## 企画の目的
- TwitterやYoutube,Twitchなど様々なプラットフォームから取得したコメントを配信に流すソースを生成するwebアプリケーションを制作

## 企画の具体的な内容
３種類のバックエンドで構成するWebアプリケーション

### node.js兼フロント担当
[s19003 上原功也](https://github.com/s19003/Graduation_Task.git)
#### 環境
- node.js

### AWSLambda担当
[n20006 金城岳見](https://github.com/n20006/GraduationTask)  
- AWSLambda
- python3

### Ruby on rails担当
[n20010 佐谷公紀](https://github.com/n20010/GraduationTask)
#### 環境
- Ruby on rails6


### 実装したい機能
- 本アプリで生成したコメントをOBSにブラウザソースでインプットできる
- ユーザーが選んだプラットフォームからコメントをAPI等で取得できる
- 取得したコメントのレイアウトをプリセットから選べる
- ユーザーのアカウントに各プラットフォームのアカウント情報やお気に入りのプリセットを登録できる
