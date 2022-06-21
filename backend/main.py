from multiprocessing import context
from os import environ
import uvicorn
import socket

from api import logger, dbo
from api.queries import query
from api.subscriptions import subscription
from api.mutations import mutation

from src.end_points import custom_video_response, Echo, Controls
from src.nodes.node_manager import NodeManager
from src.manager.serial_manager import SerialManager
from src.manager.camera_manager import CameraManager
from src.nodes.process.process import process
from starlette.routing import Route

from ariadne.asgi import GraphQL
from ariadne import (
    load_schema_from_path,
    make_executable_schema,
    snake_case_fallback_resolvers,
)

from starlette.middleware.cors import CORSMiddleware
from starlette.routing import Mount, WebSocketRoute
from starlette.applications import Starlette
from starlette.middleware import Middleware

type_defs = ""
for _file in ["schema", "inputs", "types", "results"]:
    type_defs += load_schema_from_path(f"./src/graphql/{_file}.graphql") + ("\n" * 2)


schema = make_executable_schema(
    type_defs, query, mutation, subscription, snake_case_fallback_resolvers
)


routes_app = [
    Route(
        "/videos/{video_id}", endpoint=custom_video_response, methods=["GET", "POST"]
    ),
    WebSocketRoute("/ws", endpoint=Echo),
    WebSocketRoute("/process", endpoint=process.websocket),
    *[WebSocketRoute(f"/controls/{serial._id}", endpoint=serial.websocket) for serial in SerialManager.get()],
    Mount(
        "/",
        app=CORSMiddleware(
            GraphQL(schema, debug=True),
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        ),
    )
]

app = Starlette(debug=True, routes=routes_app, on_shutdown=[dbo.close])

@app.on_event("shutdown")
def shutdown_event():
    try:
        CameraManager.stop()
    except Exception as e:
        logger.error(e)

port = environ.get("SERVER_PORT", 80)
if environ.get("NODE_ENV") == "development":
    socketI = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    socketI.connect(("8.8.8.8", 80))
    host = socketI.getsockname()[0]
    socketI.close()
elif environ.get("SERVER_IP"):
    host = environ["SERVER_IP"]
else:
    host = "0.0.0.0"

if __name__ == "__main__":
    try:
        uvicorn.run(app=app, host=host, port=int(port), log_level=logger.level)
    finally:
        CameraManager.stop()
        dbo.close()
