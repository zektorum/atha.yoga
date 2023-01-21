import React, {useState} from 'react';
import {Avatar, Badge, Button, Grid, Stack,} from '@mui/material';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import SettingsOutlinedIcon from '@mui/icons-material/SettingsOutlined';
import NotificationsNoneIcon from '@mui/icons-material/NotificationsNone';
import {Link} from 'react-router-dom';
import background from '../../../assets/public/profile_background.jpg';
import avatar from '../../../assets/public/profile_avatar.jpg';

import './index.scoped.scss';

const Profile = () => {
  const [openText, setOpenText] = useState(true);

  return (
    <>
      <Grid
        item
        display="flex"
        flexDirection="row"
        alignItems="center"
        justifyContent="space-between"
        sx={{
          width: '100%', height: '64px', px: '29px', boxShadow: '0px 8px 16px rgba(46, 60, 80, 0.1)',
        }}
      >
        <Typography fontSize="20px" fontWeight="500" color="text.secondary">
          Профиль
        </Typography>
        <Stack alignItems="center" direction="row" spacing={2}>
          <Badge color="error" variant="dot">
            <NotificationsNoneIcon fontSize="medium" color="disabled" />
          </Badge>
          <Link to="/settings">
            <SettingsOutlinedIcon color="disabled" sx={{ transform: 'translateY(3px)' }} />
          </Link>
        </Stack>
      </Grid>
      <Card sx={{ height: '90%' }}>
        <CardMedia
          component="img"
          height="168"
          image={background}
          alt="user's background"
        />
        <CardContent>
          <Avatar
            src={avatar}
            sx={{
              width: 128, height: 128, marginTop: '-80px', marginLeft: '30px', marginBottom: '12px',
            }}
          />
          <Typography variant="iter_h1" sx={{ paddingBottom: '3px', display: 'block' }}>Иван Иванов</Typography>
          <Typography
            variant="iter_h2"
            sx={{ paddingBottom: '20px', color: '#6C757D', display: 'block' }}
          >
            @ivan
          </Typography>
          <Typography variant="iter_h2" paragraph noWrap={openText}>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto corporis id
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto corporis id
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto corporis id
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto corporis id
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto corporis id
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto corporis id
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto corporis id
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto corporis id
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto corporis id
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto corporis id
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto corporis id
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Iusto corporis id
          </Typography>
          <Button
            variant="text"
            size="small"
            sx={{ textTransform: 'none', left: '90%', position: 'relative' }}
            onClick={() => setOpenText(!openText)}
          >
            {openText === true ? 'больше' : 'меньше'}
          </Button>
        </CardContent>
      </Card>
    </>
  );
};

export default Profile;
