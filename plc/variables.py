DB_TAGS = 1000
TAG_SIZE = 78

TAGS_COUNT_SIZE = 2

NAME_OFFSET = 0
NAME_SIZE = 32

TYPE_OFFSET = NAME_OFFSET + NAME_SIZE
TYPE_SIZE = 32

USE_OFFSET = TYPE_OFFSET + TYPE_SIZE
USE_SIZE = 7

READ_ONLY_OFFSET = USE_OFFSET + USE_SIZE
READ_ONLY_SIZE = 1

DB_NUMBER_OFFSET = READ_ONLY_OFFSET + READ_ONLY_SIZE
DB_NUMBER_SIZE = 2

OFFSETBYTE_OFFSET = DB_NUMBER_OFFSET + DB_NUMBER_SIZE
OFFSETBYTE_SIZE = 2

OFFSETBIT_OFFSET = OFFSETBYTE_OFFSET + OFFSETBYTE_SIZE

