<template>
  <v-container fluid>
    <v-text-field
        label="company name"
        placeholder="KBC"
        v-model="company"
        required
        @keydown.enter="searchCompany"
    ></v-text-field>
    <v-btn @click="searchCompany">Search</v-btn>
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
      this.$router.push(`/company/${this.company}`) //TODO is url encode needed
    }
  }
}
</script>
