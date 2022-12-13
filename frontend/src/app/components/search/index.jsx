import React, { useCallback, useState } from 'react';
import {
  debounce, InputBase, Paper, Typography,
} from '@mui/material';
import SearchIcon from '@mui/icons-material/Search';
import IconButton from '@mui/material/IconButton';
import { useDispatch, useSelector } from 'react-redux';
import filterSlice from '../../core/slices/lessons/filter';

const Search = () => {
  const dispatch = useDispatch();
  const [query, setQuery] = useState('');
  const { lessons, isSearching, errorMessage } = useSelector(state => state.lessons);

  async function doSearch() {
    dispatch(filterSlice(query));
  }

  const doSearchDebounced = useCallback(debounce(doSearch, 500), []);

  function updateSearch(e) {
    setQuery(e.target.value);

    doSearchDebounced();
  }

  return (
    <>
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
    </>
  );
};

export default Search;
