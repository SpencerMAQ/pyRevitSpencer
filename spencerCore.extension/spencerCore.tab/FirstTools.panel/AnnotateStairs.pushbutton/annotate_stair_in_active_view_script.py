"""An attempt to solve this problem
https://github.com/eirannejad/pyRevit/issues/250"""

# tested versions: 2018

__title__ = 'StairPath\nAllView'
__author__ = 'Michael Spencer Quinto'


import clr

from revitutils import doc, uidoc

from Autodesk.Revit.DB import Transaction, FilteredElementCollector, LinkElementId, View
from Autodesk.Revit.DB.Architecture import StairsPath, Stairs, StairsPathType


stair_collector         = FilteredElementCollector(doc)                 \
                            .OfClass(clr.GetClrType(Stairs))            \
                            .ToElements()

default_path_type_id    = FilteredElementCollector(doc)                 \
                            .OfClass(clr.GetClrType(StairsPathType))    \
                            .ToElementIds()[0]
                            # .FirstElementId()

view_collector          = FilteredElementCollector(doc)                 \
                            .OfClass(clr.GetClrType(View))              \
                            .ToElementIds()

if __name__ == '__main__':
    with Transaction(doc, 'pyRevit Annotate StairPath for All Active') as t:
        t.Start()

        for stair in stair_collector:
            StairsPath.Create(doc,
                              LinkElementId(stair.Id),
                              default_path_type_id,
                              doc.ActiveView.Id
                              )

        t.Commit()