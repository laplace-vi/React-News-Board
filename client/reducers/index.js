import { combineReducers } from 'redux';

import news from './news';
import selectors from './selectors';

const rootReducer = combineReducers({
  news,
  selectors,
});

export default rootReducer;
