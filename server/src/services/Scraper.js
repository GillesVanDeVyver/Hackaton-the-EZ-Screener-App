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
          // let resp = response.replace('\r\n','')
          //   .replace('\n','')
          //   .match(/JSON-DATA(.*)/gm)
          let resp = response.split('JSON-DATA')[1]
          resp = JSON.stringify(JSON.parse(resp))
          resolve(resp)
        });
      } else {
        // resolve({
        //   rating:Math.round(Math.random()*10),
        //   grossIncome: {
        //     data: [10, 30, 40, 40, 20, 10],
        //     labels: [2011, 2012, 2013, 2014, 2016, 2017],
        //     dataType: 'M$'
        //   },
        //   employeeCount: {
        //     data: [10, 30, 40, 40, 20, 10],
        //     labels: [2011, 2012, 2013, 2014, 2016, 2017]
        //   }
        // })
        resolve('{"score_list":[5,0,3,1,1,1,6,8,24,47],"score":8,"result_pos":["Very Great work culture","fun work place with ping pong table","Working at KBC was a very great experience. Many of my work partners were nice and easy going, this made working at my department very calming to be fair. The competitive environment inspired me to work harder and make more sales. The treatment of staff was also amazing. Conversing with bosses was great, they were always open to help you with any situation at hand. Overall, working at KBC was by far my best place of employment"],"result_neg":["Uitdagende tijden","Uitdagende tijden","Uitdagende tijden"]}')
      }
    })

  }
}