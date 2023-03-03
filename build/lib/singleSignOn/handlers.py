from todo_app.proto import todo_pb2_grpc
from todo_app.services import TodoService


def grpc_handlers(server):
    todo_pb2_grpc.add_TodoControllerServicer_to_server(
        TodoService.as_servicer(), server
    )
