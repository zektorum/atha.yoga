import { duration } from '@mui/material';
import axios from 'axios';
import dayjs from 'dayjs';
import LessonDescription from '../../components/lesson-description';
import { FILTER_URL, GET_LESSON_URL } from './utils';

const filter = ({ query }) => axios
  .post(FILTER_URL, { query });

const getLesson = id => axios
  .get(`${GET_LESSON_URL + id}/`);

const getParseDateTime = (date, time) => {
  const year = dayjs(date).get('year');
  const month = dayjs(date).get('month') < 10 ? `0${dayjs(date).get('month') + 1}` : dayjs(date).get('month');
  const day = dayjs(date).get('date');
  const hour = dayjs(time).get('hour') < 10 ? `0${dayjs(time).get('hour')}` : dayjs(time).get('hour');
  const minute = dayjs(time).get('minute') < 10 ? `0${dayjs(time).get('minute')}` : dayjs(time).get('minute');
  const parseDate = `${year}-${month}-${day}T${hour}:${minute}:00.791Z`;
  return parseDate;
};

const getParseDate = (date) => {
  const year = dayjs(date).get('year');
  const month = dayjs(date).get('month') < 10 ? `0${dayjs(date).get('month') + 1}` : dayjs(date).get('month');
  const day = dayjs(date).get('date');
  const parseDate = `${year}-${month}-${day}`;
  return parseDate;
};

const postLesson = ({ lessonState }) => axios
  .post(GET_LESSON_URL, {
    name: lessonState.name,
    description: lessonState.description,
    //  complexity: lessonState,  //removed, because obj has level property
    level: lessonState.level,
    duration: lessonState.duration,
    course_type: lessonState.type,
    link: lessonState.link,
    link_info: lessonState.conferenceId,
    onceLesson_datetime: getParseDateTime(lessonState.dateForOnceLesson, lessonState.timeForOnceLesson), //  added
    start_datetime: getParseDate(lessonState.startDateForRegularLessons),
    deadline_datetime: getParseDate(lessonState.finishDateForRegularLessons),
    payment: lessonState.payment,
    price: lessonState.cost,
    lessons: lessonState.regularLessons,
    is_draft: lessonState.isDraft,
  });

const LessonsService = { filter, getLesson, postLesson };

export default LessonsService;
