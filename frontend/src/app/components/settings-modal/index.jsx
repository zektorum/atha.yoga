import React, { useState } from 'react';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { TimePicker } from '@mui/x-date-pickers/TimePicker';
import dayjs from 'dayjs';
import 'dayjs/locale/ru';
import {
  Grid,
  Container,
  Typography,
  Switch,
  TextField,
  MenuItem,
  Select,
  Radio,
  Button,
  InputLabel,
  FormControl,
  FormControlLabel,
  RadioGroup,
  Checkbox,
  OutlinedInput,
  ListItemText,
  Divider,
} from '@mui/material';

const Modal = () => {
  const [personName, setPersonName] = useState([]);
  const [selectedDate, setSelectedDate] = useState(dayjs());
  const [selectedTime, setSelectedTime] = useState(dayjs());

  const [value, setValue] = React.useState(null);

  const [lessonData, setLessonData] = useState({
    name: '',
    description: '',
    type: 'online',
    link: '',
    conferenceId: '',
    level: [],
    duration: '',
    repeat: 'once',
    date: selectedDate,
    time: selectedTime,
    date2: '',
    time2: '',
    payment: 'paid',
    donation: true,
    cost: '',
  });

  const submit = e => {
    e.preventDefault();
    console.log(lessonData);
  };

  const update = e => {
    setLessonData({
      ...lessonData,
      [e.target.name]: e.target.value,
    });
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
    setPersonName(
      // On autofill we get a stringified value.
      typeof value === 'string' ? value.split(',') : value,
      update(event),
    );
  };

  const lessonLevels = ['Начинающий', 'Средний', 'Продвинутый'];

  const dateNormalize = date => {
    const string = String(date);
    const array = string.split(' ');
    const newDate = `${array[2]} ${array[1]} ${array[3]}`;
    return newDate;
  };

  const timeNormalize = date => {
    const string = String(date);
    const array = string.split(' ');
    const newDate = `${array[2]} ${array[1]} ${array[3]}`;
    return newDate;
  };

  return (
    <LocalizationProvider dateAdapter={AdapterDayjs} adapterLocale="ru">
      <form onSubmit={submit}>
        <Container sx={{ display: 'flex', justifyContent: 'center' }}>
          <Grid
            container
            direction="column"
            rowSpacing={3}
            sx={{ width: '60%', padding: '16px' }}
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
                rows={4}
              />
            </Grid>

            <Grid item>
              <FormControl>
                <RadioGroup
                  row
                  aria-labelledby="demo-row-radio-buttons-group-label"
                  name="row-radio-buttons-group"
                  defaultValue="online"
                >
                  <FormControlLabel
                    onChange={update}
                    value="online"
                    name="type"
                    control={<Radio />}
                    label="Онлайн"
                  />
                  <FormControlLabel
                    onChange={update}
                    name="type"
                    value="video"
                    control={<Radio />}
                    label="Видео"
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
                sx={{ width: '49%' }}
                required
              />

              <TextField
                id="lesson_link"
                label="Данные для доступа"
                name="conferenceId"
                value={lessonData.conferenceId}
                onChange={update}
                placeholder="Идентификатор конференции"
                sx={{ width: '49%' }}
              />
            </Grid>

            <Grid item>
              <FormControl fullWidth>
                <InputLabel id="lesson-level-label">Уровень подготовки</InputLabel>
                <Select
                  labelId="lesson-level-label"
                  id="lesson-level-checkbox"
                  multiple
                  required
                  fullWidth
                  name="level"
                  value={personName}
                  onChange={changeLessonLevel}
                  input={<OutlinedInput label="Уровень подготовки" />}
                  renderValue={selected => selected.join(', ')}
                >
                  {lessonLevels.map(level => (
                    <MenuItem key={level} value={level}>
                      <Checkbox checked={personName.indexOf(level) > -1} />
                      <ListItemText primary={level} />
                    </MenuItem>
                  ))}
                </Select>
              </FormControl>
            </Grid>

            <Grid item>
              <TextField
                id="lesson_duration"
                label="Длительность занятия, мин"
                name="duration"
                type="number"
                onChange={update}
                required
                value={lessonData.duration}
                sx={{ width: '49%' }}
              />
            </Grid>

            <Grid item>
              <Divider variant="middle" />
            </Grid>

            <Grid item>
              <FormControl>
                <RadioGroup
                  row
                  aria-labelledby="lesson-repeat-label"
                  name="lesson-repeat-radio-buttons-group"
                  defaultValue="once"
                >
                  <FormControlLabel
                    onChange={update}
                    value="once"
                    name="repeat"
                    control={<Radio />}
                    label="Разовое"
                  />
                  <FormControlLabel
                    onChange={update}
                    name="repeat"
                    value="regular"
                    control={<Radio />}
                    label="Регулярное"
                  />
                </RadioGroup>
              </FormControl>
            </Grid>

            <Grid item container sx={{ justifyContent: 'start', columnGap: '1%' }}>
            <DatePicker
        label="Basic example"
        value={value}
        onChange={(newValue) => {
          setValue(newValue);
        }}
        renderInput={(params) => <TextField {...params} />}
      />
              
              
              
              
              <DatePicker
                value={selectedDate}
                onChange={newValue => setSelectedDate(newValue)}
                renderInput={params => <TextField {...params} sx={{ width: '40%' }} />}
                id="date"
                label="Дата"
                type="date"
                name="date"
                required
                InputLabelProps={{
                  shrink: true,
                }}
              />
              <TimePicker
                value={selectedTime}
                onChange={newValue => {
                  setSelectedTime((newValue));
                  update();
                }}
                renderInput={params => <TextField {...params} sx={{ width: '40%' }} />}
                id="lesson_time"
                name="time"
                label="Время"
                type="time"
                required
                InputLabelProps={{
                  shrink: true,
                }}
                inputProps={{
                  step: 300, // 5 min
                }}
              />
            </Grid>



            <Grid item>
              <Divider variant="middle" />
            </Grid>

            <Grid item>
              <FormControl>
                <RadioGroup
                  row
                  aria-labelledby="lesson-cost-label"
                  name="lesson-cost-radio-buttons-group"
                  defaultValue="paid"
                >
                  <FormControlLabel
                    onChange={update}
                    value="paid"
                    name="payment"
                    control={<Radio />}
                    label="Платно"
                  />
                  <FormControlLabel
                    onChange={update}
                    name="payment"
                    value="free"
                    control={<Radio />}
                    label="Бесплатно"
                  />
                  <Divider orientation="vertical" variant="middle" flexItem />
                </RadioGroup>
              </FormControl>

              <FormControlLabel
                label="Принимать чаевые"
                control={(
                  <Switch
                    defaultChecked
                    onChange={changeDonation}
                    name="donation"
                  />
                )}
              />
            </Grid>

            <Grid item>
              <TextField
                id="lesson_cost"
                label="Стоимость, руб"
                name="cost"
                type="number"
                onChange={update}
                required
                value={lessonData.cost}
                sx={{ width: '40%' }}
              />
            </Grid>

            <Grid item container sx={{ justifyContent: 'end', columnGap: '5%' }}>
              <Button
                variant="text"
                onClick={(e) => {
                  e.preventDefault()
                  console.log(lessonData.date)
                  console.log(value)
                  console.log(dateNormalize(value.$d))
                  console.log(value.$d)
                }}
              >
                Сохранить черновик
              </Button>
              <Button
                variant="contained"
                type="submit"
              >
                Опубликовать
              </Button>
            </Grid>

          </Grid>
        </Container>
      </form>
    </LocalizationProvider>
  );
};

export default Modal;
