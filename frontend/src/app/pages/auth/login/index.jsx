import React from 'react';
import { Navigate } from 'react-router-dom';
import useAuth from '../../../utils/hooks/useAuth';
import LogIn from '../../../components/log-in/index.jsx';

const LoginPage = () => {
  const auth = useAuth();

  if (auth.isLoggedIn) {
    return <Navigate to="/profile" />;
  }

  return (
    <LogIn />
  );
};

export default LoginPage;
