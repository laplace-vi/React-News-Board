import React from 'react';
import { Router, Route, IndexRoute, useRouterHistory } from 'react-router';
import { createHashHistory } from 'history';

import App from './containers/App/App';

const appHistory = useRouterHistory(createHashHistory)({ queryKey: false });

export default (
  <Router history={appHistory}>
    <Route path="/" component={App}>
      <IndexRoute component={App} />
    </Route>
  </Router>
);
