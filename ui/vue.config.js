var HardSourceWebpackPlugin = require('hard-source-webpack-plugin');

module.exports = {
  transpileDependencies: ["vuetify"],
  configureWebpack: {
    devServer: {
      watchOptions: {
        ignored: /node_modules/,
        poll: true
      }
    },
    optimization:{
      chunkIds: 'named'
    },
    plugins: [
        new HardSourceWebpackPlugin({
          configHash: function(webpackConfig){
            return 'test'
          }
        })
    ]
  }
};
