const Scraper = require('../services/Scraper')

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
}