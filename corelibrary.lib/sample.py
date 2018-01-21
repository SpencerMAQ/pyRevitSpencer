# pyRevitSpencer: A pyRevit Plugin (GPL)
# started by Michael Spencer Quinto <https://github.com/SpencerMAQ>
#
# This file is part of pyRevitSpencer.
#
# You should have received a copy of the GNU General Public License
# along with Faraday; If not, see <http://www.gnu.org/licenses/>.
#
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""core library sample
for pyRevitSpencer"""

# tested versions: 2018

__title__ = 'Hello\nWorld'
__author__ = 'Michael Spencer Quinto'

# __context__ = 'Selection'
# Tools are active even when there are no documents available/open in Revit
# __context__ = 'zerodoc'


def sample_func():
    return 'Hello from corelibrary.lib {}'.format(__name__)
