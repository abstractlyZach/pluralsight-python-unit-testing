import pytest
import unittest.mock as mock

import alarm
import sensor

@pytest.fixture
def alarm_object():
    return alarm.Alarm()

def test_alarm_creation_raises_no_exceptions(alarm_object):
    pass

def test_alarm_is_off_by_default(alarm_object):
    assert not alarm_object.is_alarm_on

def test_pressure_too_low_sounds_alarm():
    test_sensor = TestSensor(15)
    test_alarm = alarm.Alarm(given_sensor=test_sensor)
    test_alarm.check()
    assert test_alarm.is_alarm_on

def test_pressure_too_high_sounds_alarm():
    test_sensor = TestSensor(30)
    test_alarm = alarm.Alarm(given_sensor=test_sensor)
    test_alarm.check()
    assert test_alarm.is_alarm_on

def test_pressure_normal_does_not_sound_alarm():
    test_sensor = TestSensor(20)
    test_alarm = alarm.Alarm(given_sensor=test_sensor)
    test_alarm.check()
    assert not test_alarm.is_alarm_on

def test_pressure_normal_does_not_sound_alarm_with_mock():
    test_sensor = mock.Mock(sensor.Sensor)
    test_sensor.sample_pressure.return_value = 18
    test_alarm = alarm.Alarm(given_sensor=test_sensor)
    test_alarm.check()
    assert not test_alarm.is_alarm_on



class TestSensor(object):
    def __init__(self, pressure):
        self._pressure = pressure

    def sample_pressure(self):
        return self._pressure
