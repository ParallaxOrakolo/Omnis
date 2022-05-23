from src.nodes.node_manager import NodeManager
from src.nodes.base_node import BaseNode
from src.nodes.compare.compare_funcs import comparatives
from api import logger, exception
from api.decorators import for_all_methods

NODE_TYPE = "COMPARATIVE"


@for_all_methods(exception(logger))
class CompareNode(BaseNode):
    """
    Node to execute logical operations between values.
    """

    def __init__(self, name, id, options, output_connections, input_connections):
        super().__init__(name, NODE_TYPE, id, options, output_connections)
        self.input_connections = input_connections
        self.operation = options["operation"]
        self.value1 = options["value1"]
        self.value2 = options["value2"]
        self.value3 = options["value3"]
        self.auto_run = options.get("auto_run", False)
        NodeManager.addNode(self)

    def execute(self, message=""):
        target = message.targetName.lower()
        getattr(self, target)(message)
        pass

    def value1(self, message):
        self.value1 = message.payload

    def value2(self, message):
        self.value2 = message.payload

    def value3(self, message):
        self.value3 = message.payload

    def trigger(self, message):
        try:
            self.onSuccess(
                comparatives[self.operation](self.value1, self.value2, self.value3)
            )
        except Exception as e:
            self.onFailure(f"{self._id} cant execute.", pulse=True, errorMessage=str(e))
