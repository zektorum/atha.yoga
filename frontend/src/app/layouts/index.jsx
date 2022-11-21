import React from 'react';
import { Outlet } from 'react-router-dom';
import { Box, Container } from '@mui/material';

const Layout = () => (
  <Container maxWidth="md">
    <Box sx={{ my: 4 }}>
      <Outlet />
    </Box>
  </Container>
);

export default Layout;
