from enum import Enum

class Tabs(Enum):
    Info = 0
    Encryptor = 1
    Keygen = 2
    
class EncryptionAlgo(Enum):
    sha256 = 0
    sha512 = 1
    TupleHash128 = 2
    TupleHash256 = 3
    BLAKE2s = 4
    BLAKE2b = 5