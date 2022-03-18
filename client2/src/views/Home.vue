<template>
  <v-container center>
    <v-text-field
        label="Regular"
        placeholder="Placeholder"
        v-model="company"
        required
        @keydown.enter="searchCompany"
    ></v-text-field>
    <v-btn @click="searchCompany">Search<v-btn>
  </v-container>
</template>

<script>

export default {
  name: 'Home',
  data :() => ({
    company: ''
  }),
  components: {

  },
  methods: {
    searchCompany() {
      this.$router.push(`/company/${this.company.urlencoded}`) //TODO is url encode needed
    }
  }
}
</script>
