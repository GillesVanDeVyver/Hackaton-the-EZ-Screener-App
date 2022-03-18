<template>
  <v-app>
    <v-app-bar
        color="blue accent-3"
        dense
        dark
        hide-on-scroll
    >
      <v-app-bar-nav-icon></v-app-bar-nav-icon>

      <v-toolbar-title>Company analysis tool</v-toolbar-title>



      <v-spacer></v-spacer>
      <v-btn icon v-if="showSearchBar" @click="searchCompany">
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <v-text-field v-if="showSearchBar"
                    v-model="companyName"
                    solo hide-details single-line
                    required
                    @keydown.enter="searchCompany"></v-text-field>
      <v-btn icon v-if="showSearchBar" @click="showSearchBar = false">
        <v-icon>mdi-cancel</v-icon>
      </v-btn>
      <v-btn icon @click="searchBox" v-if="!showSearchBar">
        <v-icon>mdi-magnify</v-icon>
      </v-btn>


    </v-app-bar>

    <v-main>
      <v-container>
      <router-view />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
import Dataservice from './services/Dataservice'
export default {
  name: 'App',

  data: () => ({
    text: '',
    companyName: '',
    showSearchBar: false
  }),
  methods: {
    async getText() {
      let res = await Dataservice.getTestMessage()
      console.log(res)
      return res.data
    },
    searchBox() {
      this.showSearchBar = !this.showSearchBar
    },
    searchCompany() {
      this.$router.push(`/company/${this.companyName}`) //TODO is url encode needed
      this.showSearchBar = false
    }
  },
  async mounted() {
    this.text = await this.getText()
  }
}
</script>
