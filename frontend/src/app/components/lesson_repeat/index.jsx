/* eslint-disable react/prop-types */
/* eslint-disable react/jsx-props-no-spreading */
import React, {useState} from 'react';
import dayjs from 'dayjs';
import 'dayjs/locale/ru';
import {DatePicker} from '@mui/x-date-pickers/DatePicker';
import {TimePicker} from '@mui/x-date-pickers/TimePicker';
import {
    Box,
    Button,
    FormControl,
    FormControlLabel,
    Grid,
    InputLabel,
    MenuItem,
    Radio,
    RadioGroup,
    Select,
    TextField,
    Typography,
} from '@mui/material';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import DateRangeOutlinedIcon from '@mui/icons-material/DateRangeOutlined';
import CloseOutlinedIcon from '@mui/icons-material/CloseOutlined';
import { useDispatch, useSelector } from 'react-redux';
import { setMessage } from '../../core/slices/message';
import postLessonSlice from '../../core/slices/lessonCreate/postLesson';

const dateRange = {
  'Понедельник': 0,
  'Вторник': 1,
  'Среда': 2,
  'Четверг': 3,
  'Пятница': 4,
  'Суббота': 5,
  'Восресенье': 6,
};

const getDay = (num) => {
  let day;
  for (let el in dateRange) {
    if (dateRange[el] === num) {
      day = el
    }
  }
  return day;
};

const OnceLesson = ({
  date, time, setLessonData, lessonData,
}) => {
  const setDate = newValue => {
    setLessonData({
      ...lessonData,
      dateForOnceLesson: newValue,
    });
  };

  const setTime = newValue => {
    setLessonData({
      ...lessonData,
      timeForOnceLesson: newValue,
    });
  };

  const dispatch = useDispatch();
  const { message } = useSelector(state => state.message)

  return (
    <Grid item container sx={{ justifyContent: 'start', columnGap: '4%' }}>
      <DatePicker
        label="Дата"
        value={date}
        id="lesson_date"
        minDate={dayjs(Date())}
        onChange={newValue => setDate(newValue)}
        renderInput={params => <TextField {...params} sx={{ width: '35%' }} required />}
        //error={ !!message?.invalid?.start_datetime }
        //helperText={message?.invalid?.start_datetime }
      />
      <TimePicker
        label="Время"
        value={time}
        id="lesson_time"
        onChange={newValue => setTime(newValue)}
        renderInput={params => <TextField {...params} sx={{ width: '35%' }} required />}
      />
    </Grid>
  );
};

const RegularLessons = ({
  lessons, start_datetime, deadline_datetime, lessonData, setLessonData,
}) => {
  const [regularLessonDay, setRegularLessonDay] = useState('');
  const [redularLessonTime, setRegularLessonTime] = useState(null);

  const setStartDate = newValue => {
    setLessonData({
      ...lessonData,
      startDateForRegularLesson: newValue,
    });
  };

  const setFinishDate = newValue => {
    setLessonData({
      ...lessonData,
      finishDateForRegularLesson: newValue,
    });
  };

  const getLessonInfo = () => {
    const time = dayjs(redularLessonTime).minute() > 9 ? `${dayjs(redularLessonTime).hour()}:${dayjs(redularLessonTime).minute()}` : `${dayjs(redularLessonTime).hour()}:0${dayjs(redularLessonTime).minute()}`;
    const copyRegularLessons = [...lessons];
    copyRegularLessons.push({ day: dateRange[regularLessonDay], start_time: time });
    setLessonData({
      ...lessonData,
      lessons: copyRegularLessons,
    });
    setRegularLessonDay('');
    setRegularLessonTime(null);
  };

  const deleteLesson = lesson => {
    setLessonData(lessonData.lessons.filter(p => p !== lesson));
  };

  const dispatch = useDispatch();
  const { message } = useSelector(state => state.message)

  return (
    <>
      <Grid item container sx={{ justifyContent: 'start', columnGap: '4%' }}>
        <Typography variant="modal" sx={{ fontSize: '18px', color: '#212121', paddingBottom: '20px' }}>
          Определите продолжительность серии занятий (не более 2-х месяцев)
        </Typography>

        <DatePicker
          label="Начало"
          value={start_datetime}
          minDate={dayjs(Date())}
          onChange={newValue => setStartDate(newValue)}
          renderInput={params => <TextField {...params} sx={{ width: '35%' }} required />}
        />
        <DatePicker
          label="Окончание"
          value={deadline_datetime}
          disabled={start_datetime === null}
          minDate={start_datetime}
          maxDate={dayjs(start_datetime).add(2, 'month')}
          onChange={newValue => setFinishDate(newValue)}
          renderInput={params => <TextField {...params} sx={{ width: '35%' }} required />}
        />

        <Typography
          variant="modal"
          sx={{
            fontSize: '18px', color: '#212121', paddingTop: '30px', paddingBottom: '20px',
          }}
        >
          Задайте регулярное расписание занятий на неделю
        </Typography>
      </Grid>

      <Grid
        item
        container
        sx={{
          border: '1px solid #E5E5E5',
          padding: '10px',
          minHeight: '150px',
          alignContent: 'flex-start',
          justifyContent: 'space-around',
          borderRadius: '10px',
        }}
      >
        <FormControl sx={{ width: '30%' }}>
          <InputLabel id="demo-simple-select-label">День недели</InputLabel>
          <Select
            labelId="demo-simple-select-label"
            id="demo-simple-select"
            value={regularLessonDay}
            name="dayForRegularLesson"
            label="День недели"
            onChange={e => setRegularLessonDay(e.target.value)}
          >
            <MenuItem value="Понедельник">Понедельник</MenuItem>
            <MenuItem value="Вторник">Вторник</MenuItem>
            <MenuItem value="Среда">Среда</MenuItem>
            <MenuItem value="Четверг">Четверг</MenuItem>
            <MenuItem value="Пятница">Пятница</MenuItem>
            <MenuItem value="Суббота">Суббота</MenuItem>
            <MenuItem value="Воскресенье">Воскресенье</MenuItem>
          </Select>
        </FormControl>

        <TimePicker
          label="Время"
          value={redularLessonTime}
          id="regular_lesson_time"
          sx={{ width: '30%' }}
          onChange={newValue => setRegularLessonTime(newValue)}
          renderInput={params => <TextField {...params} />}
        />

        <Button
          variant="text"
        //  disabled={regularLessonDay.length || lessonTime === null}
          onClick={getLessonInfo}
        >
          Добавить занятие
        </Button>
        {lessonData.lessons.map(lesson => (
          <Box
            key={Math.random()}
            sx={{
              width: '100%', display: 'flex', columnGap: '10%', paddingTop: '5%', paddingLeft: '15%',
            }}
          >
            <Box sx={{
              width: '40%', display: 'flex', columnGap: '10%', borderBottom: '1px solid #E5E5E5', justifyContent: 'space-between', paddingBottom: '1%',
            }}
            >
              <Box sx={{ width: '10%', display: 'flex', justifyContent: 'space-around' }}>
                <DateRangeOutlinedIcon sx={{ color: '#0D6EFD', marginRight: '5px' }} />
                <Typography variant="modal" sx={{ fontSize: '16px' }}>{getDay(lesson.day)}</Typography>
                <AccessTimeIcon sx={{ color: '#0D6EFD', marginLeft: '25px', marginRight: '5px' }} />
                <Typography variant="modal" sx={{ fontSize: '16px' }}>{lesson.start_time}</Typography>
              </Box>
              <CloseOutlinedIcon
                sx={{ color: '#616161', cursor: 'pointer' }}
                onClick={() => { deleteLesson(lesson); }}
              />
            </Box>
          </Box>
        ))}
      </Grid>
    </>
  );
};

const RepeatLessons = ({ update, lessonData, setLessonData }) => (
  <>
    <Grid item sx={{ height: '6%' }}>
      <FormControl fullWidth sx={{ paddingLeft: '2%' }}>
        <RadioGroup
          row
          aria-labelledby="lesson-repeat-label"
          name="lesson-repeat-radio-buttons-group"
          defaultValue="once"
          sx={{ columnGap: '5%' }}
        >
          <FormControlLabel
            onChange={update}
            value="once"
            name="repeat"
            control={<Radio />}
            label={<Typography variant="modal" sx={{ fontSize: '16px', color: '#212121' }}>Разовое</Typography>}
          />
          <FormControlLabel
            onChange={update}
            name="repeat"
            value="regular"
            control={<Radio />}
            label={<Typography variant="modal" sx={{ fontSize: '16px', color: '#212121' }}>Регулярное</Typography>}
          />
        </RadioGroup>
      </FormControl>
    </Grid>
    {lessonData.repeat === 'once'
      ? (
        <OnceLesson
          date={lessonData.dateForOnceLesson}
          time={lessonData.timeForOnceLesson}
          lessonData={lessonData}
          setLessonData={setLessonData}
        />
      )
      : (
        <RegularLessons
          lessons={lessonData.lessons}
          start_datetime={lessonData.startDateForRegularLesson}
          deadline_datetime={lessonData.finishDateForRegularLesson}
          lessonData={lessonData}
          setLessonData={setLessonData}
        />
      )}
  </>
);

export default RepeatLessons;
