import sensor

class Alarm(object):
    def __init__(self, given_sensor=None):
        self._sensor = given_sensor or sensor.Sensor()
        self._is_alarm_on = False
        self._low_pressure_threshold = 17
        self._high_pressure_threshold = 21

    @property
    def is_alarm_on(self):
        return self._is_alarm_on

    def check(self):
        current_pressure = self._sensor.sample_pressure()
        if current_pressure < self._low_pressure_threshold or current_pressure > self._high_pressure_threshold:
            self._is_alarm_on = True

