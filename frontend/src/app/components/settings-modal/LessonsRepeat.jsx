/* eslint-disable react/jsx-props-no-spreading */
import React, { useState } from 'react';
import {
  Typography,
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Grid,
  DatePicker,
  TimePicker,
  TextField,
} from '@mui/material';
import PropTypes from 'prop-types';
import { styled } from '@mui/material/styles';
import IconButton from '@mui/material/IconButton';
import CloseIcon from '@mui/icons-material/Close';

const OnceLesson = ({ date, }) => (
  <Grid item container sx={{ justifyContent: 'start', columnGap: '4%' }}>
    <DatePicker
      label="Дата*"
      value={date}
      id="lesson_date"
      required
      onChange={newValue => setDate(newValue)}
      renderInput={params => <TextField {...params} sx={{ width: '35%' }} />}
    />

    <TimePicker
      label="Время*"
      value={time}
      id="lesson_time"
      required
      onChange={newValue => setTime(newValue)}
      renderInput={params => <TextField {...params} sx={{ width: '35%' }} />}
    />
  </Grid>
);

export { OnceLesson };

  <Grid item>
    <Typography variant="modal" sx={{ fontSize: '18px', color: '#212121' }}>
      Определите продолжительность серии занятий (не более 2-х месяцев)
    </Typography>
  </Grid>;

const changeRegularTime = newValue => {
  setLessonData({
    ...lessonData,
    timeForRegularLesson: (newValue),
  });
};

{ /*
            <Grid item>
              <FormControl sx={{ width: '30%' }}>
                <InputLabel id="demo-simple-select-label">День</InputLabel>
                <Select
                  labelId="demo-simple-select-label"
                  id="demo-simple-select"
                  value={lessonData.dayForRegularLesson}
                  name="dayForRegularLesson"
                  required
                  label="День"
                  onChange={update}

                >
                  <MenuItem value="Monday">Понедельник</MenuItem>
                  <MenuItem value="Tuesday">Вторник</MenuItem>
                  <MenuItem value="Wednesday">Среда</MenuItem>
                  <MenuItem value="Thursday">Четверг</MenuItem>
                  <MenuItem value="Friday">Пятница</MenuItem>
                  <MenuItem value="Saturday">Суббота</MenuItem>
                  <MenuItem value="Sunday">Воскресенье</MenuItem>
                </Select>
              </FormControl>

              <TimePicker
                label="Время"
                value={lessonData.timeForRegularLesson}
                id="regular_lesson_time"
                required
                sx={{ width: '30%' }}
                onChange={newValue => changeRegularTime(newValue)}
                renderInput={params => <TextField {...params} />}
              />
            </Grid>
                  */ }
