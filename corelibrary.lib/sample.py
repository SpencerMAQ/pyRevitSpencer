"""core library sample
for pyRevitSpencer"""

__title__ = 'Hello\nWorld'
__author__ = 'Michael Spencer Quinto'

# __context__ = 'Selection'
# Tools are active even when there are no documents available/open in Revit
# __context__ = 'zerodoc'


def sample_func():
    return 'Hello from corelibrary.lib {}'.format(__name__)
