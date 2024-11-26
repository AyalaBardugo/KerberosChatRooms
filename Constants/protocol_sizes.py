class HeaderSize:
    PAYLOAD_SIZE = 23
    CLIENT_ID = 16
    VERSION = 1
    CODE = 2
    PAYLOAD = 4
    HEADER_PAYLOAD_SIZE_OFFSET = 3
    HEADER_PAYLOAD_SIZE_FORMAT = '<I'
    BYTE_SIZE = 8


class ProtocolSizes:
    CLIENT_NAME = 255
    PASSWORD = 255
    ENCRYPTED_KEY = 56
    ENCRYPTED_KEY_IV = 16
    AES_KEY = 32
    SERVER_ID = 16
    NONCE = 8
    CLIENT_ID = 16
    SYMMETRIC_KEY = 32
    TICKET = 121
    CREATION_TIME = 8
    TICKET_IV = 16
    EXPIRATION_TIME = 10
    KEY_SIZE = 32
    BLOCK_SIZE = 16
    STREAM_SIZE = 1024
    IV = 16
    AUTHENTICATOR_SIZE = 112
    MESSAGE = 4
    PADDED_VERSION = 16
    KEY_OFFSET = 48
    TIME_OFFSET = 16


class ResponseSize:
    VERSION = 1
    CODE = 2
    PAYLOAD = 4


# Message Server requests
class MSRequestsSize:
    AUTHENTICATOR = 57
    AUTHENTICATOR_IV = 16
