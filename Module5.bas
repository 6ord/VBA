Attribute VB_Name = "Module5"
Sub test3()
Attribute test3.VB_ProcData.VB_Invoke_Func = " \n14"
'
' test3 Macro
'


    ActiveSheet.Range("$A$3:$AF$1674").AutoFilter Field:=5, Criteria1:= _
        ">201312", Operator:=xlOr, Criteria2:="<201311"
End Sub

Sub SearchNameXpress()
'For Movement Analysis Report validation. Quick Client Name filer.
'
    Dim CurrentFile As String
    Dim Target As String
    
    CurrentFile = ActiveWorkbook.name
    
    'Application.CutCopyMode = False
    Target = "=*" & Selection.Value & "*"
   
    Windows("Xpress_by_Layer_9-30-13_REDUCED.xlsx").Activate
    ActiveSheet.Range("$A$1:$AG$429837").AutoFilter Field:=2, Criteria1:=Target, Operator:=xlAnd
    Windows(CurrentFile).Activate
    
End Sub

