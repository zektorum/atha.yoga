import getUrl from '../../api';

const userData = JSON.parse(localStorage.user)
const USER_ID = userData.user.id;

export const CALENDAR_URL = getUrl(`/courses/${USER_ID}/lessons`);
