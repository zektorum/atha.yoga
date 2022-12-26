/* eslint no-param-reassign: 0 */
import { createSlice } from '@reduxjs/toolkit';
import getLessonSlice from './getLesson';

const initialState = {
  lesson: null,
  errorMessage: null,
};

const lessonSlice = createSlice({
  name: 'lesson',
  initialState,
  extraReducers: {
    [getLessonSlice.fulfilled]: (state, action) => {
      state.lesson = action.payload;
      state.errorMessage = null;
    },
    [getLessonSlice.rejected]: (state, action) => {
      state.lesson = null;
      state.errorMessage = action.payload;
    },
  },
});

export default lessonSlice.reducer;
