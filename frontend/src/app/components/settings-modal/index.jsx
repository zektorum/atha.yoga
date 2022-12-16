import React, { useState } from 'react';
import { LocalizationProvider } from '@mui/x-date-pickers';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { TimePicker } from '@mui/x-date-pickers/TimePicker';
import dayjs from 'dayjs';
import 'dayjs/locale/ru';
import {
  Button,
  Grid,
  Container,
  Typography,
  TextField,
  MenuItem,
  Select,
  InputLabel,
  FormControl,
  FormControlLabel,
  FormLabel,
  RadioGroup,
  Checkbox,
  Divider,
  InputAdornment,
  Box,
} from '@mui/material';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import CurrencyRubleIcon from '@mui/icons-material/CurrencyRuble';

const Modal = () => {
  const [typeOfLesson, setTypeOfLesson] = useState('video');
  const [skillLevel, setSkillLevel] = useState('beginner');
  const [costOfLesson, setCostOfLesson] = useState('paid');
  const [selectedDurationBtn, setSelectedDurationBtn] = useState(3);
  const [selectedRepeatBtn, setSelectedRepeatBtn] = useState(1);
  const [selectedDate, setSelectedDate] = useState(dayjs());
  const [selectedTime, setSelectedTime] = useState(dayjs());
  const [startLessonDate, setStartLessonDate] = useState(dayjs());
  const [endLessonDate, setEndLessonDate] = useState(dayjs());

  return (
    <LocalizationProvider dateAdapter={AdapterDayjs} adapterLocale="ru" localeText={{ start: 'Дата начала', end: 'Дата окончания' }}>
      <Container sx={{ display: 'flex', justifyContent: 'center' }}>
        <Grid
          container
          direction="column"
          rowSpacing={3}
          sx={{ width: '40%', padding: '16px' }}
        >

          <Grid item container sx={{ justifyContent: 'center', position: 'relative' }}>
            <ArrowBackIcon sx={{ position: 'absolute', left: 0 }} />
            <Typography variant="modal">Создать занятие</Typography>
          </Grid>

          <Grid item>
            <Typography variant="modal">Основная информация</Typography>
          </Grid>

          <Grid item>
            <TextField
              id="lesson_name"
              label="Название занятия"
              defaultValue="Введите название"
              fullWidth
            />
          </Grid>

          <Grid item>
            <TextField
              id="lesson_description"
              multiline
              fullWidth
              rows={4}
              defaultValue="Описание занятия"
            />
          </Grid>

          <Grid item>
            <FormControl sx={{ width: '100%' }}>
              <InputLabel id="type_of_lesson">Тип занятия</InputLabel>
              <Select
                labelId="type_of_lesson"
                id="type_of_lesson"
                value={typeOfLesson}
                label="Тип занятия"
                fullWidth
                sx={{ width: '100%' }}
                onChange={e => setTypeOfLesson(e.target.value)}
              >
                <MenuItem value="video">Видео</MenuItem>
                <MenuItem value="online">Онлайн</MenuItem>
              </Select>
            </FormControl>
          </Grid>

          <Grid item>
            <TextField
              id="lesson_link"
              label="Ссылка"
              defaultValue="atha-yoga.com"
              fullWidth
            />
          </Grid>

          <Grid item>
            <TextField
              id="lesson_link"
              label="Данные для доступа"
              defaultValue="Введите данные"
              fullWidth
            />
          </Grid>

          <Grid item>
            <FormControl sx={{ width: '100%' }}>
              <InputLabel id="skill_level">Уровень подготовки</InputLabel>
              <Select
                labelId="skill_level"
                id="skill_level"
                value={skillLevel}
                label="Уровень подготовки"
                fullWidth
                onChange={e => setSkillLevel(e.target.value)}
              >
                <MenuItem value="beginner">Начинающий</MenuItem>
                <MenuItem value="middle">Средний</MenuItem>
                <MenuItem value="pro">Продвинутый</MenuItem>
              </Select>
            </FormControl>
          </Grid>

          <Grid item>
            <Divider variant="middle" />
          </Grid>

          <Grid item>
            <Typography variant="modal">Продолжительность</Typography>
          </Grid>

          <Grid item>
            <Grid container sx={{ justifyContent: 'space-between', width: '100%', height: 'auto' }}>
              <Button sx={{ width: '24%' }} variant={selectedDurationBtn === 1 ? 'contained' : 'outlined'} onClick={() => setSelectedDurationBtn(1)}>30 мин</Button>
              <Button sx={{ width: '24%' }} variant={selectedDurationBtn === 2 ? 'contained' : 'outlined'} onClick={() => setSelectedDurationBtn(2)}>45 мин</Button>
              <Button sx={{ width: '24%' }} variant={selectedDurationBtn === 3 ? 'contained' : 'outlined'} onClick={() => setSelectedDurationBtn(3)}>60 мин</Button>
              <Button sx={{ width: '24%' }} variant={selectedDurationBtn === 4 ? 'contained' : 'outlined'} onClick={() => setSelectedDurationBtn(4)}>Другое</Button>
            </Grid>
          </Grid>

          <Grid item sx={{ paddingTop: '0 !important' }}>
            <Typography variant="modal">Повторение</Typography>
          </Grid>

          <Grid item>
            <Grid container sx={{ justifyContent: 'space-between', width: '100%' }}>
              <Button sx={{ width: '49.5%' }} variant={selectedRepeatBtn === 1 ? 'contained' : 'outlined'} onClick={() => setSelectedRepeatBtn(1)}>Разовое</Button>
              <Button sx={{ width: '49.5%' }} variant={selectedRepeatBtn === 2 ? 'contained' : 'outlined'} onClick={() => setSelectedRepeatBtn(2)}>Повторяющееся</Button>
            </Grid>
          </Grid>

          <Grid item>
            <Grid container sx={{ justifyContent: 'space-between', width: '100%' }}>
              <DatePicker
                value={selectedDate}
                onChange={newValue => setSelectedDate(newValue)}
                renderInput={params => <TextField {...params} sx={{ width: '49.5%' }} />}
                id="date"
                label="Выберите дату"
                type="date"
                InputLabelProps={{
                  shrink: true,
                }}
              />
              <TimePicker
                value={selectedTime}
                onChange={newValue => setSelectedTime(newValue)}
                renderInput={params => <TextField {...params} sx={{ width: '49.5%' }} />}
                id="time"
                label="Выберите время"
                type="time"
                InputLabelProps={{
                  shrink: true,
                }}
                inputProps={{
                  step: 300, // 5 min
                }}
              />
            </Grid>
          </Grid>

          <Grid item>
            <Divider variant="middle" />
          </Grid>

          <Grid item>
            <Typography variant="modal">Оплата</Typography>
          </Grid>

          <Grid item>
            <FormControl sx={{ width: '100%' }}>
              <InputLabel id="lesson_cost">Тип оплаты</InputLabel>
              <Select
                labelId="lesson_cost"
                id="lesson_cost"
                value={costOfLesson}
                label="Тип занятия"
                onChange={e => setCostOfLesson(e.target.value)}
                fullWidth
              >
                <MenuItem value="paid">Платное</MenuItem>
                <MenuItem value="free">Бесплатное</MenuItem>
              </Select>
            </FormControl>
          </Grid>

          <Grid item>
            <TextField
              id="cost"
              label="Стоимость"
              defaultValue="0,00"
              fullWidth
              disabled={costOfLesson === 'free'}
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <CurrencyRubleIcon />
                  </InputAdornment>
                ),
              }}
            />
          </Grid>

          <Grid item>
            <Divider variant="middle" />
          </Grid>

          <Grid item>
            <Typography variant="modal">Расписание</Typography>

          </Grid>

          <Grid item>
            <DatePicker
              value={startLessonDate}
              onChange={newValue => setStartLessonDate(newValue)}
              renderInput={params => <TextField {...params} sx={{ width: '100%' }} />}
              id="date"
              label="Выберите дату"
              type="date"
              InputLabelProps={{
                shrink: true,
              }}
            />
          </Grid>

          <Grid item>
            <DatePicker
              value={endLessonDate}
              onChange={newValue => setEndLessonDate(newValue)}
              renderInput={params => <TextField {...params} sx={{ width: '100%' }} />}
              id="date"
              label="Выберите дату"
              type="date"
              InputLabelProps={{
                shrink: true,
              }}
            />
          </Grid>

          <Grid item>
            <FormControl>
              <FormLabel id="lesson_day">
                <Typography variant="modal">Дни недели</Typography>
              </FormLabel>
              <RadioGroup
                aria-labelledby="lesson_day"
                name="radio-buttons-group"
              >
                <FormControlLabel control={<Checkbox />} label="Понедельник" />
                <FormControlLabel control={<Checkbox />} label="Вторник" />
                <FormControlLabel control={<Checkbox />} label="Среда" />
                <FormControlLabel control={<Checkbox />} label="Четверг" />
                <FormControlLabel control={<Checkbox />} label="Пятница" />
                <FormControlLabel control={<Checkbox />} label="Суббота" />
                <FormControlLabel control={<Checkbox />} label="Воскресенье" />
              </RadioGroup>
            </FormControl>
          </Grid>
          <Grid item>
            <Button
              fullWidth
              variant="contained"
              type="submit"
            >
              Создать занятие
            </Button>
          </Grid>
        </Grid>
      </Container>
    </LocalizationProvider>
  );
};

export default Modal;
