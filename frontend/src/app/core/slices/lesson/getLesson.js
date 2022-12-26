import { createAsyncThunk } from '@reduxjs/toolkit';
import LessonsService from '../../../services/lessons';

const getLessonSlice = createAsyncThunk(
  'courses/id',
  async (lessonId, thunkAPI) => {
    try {
      const result = await LessonsService.getLesson(lessonId);

      return result.data;
    } catch (error) {
      const message = error.response.data;

      return thunkAPI.rejectWithValue(message);
    }
  },
);

export default getLessonSlice;
