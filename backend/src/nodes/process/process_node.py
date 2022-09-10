from src.nodes.node_manager import NodeManager
from src.nodes.base_node import BaseNode
from src.manager.process_manager import ProcessManager as process
from api import logger, exception
from api.decorators import for_all_methods
from threading import Thread
from src.utility.crud.user import User

NODE_TYPE = "ProcessNode"

process_options = {"stop": process.stop, "pause": process.pause, "start": process.start}


@for_all_methods(exception(logger))
class ProcessNode(BaseNode):
    """
        self_running = [("start", process_node, "process.start")]


        process.start(
            for node in self_running:
                node.execute() => {
                    if node.auto_run: Sinal.foreach(True)
                    else: self.function() # in another thread to prevent infinity recursion
                }
        )
    """

    def __init__(self, name, id, options, output_connections, input_connections):
        super().__init__(name, NODE_TYPE, id, options, output_connections)
        self.input_connections = input_connections
        self.function = process_options[options["action"]]
        self.auto_run = options.get("auto_run", False)
        self.manager = process
        NodeManager.addNode(self)

    # @Wizard._decorator # Since this can be a start node, a wizar is not necessary
    def execute(self, message=""):
        if self.auto_run:
            self.on("Gatilho", True)
        else:
            Thread(target=self.function, kwargs={'user':User('omnis', 'bot', 'developer', 'parallax@orakolo.com')}).start()

    @staticmethod
    def get_info(**kwargs):
        return {
            "options": {
                "actions": list(process_options.keys()),
            }
        }