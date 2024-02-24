import argparse
from json import dumps

from functools import wraps
from time import perf_counter
from loguru import logger

import grpc
from server.proto import conf_pb2_grpc
from server.proto import conf_pb2

def Loger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = None
        logger.info(f"function start: ({func.__name__}) with parameters: {args} :\n")
        start = perf_counter()
        try:
            result = func(*args, **kwargs)
            logger.info(f"The function ({func.__name__}) ended with the result: {result}")
            logger.info(f"The function ({func.__name__}) has been completed for {(perf_counter() - start):.4f}\n")
        except Exception:
            logger.exception(f"the function ({func.__name__}) ended with an error\n")
        return result
    return wrapper

@Loger
def createArgParser():
    parser = argparse.ArgumentParser(prog="ServerClient", 
                                     description="Submits coordinates to the server and gets the list of ships in the stream",
                                     epilog="The client cannot be used without the transferred instruments")
    parser.add_argument("Cord", nargs = 6, type = float,
                         help = "The coordinates should be passed through a space as fractional natural numbers in the amount of 6 pcs")

    return parser

def printJson(response):
    aligment = conf_pb2.eAlignment.Name(response.alignment)
    classs = conf_pb2.eClass.Name(response.clas)
    officers = [{'first_name' : j.first_name, 'last_name' : j.last_name, 'rank' : j.rank} for j in response.officers]
    print(dumps({"alignment": aligment, "name": response.name, "class": classs, 
                 "length": response.length, "crew_size": response.crewSize, "armed": response.armed, 
                 "officers": officers}, indent=4, sort_keys=True))
    
@Loger
def main():
    parser = createArgParser()
    args = parser.parse_args()
    channel = grpc.insecure_channel('localhost:8888')
    stub = conf_pb2_grpc.genShipServerStub(channel)
    for response in stub.getShip(conf_pb2.cord(num0=args.Cord[0], num1=args.Cord[1], num2=args.Cord[2],
                                               num3=args.Cord[3], num4=args.Cord[4], num5=args.Cord[5])):
        printJson(response)
        
if __name__ == "__main__":
    logger.info("client server")
    main()