import React, { Component, PropTypes } from 'react';
import { Spin } from 'antd';

require('./Loading.scss');

export class Loading extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <div className="spin">
        <Spin spining={this.props.isFetch} size="default" />
      </div>
    );
  }
}
