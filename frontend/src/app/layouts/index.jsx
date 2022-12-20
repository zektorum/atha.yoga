import React from 'react';
import { Outlet } from 'react-router-dom';
import { Typography } from '@mui/material';
import signUpLogo from '../../assets/public/signUpLogo.svg';

const Layout = () => (
  <div style={{
    display: 'flex', justifyContent: 'space-between', alignItems: 'start', height: '100%',
  }}
  >
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
      }}
    >
      <img style={{ maxWidth: '100%' }} src={signUpLogo} alt="Atha yoga logo" />
      <Typography variant="h5" color="common.white" textAlign="center">Исследуйте • Занимайтесь • Создавайте</Typography>
    </div>
    <Outlet />
  </div>
);

export default Layout;
