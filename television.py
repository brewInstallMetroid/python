class Television():
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3


    def __init__ (self) -> None:
        '''
        Method declaring and containing default tv status values
        '''
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__volume_storage = 0


    def power(self) -> None:
        '''
        Method to turn tv off/on, changing self.__status
        '''
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False


    def mute(self) -> None:
        '''
        Method to save current volume value, then mute or unmute tv
        '''
        if self.__status:
            self.__volume_storage = self.__volume
            if self.__muted == False:
                self.__volume = Television.MIN_VOLUME
                self.__muted = True
            else:
                self.__volume = self.__volume_storage
                self.__muted = False


    def channel_up(self) -> None:
        '''
        Method for increasing tv channel, looping if channel is increased past Television.MAX_CHANNEL
        '''
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL


    def channel_down(self) -> None:
        '''
        Method for decreasing tv channel, looping if channel is decreased past Television.MIN_CHANNEL
        '''
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL


    def volume_up(self) -> None:
        '''
        Method for increasing volume/unmuting + increasing volume
        '''
        if self.__status:
            if self.__muted == True:
                self.__volume = self.__volume_storage
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1


    def volume_down(self) -> None:
        '''
        Method for decreasing volume/unmuting + decreasing volume
        '''
        if self.__status:
            if self.__muted == True:
                self.__volume = self.__volume_storage
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1


    def __str__(self) -> str:
        '''
        Method to display all tv statuses
        :return: all tv statuses
        '''
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"