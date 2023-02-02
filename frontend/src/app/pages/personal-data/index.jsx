import React from 'react';
import { Box, Container } from '@mui/material';
import Header from '../../components/header';
import PersonDataTeacher from '../../components/personal-data/teacher';
import PersonDataStudent from '../../components/personal-data/student';

const PersonDataPage = () => {
  const userDataLocal = (JSON.parse(localStorage.getItem('user'))).user;
  return (
    <Box>
      <Header withBackBtn />
      <Container>
        <Box display="flex" justifyContent="center">
          {userDataLocal.public_teacher_profiles ? <PersonDataTeacher /> : <PersonDataStudent />}
        </Box>
      </Container>
    </Box>
  );
};

export default PersonDataPage;
