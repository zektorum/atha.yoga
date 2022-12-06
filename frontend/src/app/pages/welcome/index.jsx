import React, { useEffect, useState } from 'react';
import Logo from '../../components/logo/index.jsx';
import SplashScreens from '../../components/splash-screens/index.jsx';

const WelcomePage = () => {
  const [isLogo, setIsLogo] = useState(true);

  useEffect(() => {
    setTimeout(() => setIsLogo(false), 2000);
  }, []);

  return isLogo ? <Logo /> : <SplashScreens />;
};

export default WelcomePage;
