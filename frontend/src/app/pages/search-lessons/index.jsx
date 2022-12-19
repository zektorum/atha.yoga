import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import {
  Box, InputBase, Paper, Typography, Container,
} from '@mui/material';
import SettingsIcon from '@mui/icons-material/Settings';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';
import filterSlice from '../../core/slices/lessons/filter';
import useDebounce from '../../utils/hooks/useDebounce';
import LessonCard from '../../components/lesson-card';

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
    <Box sx={{ width: '100%' }}>
      <Box
        display="flex"
        flexDirection="row"
        alignItems="center"
        justifyContent="space-between"
        sx={{
          width: '100%', height: '64px', px: '29px', boxShadow: '0px 8px 16px rgba(46, 60, 80, 0.1)',
        }}
      >
        <Typography fontSize="24px" fontWeight="500" color="text.secondary">
          Календарь
        </Typography>
        <SettingsIcon color="disabled" />
      </Box>
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
      <Container>
        <Box sx={{
          display: 'flex',
          flexWrap: 'wrap',
          justifyContent: 'center',
        }}
        >
          {lessons && lessons.data?.map(lesson => (

            <LessonCard
              key={lesson.id}
              title={lesson.name}
              description={lesson.description}
            />
          ))}
        </Box>
      </Container>
      {/* {lessons && console.log(lessons.data)} */}
    </Box>
  );
};

export default SearchLessonsPage;
