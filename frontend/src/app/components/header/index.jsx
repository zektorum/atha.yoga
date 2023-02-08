import React, { useState } from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import {
  AppBar, Typography, Stack, Badge, Toolbar, Menu, MenuItem, Avatar, Box,
} from '@mui/material';
import Divider from '@mui/material/Divider';

import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import NotificationsNoneIcon from '@mui/icons-material/NotificationsNone';
import ExpandMoreOutlinedIcon from '@mui/icons-material/ExpandMoreOutlined';
import SettingsOutlinedIcon from '@mui/icons-material/SettingsOutlined';
import DriveFileRenameOutlineOutlinedIcon from '@mui/icons-material/DriveFileRenameOutlineOutlined';
import InfoOutlinedIcon from '@mui/icons-material/InfoOutlined';
import LogoutOutlinedIcon from '@mui/icons-material/LogoutOutlined';

import useAuth from '../../utils/hooks/useAuth';

import menuAvatar from '../../../assets/public/menu-avatar.png';

const menuItems = [
  {
    title: 'Настройки',
    icon: <SettingsOutlinedIcon fontSize="medium" sx={{ color: '#9E9E9E', transform: 'translateY(-1px)', mr: '14px' }} />,
    link: '/settings',
  },
  {
    title: 'Журнал',
    icon: <DriveFileRenameOutlineOutlinedIcon fontSize="medium" sx={{ color: '#9E9E9E', transform: 'translateY(-1px)', mr: '14px' }} />,
    link: '#',
  },
  {
    title: 'О проекте',
    icon: <InfoOutlinedIcon fontSize="medium" sx={{ color: '#9E9E9E', transform: 'translateY(-1px)', mr: '14px' }} />,
    link: '#',
  },
];

const Header = ({ title, withBackBtn = false }) => {
  const auth = useAuth();
  const navigate = useNavigate();
  const [anchorEl, setAnchorEl] = useState(null);

  const openMenu = Boolean(anchorEl);
  const handleMenuClick = event => {
    setAnchorEl(event.currentTarget);
  };
  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  return (
    <AppBar
      position="sticky"
      color="default"
      sx={{ boxShadow: '0px 8px 16px rgba(46, 60, 80, 0.1)', backgroundColor: '#fff' }}
    >
      <Toolbar
        sx={{
          display: 'flex',
          justifyContent: 'space-between',
        }}
      >
        <Stack direction="row" alignItems="center" spacing={1} color="text.secondary">
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
        <Stack alignItems="center" direction="row">
          <Badge color="error" variant="dot" sx={{ mr: '20px', '& .MuiBadge-badge': { top: '2px', right: '2px' } }}>
            <NotificationsNoneIcon fontSize="large" sx={{ color: '#9E9E9E', height: '28px', width: '28px' }} />
          </Badge>
          <Avatar
            sx={{
              width: '30px',
              height: '30px',
              backgroundImage: `url(${menuAvatar})`,
              backgroundRepeat: 'no-repeat',
              backgroundSize: 'cover',
              backgroundPosition: 'center',
              mr: { xs: '4px', sm: '8px' },
            }}
          />
          <Box
            id="basic-button"
            aria-controls={openMenu ? 'basic-menu' : undefined}
            aria-haspopup="true"
            aria-expanded={openMenu ? 'true' : undefined}
            onClick={handleMenuClick}
            sx={{ display: 'flex', cursor: 'pointer' }}
          >
            <Typography color="text.secondary" sx={{ fontSize: '16px', display: { xs: 'none', sm: 'block' } }}>username</Typography>
            <ExpandMoreOutlinedIcon
              fontSize="medium"
              sx={{ color: '#9E9E9E' }}
            />
          </Box>
          <Menu
            id="basic-menu"
            anchorEl={anchorEl}
            open={openMenu}
            onClose={handleMenuClose}
            sx={{ top: '12px' }}
            MenuListProps={{
              'aria-labelledby': 'basic-button',
            }}
          >
            {menuItems.map(el => (
              <div key={el.title}>
                <MenuItem
                  component={NavLink}
                  to={el.link}
                  sx={{ fontSize: '16px', minWidth: '220px' }}
                  onClick={handleMenuClose}
                >
                  {el.icon}
                  <Typography sx={{ fontSize: '16px' }}>{el.title}</Typography>
                </MenuItem>
                <Divider sx={[el.title === 'О проекте' && { borderColor: '#fff' }]} />
              </div>
            ))}
            <MenuItem sx={{ fontSize: '16px', minWidth: '220px' }}>
              <LogoutOutlinedIcon fontSize="medium" sx={{ color: '#9E9E9E', transform: 'translateY(-1px)', mr: '14px' }} />
              <Typography
                variant="body2"
                onClick={auth.logout}
                sx={{ fontSize: '16px' }}
              >
                Выход
              </Typography>

            </MenuItem>
          </Menu>
        </Stack>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
