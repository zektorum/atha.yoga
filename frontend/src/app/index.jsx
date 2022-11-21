import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { CssBaseline, ThemeProvider } from '@mui/material';
import WelcomePage from './pages/welcome';
import LoginPage from './pages/auth/login';
import RegisterPage from './pages/auth/register';
import ProfilePage from './pages/profile';
import ErrorPage from './pages/error';
import AuthProvider from './utils/providers/auth';
import BaseLayout from './layouts';
import ProfileLayout from './layouts/profile';
import useAuth from './utils/hooks/useAuth';
import theme from './theme';

import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

import './theme/style.scss';

const App = () => {
  const auth = useAuth();
  const Layout = auth.isLoggedIn ? ProfileLayout : BaseLayout;

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Routes>
        <Route path="/" element={<Layout auth={auth} />}>
          <Route index element={!auth.isLoggedIn ? <WelcomePage /> : <Navigate replace to="profile" />} />
          <Route path="login" element={<LoginPage />} />
          <Route path="register" element={<RegisterPage />} />
          <Route path="profile" element={<ProfilePage auth={auth} />} />
          <Route path="*" element={<ErrorPage />} />
        </Route>
      </Routes>
    </ThemeProvider>
  );
};

const Root = () => (
  <AuthProvider>
    <App />
  </AuthProvider>
);

export default Root;
