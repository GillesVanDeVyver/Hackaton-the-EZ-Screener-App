let data = {}
if(process.env.NODE_PC === 'production') {
  data = {
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
data = {
    backend: {
      url: 'http://localhost:3000',
        port: 3000,
    },
    frontend: {
      url: 'http://localhost:8081',
    },
  }
}

export default data


