from src.pivotal_services.PivotalServices import PivotalServices


class Epics(PivotalServices):

    def __init__(self):
        super(Epics, self).__init__("epics")
