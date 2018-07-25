Attribute VB_Name = "Module3"

Sub sector_BreakOutSheetsAndRename()
Attribute sector_BreakOutSheetsAndRename.VB_ProcData.VB_Invoke_Func = " \n14"
    
    'NEEDS Private Function getAllRangeAddy() and AllSheetNames worksheet
    
    Const numValues = 11
    
    Dim StartSheet As String
    
    Dim MyRange As Range
    Dim i As Integer
    
    Dim FromSheet As String
    Dim ToSheet As String
    Dim StartCell As String
    Dim EntireDataset As String
    Dim FilterColumnNum As Integer
    
    Dim AllSheetNamesArray(numValues) As String
    
EntireDataset = getAllRangeAddy()
    
    'Sheets("AllSectors").Select
    Range("b6").Select
    
    For x = 0 To (numValues - 1)
        
        FromSheet = ActiveSheet.name
        StartCell = ActiveCell.Address
        FilterColumnNum = ActiveCell.Column
        'EntireDataset = getAllRangeAddy()
    
        StartSheet = ActiveSheet.name
        
        Sheets("tables").Select
        Range("k2").Select
        Range(Selection, Selection.End(xlDown)).Select
        Set MyRange = Selection
        i = 0

        For Each c In MyRange
            'AllSheetNamesArray(i) = c
            AllSheetNamesArray(i) = c.Value
            i = i + 1
            'MsgBox (AllSheetNamesArray(i))
        Next c
        
        Sheets(StartSheet).Select
        AllSheetNamesArray(x) = ""
        'MsgBox (AllSheetNamesArray)
        'STARTING TO FILTER
        
        ActiveSheet.Range(EntireDataset).AutoFilter Field:=FilterColumnNum - 1, _
        Criteria1:=AllSheetNamesArray, _
        Operator:=xlFilterValues
    
        Range(StartCell).Select
        'down 1 cell
        ActiveCell.Offset(1, 0).Activate
        'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
        Range(Selection, Selection.End(xlDown)).Select
'MsgBox (EntireDataset)
        Selection.EntireRow.Delete
        ActiveSheet.ShowAllData
        'up 1 cell
        ActiveCell.Offset(-1, 0).Activate
        'down 1 cell
        ActiveCell.Offset(1, 0).Activate
        ToSheet = Selection.Value
        'Selection.Copy
        Sheets(FromSheet).name = ToSheet
        Application.CutCopyMode = False
        'next sheet
        ActiveSheet.Next.Select
    Next x

End Sub

Private Function getAllRangeAddy()
' User must be in any cell on the first row of dataset. Returns range address of entire dataset. ex, "$A$1:$Z$67"

    Dim rr As String
    
    'Selection.End(xlToRight).Select
    Range(Selection, Selection.End(xlToRight)).Select
    Range(Selection, Selection.End(xlDown)).Select
    rr = Selection.Address
    getAllRangeAddy = rr
End Function



Sub sector_PopOutSheets()
'
' PopOutSheets Macro
Const numValues = 11
Const OtherSheet = "Out Translation"

Dim origFile As String

Dim i As Integer
Dim AllSheetNamesArray(numValues) As String

origFile = ActiveWorkbook.name

Sheets("tables").Select
Range("K2").Select
Range(Selection, Selection.End(xlDown)).Select
Set MyRange = Selection
i = 0

For Each c In MyRange
    AllSheetNamesArray(i) = c.Value
    i = i + 1
Next c

For x = 1 To numValues
    'Sheets(Array(AllSheetNamesArray(x - 1), OtherSheet)).Copy
    'Sheets(OtherSheet).Visible = False
    Sheets(Array(AllSheetNamesArray(x - 1))).Copy
    'Sheets(OtherSheet).Visible = False
    Windows(origFile).Activate
Next x


End Sub





Sub SaveFilesPerSheetName()
Attribute SaveFilesPerSheetName.VB_ProcData.VB_Invoke_Func = "q\n14"

    Dim myfile As String
    
    myfile = "F:\Marsh\samples\" & "SunshineSector_" & ActiveSheet.name & ".xlsx"
    ActiveWorkbook.SaveAs Filename:=myfile, FileFormat:=xlOpenXMLWorkbook, CreateBackup:=False
    
End Sub

Sub RenameSheets()
    
    'AllSheetNames to contain all sheet names
    'sufficient number of blank sheets created
    'Set numValue Constant
    'first sheet selected
    'Run Macro
    
    Const numValues = 11
    
    Dim StartSheet As String
    
    Dim MyRange As Range
    Dim i As Integer
    
    Dim AllSheetNamesArray(numValues) As String
    
    StartSheet = ActiveSheet.name
    Sheets("AllSheetNames").Select
    Range("A1").Select
    Range(Selection, Selection.End(xlDown)).Select
    Set MyRange = Selection
    i = 0
    
    For Each c In MyRange
        AllSheetNamesArray(i) = c.Value
        i = i + 1
    Next c
    
    Sheets(StartSheet).Select
    
    For x = 0 To (numValues - 1)
       ActiveSheet.name = AllSheetNamesArray(x)
       ActiveSheet.Next.Select
    Next x
    
End Sub
