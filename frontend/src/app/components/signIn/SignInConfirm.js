import * as React from 'react';
import Link from '@mui/material/Link';
import Typography from '@mui/material/Typography';
import letter from '../../assets/letter.svg';

export default function SignInConfirm() {
  return (
  <div className="sign_in_confirm__container">
    <img src={letter} alt="Письмо" />
    <Typography variant="h6" maxWidth={270} textAlign="center" sx={{ mt: 4, mb: 2 }}>
      Письмо с подтверждением регистрации отправлено
      вам на почту
    </Typography>
    <Typography variant="body2" color="text.secondary" maxWidth={240} textAlign="center">
      Следуйте инструкции из письма.
      Если письмо не пришло,
    </Typography>
    <Link href="#" variant="body2" underline="none">
      отправить письмо еще раз.
    </Link>
  </div>
  )}
