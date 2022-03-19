const Scraper = require('../services/Scraper')
const path = require("path");
const express = require("express");

module.exports = (app) => {
  app.get('/', (req, res) => {
    res.send('hello there')
  })

  app.get('/company-data', async (req, res) => {
    Scraper.getCompanyInfo(req.query.companyName).then(data => {
      res.json(data)
    })
    // res.send( `${req.query.companyName} is now your friend`)
  })
  app.use(express.static(path.join(__dirname,'..','..','..','client2','dist')))
  app.get('*', (req, res) => {
    res.sendFile(
      path.join(__dirname, '..', '..','..', 'client2', 'dist', 'index.html')
    )
  })
}