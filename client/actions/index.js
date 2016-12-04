export const FETCH_NEWS = 'FETCH_NEWS';
export const SELECT_ITEM = 'SELECT_ITEM';

export function selectItem(item, id) {
  return {
    type: SELECT_ITEM,
    item,
    id,
  };
}

export function fetchNews(item, id) {
  switch (item) {
    case 'Github':
      return {
        type: FETCH_NEWS,
        api: `/api/github/repo_list`,
        method: 'GET',
        id,
      };
    case 'Hacker News':
      return {
        type: FETCH_NEWS,
        api: `/api/hacker/news`,
        method: 'GET',
        id,
      };
    case 'Segment Fault':
      return {
        type: FETCH_NEWS,
        api: `/api/segmentfault/blogs`,
        method: 'GET',
        id,
      };
    case '开发者头条':
      return {
        type: FETCH_NEWS,
        api: `/api/toutiao/posts`,
        method: 'GET',
        id,
      };
    case '伯乐头条':
      return {
        type: FETCH_NEWS,
        api: `/api/jobbole/news`,
        method: 'GET',
        id,
      };
    default:
      return {};
  }
}
