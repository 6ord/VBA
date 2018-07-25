Attribute VB_Name = "Module4"
Function aon_coe(client As String, brokername As String, brokeroffice As String, brokerdept As String, brokerregion As String, _
productsegment As String, sort As String)
'TriageFormatting_v2: Top Products Sheet: H,R,Y,U,T,X,Z'
'TriageFormatting_v2: Comm Pckges Sheet: C,S,Z,V,U,Y,AA'
'TriageFormatting_v2: Distr tab (Making Broker Distribution) B,V,AC,Y,X,AB,AD
'Func tab of Combined (Making Registrations.xls) B,W,BQ,Y,Z,AC,BR
'Mang Rpt tab of Combined, actually from Distr Tab from WishList (Making Management Reports) C,W,AD,Z,Y,AC,AE
'
'Test Version OCT 8, 2013 (AGCN & Toronto Construction)
'LAST UPDATED OCT 25, 2013 (OAKVILLE MOVE TO BURLINGTON)


    If (brokername = "Pellen,Adrian G" Or brokername = "Pellen,Adrian" Or sort = "EIL") Then
        aon_coe = "Environ"
    ElseIf (sort = "Public Sector" Or brokerdept = "Public SectorNB") Then
        aon_coe = "Public Sector"
    ElseIf (brokerdept = "Power and UtlitiesNB" Or brokername = "Dodsworth,Terry") Then
        aon_coe = "Power & Utilities"
    'ElseIf ((client <> "Peter Kiewit Infrastructure Co.") And _
            (sort = "Construction" Or brokerdept = "Contruction Large Accts Proj" Or _
            brokerdept = "Construction Mid MarketNB")) Then                                 'OCT 8 2013 replace
    ElseIf (sort = "Construction" Or brokerdept = "Contruction Large Accts Proj" Or _
            brokerdept = "Construction Mid MarketNB" Or brokerdept = "ConstructionTOR") Then
          If (brokeroffice = "Toronto") Then
            aon_coe = "Construction - Toronto"
          Else
            aon_coe = "Construction"
          End If
    ElseIf (sort = "Energy" Or brokerdept = "Energy Large AccountsNB" Or brokerdept = "Energy Mid MarketNB") Then
            If (brokerdept = "Energy Mid MarketNB" Or brokername = "Nguyen,Thuan V") Then
                aon_coe = "Energy Mid"
            Else
                aon_coe = "Energy Lrg"
            End If
    ElseIf (brokername = "Duggan,Rob W" Or (productsegment = "Marine" And (brokeroffice = "Halifax" Or brokeroffice = "St. John's"))) Then
        aon_coe = "Marine - Atl"
    ElseIf (brokername = "Egger,Doreen L." Or (productsegment = "Marine" And (brokerregion = "Prairies" Or brokerregion = "B.C. & Yukon"))) Then
        aon_coe = "Marine - BC & Prairies"
    ElseIf (brokername = "Wong,Kathleen" Or (productsegment = "Marine" And brokerregion = "Ontario")) Then
        aon_coe = "Marine - Ont"
    ElseIf (brokername = "Rossi,John" Or (productsegment = "Marine" And brokeroffice = "Montreal") Or (productsegment = "Marine" And brokeroffice = "Quebec City")) Then
        aon_coe = "Marine - Quebec"
    ElseIf (sort = "FSG" Or brokerdept = "Financial Services Group") Then
        If (brokeroffice = "Winnipeg") Then
            aon_coe = "FSG - Winnipeg"
        ElseIf (brokeroffice = "Regina") Then
            aon_coe = "FSG - Regina"
        ElseIf (brokeroffice = "Edmonton") Then
            aon_coe = "FSG - Edmonton"
        ElseIf (brokerregion = "Prairies") Then
            aon_coe = "FSG - Calgary"
        ElseIf (brokerregion = "B.C. & Yukon") Then
            aon_coe = "FSG - BC & Yukon"
        ElseIf (brokerregion = "Ontario") Then
            aon_coe = "FSG - Ont"
        ElseIf (brokerregion = "Quebec" Or brokerregion = "Atlantic") Then
            aon_coe = "FSG - East"
        Else
            aon_coe = "FSG"
        End If
    ElseIf (productsegment = "Aviation") Then
        If (brokeroffice = "Quebec City") Then
            aon_coe = "Aviation - QueCity"
        ElseIf (brokerregion = "Ontario") Then
            aon_coe = "Aviation - Ontario"
        ElseIf (brokeroffice = "Vancouver") Then
            aon_coe = "Aviation - Vancouver"
        ElseIf (brokeroffice = "Montreal" Or brokerregion = "Atlantic") Then
            aon_coe = "Aviation - East"
        Else
            aon_coe = "Aviation"
        End If
    'ElseIf (sort = "AGCN") Then                                                          'OCT 8 2013 replace
    ElseIf (sort = "AGCN" Or brokerdept = "Aon Global Client Network TOR") Then
        aon_coe = "AGCN"
    ElseIf (brokeroffice = "Halifax" Or brokername = "Macdonald,Bruce") Then
        aon_coe = "Halifax"
    ElseIf (brokeroffice = "St. John's") Then
        aon_coe = "St. John's"
    ElseIf (brokeroffice = "Winnipeg" Or brokername = "Flook,Bruce") Then
        aon_coe = "Winnipeg"
    ElseIf (brokeroffice = "Quebec City" Or brokeroffice = "Sherbrooke" Or brokername = "McLean,Jimmy") Then
        aon_coe = "QC & Shrbrke"
    'Combined Broker List of Michel Brokers
    ElseIf (sort = "Michel L") Then
        aon_coe = "Montreal - Michel L"
    ElseIf (brokeroffice = "Montreal") Then
        If (productsegment = "Casualty - FSG") Then
            aon_coe = "FSG - East"
        'ElseIf (brokername = "L'Ecuyer,Josee") Then
        '    aon_coe = "Montreal - Josee L'Ecuyer"
        Else
            aon_coe = "Montreal - Josee L"
        End If
    ElseIf (brokeroffice = "Burlington") Then                           'Oct 25 changes on 2 lines
        aon_coe = "Ontario - Burlington"
    ElseIf (brokeroffice = "Oakville") Then
        aon_coe = "Ontario - Burlington"
    ElseIf (brokeroffice = "London" Or brokeroffice = "Windsor" Or brokeroffice = "Sarnia") Then
        aon_coe = "Ontario - London/Windsor/Sarnia"
    ElseIf (brokeroffice = "Thunder Bay") Then
        aon_coe = "Ontario - Thunder Bay"
    ElseIf (brokeroffice = "Ottawa") Then
        aon_coe = "Ontario - Ottawa"
    ElseIf (brokerregion = "Ontario") Then
        aon_coe = "Ontario - Toronto"
    ElseIf (brokerregion = "Prairies") Then
        aon_coe = "Prairies"
    ElseIf (brokerregion = "B.C. & Yukon") Then
        aon_coe = "B.C. & Yukon"
    Else
        aon_coe = ".None"
    End If
End Function


