import getUrl from '../../api';

const userData = JSON.parse(localStorage.user)
const USER_ID = userData.user.id;

export const CALENDAR_URL = getUrl(`/courses/${USER_ID}/lessons`);
export const CALENDAR_URL2 = getUrl(`/courses/im`);
export const CALENDAR_URL3 = getUrl(`/courses/im/enrolled-lessons`);
export const CALENDAR_URL4 = getUrl(`/courses/im/participated-lessons`);

