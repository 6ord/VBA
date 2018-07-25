Attribute VB_Name = "Module2"
Sub NameSearch()
'
    Dim SearchCriteria As String
    SearchCriteria = "=*" & Selection.Value & "*"
    
    Windows("Xpress_by_Layer_11-30-13(REDUCED).xlsx").Activate
    ActiveSheet.Range("$A$1:$AD$452682").AutoFilter Field:=2, Criteria1:=SearchCriteria, Operator:=xlAnd
End Sub



