import React, { useEffect, useState } from 'react';
import Logo from '../../components/welcome/Logo';
import SplashScreens from '../../components/welcome/SplashScreens';

const WelcomePage = () => {
  const [isLogo, setIsLogo] = useState(true);

  useEffect(() => {
    setTimeout(() => setIsLogo(false), 2000);
  }, []);

  return isLogo ? <Logo /> : <SplashScreens />;
};

export default WelcomePage;
