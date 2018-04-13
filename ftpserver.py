# System imports
import sqlite3 as db
import subprocess
import os,sys


# Package imports
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Local Imports
from static import IP_ADDR, PORT


def create_server():
    authorizer      = DummyAuthorizer()
    conn            = db.connect("main.db")
    ftprootdir      = str(os.getcwd()) + "/recv_img/"

    user_details    = conn.cursor().execute("SELECT * FROM login")
    for user in user_details:
        ftpuserrootdir = ftprootdir + user[0]
        authorizer.add_user(user[0],user[1],ftprootdir, perm="elradfmw")
        os.makedirs(ftpuserrootdir, exist_ok=True)
        print("[ " + user[0] + " ]'s\t\t\tFTP_ROOT_DIRECTORY created :) ")

    handler = FTPHandler
    handler.authorizer = authorizer

    server = FTPServer((IP_ADDR,PORT),handler)
    server.serve_forever()


if __name__ == "__main__":
    create_server()
