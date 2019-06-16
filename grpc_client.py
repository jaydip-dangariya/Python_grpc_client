from __future__ import print_function
import logging

import grpc
from pprint import pprint
import UserService_pb2
import UserService_pb2_grpc
import sys
import random
import uuid

# Jaydip Dangariya

def run():
    channel = grpc.insecure_channel('localhost:8080')
    stub = UserService_pb2_grpc.UserServiceStub(channel)
    arguments = int(sys.argv[1])

    # add user
    if arguments == 0:
        # Not implemented correctly
        #hobbies = ['Reading' + str(random.random()), 'Listing' + str(random.random())]
        #name = "Jaydip" + str(uuid.uuid1())
        # stub.addUser(UserService_pb2.AddUserRequest())
        print('User inserted')

    # get all users
    if arguments == 1:
        response = stub.getAllUser(UserService_pb2.GetAllUserRequest())
        print("User client received: " + str(response))


if __name__ == '__main__':
    logging.basicConfig()
    run()