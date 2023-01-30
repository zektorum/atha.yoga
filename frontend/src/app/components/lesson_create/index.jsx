/* eslint-disable no-console */
/* eslint-disable react/jsx-props-no-spreading */
import React, { useState, useRef } from 'react';
import { Link } from 'react-router-dom';
import 'dayjs/locale/ru';
import dayjs from 'dayjs';
import { Navigate } from 'react-router-dom';
import { useLocation } from 'react-router-dom';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import {
  Badge,
  Box,
  Button,
  Checkbox,
  Container,
  Divider,
  FormControl,
  FormControlLabel,
  FormHelperText,
  Grid,
  InputLabel,
  ListItemText,
  MenuItem,
  OutlinedInput,
  Radio,
  RadioGroup,
  Select,
  Stack,
  TextField,
  Typography,
} from '@mui/material';
import Header from '../../components/header';
import PaymentMethod from '../lesson_payment/index';
import RepeatLessons from '../lesson_repeat/index';
import LessonsService from '../../services/lessons';
import { useDispatch, useSelector } from 'react-redux';
import { setMessage } from '../../core/slices/message';
import postLessonSlice from '../../core/slices/lessonCreate/postLesson';
import AlertDialog from '../lesson_alert';

const LessonCreate = () => {
  const [lessonLevels, setLessonLevels] = useState([]);
  const [lessonData, setLessonData] = useState({
    name: '',
    description: '',
    course_type: 'ONLINE',
    link: '',
    link_info: '',
    level: [],
    complexity: 'EASY',
    duration: '',
    duration_number: '',
    repeat: 'once',
    start_datetime: '',
    deadline_datetime: '',
    dateForOnceLesson: null,
    timeForOnceLesson: null,
    startDateForRegularLesson: null,
    finishDateForRegularLesson: null,
    lessons: [],
    regularLessonsWithDate: [],
    payment: 'PAYMENT',
    donation: true,
    price: '',
    is_draft: false,
  });
  const [errorMessageForLevel, setErrorMessageForLevel] = useState('');
  const [errorMessageForCost, setErrorMessageForCost] = useState('');
  const [errorMessageForOnceLessonDate, setErrorMessageForOnceLessonDate] = useState('');
  const [errorMessageForOnceLessonTime, setErrorMessageForOnceLessonTime] = useState('');
  const [errorMessageForStartRegularLessonDate, setErrorMessageForStartRegularLessonDate] = useState('');
  const [errorMessageForFinishRegularLessonDate, setErrorMessageForFinishRegularLessonDate] = useState('');
  const [errorMessageForRegularLessons, setErrorMessageForRegularLessons] = useState('');
  const [errorMessageForLessonId, setErrorMessageForLessonId] = useState('');
  const [isFormSend, setIsFormSend] = useState(false);
  
  const location = useLocation();

  const getErrorMessageForCost = () => {
    if (lessonData.payment === 'PAYMENT' && lessonData.price.length === 0) {
      setErrorMessageForCost('Это поле не может быть пустым.')
    } else {
      setErrorMessageForCost('')
    }
  }

  const getErrorMessageForLessonId = () => {
    if (lessonData.link_info.length === 0) {
      setErrorMessageForLessonId('Это поле не может быть пустым.')
    } else {
      setErrorMessageForLessonId('')
    }
  }

  const getErrorMessageForOnceLessonDate = () => {
    if (lessonData.dateForOnceLesson === null && lessonData.repeat === 'once') {
      setErrorMessageForOnceLessonDate('Это поле не может быть пустым.')
    } else if (lessonData.dateForOnceLesson < Date.now()) {
      console.log(Date.now())
      setErrorMessageForOnceLessonDate('Дата должна быть не ранее сегодняшней')
    } else {
      setErrorMessageForOnceLessonDate('')
    }
  }

  const getErrorMessageForOnceLessonTime = () => {
    if (lessonData.timeForOnceLesson === null && lessonData.repeat === 'once') {
      setErrorMessageForOnceLessonTime('Это поле не может быть пустым.')
    } else {
      setErrorMessageForOnceLessonTime('')
    }
  }

  const getErrorMessageForStartRegularLessonDate = () => {
    if (lessonData.startDateForRegularLesson === null && lessonData.repeat !== 'once') {
      setErrorMessageForStartRegularLessonDate('Это поле не может быть пустым.')
    } else {
      setErrorMessageForStartRegularLessonDate('')
    }
  }

  const getErrorMessageForFinishRegularLessonDate = () => {
    if (lessonData.finishDateForRegularLesson === null && lessonData.repeat !== 'once') {
      setErrorMessageForFinishRegularLessonDate('Это поле не может быть пустым.')
    } else {
      setErrorMessageForFinishRegularLessonDate('')
    }
  }

  const getErrorMessageForRegularLessons = () => {
    if (lessonData.lessons.length === 0 && lessonData.repeat !== 'once') {
      setErrorMessageForRegularLessons('Обязательно наличие одного цикла занятий.')
    } else {
      setErrorMessageForRegularLessons('')
    }
  }

  const dispatch = useDispatch();
  const { message } = useSelector(state => state.message)
 
  const getErrorMessageForLevel = () => {
    if (lessonData.level.length === 0) {
      setErrorMessageForLevel('Это поле не может быть пустым.')
    } else {
      setErrorMessageForLevel('')
    }
  }

  const getStartDate = () => {
    const date = lessonData.dateForOnceLesson;
    const time = lessonData.timeForOnceLesson;
    const hour = dayjs(time).get('hour');
    const minute = dayjs(time).get('minute');
    const startDateValue = dayjs(date).set('hour', hour).set('minute', minute);
    return startDateValue.format()
  };

  const getFinishDate = () => {
    const start_datetime = getStartDate();
    const duration = lessonData.duration.split(':');
    const minute = Number(duration[0] * 60) + Number(duration[1])
    const deadline_datetime = dayjs(start_datetime).add(minute, 'minute');
    return deadline_datetime.format();
  };

  const getCorrectDateTime = () => {
    if (lessonData.dateForOnceLesson !== null) {
      setLessonData(lessonData.start_datetime = getStartDate());
      setLessonData(lessonData.deadline_datetime = getFinishDate());
    } else {
      setLessonData(lessonData.start_datetime = lessonData?.startDateForRegularLesson?.format());
      setLessonData(lessonData.deadline_datetime = lessonData?.finishDateForRegularLesson?.format());
    }
  };

  const getDuration = (duration) => {
    const today = new Date;
    today.setHours(0, duration, 0, 0);
    const now = today.toLocaleTimeString('ru-RU');
    return now
  }

  const getCorrectOtherData = () => {
    setLessonData(lessonData.level = lessonData.level.map(el => {
      if (el === 'Начинающий') el = 'STARTING';
      if (el === 'Средний') el = 'CONTINUER';
      if (el === 'Продвинутый') el = 'ADVANCED';
      return el;
    }));
    lessonData.payment === 'FREE' ? setLessonData(lessonData.price = 0) : '';
    setLessonData(lessonData.duration = getDuration(lessonData.duration_number))
  }

  const update = e => {
    setLessonData({
      ...lessonData,
      [e.target.name]: e.target.value,
    });
  };

  const saveFormUsDraft = () => {
    console.log(location)
    getCorrectDateTime();
    getCorrectOtherData();
    getErrorMessageForLevel();
    getErrorMessageForCost();
    getErrorMessageForOnceLessonDate();
    getErrorMessageForOnceLessonTime();
    getErrorMessageForFinishRegularLessonDate();
    getErrorMessageForStartRegularLessonDate();
    getErrorMessageForRegularLessons();
    getErrorMessageForLessonId();
    setLessonData({
      ...lessonData,
      is_draft: false,
    });
    console.log(lessonData);
    console.warn(message)
    dispatch(postLessonSlice({ ...lessonData }));
    LessonsService.postLesson(lessonData)
    .then(setIsFormSend(true))
  };

  const saveForm = () => {
    getCorrectDateTime();
    getCorrectOtherData();
    getErrorMessageForLevel();
    getErrorMessageForCost();
    getErrorMessageForOnceLessonDate();
    getErrorMessageForOnceLessonTime();
    getErrorMessageForFinishRegularLessonDate();
    getErrorMessageForStartRegularLessonDate();
    getErrorMessageForRegularLessons();
    getErrorMessageForLessonId();
    setLessonData({
      ...lessonData,
      is_draft: false,
    });
    console.log(lessonData);
    console.warn(message)
    dispatch(postLessonSlice({ ...lessonData }));
    LessonsService.postLesson(lessonData)
    .then(setIsFormSend(true))
  };

  const changeDonation = e => {
    const value = !(e.target.value === 'on');
    setLessonData({
      ...lessonData,
      [e.target.name]: value,
    });
  };

  const changeLessonLevel = event => {
    const {
      target: { value },
    } = event;
    setLessonLevels(
      typeof value === 'string' ? value.split(',') : value,
      update(event),
    );
  };

  const levels = ['Начинающий', 'Средний', 'Продвинутый'];

  return (
    <LocalizationProvider dateAdapter={AdapterDayjs} adapterLocale="ru">
      <Header title="Создание занятия" withBackBtn />
      <form onSubmit={e => {
        e.preventDefault();
      }}
      >
        <Container sx={{ display: 'flex', justifyContent: 'center' }}>
          <Grid
            container
            direction="column"
            rowSpacing={3}
            sx={{ width: '70%', padding: '16px' }}
          >

            <Grid item>
              <Typography variant="modal">Обязательные поля *</Typography>
            </Grid>

            <Grid item>
              <TextField
                id="lesson_name"
                label="Название занятия"
                name="name"
                onChange={update}
                value={lessonData.name}
                required
                fullWidth
                error={ !!message?.invalid?.name }
                helperText={message?.invalid?.name}
              />
            </Grid>

            <Grid item>
              <TextField
                id="lesson_description"
                label="Описание"
                name="description"
                placeholder="Первые N символов будут показаны в карточке занятия при поиске"
                onChange={update}
                value={lessonData.description}
                multiline
                fullWidth
                required
                rows={4}
                error={ !!message?.invalid?.description }
                helperText={message?.invalid?.description}
              />
            </Grid>

            <Grid item sx={{ height: '6%' }}>
              <FormControl fullWidth sx={{ paddingLeft: '2%' }}>
                <RadioGroup
                  row
                  aria-labelledby="row-radio-buttons-group-label"
                  name="row-radio-buttons-group"
                  defaultValue="ONLINE"
                  sx={{ columnGap: '5%' }}
                >
                  <FormControlLabel
                    onChange={update}
                    value="ONLINE"
                    name="course_type"
                    control={<Radio />}
                    label={<Typography variant="modal" sx={{ fontSize: '16px', color: '#212121' }}>Онлайн</Typography>}
                  />
                  <FormControlLabel
                    onChange={update}
                    name="course_type"
                    value="VIDEO"
                    control={<Radio />}
                    label={<Typography variant="modal" sx={{ fontSize: '16px', color: '#212121' }}>Видео</Typography>}
                  />
                </RadioGroup>
              </FormControl>
            </Grid>

            <Grid item container sx={{ justifyContent: 'space-between' }}>
              <TextField
                id="lesson_link"
                label="Ссылка на занятие"
                name="link"
                value={lessonData.link}
                onChange={update}
                sx={{ width: '48%' }}
                required
                error={ !!message?.invalid?.link }
                helperText={message?.invalid?.link}
              />

              <TextField
                id="lesson_link"
                label="Данные для доступа"
                name="link_info"
                value={lessonData.link_info}
                onChange={update}
                placeholder="Идентификатор конференции"
                sx={{ width: '48%' }}
                required
                error={ !!errorMessageForLessonId }
                helperText={errorMessageForLessonId}
              />
            </Grid>

            <Grid item>
              <FormControl fullWidth error={ !!errorMessageForLevel }>
                <InputLabel id="lesson-level-label">Уровень подготовки</InputLabel>
                <Select
                  labelId="lesson-level-label"
                  id="lesson-level-checkbox"
                  multiple
                  required
                  fullWidth
                  name="level"
                  value={lessonLevels}
                  onChange={changeLessonLevel}
                  input={<OutlinedInput label="Уровень подготовки" />}
                  renderValue={selected => selected.join(', ')}
                >
                  {levels.map(level => (
                    <MenuItem key={level} value={level}>
                      <Checkbox checked={lessonLevels.indexOf(level) > -1} />
                      <ListItemText primary={level} />
                    </MenuItem>
                  ))}
                </Select>
                <FormHelperText>{ errorMessageForLevel }</FormHelperText>
              </FormControl>
            </Grid>

            <Grid item>
              <TextField
                id="lesson_duration"
                label="Длительность занятия, мин"
                name="duration_number"
                type="number"
                onChange={update}
                required
                value={lessonData.duration_number}
                sx={{ width: '49%' }}
                error={ !!message?.invalid?.duration }
                helperText={message?.invalid?.duration}
              />
            </Grid>

            <Grid item>
              <Divider variant="middle" sx={{ paddingTop: '20px' }} />
            </Grid>

            <RepeatLessons
              update={update}
              lessonData={lessonData}
              setLessonData={setLessonData}
              errorDateForOnceLesson={errorMessageForOnceLessonDate}
              errorTimeForOnceLesson={errorMessageForOnceLessonTime}
              errorStartForRegularLesson={errorMessageForStartRegularLessonDate}
              errorFinishForRegularLesson={errorMessageForFinishRegularLessonDate}
              errorLessons={errorMessageForRegularLessons}
              errorMessage={message}
            />

            <Grid item>
              <Divider variant="middle" sx={{ paddingTop: '20px' }} />
            </Grid>

            <PaymentMethod
              update={update}
              changeDonation={changeDonation}
              payment={lessonData.payment}
              price={lessonData.price}
              error={errorMessageForCost}
            />
            <Grid item container sx={{ justifyContent: 'end', columnGap: '5%' }}>
              <Button
                size="large"
                variant="text"
                onClick={saveFormUsDraft}
              >
                Сохранить черновик
              </Button>

              <Button
                size="large"
                variant="contained"
                type="submit"
                onClick={saveForm}
              >
                Опубликовать
              </Button>
            </Grid>

          </Grid>
        </Container>
      </form>
      {isFormSend ? <Navigate to="/my-lessons" /> : ''}
      {location.pathname !== '/create-lesson' ? <AlertDialog /> : ''}
    </LocalizationProvider>
  );
};

export default LessonCreate;
