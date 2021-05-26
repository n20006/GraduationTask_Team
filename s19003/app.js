const express = require('express')

const app = express()
const port = 3000

app.use(express.static('public'))
app.use(express.json())
app.use(express.urlencoded({ extended: true }))

// POST
app.post('/', (req, res) => {
  res.send(req.body)
})

// サーバーを起動する処理
app.listen(port, () => {
  console.log(`http://localhost:${port}`)
})
