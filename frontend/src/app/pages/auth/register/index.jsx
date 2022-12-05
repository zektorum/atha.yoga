import React from 'react';
import { useSelector } from 'react-redux';
import { Link, Navigate, useNavigate } from 'react-router-dom';
import useAuth from '../../../utils/hooks/useAuth';

const RegisterPage = () => {
  const { message } = useSelector(state => state.message);
  const auth = useAuth();
  const navigate = useNavigate();

  const handleSubmit = e => {
    e.preventDefault();

    const formData = new FormData(e.target);
    const email = formData.get('email');
    const password = formData.get('password');

    auth.register({ email, password }, () => {
      navigate('/profile');
    });
  };

  if (auth.isLoggedIn) {
    return <Navigate to="/profile" />;
  }

  return (
    <div>
      <h2>Register page</h2>
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
            Register
          </button>
        </div>

        <div>{message}</div>

        <Link to="/login">Login</Link>
      </form>
    </div>
  );
};

export default RegisterPage;
