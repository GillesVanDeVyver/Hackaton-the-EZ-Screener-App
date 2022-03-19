<template>
  <v-container >
    <h1>Information for <b>{{getCompany}}</b></h1>
    <h3>{{companyData?(companyData.message?companyData.message:'Source Indeed.com'):'Data Loading'}}</h3>
    <v-progress-circular
        v-if="loader"
        indeterminate
        color="primary"
    ></v-progress-circular>
    <v-card v-if="companyData && companyData.score"
            class="mx-auto my-12"
            max-width="450"
            color="#385F73"
            dark>
      <v-card-title>
        Rating {{companyData.score}}/10
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

    <v-card v-if="companyData && companyData.result_neg"
            class="mx-auto my-12"
            max-width="450"
            color="red"
            dark>
      <v-card-title>
        Most negative reviews
      </v-card-title>
      <v-card-text>
        <v-list>
          <v-list-item :key="rev.id" v-for="rev of companyData.result_neg">
            {{rev.rev}}
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>

    <v-card v-if="companyData && companyData.result_pos"
            class="mx-auto my-12"
            max-width="450"
            color="green"
            dark>
      <v-card-title>
        Most Positive reviews
      </v-card-title>
      <v-card-text>
        <v-list>
          <v-list-item :key="rev.id" v-for="rev of companyData.result_pos">
            {{rev.rev}}
          </v-list-item>
        </v-list>
      </v-card-text>
    </v-card>

    <v-card v-if="companyData && companyData.score_list"
            class="mx-auto my-12"
            max-width="450"
            color="#cccccc"
            dark>
      <v-card-title>
        Score Distribution
      </v-card-title>
      <v-card-text>
        <BarChart title="Score Distribution" data-type="" :chartData=companyData.score_list :labels="[1,2,3,4,5,6,7,8,9,10]"></BarChart>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import Dataservice from '../services/Dataservice'
import ProfitChart from '../components/ProfitChart'
import BarChart from '../components/BarChart'

export default {
  name: 'Home',
  components: {
    ProfitChart,
    BarChart
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
      this.companyData = JSON.parse((await Dataservice.getCompanyData(companyName)).data)
      this.companyData.result_neg = this.companyData.result_neg.map((rev,i) => ({rev:rev,id:i}))
      this.companyData.result_pos = this.companyData.result_pos.map((rev,i) => ({rev:rev,id:i}))
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
      return this.companyData.score * 10
    }
  },
  watch: {
    getCompany(val) {
      this.startCompanySearch(val)
    }
  }
}
</script>
