import { createAsyncThunk } from '@reduxjs/toolkit';
import AuthService from '../../../services/auth';
import { setMessage } from '../message';

const loginSlice = createAsyncThunk(
  'auth/login',
  async ({ email, password }, thunkAPI) => {
    try {
      return await AuthService.login({ email, password });
    } catch (error) {
      const message = error.response.data;
      thunkAPI.dispatch(setMessage(message));

      return thunkAPI.rejectWithValue();
    }
  },
);

export default loginSlice;
