from src.nodes.node_manager import NodeManager
from src.nodes.base_node import BaseNode, Wizard
from api import logger, exception
from api.decorators import for_all_methods

NODE_TYPE = "OrNode"


@for_all_methods(exception(logger))
class OrNode(BaseNode):
    """
    insert_node_description_here
    """

    def __init__(self, name, id, options, output_connections, input_connections):
        super().__init__(name, NODE_TYPE, id, options, output_connections)
        NodeManager.addNode(self)

    @Wizard._decorator
    def execute(self, message=""):
        self.on("Saida", message)