import React from 'react';

import { render } from 'react-dom';
import { Provider } from 'react-redux';
import configureStore from './store/configureStore';
import AppRoutes from './routes';
import { Router, Route } from 'react-router';

import 'antd/dist/antd.css';

const store = configureStore();

render(
  <Provider store={store}>
    {AppRoutes}
  </Provider>,
  document.getElementById('root')
);
