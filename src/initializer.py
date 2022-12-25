from pyorient.ogm import Graph, Config

from machina.core.worker import Worker
from machina.core.models import *

class Initializer(Worker):
    """Initializer initializes the database and exits"""

    next_queues = []
    types = []

    def __init__(self, *args, **kwargs):
        super(Initializer, self).__init__(*args, **kwargs)

    def init_orientdb(self):

        
        self.logger.info("creating Nodes and Relationships")
        self.graph.create_all(Node.registry)
        self.graph.create_all(Relationship.registry)