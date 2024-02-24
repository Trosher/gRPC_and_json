from random import randint

from functools import wraps
from time import perf_counter
from loguru import logger

from concurrent.futures import ThreadPoolExecutor
import grpc
from proto import conf_pb2_grpc
from proto import conf_pb2
from gen import genDataShip

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


class RouteGuideServicer(conf_pb2_grpc.genShipServerServicer):
    @Loger
    def getShip(self, request, context):
        conf_pb2.allShip
        for _ in range(randint(0, 10)):
            ship = genDataShip()
            yield conf_pb2.allShip(alignment = ship['alignment'], name = ship['name'], clas = ship['class'],
                                   length = ship['length'], crewSize = ship['crew_size'], armed = ship['armed'],
                                   officers = ship['officers'])
        
@Loger
def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    conf_pb2_grpc.add_genShipServerServicer_to_server(RouteGuideServicer(), server)
    server.add_insecure_port('[::]:8888')
    server.start()
    server.wait_for_termination()
    
if __name__ == "__main__":
    logger.info("start server")
    serve()