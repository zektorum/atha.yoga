module.exports = env => {
  const base = {
    appDefinitions: {
      __API_URL__: process.env.API_URL || '/api',
      __ENVIRONMENT__: env,
    },
  };
  const title = 'atha.yoga';
  const html = {
    description: title,
    title: `[${env.toUpperCase()}] ${title}`,
  };
  const baseDev = {
    ...base,
    isDev: true,
    compress: false,
    html,
    mode: 'development',
  };
  const baseProd = {
    ...base,
    isDev: false,
    compress: true,
    html,
    mode: 'production',
  };

  switch (env) {
    case 'prod':
      return {
        ...baseProd,
        html: {
          ...baseProd.html,
          title,
        },
      };
    case 'local':
    default:
      return baseDev;
  }
};
