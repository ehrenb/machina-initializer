from datetime import datetime

from neomodel import install_all_labels

from machina.core.worker import Worker
from machina.core.models import *

class Initializer(Worker):
    """Initializer initializes the database and exits"""

    next_queues = []
    types = []

    def __init__(self, *args, **kwargs):
        super(Initializer, self).__init__(*args, **kwargs)

    def init_neo4j(self):

        self.logger.info("initializing neo4j models")
        install_all_labels()

        # TEST inputs

        # for i in range(0,10):
        #     ts = datetime.now()
        #     md5sum = 'test123'
        #     sha256sum = 'test456'
        #     type = 'testtype'
        #     size=12345

        #     art = Artifact(
        #         md5=md5sum,
        #         sha256=sha256sum,
        #         ts=ts,
        #         size=size,
        #         type=type
        #     ).save()

        # test = PNG(
        #     md5=md5sum,
        #     sha256=sha256sum,
        #     ts=ts,
        #     type=type,
        #     size=size,
        #     exif={'test':123}
        # ).save()
        
        # zip = Zip(
        #     md5=md5sum,
        #     sha256=sha256sum,
        #     ts=ts,
        #     type=type,
        #     size=size
        # ).save()

        # extracts_rel = zip.extracts.connect(test).save()
        # similar_rel = zip.similar.connect(test).save()
        # retyped_rel = zip.retyped.connect(test).save()
