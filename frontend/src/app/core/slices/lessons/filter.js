import { createAsyncThunk } from '@reduxjs/toolkit';
import LessonsService from '../../../services/lessons';

const filterSlice = createAsyncThunk(
  'lessons/filter',
  async (query, thunkAPI) => {
    if (query) {
      try {
        const result = await LessonsService.filter({});

        return result.data;
      } catch (error) {
        const message = error.response.data;

        return thunkAPI.rejectWithValue(message);
      }
    }
  },
);

export default filterSlice;
