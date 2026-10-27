import grpc
from src.grpc import inventory_pb2, inventory_pb2_grpc


class GrpcClient:
    def __init__(self, host: str = "localhost", port: int = 50051):
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = inventory_pb2_grpc.InventoryServiceStub(self.channel)

    def get_stock(self, request: inventory_pb2.GetStockRequest) -> inventory_pb2.GetStockResponse:
        return self.stub.GetStock(request)

    def reserve_stock(self, request: inventory_pb2.ReserveStockRequest) -> inventory_pb2.ReserveStockResponse:
        return self.stub.ReserveStock(request)

    def close(self):
        self.channel.close()
