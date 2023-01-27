/* eslint no-param-reassign: 0 */
import { createSlice } from '@reduxjs/toolkit';
import postLessonSlice from './postLesson';

const initialState = {
  lesson: [],
  errorMessage: null,
};

const postLessonInfoSlice = createSlice({
  name: 'postLesson',
  initialState,
  extraReducers: {
    [postLessonSlice.fulfilled]: (state, action) => {
      state.lesson = action.payload;
      state.errorMessage = null;
    },
    [postLessonSlice.rejected]: (state, action) => {
      state.lesson = [];
      state.errorMessage = action.payload;
    },
  },
});

export default postLessonInfoSlice.reducer;
