import { useEffect, useState } from 'react';
import axios from 'axios';
import { getData } from '../../../services/api';

const usePutRequest = (url, payload) => {
  const [data, setData] = useState(null);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.put(url, payload)
      .then(response => setData(getData(response)))
      .catch(err => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  return { data, error, loading };
};

export default usePutRequest;
