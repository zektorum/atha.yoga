import React from 'react';
import './styles.scoped.scss';
import CssBaseline from '@mui/material/CssBaseline';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import LogInPage from './pages/logIn/index.js';
import WelcomePage from './pages/welcome/index.js';
import SignInPage from './pages/signIn/index.js';

const theme = createTheme({
  palette: {
    primary: {
      main: '#0D6EFD',
    },
    text: {
      primary: '#212121',
      secondary: '#616161',
    },
  },
  h4: {
    fontWeight: 500,
  },
  h1: {
    fontWeight: 500,
  },
});

export default function MyApp() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <WelcomePage />
    </ThemeProvider>
  );
}
