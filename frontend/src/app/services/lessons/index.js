import axios from 'axios';
import { FILTER_URL, GET_LESSON_URL } from './utils';

const filter = ({ query }) => axios
  .post(FILTER_URL, { query });

const getLesson = ({ id }) => axios
  .get(`${GET_LESSON_URL + id}/`);

const LessonsService = { filter, getLesson };

export default LessonsService;
