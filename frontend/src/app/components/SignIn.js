import * as React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Link from '@mui/material/Link';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import InputAdornment from '@mui/material/InputAdornment';
import Visibility from '@mui/icons-material/Visibility';
import VisibilityOff from '@mui/icons-material/VisibilityOff';
import IconButton from '@mui/material/IconButton';
import OutlinedInput from '@mui/material/OutlinedInput';
import Container from '@mui/material/Container';
import facebook from '../../assets/facebook.svg';
import google from '../../assets/google.svg';
import yandex from '../../assets/yandex.svg';
import vk from '../../assets/vk.svg';

export default function LogIn() {
  const [values, setValues] = React.useState({
    amount: '',
    password: '',
    weight: '',
    weightRange: '',
    showPassword: false,
  });

  const handleChange = (prop) => (event) => {
    setValues({ ...values, [prop]: event.target.value });
  };

  const handleClickShowPassword = () => {
    setValues({
      ...values,
      showPassword: !values.showPassword,
    });
  };

  const handleMouseDownPassword = (event) => {
    event.preventDefault();
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    console.log({
      email: data.get('email'),
      password: data.get('password'),
    });
  };

  return (
    <Container component="main" maxWidth="xs">
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}
        >
          <Typography component="h1" variant="h4" gutterBottom>
            Создать аккаунт
          </Typography>
          <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }} class="form__container">
            <TextField
              margin="normal"
              label="Электронная почта"
              fullWidth
              id="email"
              placeholder="E-mail"
              name="email"
              autoComplete="email"
              autoFocus
            />
            <OutlinedInput
              margin="normal"
              fullWidth
              name="password"
              placeholder="Пароль"
              id="password"
              autoComplete="current-password"
              type={values.showPassword ? 'text' : 'password'}
              value={values.password}
              onChange={handleChange('password')}
              endAdornment={
                <InputAdornment position="end">
                  <IconButton
                    aria-label="toggle password visibility"
                    onClick={handleClickShowPassword}
                    onMouseDown={handleMouseDownPassword}
                  >
                   {values.showPassword ? <VisibilityOff /> : <Visibility />}
                  </IconButton>
                </InputAdornment>
              }
            />
            <Grid container alignItems="center">
              <Grid item>
                <FormControlLabel
                  control={<Checkbox checked value="remember" color="primary" />}
                  label="Я принимаю условия"
                />
              </Grid>
              <Grid item>
                <Link href="#" variant="body2" underline="none">
                  {'пользовательского'}
                </Link>
              </Grid>
              <Grid item>
                <Link href="#" variant="body2" underline="none">
                  {'соглашения'}
                </Link>
              </Grid>
            </Grid>
            <Button
              size="large"
              type="submit"
              fullWidth
              variant="contained"
              sx={{ mt: 3, mb: 2 }}
            >
              Создать
            </Button>
            <Grid container spacing={1} alignItems="center" justifyContent="center">
              <Grid item>
                <Typography variant="body2">
                  Уже есть аккаунт?
                </Typography>
              </Grid>
              <Grid item>
                <Link href="#" variant="body2" underline="none">
                  Войти
                </Link>
              </Grid>
            </Grid>
            <div class="line"></div>
            <Typography variant="body2" textAlign="center">
               Или войти с помощью
            </Typography>
            <Grid container spacing={3} justifyContent="center" alignItems="center" marginTop={1}>
              <Grid item xs={2}>
                <Link href="#">
                  <img src={facebook} alt="icon" />
                </Link>
              </Grid>
              <Grid item xs={2}>
                <Link href="#">
                  <img src={google} alt="icon" />
                </Link>
              </Grid>
              <Grid item xs={2}>
                <Link href="#">
                  <img src={yandex} alt="icon" />
                </Link>
              </Grid>
              <Grid item xs={2}>
                <Link href="#">
                  <img src={vk} alt="icon" />
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
    </Container>
  );
}
