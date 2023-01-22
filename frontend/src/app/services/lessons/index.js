import axios from 'axios';
import { FILTER_URL, LESSON_URL } from './utils';

const filter = ({ query }) => axios
  .post(FILTER_URL, { query });

const getLesson = id => axios
  .get(`${LESSON_URL + id}/`);

const postLesson = lessonState => axios
  .post(LESSON_URL, {
    name: lessonState.name,
    description: lessonState.description,
    complexity: 'easy', // need to remove, because obj has level property
    level: lessonState.level,
    duration: lessonState.duration,
    course_type: lessonState.type,
    link: lessonState.link,
    link_info: lessonState.conferenceId,
    start_datetime: lessonState.startDate,
    deadline_datetime: lessonState.finishDate,
    payment: lessonState.payment,
    price: lessonState.cost,
    lessons: lessonState.regularLessons,
    is_draft: lessonState.isDraft,
  });

const LessonsService = { filter, getLesson, postLesson };

export default LessonsService;
