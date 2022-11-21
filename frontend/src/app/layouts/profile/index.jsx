import React from 'react';
import { Link, Outlet } from 'react-router-dom';
import { Box, Container } from '@mui/material';

const ProfileLayout = ({ auth }) => (
  <Container maxWidth="sm">
    <Box sx={{ my: 4 }}>
      <h1>Protected Profile layout</h1>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/profile">Profile</Link>
            </li>
            <li>
              <button onClick={auth.logout}>Logout</button>
            </li>
          </ul>
        </nav>

        <hr />

        <Outlet />
      </div>
    </Box>
  </Container>
);

export default ProfileLayout;
