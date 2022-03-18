<template>
  <v-container >
    <h1>Information for {{getCompany}}</h1>
    <h3>{{companyData?companyData:'Data Loading'}}</h3>
  </v-container>
</template>

<script>
import Dataservice from '../services/Dataservice'
export default {
  name: 'Home',
  data: () => ({
    companyName: '',
    companyData: {},
    loader: false
  }),
  methods: {
    async startCompanySearch(companyName) {
      this.loader = true
      this.companyData = (await Dataservice.getCompanyData(companyName)).data
      this.loader = false
    },
    startLoadingBar() {

    },
    stopLoadingBar() {

    }
  },
  async mounted() {
    this.companyName = this.getCompany
    this.startCompanySearch(this.companyName)
  },
  computed: {
    getCompany() {
      return this.$route.params.company
    }
  },
  watch: {
    getCompany(val) {
      this.startCompanySearch(val)
    }
  }
}
</script>
