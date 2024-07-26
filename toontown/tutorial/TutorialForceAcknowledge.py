from panda3d.core import *
from toontown.toontowngui import TTDialog
from toontown.toonbase import TTLocalizer

class TutorialForceAcknowledge:

    def __init__(self, doneEvent):
        self.doneEvent = doneEvent
        self.dialog = None
        return

    def enter(self):
        pass

    def exit(self):
        pass

    def handleOk(self, value):
        messenger.send(self.doneEvent, [self.doneStatus])
