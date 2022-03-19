const express = require('express')
const routes = require('./routes')
const morgan = require('morgan')
const bodyParser = require('body-parser')
const helmet = require('helmet')
const cors = require('cors')
const CookieParser = require('cookie-parser')
const config = require('./config')
// const { sequelize } = require('./models')
const fs = require('fs')
const https = require('https')
const path = require('path')

const app = express()




// log all the connection information
app.use(morgan('combined'))
//app.use(bodyParser.urlencoded({ extended: false }))

// enable parsing json from requests
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({ extended: true }))

// to extract cookies from request
app.use(CookieParser())
// for security
// app.use(helmet())
app.use(express.static(path.join(__dirname,'..','..','client2','dist')))
app.get('*', (req, res) => {
  res.sendFile(
    path.join(__dirname, '..', '..', 'client2', 'dist', 'index.html')
  )
})

// allows connection from any origin + cookies
app.use(cors({ credentials: false, origin: config.frontend.url }))
// app.use(cors())



routes(app)

console.log('mode', process.env.NODE_ENV || 'develop')
app.listen(config.backend.port, () => {
  console.log('now listening on port ' + config.backend.port)
})

