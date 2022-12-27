import React from 'react';
import { Outlet } from 'react-router-dom';

const Layout = () => (
  <div style={{
    display: 'flex', justifyContent: 'space-between', alignItems: 'start', height: '100%',
  }}
  >
    <Outlet />
  </div>
);

export default Layout;
