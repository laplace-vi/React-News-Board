"use strict";

var webpack = require('webpack');
var path = require('path');
var HtmlwebpackPlugin = require('html-webpack-plugin');
var OpenBrowserPlugin = require('open-browser-webpack-plugin');

var ROOT_PATH = path.resolve(__dirname);

module.exports = {
  devtool: process.env.NODE_ENV === 'production' ? '' : 'source-map',
  entry: [
    path.resolve(ROOT_PATH, './index'),
  ],
  module: {
    preLoaders: [
      {
        test: /\.js?$/,
        loaders: process.env.NODE_ENV === 'production' ? [] : ['eslint'],
        include: __dirname
      }
    ],
    loaders: [
      { test: /\.js?$/, exclude: /node_modules/, loaders: ['babel-loader'] },
      { test: /\.scss$/, loaders: ['style', 'css', 'sass'] },
      { test: /\.css?$/, loader: 'style!css' },
      { test: /\.less$/, loader: 'style!css!less' },
      { test: /\.gif$/, loader: "url-loader?mimetype=image/png" },
      { test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "url-loader?limit=10000&minetype=application/font-woff" },
      { test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "file-loader?name=[name].[ext]" }
    ],
  },
  sassLoader: {
    includePaths: [
      path.resolve(ROOT_PATH, './node_modules/compass-mixins/lib'),
      path.resolve(ROOT_PATH, './node_modules/primer-css/scss')
    ]
  },
  resolve: {
    extensions: ['', '.js', '.jsx']
  },
  output: {
    path: path.resolve(ROOT_PATH, 'public'),
    publicPath: '/',
    filename: 'bundle.js'
  },
  devServer: {
    contentBase: path.resolve(ROOT_PATH, 'public'),
    proxy: {
      '/api/*': {
        target: 'http://127.0.0.1:2345'
      },
    },
    historyApiFallback: true,
    hot: true,
    inline: true,
    progress: true
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new HtmlwebpackPlugin({
      template: './index.html'
    }),
    new OpenBrowserPlugin({
      url: 'http://localhost:8080'
    })
  ]
};
