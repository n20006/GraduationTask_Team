/* モジュール */
const http = require("http");

/* 変数 */
const port = 3000;
const hostname = "127.0.0.1";

/* HTTPサーバーを作成する */
const server = http.createServer();

server.on("request", (req, res) => {
  // ステータスコード200でHTMLレスポンスヘッダを出力する
  res.statusCode = 200;

  res.setHeader("Content-Type", "text/plain");

  res.write("URL:" + req.url + "\n");

  res.end();
});

/* サーバーを実行する */
server.listen(port, hostname);
