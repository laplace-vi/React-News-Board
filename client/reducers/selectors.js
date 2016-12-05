import { SELECT_ITEM } from '../actions';
import _ from 'lodash';

const initialState = [
  {
    item: 'Github',
    boardId: 0,
  },
  {
    item: 'Hacker News',
    boardId: 1,
  },
  {
    item: '开发者头条',
    boardId: 2,
  },
  {
    item: 'Segment Fault',
    boardId: 3,
  },
];

export default function reducer(state = initialState, action = {}) {
  switch (action.type) {
    case SELECT_ITEM:
      return _.sortBy([
        {
          item: action.item,
          boardId: action.id,
        },
        ...state.filter(element =>
            element.boardId !== action.id
        ),
      ], 'boardId');
    default:
      return state;
  }
}
