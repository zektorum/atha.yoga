import { createAsyncThunk } from '@reduxjs/toolkit';
import AuthService from '../../../services/auth';

const logoutSlice = createAsyncThunk('auth/logout', async () => {
  await AuthService.logout();
});

export default logoutSlice;
