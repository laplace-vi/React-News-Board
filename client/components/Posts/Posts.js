import React, { Component, PropTypes } from 'react';
import { Loading } from '../Loading/Loading';

require('./Posts.scss');

export default class Posts extends Component {
  constructor() {
    super();
  }

  render() {
    const { isFetching, postList } = this.props;
    return (
      <div className="desk-items">
        {
          isFetching ? <Loading isFetch={isFetching} /> :
            <ul>
            {
              postList.map((post, i) => {
                return (
                  <div className="item" key={i}>
                    <div className="item-name">
                      <a href={post.url} target="_blank">{post.title}</a>
                    </div>
                    {
                      post.desc ?
                        <div className="item-container">
                          <div className="item-content">
                            <p>{post.desc}</p>
                          </div>
                        </div>
                        : null
                    }
                    <div className="item-annotation">
                      <p>{post.subdesc}</p>
                    </div>
                  </div>
                );
              }, this)
            }
            </ul>
        }
      </div>
    );
  }
}

Posts.propTypes = {
  postList: PropTypes.arrayOf(
    PropTypes.object.isRequired
  ).isRequired,
  isFetching: PropTypes.bool.isRequired,
};
