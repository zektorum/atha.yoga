import React from 'react';
import { AuthContext } from '../../providers/auth';

const useAuth = () => React.useContext(AuthContext);

export default useAuth;
