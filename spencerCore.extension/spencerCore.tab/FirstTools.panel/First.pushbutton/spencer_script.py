"""Just a script that
Displays Hello world."""

__title__ = 'Hello\nWorld'
__author__ = 'Michael Spencer Quinto'

# __context__ = 'Selection'
# Tools are active even when there are no documents available/open in Revit
__context__ = 'zerodoc'


from Autodesk.Revit.UI import TaskDialog

TaskDialog.Show('spencerCorePyRevut', 'Hello World!')
