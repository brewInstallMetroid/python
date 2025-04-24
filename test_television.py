import pytest
from television import *


class Test:
    def setup_method(self):
        self.tv1 = Television()
    def teardown_method(self):
        del self.tv1


    def test___init__(self): #1.default values
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"


    def test_power(self): #1.tv on | 2.tv off
        self.tv1.power()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.tv1.power()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"


    def test_mute(self): #1.tv on, vup, mute | tv on, unmute | tv off, mute
        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.tv1.mute()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"

        self.tv1.power()
        self.tv1.mute()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"


    def test_channel_up(self): #1.tv off, cup | 2.tv on, cup | 3.tv on, cup past 3
        self.tv1.channel_up()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

        self.tv1.power()
        self.tv1.channel_up()
        assert self.tv1.__str__() == "Power = True, Channel = 1, Volume = 0"

        self.tv1.channel_up()
        self.tv1.channel_up()
        self.tv1.channel_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"


    def test_channel_down(self): #1.tv off, cdown | 2.tv on, cdown past 0
        self.tv1.channel_down()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

        self.tv1.power()
        self.tv1.channel_down()
        assert self.tv1.__str__() == "Power = True, Channel = 3, Volume = 0"


    def test_volume_up(self): #1.tv off, vup | 2.tv on, vup | 3.tv on, mute, vup | 4.vup past 2
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

        self.tv1.power()
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 1"

        self.tv1.mute()
        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 2"

        self.tv1.volume_up()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 2"


    def test_volume_down(self): #1.tv off, vdown | 2.tv on, vup, then vdown | 3.tv on, mute, vdown
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = False, Channel = 0, Volume = 0"

        self.tv1.power()
        self.tv1.volume_up()
        self.tv1.volume_up()
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 1"

        self.tv1.mute()
        self.tv1.volume_down()
        assert self.tv1.__str__() == "Power = True, Channel = 0, Volume = 0"
