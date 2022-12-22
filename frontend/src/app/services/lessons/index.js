import axios from 'axios';
import { FILTER_URL } from './utils';

const filter = ({ query }) => axios
  .post(FILTER_URL, { query });

const LessonsService = { filter };

export default LessonsService;
