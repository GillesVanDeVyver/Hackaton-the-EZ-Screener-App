import axios from '../plugins/axios'

export default {
  async getTestMessage() {
    return axios.get('/')
  },
  async getCompanyData(companyName) {
    return axios.get('/company-data', {
      params: {
        companyName
      }
    })
  }
}
