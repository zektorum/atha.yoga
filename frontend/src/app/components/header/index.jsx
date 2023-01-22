import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import {
  Typography, Grid, Stack, Badge,
} from '@mui/material';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import SettingsOutlinedIcon from '@mui/icons-material/SettingsOutlined';
import NotificationsNoneIcon from '@mui/icons-material/NotificationsNone';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';

const Header = ({ title, withBackBtn = false }) => {
  const navigate = useNavigate();
  return (
    <Grid
      item
      display="flex"
      flexDirection="row"
      alignItems="center"
      justifyContent="space-between"
      mb="20px"
      sx={{
        width: '100%', minHeight: '64px', px: '29px', boxShadow: '0px 8px 16px rgba(46, 60, 80, 0.1)',
      }}
    >
      <Stack direction="row" alignItems="center" spacing={2} color="text.secondary">
        { withBackBtn && (
        <ArrowBackIcon
          fontSize="medium"
          sx={{ cursor: 'pointer' }}
          onClick={() => {
            navigate(-1);
          }}
        />
        )}
        <Typography fontSize="20px" fontWeight="500">
          {title || 'Назад'}
        </Typography>
      </Stack>
      <Stack alignItems="center" direction="row" spacing={2}>
        <Badge color="error" variant="dot">
          <NotificationsNoneIcon fontSize="medium" color="disabled" />
        </Badge>
        { title === 'Настройки' ? (
          <Link to="/profile">
            <AccountCircleIcon color="disabled" sx={{ transform: 'translateY(3px)' }} />
          </Link>
        )
          : (
            <Link to="/settings">
              <SettingsOutlinedIcon color="disabled" sx={{ transform: 'translateY(3px)' }} />
            </Link>
          )}
      </Stack>
    </Grid>
  );
};

export default Header;