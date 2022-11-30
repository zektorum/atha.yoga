import React from 'react';
import { useSelector } from 'react-redux';
import { Link, Navigate, useLocation, useNavigate } from 'react-router-dom';
import useAuth from '../../../utils/hooks/useAuth';
import LogIn from '../../../components/LogInDefault.js;

const LoginPage = () => {
  const { message } = useSelector(state => state.message);
  const auth = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const from = location.state?.from?.pathname || '/';

  const handleSubmit = e => {
    e.preventDefault();

    const formData = new FormData(e.target);
    const email = formData.get('email');
    const password = formData.get('password');

    auth.login({ email, password }, () => {
      navigate(from, { replace: true });
    });
  };

  if (auth.isLoggedIn) {
    return <Navigate to="/profile" />;
  }

  return (
    <LogIn />
    <div>
      <h2>Login page</h2>
      <form onSubmit={handleSubmit} autoComplete="off">
        <div>
          <label htmlFor="email">email</label>
          <input name="email" type="email" />
        </div>

        <div>
          <label htmlFor="password">password</label>
          <input name="password" type="password" />
        </div>

        <div>
          <button type="submit" disabled={auth.isLoading}>
            Login
          </button>
        </div>

        <div>{message}</div>

        <Link to="/register">Register</Link>
      </form>
    </div>
  );
};

export default LoginPage;
