import { FETCH_NEWS } from '../actions';
import _ from 'lodash';

const initialState = [
  {
    isFetching: true,
    posts: [],
    boardId: 0,
  },
  {
    isFetching: true,
    posts: [],
    boardId: 1,
  },
  {
    isFetching: true,
    posts: [],
    boardId: 2,
  },
  {
    isFetching: true,
    posts: [],
    boardId: 3,
  },
];

export default function reducer(state = initialState, action = {}) {
  switch (action.type) {
    case FETCH_NEWS:
      if (action.status === 'FETCHING') {
        return _.sortBy([
          {
            isFetching: true,
            posts: [],
            boardId: action.id,
          },
          ...state.filter(element =>
            element.boardId !== action.id
          ),
        ], 'boardId');
      }
      if (action.status === 'SUCCESS') {
        return _.sortBy([
          {
            isFetching: false,
            posts: action.resp.data,
            boardId: action.id,
          },
          ...state.filter(element =>
            element.boardId !== action.id
          ),
        ], 'boardId');
      }
      return state;

    default:
      return state;
  }
}
