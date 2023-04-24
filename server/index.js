const fetch = require('node-fetch');
const express = require('express')
const app = express()
const { base64encode, base64decode } = require('nodejs-base64');

app.get('/', function (req, res) {
  base64decode(req.query.str)
})

app.listen(5000)
