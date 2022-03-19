<template>
  <v-container >
    <h1>Information for <b>{{getCompany}}</b></h1>
    <h3>{{companyData?(companyData.message?companyData.message:'No messages'):'Data Loading'}}</h3>
    <v-card v-if="companyData && companyData.rating"
            class="mx-auto my-12"
            max-width="450"
            color="#385F73"
            dark>
      <v-card-title>
        Rating {{companyData.rating}}/10
      </v-card-title>
      <v-card-text>
        <!--<v-rating

            v-model="companyData.rating"
            :length="5"
            color="red lighten-3"
            background-color="grey lighten-1"
            :readonly="true"
            :size="18"
        ></v-rating>-->
        <v-progress-circular
            :rotate="-90"
            :size="100"
            :width="15"
            :value="scaledRating"
            color="red"
        >
          {{ companyData.rating }}
        </v-progress-circular>
      </v-card-text>

    </v-card>

    <v-card v-if="companyData && companyData.grossIncome"
            class="mx-auto my-12"
            max-width="450"
            color="#97c20c"
            dark>
      <v-card-title>
        Gross Income
      </v-card-title>
      <v-card-text>
        <!--<v-rating

            v-model="companyData.rating"
            :length="5"
            color="red lighten-3"
            background-color="grey lighten-1"
            :readonly="true"
            :size="18"
        ></v-rating>-->
        <ProfitChart title="Gross Profit"
                     :chartData="companyData.grossIncome.data"
                     :labels="companyData.grossIncome.labels"
                      :data-type="companyData.grossIncome.dataType">

        </ProfitChart>
      </v-card-text>

    </v-card>
  </v-container>
</template>

<script>
import Dataservice from '../services/Dataservice'
import ProfitChart from '../components/ProfitChart'
export default {
  name: 'Home',
  components: {
    ProfitChart
  },
  data: () => ({
    companyName: '',
    companyData: false,
    loader: false
  }),
  methods: {
    async startCompanySearch(companyName) {
      this.loader = true
      this.companyData = false
      this.companyData = (await Dataservice.getCompanyData(companyName)).data
      console.log('companyData')
      console.log(this.companyData)
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
    },
    scaledRating() {
      return this.companyData.rating * 10
    }
  },
  watch: {
    getCompany(val) {
      this.startCompanySearch(val)
    }
  }
}
</script>
