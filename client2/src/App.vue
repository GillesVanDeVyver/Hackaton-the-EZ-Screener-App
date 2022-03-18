<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      {{text}}
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import Dataservice from './services/Dataservice'
export default {
  name: 'App',

  data: () => ({
    text: ''
  }),
  methods: {
    async getText() {
      let res = await Dataservice.getTestMessage()
      console.log(res)
      return res.data
    }
  },
  async mounted() {
    this.text = await this.getText()
  }
}
</script>
