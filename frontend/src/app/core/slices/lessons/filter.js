import { createAsyncThunk } from '@reduxjs/toolkit';
import LessonsService from '../../../services/lessons';

const filterSlice = createAsyncThunk(
  'courses/filter',
  async (query, thunkAPI) => {
    try {
      const result = await LessonsService.filter(query ? { query } : {});

      return result.data;
    } catch (error) {
      const message = error.response.data;

      return thunkAPI.rejectWithValue(message);
    }
  },
);

export default filterSlice;
