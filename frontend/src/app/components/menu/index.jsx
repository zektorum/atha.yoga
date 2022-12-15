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
import menu_logo from '../../../assets/public/menu_logo.svg';

const Menu = ({ auth }) => {
  const menu_item_style = {
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
        <div style={{ textAlign: 'center', marginBottom: '18px' }}>
          <img src={menu_logo} alt="atha yoga logo" style={{ width: '103px', height: '26px' }} />
        </div>
        <MenuItem
          component={Link}
          to="search-lessons"
          sx={{ ...menu_item_style }}
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
        <MenuItem component={Link} to="" sx={{ ...menu_item_style }}>
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
        <MenuItem component={Link} to="" sx={{ ...menu_item_style }}>
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
        <MenuItem component={Link} to="/calendar" sx={{ ...menu_item_style }}>
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
        <MenuItem component={Link} to="/profile" sx={{ ...menu_item_style }}>
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
