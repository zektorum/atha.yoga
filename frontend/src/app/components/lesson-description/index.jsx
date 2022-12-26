/* eslint-disable react/prop-types */
import React from 'react';
import {
  Box, Button, Typography, Avatar,
} from '@mui/material';
import { Link } from 'react-router-dom';
import FavoriteIcon from '@mui/icons-material/Favorite';
import StarOutlineIcon from '@mui/icons-material/StarOutline';
import ModeCommentOutlinedIcon from '@mui/icons-material/ModeCommentOutlined';
import avatar from '../../../assets/public/profile_avatar.jpg';

const LessonDescription = ({ title, description, price }) => (
  <>
    <Box display="flex" alignItems="start" gap="16px" mb="8px">
      <Typography width="827px" variant="h4" fontSize="24px">
        {title}
      </Typography>
      <Typography
        display="flex"
        alignItems="center"
        justifyContent="center"
        fontSize="13px"
        sx={{
          height: '24px', width: '99px', p: '3px 4px', color: '#ffffff', background: '#4CAF50', borderRadius: '16px',
        }}
      >
        Вы участник
      </Typography>
      <FavoriteIcon sx={{ color: '#E91E63' }} />
    </Box>
    <Typography display="flex" alignItems="center" fontSize="14px" color="text.secondary" mb="32px">
      Начинающий • Средний • Продвинутый
    </Typography>
    <Box display="flex" alignItems="center" flexWrap="wrap" gap="3px" mb="32px">
      <Typography variant="h4" fontSize="24px" mr="16px">
        ₽
        {' '}
        {price}
      </Typography>
      <StarOutlineIcon sx={{ color: '#FF9800' }} />
      <Typography variant="h4" fontSize="16px">4.8</Typography>
      <Typography variant="h4" fontSize="16px" color="#BDBDBD" mr="16px">(505) оценок</Typography>
      <ModeCommentOutlinedIcon sx={{ color: '#616161' }} />
      <Typography>505</Typography>
    </Box>
    <Box width="982px" maxHeight="176px" display="flex" flexDirection="column" mb="32px">
      <Typography fontSize="16px" noWrap={false}>
        {description}
      </Typography>
      <Typography component={Link} fontSize="16px" color="primary" sx={{ textDecoration: 'none' }}>
        Показать еще
      </Typography>
      <Typography />
    </Box>
    <Box display="flex" flexDirection="column" gap="8px" mb="32px">
      <Box display="flex" flexDirection="row" gap="8px">
        <Typography
          display="flex"
          alignItems="center"
          justifyContent="center"
          fontSize="13px"
          sx={{ width: '111px', background: '#EEEEEE', borderRadius: '16px' }}
        >
          Пн 14:30-15:30
        </Typography>
        <Typography
          display="flex"
          alignItems="center"
          justifyContent="center"
          fontSize="13px"
          sx={{ width: '111px', background: '#EEEEEE', borderRadius: '16px' }}
        >
          Пн 15:30-16:30
        </Typography>
        <Typography
          display="flex"
          alignItems="center"
          justifyContent="center"
          fontSize="13px"
          sx={{ width: '111px', background: '#EEEEEE', borderRadius: '16px' }}
        >
          Пн 17:30-18:30
        </Typography>
      </Box>
      <Typography
        display="flex"
        alignItems="center"
        justifyContent="center"
        fontSize="13px"
        sx={{ width: '111px', background: '#EEEEEE', borderRadius: '16px' }}
      >
        Ср 14:30-15:30
      </Typography>
      <Button
        component={Link}
        color="primary"
        sx={{
          width: '174px', p: '4px 5px', fontSize: '13px', fontWeight: '500',
        }}
      >
        Показать расписание
      </Button>
    </Box>
    <Box display="flex" alignItems="center" flexWrap="wrap" gap="6px" mb="56px">
      <Avatar
        src={avatar}
        sx={{
          width: '40px', height: '40px',
        }}
      />
      <Typography
        fontSize="16px"
      >
        Иван Иванов
      </Typography>
    </Box>
    <Box display="flex" justifyContent="flex-end">
      <Button
        variant="contained"
        sx={{
          fontSize: '16px', fontWeight: '500', width: '227px',
        }}
      >
        Записаться
      </Button>
    </Box>
  </>
);

export default LessonDescription;
