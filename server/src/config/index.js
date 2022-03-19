
if(process.env.NODE_PC === 'stylify') {
  module.exports = {
    backend: {
      url: 'http://stylify.duckdns.org:3050',
      port: 3050
    },
    frontend: {
      url: 'http://stylify.duckdns.org:3050',
      port: 3050
    },
  }
} else {
  module.exports = {
    backend: {
      url: 'http://localhost:3000',
      port: 3000
    },
    frontend: {
      url: 'http://localhost:8081',
      port: 8081
    },
  }
}


