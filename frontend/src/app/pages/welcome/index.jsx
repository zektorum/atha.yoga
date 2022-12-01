import React, { useEffect, useState } from 'react';
import Logo from '../../components/Logo';
import SplashScreens from '../../components/SplashScreens';

const WelcomePage = () => {
  const [isLogo, setIsLogo] = useState(true);

  useEffect(() => {
    setTimeout(() => setIsLogo(false), 2000);
  }, []);

  return isLogo ? <Logo /> : <SplashScreens />;
};

export default WelcomePage;
