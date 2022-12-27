import React from 'react';
import logo from '../../../assets/public/logo.svg';

import './style.scoped.scss';

const Logo = ({ shown }) => (
  <div className={`logo__container ${!shown ? 'logo__container--hidden' : ''}`}>
    <img src={logo} alt="logo-image" />
  </div>
);

export default Logo;
