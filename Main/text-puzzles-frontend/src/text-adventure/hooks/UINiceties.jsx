import { useEffect, useRef } from 'react';

const scrollOnUpdate = (dependency) => {
  const ref = useRef(null);

  useEffect(() => {
    if (ref.current) {
      ref.current.scrollTop = ref.current.scrollHeight;
    }
  }, [dependency]);

  return ref;
};

export default scrollOnUpdate;