from Model import Model


class London(Model):
    def __init__(self):
        super().__init__()
        self.setFileLocation("./graphs/London.json")
        self.loadGraph()
