/* eslint-disable react/jsx-props-no-spreading */
import React, { useState } from 'react';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import { TimePicker } from '@mui/x-date-pickers/TimePicker';
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
  Box,
  Divider,
} from '@mui/material';

const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};
/*
const ExitModal = () => {
  const [open, setOpen] = useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  return (
    <>
      <Button
        variant="text"
        onClick={handleOpen}
      >
        Сохранить черновик
      </Button>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        <Box sx={style}>
          <Typography id="modal-modal-title" variant="modal">
            Данные не были сохранены
          </Typography>
          <Typography id="modal-modal-description" sx={{ mt: 2 }}>
            Сохранить, как черновик?
          </Typography>
          <Button variant="text">Не сохранять</Button>
          <Button variant="text">Сохранить</Button>
        </Box>
      </Modal>
    </>
  );
};
*/

const Modal = () => {
  const [personName, setPersonName] = useState([]);

  const [lessonData, setLessonData] = useState({
    name: '',
    description: '',
    type: 'online',
    link: '',
    conferenceId: '',
    level: [],
    duration: '',
    repeat: 'once',
    date: null,
    time: null,
    timeForRegularLesson: null,
    dayForRegularLesson: '',
    regularLessonInfo: {},
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
    const newTime = array[4].split(':');
    return `${newTime[0]}:${newTime[1]}`;
  };

  const changeDate = newValue => {
    setLessonData({
      ...lessonData,
      date: dateNormalize(newValue.$d),
    });
  };

  const changeTime = newValue => {
    setLessonData({
      ...lessonData,
      time: timeNormalize(newValue.$d),
    });
  };

  const changeRegularTime = newValue => {
    setLessonData({
      ...lessonData,
      timeForRegularLesson: (newValue),
    });
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
                label="Дата"
                value={lessonData.date}
                id="lesson_date"
                required
                sx={{ width: '25%' }}
                onChange={newValue => changeDate(newValue)}
                renderInput={params => <TextField {...params} />}
              />

              <TimePicker
                label="Время"
                value={lessonData.time}
                id="lesson_time"
                required
                sx={{ width: '25%' }}
                onChange={newValue => changeTime(newValue)}
                renderInput={params => <TextField {...params} />}
              />

            </Grid>
            {/*
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
                  */}
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
                    sx={{ marginRight: '44px' }}
                  />
                  <Divider orientation="vertical" variant="middle" flexItem />
                </RadioGroup>
              </FormControl>

              <FormControlLabel
                label="Принимать чаевые"
                sx={{ marginLeft: '44px' }}
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
                required={lessonData.payment !== 'free'}
                disabled={lessonData.payment === 'free'}
                value={lessonData.cost}
                sx={{ width: '40%' }}
              />
            </Grid>

            <Grid item container sx={{ justifyContent: 'end', columnGap: '5%' }}>
              <Button
                variant="text"
              >
                Сохранить черновик
              </Button>

              <Button
                variant="contained"
              >
                Создать
              </Button>

            </Grid>

          </Grid>
        </Container>
      </form>
    </LocalizationProvider>
  );
};

export default Modal;
