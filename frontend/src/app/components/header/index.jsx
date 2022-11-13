import React from 'react';
import PropTypes from 'prop-types';

import './style.scoped.scss';

const Header = ({ text }) => <h1 className="header">{text}</h1>;

export default Header;

Header.propTypes = {
  text: PropTypes.string.isRequired,
};
