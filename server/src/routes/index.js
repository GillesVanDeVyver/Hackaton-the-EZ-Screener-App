

module.exports = (app) => {
  app.get('/', (req, res) => {
    res.send('hello there')
  })

  app.get('/company-data', (req, res) => {
    console.log(req)
    res.send( `${req.query.companyName} is now your friend`)
  })
}