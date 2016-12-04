import React, { Component, PropTypes } from 'react';
import { Select } from 'antd';

require('./Picker.scss');

export default class Picker extends Component {
  render() {
    const { value, onChange, options, id } = this.props;

    function handleChange(val) {
      onChange(val, id);
    }

    return (
      <div className="select-container">
        <Select onChange={handleChange} value={value} style={{ width: 120 }}>
          {
            options.map(option =>
              <Option value={option} key={option}>
                {option}
              </Option>
            )
          }
        </Select>
      </div>
    );
  }
}

Picker.propTypes = {
  options: PropTypes.arrayOf(
    PropTypes.string.isRequired
  ).isRequired,
  value: PropTypes.string.isRequired,
  onChange: PropTypes.func.isRequired,
  id: PropTypes.number,
};
