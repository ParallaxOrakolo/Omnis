from src.nodes.node_manager import NodeManager
from src.nodes.base_node import BaseNode

from .identify_functions import identifyObjects
from api import logger, exception
from api.decorators import for_all_methods

NODE_TYPE = "IDENTIFY"


@for_all_methods(exception(logger))
class IdentifyNode(BaseNode):
    """
    Find a list of countours in an image that match a giver filters.

    Signals ->
        "onSuccess" -> returns a list of dimensional countour data.
    """

    def __init__(self, name, id, options, output_connections, input_connections):
        super().__init__(name, NODE_TYPE, id, options, output_connections)
        self.input_connections = input_connections
        self.filters = options["filters"]
        self.propertie = options["propertie"]
        self.auto_run = options["auto_run"]["value"]
        NodeManager.addNode(self)

    def execute(self, message):
        object_data_list = identifyObjects(message.payload, **self.filters)
        self.onSuccess(object_data_list)
        # for object_data in object_data_list:
        #     for prop_key in self.propertie:
        #         if object_data.get(prop_key) is not None:
        #             self.on(prop_key, object_data.get(prop_key))

        # self.on("object", object_data)
        # self.onSuccess(object_data())
