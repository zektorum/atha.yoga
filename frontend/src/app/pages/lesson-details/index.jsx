import React from 'react';
import {
  Box, Button, Typography, Avatar,
} from '@mui/material';
import SettingsIcon from '@mui/icons-material/Settings';
import ArrowBackIcon from '@mui/icons-material/ArrowBack';
import { Link } from 'react-router-dom';
import FavoriteIcon from '@mui/icons-material/Favorite';
import StarOutlineIcon from '@mui/icons-material/StarOutline';
import ModeCommentOutlinedIcon from '@mui/icons-material/ModeCommentOutlined';
import avatar from '../../../assets/public/profile_avatar.jpg';

const LessonDetailsPage = () => {
  const isWrap = false;
  return (
    <>
      <Box
        display="flex"
        flexDirection="row"
        alignItems="center"
        justifyContent="space-between"
        sx={{
          width: '100%', minHeight: '64px', px: '29px', boxShadow: '0px 8px 16px rgba(46, 60, 80, 0.1)', mb: '32px',
        }}
      >
        <Typography component={Link} to="/search-lessons" fontSize="24px" fontWeight="500" color="text.secondary" sx={{ textDecoration: 'none' }}>
          <ArrowBackIcon sx={{ mr: '14px', verticalAlign: '-2px' }} fontSize="medium" color="action" />
          Назад
        </Typography>
        <SettingsIcon color="disabled" />
      </Box>
      <Box
        display="flex"
        margin="0 auto"
        justifyContent="center"
        flexDirection="column"
      >
        <Box display="flex" alignItems="start" gap="16px" mb="8px">
          <Typography width="827px" variant="h4" fontSize="24px">
            Хатха-йога для начинающих, поддерживающая тело и дух в отличной форме
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
          <Typography variant="h4" fontSize="24px" mr="16px">₽ 350</Typography>
          <StarOutlineIcon sx={{ color: '#FF9800' }} />
          <Typography variant="h4" fontSize="16px">4.8</Typography>
          <Typography variant="h4" fontSize="16px" color="#BDBDBD" mr="16px">(505) оценок</Typography>
          <ModeCommentOutlinedIcon sx={{ color: '#616161' }} />
          <Typography>505</Typography>
        </Box>
        <Box width="982px" minHeight="176px" display="flex" flexDirection="column" mb="32px">
          <Typography fontSize="16px" noWrap={isWrap}>
            Хатха йога идеальна для начинающих и практикующих.
            Начав заниматься хатха йогой, вы полюбите этот стиль за простоту и эффективность.
            Практикуя йогу, вы станете на путь обретения равновесия и духовного роста.
            Асаны не только воздействуют на мышцы тела, но и стимулируют
            выработку гормонов, массируют внутренние органы брюшной полости человека.
            Контроль за дыханием в йоге — один из наиболее важных элементов практики.
            Дыхательные упражнения (Пранаямы) учат управлять своими эмоциями,
            контролировать состояние, помогают правильно функционировать сердечно-сосудистой
            и другим системам организма. Ведь неправильное дыхание, спазмы, блоки и
            зажимы - одна из главных причин многих болезней...
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
        <Typography
          display="flex"
          alignItems="center"
          justifyContent="flex-start"
          gap="6px"
          fontSize="16px"
          mb="56px"
        >
          <Avatar
            src={avatar}
            sx={{
              width: '40px', height: '40px',
            }}
          />
          Иван Иванов
        </Typography>
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
      </Box>
    </>
  );
};

export default LessonDetailsPage;
