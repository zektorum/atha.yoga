import { duration } from '@mui/material';
import axios from 'axios';
import dayjs from 'dayjs';
import LessonDescription from '../../components/lesson-description';
import { FILTER_URL, GET_LESSON_URL } from './utils';

const filter = ({ query }) => axios
  .post(FILTER_URL, { query });

const getLesson = id => axios
  .get(`${GET_LESSON_URL + id}/`);

const postLesson = ({ lessonState }) => axios
  .post(GET_LESSON_URL, {
    name: lessonState.name,
    description: lessonState.description,
    //  complexity: lessonState,
    level: lessonState.level,
    duration: lessonState.duration,
    course_type: lessonState.type,
    link: lessonState.link,
    link_info: lessonState.conferenceId,
    //  onceLesson_datetime: `${dayjs(lessonState.date).get('year')}-${dayjs(lessonState.date).get('month') < 10 ? `0${dayjs(lessonState.date).get('month') + 1}` : dayjs(lessonState.date).get('month')}-${dayjs(lessonState.date).get('date')}T${dayjs(lessonState.time).get('hour') < 10 ? `0${dayjs(lessonState.time).get('hour')}` : dayjs(lessonState.time).get('hour')}:${dayjs(lessonState.time).get('minute') < 10 ? `0${dayjs(lessonState.time).get('minute')}` : dayjs(lessonState.time).get('minute')}:00.791Z`,
    start_datetime: lessonState,
    deadline_datetime: lessonState,
    payment: lessonState.payment,
    price: lessonState.cost,
    lessons: lessonState.regularLessons,
    is_draft: false,
  });

const LessonsService = { filter, getLesson, postLesson };

export default LessonsService;
