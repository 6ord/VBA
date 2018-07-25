Attribute VB_Name = "Module6"
Sub Sector_print()
Attribute Sector_print.VB_ProcData.VB_Invoke_Func = " \n14"
'
    ActiveWindow.SelectedSheets.PrintOut Copies:=1, Collate:=True, _
        IgnorePrintAreas:=False
End Sub
Sub Sector_move()
Attribute Sector_move.VB_ProcData.VB_Invoke_Func = " \n14"
'copies contents under headings, and paste to another accruing sheet with same headings
    Range("D7").Select
    Range(Selection, Selection.End(xlToRight)).Select
    Range(Selection, Selection.End(xlDown)).Select
    Selection.Copy
    Sheets("AllSectors").Select
    Range("B5").Select
    Selection.End(xlDown).Select
    'down 1 cell
    ActiveCell.Offset(1, 0).Activate
    
    Selection.PasteSpecial Paste:=xlPasteValuesAndNumberFormats, Operation:= _
        xlNone, SkipBlanks:=False, Transpose:=False
    Selection.PasteSpecial Paste:=xlPasteFormats, Operation:=xlNone, _
        SkipBlanks:=False, Transpose:=False
    Sheets("SectorRpt").Select
End Sub

