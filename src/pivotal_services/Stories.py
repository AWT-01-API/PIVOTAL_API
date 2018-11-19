from src.pivotal_services.PivotalServices import PivotalServices


class Stories(PivotalServices):

    def __init__(self, project_id, story_id=None):
        super(Stories, self).__init__('/' + project_id + "/stories", story_id)
