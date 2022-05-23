from .models import NodeSheet, grok
from ariadne import QueryType
from src.nodes.node_manager import NodeManager
from src.nodes.node_registry import NodeRegistry
from threading import enumerate as thread_enumerate
from src.manager.camera_manager import CameraManager
from src.manager.serial_manager import SerialManager
from src.nodes.calibration.camera_calibration import CameraCalibration
from threading import Thread

query = QueryType()

payload = {"success": False, "errors": None}


@query.field("getNodeSheet")
def getNodeSheet_resolver(obj, info, **kwargs):
    """Get a NodeSheet by id and return it like a payload"""
    result = NodeSheet().getNodeSheetById(_id=kwargs.get("_id"))
    payload["success"] = True
    payload["data"] = result
    return payload


@query.field("allPhotos")
def resolve_allPhotos(obj, info, **kwargs):
    """Get all photos from the database"""
    payload = [{"filename": "a.png", "path": "imgs/a.png"}]
    return payload


@query.field("getSerials")
def resolve_getSerials(obj, info, **kwargs):
    return {"status": True, "data": SerialManager.get()}


@query.field("getCameras")
def resolve_getCameras(obj, info, **kwargs):
    return {"status": True, "data": CameraManager.get()}


@query.field("getSketchList")
def resolve_get_sketch_list(obj, info):
    returns = list(NodeSheet().get_sketch_list())
    return {"status": True, "data": returns}


@query.field("getNodeInfo")
def resolve_getNodeInfo(obj, info, node_type, **kwargs):
    """Get a Node by id and return it like a payload"""
    result = (NodeRegistry.getNodeClassByName(node_type)).get_info(**kwargs.get("kwargs", {}))
    return {"status": True, "data": result}


@query.field("getManutention")
def resolve_getManutention(obj, info):
    """Get a Node by id and return it like a payload"""
    return {"status": True, "data": grok.get_url()}


@query.field("getThr")
def resolve_getThr(obj, info):
    """Get a Node by id and return it like a payload"""
    return list([thread.name for thread in thread_enumerate()])


@query.field("calibrateCamera")
def resolve_calibrateCamera(obj, info, **kwargs):
    Thread(target=CameraCalibration(**kwargs.get("input", {})).calibrate).start()
    # CameraCalibration().calibrate()
    return True

@query.field("getLoadedNodes")
def resolve_getLoadedNodes(obj, info):
    """Get a Node by id and return it like a payload"""
    return NodeManager.getActiveNodes()