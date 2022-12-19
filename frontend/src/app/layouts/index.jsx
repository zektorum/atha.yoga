import React from 'react';
import { Outlet } from 'react-router-dom';
import signUpLogo from '../../assets/public/signUpLogo.svg';
import { Typography } from '@mui/material';

const Layout = () => (
  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'start'}}>
    <div
      style={{
        width: '31vw',
        height: '100vh',
        backgroundColor: '#0D6EFD',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        gap: '35px',
      }}>
      <img style={{maxWidth: '100%'}} src={signUpLogo} alt="Atha yoga logo" />
      <Typography variant="h5" color="common.white">Исследуйте • Занимайтесь • Создавайте</Typography>
    </div>
    <Outlet />
  </div>
);

export default Layout;
