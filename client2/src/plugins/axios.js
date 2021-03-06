import Vue from 'vue'
import config from '../config'
// @ts-ignore
import axios from 'axios'

const ax = axios.create({
  baseURL: config.backend.url, // axios sends request to express Rest endpoint in the server
  withCredentials: false,
  headers: {
    'Access-Control-Allow-Origin': config.frontend.url,
  },
  //httpsAgent: new https.Agent({ rejectUnauthorized: false })
})
Vue.prototype.$axios = ax

export default ax
