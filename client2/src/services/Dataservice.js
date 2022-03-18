import axios from '../plugins/axios'

export default {
  async getTestMessage() {
    return axios.get('/')
  },
}
