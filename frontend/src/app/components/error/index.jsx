import React from 'react';
import PropTypes from 'prop-types';

const Error = ({ message }) => <div>{message}</div>;

Error.propTypes = {
  message: PropTypes.string,
};

export default Error;
