import axios from 'axios';
import { CALENDAR_URL } from './utils';
import authHeader from '../auth/header';

const getShedule = () => axios
  .get(CALENDAR_URL, { headers: authHeader() });

export default getShedule;
