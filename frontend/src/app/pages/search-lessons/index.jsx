import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import {
  Box,
  InputBase, Paper, Typography,
} from '@mui/material';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';
import filterSlice from '../../core/slices/lessons/filter';
import useDebounce from '../../utils/hooks/useDebounce';

const SearchLessonsPage = () => {
  const dispatch = useDispatch();
  const [query, setQuery] = useState('');
  const { lessons, isSearching, errorMessage } = useSelector(state => state.lessons);

  const searchQuery = useDebounce(query, 500);

  useEffect(() => {
    dispatch(filterSlice(query));
  }, [searchQuery]);
  function updateSearch(e) {
    setQuery(e.target.value);
  }

  return (
    <Box>
      <Paper
        component="form"
        sx={{
          p: '2px 4px', display: 'flex', alignItems: 'center', width: 400,
        }}
      >
        <IconButton type="button" sx={{ p: '10px' }}>
          <SearchIcon />
        </IconButton>
        <InputBase
          sx={{ ml: 1, flex: 1 }}
          value={query}
          onChange={e => updateSearch(e)}
        />
      </Paper>
      {isSearching && <Typography>Searching...</Typography>}
      {errorMessage && (
        <Typography color="error.main">
          Error:
          {errorMessage}
        </Typography>
      )}
      {lessons && <Typography>{JSON.stringify(lessons)}</Typography>}
    </Box>
  );
};

export default SearchLessonsPage;
