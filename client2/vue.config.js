module.exports = {
  transpileDependencies: ['vuetify'],
  pwa: {
    name: 'Company Analyser',
    themeColor: '#4DBA87',
    msTileColor: '#000000',
    appleMobileWebAppCapable: 'yes',
    appleMobileWebAppStatusBarStyle: 'black',

    // configure the workbox plugin
    workboxPluginMode: 'GenerateSW',
    workboxOptions: {
      // cleanupOutdatedCaches: true,
      skipWaiting: true
    }
  }
}
