"""An attempt to solve this problem
https://github.com/eirannejad/pyRevit/issues/250"""

# tested versions: 2018

__title__ = 'StairPath\nAllView'
__author__ = 'Michael Spencer Quinto'


import clr

from revitutils import doc, uidoc

from Autodesk.Revit.DB import Transaction, FilteredElementCollector, LinkElementId, View, ViewPlan, ViewType
from Autodesk.Revit.DB.Architecture import StairsPath, Stairs, StairsPathType




default_path_type_id    = FilteredElementCollector(doc)                 \
                            .OfClass(clr.GetClrType(StairsPathType))    \
                            .ToElementIds()[0]
                            # .FirstElementId()

# TODO: filter only to plan views using FilteredElementCollector
view_collector          = FilteredElementCollector(doc)                 \
                            .OfClass(clr.GetClrType(ViewPlan))          \
                            .ToElements()

if __name__ == '__main__':
    with Transaction(doc, 'pyRevit Annotate StairPath for All Active') as t:
        t.Start()

        for plan_view in view_collector:
            # Note: .OwnedByView(plan_view.Id) gives null results
            # THE HELL is there a problem with OWNERVIEWID???
            stair_collector = FilteredElementCollector(doc)             \
                                .OfClass(clr.GetClrType(Stairs)) \
                                .ToElements()
            # print(stair_collector)
            # if stair_collector:
            #     print('hoola')


            # if plan_view.ViewType == ViewType.FloorPlan:
            for stair in stair_collector:

                # apparently stair.OwnerViewId returns an invalid elemId
                print(stair.Id.ToString(), stair.OwnerViewId.ToString(), plan_view.Id.ToString())
                # test
                if stair.OwnerViewId == plan_view.Id:

                    StairsPath.Create(doc,
                                      LinkElementId(stair.Id),
                                      default_path_type_id,
                                      plan_view.Id
                                      )

        t.Commit()