import axios from 'axios';
import authHeader from '../auth/header';
import { USER_BOARD_URL } from './utils';

const getUserBoard = () => axios.get(USER_BOARD_URL, { headers: authHeader() });

const userService = {
  getUserBoard,
};

export default userService;
