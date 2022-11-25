from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, SimpleRateThrottle

DENIED_DURATION = 600


class CustomUserRateThrottle(UserRateThrottle):
    def throttle_success(self):
        """
        Inserts the current request's timestamp along with the key
        into the cache.
        """
        self.duration = DENIED_DURATION
        self.history.insert(0, self.now)
        self.cache.set(self.key, self.history, self.duration)
        return True

    def wait(self):
        """
        Returns the recommended next request time in seconds.
        """
        self.duration = DENIED_DURATION
        if self.history:
            remaining_duration = self.duration - (self.now - self.history[-1])
        else:
            remaining_duration = self.duration

        available_requests = self.num_requests - len(self.history) + 1
        if available_requests <= 0:
            return None

        return remaining_duration / float(available_requests)


class CustomAnonRateThrottle(AnonRateThrottle):
    def throttle_success(self):
        """
        Inserts the current request's timestamp along with the key
        into the cache.
        """
        self.duration = DENIED_DURATION
        self.history.insert(0, self.now)
        self.cache.set(self.key, self.history, self.duration)
        return True

    def wait(self):
        """
        Returns the recommended next request time in seconds.
        """
        self.duration = DENIED_DURATION
        if self.history:
            remaining_duration = self.duration - (self.now - self.history[-1])
        else:
            remaining_duration = self.duration

        available_requests = self.num_requests - len(self.history) + 1
        if available_requests <= 0:
            return None

        return remaining_duration / float(available_requests)
