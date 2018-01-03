"""An attempt to solve this problem
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

# NOTE: silly me, I didn't realize OwnerViewId is only for elements appearing
# in only one view

# try this instead http://thebuildingcoder.typepad.com/blog/2017/05/retrieving-elements-visible-in-view.html
if __name__ == '__main__':
    with Transaction(doc, 'pyRevit Annotate StairPath for All Active') as t:
        t.Start()

        for plan_view in view_collector:

            # collect all stairs inside plan_view
            try:
                stair_collector = FilteredElementCollector(doc, plan_view.Id)   \
                                    .OfClass(clr.GetClrType(Stairs))            \
                                    .ToElements()

            # says that plan_view.Id is sometimes invalid
            except ArgumentException:
                continue


            # if plan_view.ViewType == ViewType.FloorPlan:
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

        t.Commit()
