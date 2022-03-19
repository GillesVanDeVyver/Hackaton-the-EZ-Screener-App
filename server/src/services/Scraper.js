const {spawn} = require('child_process');

module.exports = {
  async getCompanyInfo(companyName) {
    return new Promise((resolve, reject) => {
      if(true) {
        const python = spawn('python', ['../functions.py', `${companyName}`]);
        let response = ''
        // collect data from script
        python.stdout.on('data', function (data) {
          console.log(`Python Data: ${data}`)
          response += data
        });
        python.stderr.on('data', function(data)  {
          console.log(`Python error: ${data}`)
        })
        // in close event we are sure that stream from child process is closed
        python.on('close', (code) => {
          console.log(`Python closed with exit code ${code}`)
          // send data to browser
          let resp = response.match("JSON-DATA\\n(.*?)\\n")[1]
          resp = JSON.stringify(JSON.parse(resp))
          resolve(resp)
        });
      } else {
        resolve({
          rating:Math.round(Math.random()*10),
          grossIncome: {
            data: [10, 30, 40, 40, 20, 10],
            labels: [2011, 2012, 2013, 2014, 2016, 2017],
            dataType: 'M$'
          },
          employeeCount: {
            data: [10, 30, 40, 40, 20, 10],
            labels: [2011, 2012, 2013, 2014, 2016, 2017]
          }
        })
      }
    })

  }
}