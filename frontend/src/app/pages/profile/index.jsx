import React from 'react';
import { Navigate } from 'react-router-dom';

const ProfilePage = ({ auth: { user } }) => {
  if (!user) {
    return (
      <Navigate to="/login" />
    );
  }

  return (
    <div>
      <h2>Profile</h2>
      <p>
        <strong>Id: </strong>
        {user.user.id}
      </p>
      <p>
        <strong>Email: </strong>
        {user.user.email}
      </p>
      <p>
        <strong>Token: </strong>
        {user.accessToken.substring(0, 20)}
      </p>
    </div>
  );
};

export default ProfilePage;
