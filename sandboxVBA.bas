Attribute VB_Name = "sandboxVBA"




Function big_decision(x As Integer)
    If (x = 1) Then
        big_decision = "uno"
    ElseIf (x = 2) Then
        big_decision = "deux"
    ElseIf (x = 3) Then
        big_decision = "trio"
    ElseIf (x = 4) Then
        big_decision = "quads"
    ElseIf (x = 5) Then
        big_decision = "cinqo!"
    ElseIf (x = 6 Or x = 7 Or x = 8) Then
        If (x = 6) Then
            big_decision = "six"
        ElseIf (x = 7) Then
            big_decision = "seven"
        'Else (x = 8) Then
        Else
            big_decision = "eight"
        End If
        'Else: bigdecision = "eight"
        'If (2 > 1) Then bigdecision = "seven or eight"
     Else
        big_decision = "loco"
     End If
End Function

Function embededcriteria(x, y, z)
    If (x = "a" Or (y = "b" And z = "c")) Then
        embededcriteria = "ok for now"
    End If
End Function

Function hypo(x, y)
    hypo = Sqr(x ^ 2 + y ^ 2)
End Function

Sub hollowCell()
    If isEmpty(ActiveCell) Then
        ' isEmpty = True
        MsgBox "This cell is empty"
    Else
        ' isEmpty = False
        MsgBox "This cell is not empty"
    End If
End Sub

Sub hollowRange()
    'If isEmpty(Selection) Then
    'If (ActiveRange. = 0) Then
    If Application.CountA(Selection) = 0 Then
        ' isEmpty = True
        MsgBox "This range is empty"
    Else
        ' isEmpty = False
        MsgBox "This range is not empty"
    End If
End Sub

Sub outContents()
    MsgBox "This cell says " + ActiveCell.Value
End Sub

Sub smartSelectRows()
    'MsgBox "Select top of dataset."
    
    'Dim firstRow As Integer
    'Dim lastRow As Integer
    'Dim lastColumn As Integer
    Dim last As Boolean 'Cursor will loop through cells. "last" will equal TRUE when the last cell with contents is found
    Dim firstRange As Range 'Just the starting point
    Dim lastRange As Range 'temp variable that keeps count which row was the last one which wasn't empty
    Dim targetRange As String 'final string we're trying to build, which will specify the range. When the last row number is determined from the loop, targetRange will be built based on that last row number
    
    'lastRow = ActiveCell.Row
    last = False
    
    Set firstRange = ActiveCell 'sets the starting point of the range right off the bat. Will be used later when building the targetRange String
    
    Do 'Here is the loop going down the cells, and finding the last row
        If isEmpty(ActiveCell) Then
            last = True
        Else
            Set lastRange = ActiveCell
            'lastRow = lastRow + 1
            ActiveCell.Offset(1, 0).Select
        End If
    Loop While last = False
    
    'firstRange.Select
    'MsgBox "Here's the first cell."
    'lastRange.Select
    'MsgBox "Here's the last cell."
    
    Let targetRange = firstRange.Row & ":" & lastRange.Row 'build the targetRange string
   MsgBox (targetRange)
    Rows(targetRange).Select 'select the range
    
End Sub


Sub smartSelectRange()
    'MsgBox "Select top of dataset."
    
    'Dim firstRow As Integer
    'Dim lastRow As Integer
    'Dim lastColumn As Integer
    Dim last As Boolean
    Dim firstRange As Range
    Dim lastRange As Range
    Dim targetRange As String
    
    'lastRow = ActiveCell.Row
    last = False
    
    Set firstRange = ActiveCell
    
    Do
        If isEmpty(ActiveCell) Then
            last = True
        Else
            Set lastRange = ActiveCell
            'lastRow = lastRow + 1
            ActiveCell.Offset(1, 0).Select
        End If
    Loop While last = False
    
    'firstRange.Select
    'MsgBox "Here's the first cell."
    'lastRange.Select
    'MsgBox "Here's the last cell."
    
    Let targetRange = firstRange.Row & ":" & lastRange.Row
    Rows(targetRange).Select
    
End Sub

