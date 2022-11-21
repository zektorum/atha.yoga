module.exports = {
  env: {
    browser: true,
    es2021: true,
  },
  extends: [
    'plugin:react/recommended',
    'airbnb',
  ],
  overrides: [
  ],
  parserOptions: {
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  plugins: [
    'react',
  ],
  rules: {
    'react/require-default-props': 'off',
    'react/function-component-definition': [2, {
      namedComponents: 'arrow-function',
    }],
    'arrow-parens': ['error', 'as-needed'],
  },
  globals: {
    __API_URL__: 'readonly',
  },
};
