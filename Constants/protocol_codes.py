class RequestsCodes:
    CLIENT_REGISTRATION = 1024
    SERVER_REGISTRATION = 1025
    MESSAGES_SERVERS_LIST = 1026
    SYMMETRIC_KEY_REQUEST = 1027
    MSG_REQUEST = 1028
    SEND_MESSAGE = 1029


class ResponsesCodes:
    REGISTRATION_SUCCESS = 1600
    REGISTRATION_FAILURE = 1601
    MESSAGES_SERVERS_LIST = 1602
    SYMMETRIC_KEY_REQUEST = 1603
    SYMMETRIC_KEY_CONFIRMATION = 1604
    MESSAGE_CONFIRMATION = 1605


class ProtocolCodes:
    CLIENT_VERSION = 24


class Config:
    DEFAULT_PORT_NUMBER = 1256