import { configureStore } from '@reduxjs/toolkit';
import auth from '../slices/auth';
import message from '../slices/message';
import lessons from '../slices/lessons';

const store = configureStore({
  reducer: {
    auth,
    message,
    lessons,
  },
});

export default store;
