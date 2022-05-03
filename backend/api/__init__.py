from os import environ
from platform import system
from dotenv import load_dotenv
from vidgear.gears.asyncio import WebGear_RTC

from .log import logger, exception
from .decorators import for_all_methods

from src.manager.mongo_manager import connectToMongo, getDb
from src.manager.serial_manager import SerialManager
from src.manager.camera_manager import CameraManager
from src.nodes.serial.custom_serial import Serial
from src.nodes.serial.gcode_obj import SerialGcodeOBJ
from src.nodes.camera.custom_camera import Camera


load_dotenv()
environ.setdefault("SO", system())

connectToMongo()
dbo = getDb()


@exception(logger)
def Managers_Import(definitions):
    for collection, manager_class in definitions.items():
        for config in dbo.find_many(collection, {}):
            if not config.get("disabled", False):
                match config.get("is_gcode"):
                    case True:
                        manager_class["manager"].add(
                            manager_class["class"][1](**config)
                        )
                    case _:
                        manager_class["manager"].add(
                            manager_class["class"][0](**config)
                        )


mangers = {
    "camera-manager": {"manager": CameraManager, "class": [Camera]},
    "serial-manager": {"manager": SerialManager, "class": [Serial, SerialGcodeOBJ]},
}

options = {
    "custom_stream": CameraManager,
    "custom_data_location": "./",
    "frame_size_reduction": 50,
    "jpeg_compression_quality": 21,
}

Managers_Import(mangers)
CameraStreamer = WebGear_RTC(logging=True, **options)
