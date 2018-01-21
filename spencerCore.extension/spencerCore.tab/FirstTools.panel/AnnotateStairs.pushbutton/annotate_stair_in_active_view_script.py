# pyRevitSpencer: A pyRevit Extension (GPL)
# started by Michael Spencer Quinto <https://github.com/SpencerMAQ>
#
# This file is part of pyRevitSpencer.
#
# You should have received a copy of the GNU General Public License
# along with Faraday; If not, see <http://www.gnu.org/licenses/>.
#
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>

"""Places Annotation Stair Paths for all visible views
as an attempt to solve this problem:
https://github.com/eirannejad/pyRevit/issues/250"""

# tested versions: 2018

__title__   = 'StairPath\nAllView'
__author__  = 'Michael Spencer Quinto'
__version__ = 0.0


import clr

from revitutils import doc, uidoc

from Autodesk.Revit.DB import Transaction, FilteredElementCollector, LinkElementId, View, ViewPlan, ViewType
from Autodesk.Revit.DB.Architecture import StairsPath, Stairs, StairsPathType
from Autodesk.Revit.Exceptions import ArgumentException


default_path_type_id    = FilteredElementCollector(doc)                 \
                            .OfClass(clr.GetClrType(StairsPathType))    \
                            .ToElementIds()[0]
                            # .FirstElementId()

view_collector          = FilteredElementCollector(doc)                 \
                            .OfClass(clr.GetClrType(ViewPlan))          \
                            .ToElements()


# try: http://thebuildingcoder.typepad.com/blog/2017/05/retrieving-elements-visible-in-view.html
if __name__ == '__main__':
    with Transaction(doc, 'pyRevit Annotate StairPath for All Active') as t:
        t.Start()

        for plan_view in view_collector:

            # view_collector also catches ViewPlan templates causing errors
            if not plan_view.IsTemplate:

                # collect all stairs inside plan_view
                stair_collector = FilteredElementCollector(doc, plan_view.Id)   \
                                    .OfClass(clr.GetClrType(Stairs))            \
                                    .ToElements()

                if plan_view.ViewType == ViewType.FloorPlan:
                    for stair in stair_collector:

                        try:
                            StairsPath.Create(doc,
                                              LinkElementId(stair.Id),
                                              default_path_type_id,
                                              plan_view.Id
                                              )

                        # says that plan_view.Id is sometimes invalid
                        except ArgumentException:
                            pass
                            # raise

        t.Commit()
