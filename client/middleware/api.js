import fetch from 'isomorphic-fetch';
import merge from 'lodash.merge';

export default ({ dispatch, getState }) => {
  return next => action => {
    if (typeof action === 'function') {
      return action(dispatch, getState);
    }

    const { type, api, request, method = 'GET', ...rest } = action;
    if (!api) {
      return next(action);
    }

    next({ ...rest, type, status: 'FETCHING' });

    return fetch(api, {
      method,
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
      credentials: 'same-origin',
      ...(method == 'POST' || method == 'PUT' || method == 'GET' ?
        { body: request && JSON.stringify(request) } :
        {}),
    }).then(resp => {
      if (resp.status !== 200) {
        next({ ...rest, type, api, status: 'ERROR', resp: {} });
      } else {
        resp.json().then(json => next(merge({}, { ...rest, type, api, status: 'SUCCESS', resp: json })));
      }
    });
  };
};
