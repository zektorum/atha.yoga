import { configureStore } from '@reduxjs/toolkit';
import auth from '../slices/auth';
import message from '../slices/message';

const store = configureStore({
  reducer: {
    auth,
    message,
  },
});

export default store;
