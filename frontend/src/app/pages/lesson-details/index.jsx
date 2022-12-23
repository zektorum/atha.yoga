import React from 'react';
import { Box, Typography } from '@mui/material';
import SettingsIcon from '@mui/icons-material/Settings';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';

const LessonDetailsPage = () => (
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
      <ArrowBackIcon sx={{ mr: '14px', verticalAlign: '-2px' }} fontSize="medium" color="action" />
      Назад
    </Typography>
    <SettingsIcon color="disabled" />
  </Box>
);

export default LessonDetailsPage;
