const getUrl = pathname => {
  if (!pathname.startsWith('/')) {
    throw new Error('pathname should start with /');
  }

  return `${__API_URL__}${pathname}`;
};

export const getData = ({ data }) => {
  if (data.data) {
    return data.data;
  }

  return data;
};

export default getUrl;
