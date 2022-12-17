import React from 'react';
import { Grid, Typography } from '@mui/material';
import MenuList from '@mui/material/MenuList';
import MenuItem from '@mui/material/MenuItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import SearchIcon from '@mui/icons-material/Search';
import ListItemText from '@mui/material/ListItemText';
import FavoriteBorderIcon from '@mui/icons-material/FavoriteBorder';
import CalendarMonthOutlinedIcon from '@mui/icons-material/CalendarMonthOutlined';
import ConfirmationNumberOutlinedIcon from '@mui/icons-material/ConfirmationNumberOutlined';
import AccountCircleOutlinedIcon from '@mui/icons-material/AccountCircleOutlined';
import { Link } from 'react-router-dom';
import menuLogo from '../../../assets/public/menu_logo.svg';

const Menu = ({ auth }) => {
  const menuItemStyle = {
    minHeight: '36px',
    '& .MuiTypography-root': {
       color: 'text.secondary',
    },
    '&:hover': {
      backgroundColor: 'primary.main',
      borderRadius: '5px',
      '& .MuiSvgIcon-root, & .MuiTypography-root': {
        color: 'common.white',
      },
    },
  };
  return (
    <Grid container>
      <MenuList
        sx={{
          height: '100vh',
          display: 'flex',
          flexDirection: 'column',
          justifyContent: 'start',
          p: 2,
          backgroundColor: '#F5F5F5'
        }}
      >
        <button onClick={auth.logout}>Logout</button>
        <div style={{ textAlign: 'center', marginBottom: '18px' }}>
          <img src={menuLogo} alt="atha yoga logo" style={{ width: '103px', height: '26px' }} />
        </div>
        <MenuItem
          component={Link}
          to="search-lessons"
          sx={{ ...menuItemStyle }}
        >
          <ListItemIcon>
            <SearchIcon color="disabled" fontSize="medium" />
          </ListItemIcon>
          <ListItemText
            primary={(
              <Typography
                variant="body2"
              >
                Поиск
              </Typography>
              )}
          />
        </MenuItem>
        <MenuItem component={Link} to="" sx={{ ...menuItemStyle }}>
          <ListItemIcon>
            <FavoriteBorderIcon color="disabled" fontSize="medium" />
          </ListItemIcon>
          <ListItemText
            primary={(
              <Typography
                variant="body2"
              >
                Избранное
              </Typography>
              )}
          />
        </MenuItem>
        <MenuItem component={Link} to="" sx={{ ...menuItemStyle }}>
          <ListItemIcon>
            <ConfirmationNumberOutlinedIcon color="disabled" fontSize="medium" />
          </ListItemIcon>
          <ListItemText
            primary={(
              <Typography
                variant="body2"
              >
                Абонементы
              </Typography>
                )}
          />
        </MenuItem>
        <MenuItem component={Link} to="/calendar" sx={{ ...menuItemStyle }}>
          <ListItemIcon>
            <CalendarMonthOutlinedIcon color="disabled" fontSize="medium" />
          </ListItemIcon>
          <ListItemText
            primary={(
              <Typography
                variant="body2"
              >
                Календарь
              </Typography>
                )}
          />
        </MenuItem>
        <MenuItem component={Link} to="/profile" sx={{ ...menuItemStyle }}>
          <ListItemIcon>
            <AccountCircleOutlinedIcon color="disabled" fontSize="medium" />
          </ListItemIcon>
          <ListItemText
            primary={(
              <Typography
                variant="body2"
              >
                Профиль
              </Typography>
                )}
          />
        </MenuItem>
      </MenuList>
    </Grid>
  );
};

export default Menu;
