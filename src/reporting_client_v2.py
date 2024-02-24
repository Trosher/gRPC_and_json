import argparse

from functools import wraps
from time import perf_counter
from loguru import logger

from pydantic import BaseModel, ValidationError, model_validator

import grpc
from ex00.server.proto import conf_pb2_grpc
from ex00.server.proto import conf_pb2

class shipCheck(BaseModel):
    aligment:str
    name:str
    clas:str
    length:float
    crewSize:int
    armed:bool
    officers:list[dict[str, str]]
    
    @model_validator(mode = "after")
    @classmethod
    def validationToShip(cls, values):
        def check(lengthParam, crewSizeParam, armedParam, aligmentParam):
            if not (lengthParam[0] <= values.length <= lengthParam[1] 
                    and crewSizeParam[0] <= values.crewSize <= crewSizeParam[1]
                    and True if armedParam == True else values.armed != True 
                    and True if aligmentParam == True else values.aligment != "Enemy"):
                raise ValueError("The ship is not valid")
            
        dict_valid_param = {'Corvette':[[80,250],[4,10],True,True],
                            'Frigate':[[300,600],[10,15],True,False],
                            'Cruiser':[[500,1000],[15,30],True,True],
                            'Destroyer':[[800,2000],[50,80],True,False],
                            'Carrier':[[1000,4000],[120,250],False,True],
                            'Dreadnought':[[5000,20000],[300,500],True,True]}
        args = dict_valid_param[values.clas]
        check(args[0],args[1],args[2],args[3])

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
                logger.info(f"Assert construct worked inside the function ({func.__name__})\n")
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

def checkShip(response):
    aligment = conf_pb2.eAlignment.Name(response.alignment)
    clas = conf_pb2.eClass.Name(response.clas)
    officers = [{'first_name' : j.first_name, 'last_name' : j.last_name, 'rank' : j.rank} for j in response.officers]
    return shipCheck(**{"aligment" : aligment, "name" : response.name, "clas" : clas,
                     "length" : response.length, "crewSize" : response.crewSize, "armed" : response.armed,
                     "officers" : officers})

def printAndCheckResponse(response):
    try:
        validShip = checkShip(response)
        print(validShip.model_dump_json(indent=2))
    except ValidationError:
        pass
    
@Loger
def main():
    parser = createArgParser()
    args = parser.parse_args()
    channel = grpc.insecure_channel('localhost:8888')
    stub = conf_pb2_grpc.genShipServerStub(channel)
    for response in stub.getShip(conf_pb2.cord(num0=args.Cord[0], num1=args.Cord[1], num2=args.Cord[2],
                                               num3=args.Cord[3], num4=args.Cord[4], num5=args.Cord[5])):
        printAndCheckResponse(response)
        
if __name__ == "__main__":
    logger.info("client server")
    main()