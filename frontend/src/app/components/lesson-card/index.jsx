/* eslint-disable react/prop-types */
/* eslint-disable react/destructuring-assignment */
/* eslint-disable linebreak-style */
import React from 'react';
import { Typography, Box, Grid } from '@mui/material';
import SchoolIcon from '@mui/icons-material/School';
import DateRangeOutlinedIcon from '@mui/icons-material/DateRangeOutlined';
import AccessTimeOutlinedIcon from '@mui/icons-material/AccessTimeOutlined';

const LessonCard = props => (
  <Box
    width="385px"
    m="16px"
    sx={{ borderRadius: '8px', boxShadow: '0px 8px 16px rgba(46, 60, 80, 0.1)' }}
  >
    <Grid container alignItems="flex-start" justifyContent="center">
      <Grid item>
        <Typography>
          <SchoolIcon color="primary" fontSize="large" sx={{ m: '16px' }} />
        </Typography>
      </Grid>
      <Grid item xs container>
        <Grid item xs container direction="column" sx={{ py: '16px' }}>
          <Grid item>
            <Typography sx={{ fontSize: '18px', mb: '12px' }}>
              {props.title}
            </Typography>
          </Grid>
          <Grid item>
            <Typography
              color="text.secondary"
              sx={{
                width: '252px', fontSize: '14px', mb: '8px', lineHeight: '120%',
              }}
            >
              {props.description}
            </Typography>
          </Grid>
          <Grid item display="flex">
            <Typography color="text.secondary" mr="16px">
              <DateRangeOutlinedIcon fontSize="20" color="primary" sx={{ mr: '6px', verticalAlign: '-2px' }} />
              26.11
            </Typography>
            <Typography color="text.secondary">
              <AccessTimeOutlinedIcon fontSize="20" color="primary" sx={{ mr: '6px', verticalAlign: '-2px' }} />
              14:00 - 15:30
            </Typography>
          </Grid>
        </Grid>
      </Grid>
    </Grid>
  </Box>
);

export default LessonCard;
