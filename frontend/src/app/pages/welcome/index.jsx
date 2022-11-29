import React from 'react';
import { Link } from 'react-router-dom';

const WelcomePage = () => {
  const [isLogo, setIsLogo] = useState(true);

  useEffect(() => {
    setTimeout(() => setIsLogo(false), 2000);
  }, [])

  return isLogo ? <Logo /> : <SplashScreens />;
}
  
(
  <div>
    <h2>Splash screens</h2>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. At enim excepturi facere illo in ipsum itaque maxime modi natus nulla perferendis, porro quam quas repudiandae rerum sapiente, soluta voluptate voluptates!</p>
    <div>
      <Link to="/login">Login</Link>
    </div>
    <div>
      <Link to="/register">Register</Link>
    </div>
  </div>
);

export default WelcomePage;
