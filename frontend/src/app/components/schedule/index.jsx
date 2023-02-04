/* eslint-disable linebreak-style */
import React, { useEffect } from 'react';
import { Box } from '@mui/material';
import Header from '../header';
import ScheduleLessonCard from '../schedule-lesson-card';
import { useState } from 'react';
import getShedule from '../../services/shedule';
import LessonsService from '../../services/lessons';

const getDataForSchedule = (lesson) => {
  //const lessonName = LessonsService.getLesson(lesson.course)
  //  .then(response => response.data)
  //  .then(data => (data.data.base_course.name))

  const msStart = Date.parse(lesson.start_at);
  const msFinish = Date.parse(lesson.end_at);
  const newStart = new Date(msStart);
  const newFinish = new Date(msFinish);

  const [
    month,
    weekday,
    day,
    startHour,
    startMinutes,
    finishHour,
    finishMinutes,
  ] = [
    newStart.getMonth(),
    newStart.getDay(),
    newStart.getDate(),
    newStart.getHours(),
    newStart.getMinutes(),
    newFinish.getHours(),
    newFinish.getMinutes(),
  ];

  const dayOfWeek = {
    1: 'ПН',
    2: 'ВТ',
    3: 'СР',
    4: 'ЧТ',
    5: 'ПТ',
    6: 'СБ',
    0: 'ВС',
  };

  const normalizeDate = (num, type) => {
    if (num <= 9) {
      return type === 'month' ? `0${num + 1}` : `0${num}`;
    }
    return num;
  };

  const getTimeInterval = () => {
    const startTime = `${normalizeDate(startHour, 'hour')}:${normalizeDate(
      startMinutes,
      'minutes'
    )}`;
    const finishTime = `${normalizeDate(finishHour, 'hour')}:${normalizeDate(
      finishMinutes,
      'minutes'
    )}`;
    const timeInterval = `${startTime} - ${finishTime}`;
    return timeInterval;
  };

  return {
    name: 'Wait name',
    weekday: dayOfWeek[weekday],
    date: `${normalizeDate(day, 'day')}.${normalizeDate(month, 'month')}`,
    timeInterval: getTimeInterval(),
  };
};

const ScheduleLessons = () => {
  const [lessons, setLessons] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  useEffect(() => {
    getShedule()
      .then(response => {
        const data = response.data.data;
        const filteredData = data.sort((a,b) => new Date(a.start_at) - new Date(b.start_at))
        setLessons(filteredData)
      })
      .catch(err => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  const lessonsData = lessons.map((lesson) => {
    const dataForLesson = getDataForSchedule(lesson);
    return (
      <ScheduleLessonCard
        name={dataForLesson.name}
        weekday={dataForLesson.weekday}
        date={dataForLesson.date}
        timeInterval={dataForLesson.timeInterval}
        key={lesson.id}
      />
    );
  })

  return (
    <Box
      sx={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      }}
    >
      <Header title='Календарь' />
      {lessonsData}
    </Box>
  );
};

export default ScheduleLessons;
