class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        ''' 
        Initializes the Television object with default values:
        - Muted status set to False
        - Volume set to MIN_VOLUME
        - Channel set to MIN_CHANNEL
        - Power status set to False (off)
        '''
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__status = False

    ''' 
    Toggles the power status of the television.
    If the TV is off, it turns on; if it is on, it turns off.
    '''
    def power(self) -> None:
        self.__status = not self.__status

    ''' 
    Toggles the muted status of the television.
    Only affects the TV if it is currently on.
    '''
    def mute(self) -> None:
        if self.__status:
            self.__muted = not self.__muted

    ''' 
    Increases the channel by 1.
    Wraps around to MIN_CHANNEL if the current channel exceeds MAX_CHANNEL.
    Only affects the TV if it is currently on.
    '''
    def channel_up(self) -> None:
        if self.__status:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    ''' 
    Decreases the channel by 1.
    Wraps around to MAX_CHANNEL if the current channel is at MIN_CHANNEL.
    Only affects the TV if it is currently on.
    '''
    def channel_down(self) -> None:
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    ''' 
    Increases the volume by 1.
    Unmutes the TV if it is muted.
    Does not exceed MAX_VOLUME.
    Only affects the TV if it is currently on.
    '''
    def volume_up(self) -> None:
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    ''' 
    Decreases the volume by 1.
    Unmutes the TV if it is muted.
    Does not go below MIN_VOLUME.
    Only affects the TV if it is currently on.
    '''
    def volume_down(self) -> None:
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    ''' 
    Returns a string representation of the television's current state,
    including power status, channel, and volume.
    '''
    def __str__(self) -> str:
        power_status = "True" if self.__status else "False"
        volume_status = Television.MIN_VOLUME if self.__muted else self.__volume
        return f'Power = {power_status}, Channel = {self.__channel}, Volume = {volume_status}'

