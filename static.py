# System imports
from os import makedirs as mkdirs
from datetime import datetime

# Global Variables
IP_ADDR = "192.168.43.92"
PORT = 1026
NOF_KEYS = 64


# Static Functions
def timestamp_generator():
    timestamp   = str(datetime.now())
    year        = timestamp[0:4]
    month       = timestamp[5:7]
    date        = timestamp[8:10]

    hour        = timestamp[11:13]
    minute      = timestamp[14:16]
    second      = timestamp[17:19]

    timestamp   = year + '-' + month + '-' + date + '-' + hour + '-' + minute + '-' + second

    return timestamp


def amtopm(rawtime):
    return datetime.strptime(rawtime, "%H-%M-%S").strftime("%I:%M:%S %p")


def create_user_files(userid):
    fileslist   = []

    dir1        = "images/" + userid + "/downloaded_img"
    dir2        = "images/" + userid + "/enc_img"
    dir3        = "images/" + userid + "/input_img"

    fileslist.append(dir1)
    fileslist.append(dir2)
    fileslist.append(dir3)
    for f in fileslist:
        mkdirs(f,exist_ok=True)

    print("User Files CREATED :) ")

