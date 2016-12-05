import React, { Component, PropTypes } from 'react';
import { connect } from 'react-redux';

import Posts from '../../components/Posts/Posts';
import Picker from '../../components/Picker/Picker';

import { fetchNews, selectItem } from '../../actions';
import { Icon } from 'antd';

require('./App.scss');

class App extends Component {
  constructor(props) {
    super(props);
    this.handleChange = this.handleChange.bind(this);
  }

  componentDidMount() {
    for (const value of this.props.selectors) {
      this.props.dispatch(fetchNews(value.item, value.boardId));
    }
  }

  componentWillReceiveProps(nextProps) {
    for (const value of nextProps.selectors) {
      if (value.item !== this.props.selectors[value.boardId].item) {
        nextProps.dispatch(fetchNews(value.item, value.boardId));
      }
    }
  }

  handleChange(nextItem, id) {
    this.props.dispatch(selectItem(nextItem, id));
  }

  render() {
    const boards = [];
    for (const value of this.props.selectors) {
      boards.push(value.boardId);
    }
    const options = ['Github', 'Hacker News', 'Segment Fault', '开发者头条', '伯乐头条'];
    return (
      <div className="mega">
        <div className="header">
          <a href="https://github.com/ethan-funny/React-News-Board" className="button" target="_blank">
            <Icon type="github" />
            <span> Star</span>
          </a>
        </div>
        <main>
          <div className="desk-container">
            {
              boards.map((board, i) =>
                <div className="desk" style={{ opacity: 1 }} key={i}>
                  <Picker value={this.props.selectors[board].item}
                    onChange={this.handleChange}
                    options={options}
                    id={board}
                  />
                  <Posts
                    isFetching={this.props.news[board].isFetching}
                    postList={this.props.news[board].posts}
                    id={board}
                  />
                </div>
              )
            }
          </div>
        </main>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    news: state.news,
    selectors: state.selectors,
  };
}

export default connect(mapStateToProps)(App);
