const {spawn} = require('child_process');

module.exports = {
  async getCompanyInfo(companyName) {
    return new Promise((resolve, reject) => {
      if(false) {
        const python = spawn('python', ['scriptname.py', `"${companyName}"`]);
        let response = ''
        // collect data from script
        python.stdout.on('data', function (data) {
          console.log(`Python Data: ${data}`)
          response += data
        });
        // in close event we are sure that stream from child process is closed
        python.on('close', (code) => {
          console.log(`Python closed with exit code ${code}`)
          // send data to browser
          resolve(response)
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