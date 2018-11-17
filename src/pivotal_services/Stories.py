from src.pivotal_services.PivotalServices import PivotalServices


class Stories(PivotalServices):

    def __init__(self):
        super(Stories, self).__init__("stories")
