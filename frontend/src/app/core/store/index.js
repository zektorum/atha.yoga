import { configureStore } from '@reduxjs/toolkit';
import auth from '../slices/auth';
import message from '../slices/message';
import lessons from '../slices/lessons';
import lesson from '../slices/lesson';

const store = configureStore({
  reducer: {
    auth,
    message,
    lessons,
    lesson,
  },
});

export default store;
