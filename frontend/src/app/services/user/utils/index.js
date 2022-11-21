import storage from '../../api/storage';

export const USER_STORAGE_KEY = 'user';
export const USER_BOARD_URL = '/users/1';

export const user = storage.get(USER_STORAGE_KEY);
