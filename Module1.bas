Attribute VB_Name = "Module1"
Public Function rvrsName(name)
' Input "Doe,John"
' Output "John Doe"
   Dim first As String
   Dim last As String
    
   Dim commaIndex As Integer
   commaIndex = Application.Find(",", name, 1)
    
   first = Mid(name, commaIndex + 1, Len(name))
   last = Left(name, commaIndex - 1)
   
   rvrsName = Application.CONCATENATE(first, " ", last)

End Function



Sub RemoveBlankRows()

    Dim s As Integer
    's used as sum of cells. zero means row is empty
    Dim Rng As Range
    
    Cells.Find(What:="StartBlankRowDelete").Activate
    ActiveCell.Offset(1, 1).Activate

    'r is number of rows this needs to loop through
    For r = 1 To 16
        Range(ActiveCell.Address & "," & ActiveCell.Offset(0, 1).Address).Select 'SelectionX
        Set Rng = Selection
        'Set Rng = ThisWorkbook.Sheets("Sheet1").Selection.Range
        Let s = 0
        For Each cell In Rng
            s = s + cell.Value
        Next
'MsgBox ("s =") & s
        If s = 0 Then
            ActiveCell.Offset(0, -1).Activate   'need these 2 lines b/c SelectionX has two cells selected.
            ActiveCell.Offset(0, 1).Activate    'Also see ***Assumption*** in DeleteSelectedRows()
            Call DeleteSelectedRows
            'ActiveCell.EntireRow.Delete <- this is buggy
        ElseIf s > 0 Then
            ActiveCell.Offset(1, 0).Activate

        End If
    Next
   
End Sub


Private Function DeleteSelectedRows()
'DELETE ENTIRE ROW FOR EACH ROW IN CURRENT SELECTION, ***ASSUMING ONE CELL IS SELECTED PER ROW***
    Dim laRows() As String
    Dim rRow As Range
    Dim lX As Long
    
    For Each rRow In Selection.Rows
        lX = lX + 1
        ReDim Preserve laRows(lX)
        laRows(lX) = rRow.EntireRow.Address
    Next rRow
    
    For lX = UBound(laRows) To 1 Step -1
        Range(laRows(lX)).EntireRow.Delete
    Next lX
End Function

Sub Test1()
    
    'Dim Rng As Range
    'Dim s As Integer
    'Set Rng = Selection
    'For Each cell In Rng
    '    s = s + cell.Value
    'Next
    'MsgBox "Sum is " & s

    'Application.SendKeys ("+{RIGHT}")


  Range(ActiveCell.Address & "," & ActiveCell.Offset(0, 1).Address).Select
  ActiveCell.Offset(1, 0).Activate
  'Call DeleteSelectedRows
End Sub
Private Sub Loop_and_SendKey_Example()
    Cells.Find(What:="StartBlankRowDelete").Activate
    ActiveCell.Offset(1, 1).Select
    Dim i As Integer
    i = 0
    '15 times
'MsgBox "1"
    'Do
'MsgBox "2"
    Application.SendKeys ("+{RIGHT}")
    Do
'MsgBox "3"
    If Application.CountA(Selection) = 0 Then
        Selection.EntireRow.Delete
'MsgBox "5 - Range Empty, Delete"
    ElseIf Application.CountA(Selection) > 0 Then
        ActiveCell.Offset(1, 0).Select
        'Application.SendKeys ("{DOWN}")
        'MsgBox "6 - Range not Empty"
'MsgBox "7"
    End If
'MsgBox "8"
    i = i + 1
'MsgBox "9"
    Loop Until i = 15
    
End Sub

