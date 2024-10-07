
from root_app.controllers.hello import Hello
from root_app.views.base import Base_UI

class Base(Base_UI):
    def __init__(self, **kwargs):
        super().__init__()

        # get paramter from app.py
        self.parentApp = kwargs['parentApp']
        self.rootDirectory = kwargs['rootDirectory']

        # load controller
        self.helloController = Hello(self)

        # init UI
        self.initUI()

    def initUI(self):
        print('setup UI')
        self.setupUI()

        self.body_stacked.addWidget(self.helloController.initUI())