Sub ResultsHeaders()

    Sheet6.Activate
    
    Range("A1").Value = "Ticker"
    Range("B1").Value = "Total Change"
    Range("C1").Value = "% of Change"
    Range("D1").Value = "Avg. Daily Change"
    Range("E1").Value = "Total vol."
    Range("G2").Value = "Total Shares"
    Range("G5").Value = "Greatest % Increase"
    Range("G8").Value = "Greatest % Decr"
    Range("G10").Value = "Greatest Daily Avg. Daily Change"
    Range("I1").Value = "Ticker"
    
End Sub

Sub StockSolutions()

    Dim Ticker As String
    Dim TotalChange As Double
    Dim Days As Double
    Dim DailyChange As Double
    Dim Change As Double
    Dim AvgDailyChange As Double
    Dim Summary As Double
    Dim tstart As Double
    Dim PercentChange As Single
    Dim LastRow As Double
    Dim Volume As Double

    Dim WS As Worksheet
    Dim OWS As Worksheet

    Set OWS = Sheets("2016")
    OWS.Activate

    tstart = 2
    Summary = 2
    DailyChange = 0
    Volume = 0
    TotalChange = 0


    'LastRow of Ticker
    LastRow = Cells(Rows.Count, "A").End(xlUp).Row
    
    For i = 2 To LastRow
    
    If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

    Volume = Volume + Cells(i, 7).Value
    
    TotalChange = Cells(i, 6).Value - Cells(tstart, 3).Value
    
    PercentChange = (TotalChange / Round(Cells(tstart, 3), 6))
    
    Days = (i - tstart) + 1
    
    AvgDailyChange = (DailyChange + Cells(i, 4).Value - Cells(i, 5).Value) / Days
    
    Ticker = Cells(i, 1).Value
    
    tstart = i + 1

    'Print Values in Results Sheet
    Sheets("Results").Range("A" & Summary).Value = Ticker

    Sheets("Results").Range("B" & Summary).Value = TotalChange

    Sheets("Results").Range("C" & Summary).Value = PercentChange

    Sheets("Results").Range("D" & Summary).Value = AvgDailyChange

    Sheets("Results").Range("E" & Summary).Value = Volume

    'Format Colors for Yearly_Change
    If Sheet6.Range("B" & Summary).Value < 0 Then
    Sheet6.Range("B" & Summary).Interior.ColorIndex = 3

    Else
    Sheet6.Range("B" & Summary).Interior.ColorIndex = 4
     
    End If

    'Reset totals
    Ticker = 0
    Days = 0
    DailyChange = 0
    AvgDailyChange = 0
    Volume = 0
    Summary = Summary + 1

    'If the cell immediately following the row is the same ticker..
    Else

    Volume = Volume + Cells(i, 7).Value

    TotalChange = TotalChange + (Cells(i, 6).Value - Cells(i, 3).Value)

    Change = Cells(i, 4).Value - Cells(i, 5).Value

    DailyChange = DailyChange + Change


    End If

Next i


    'Print to Greatest Table
    Sheet6.Activate

   
    Dim ResultsRow As Double
    Dim GreatVolume As Double
    Dim GreatIncrease As Double
    Dim GreatDecrease As Double
    Dim GreatAvgChange As Double
    Dim GreatTicker As String
    Dim GreatIncTicker As String
    Dim GreatDecTicker As String
    Dim GreatAvgTicker As String

    GreatVolume = 0
    GreatIncrease = 0
    GreatAvgChange = 0

    ResultsRow = Cells(Rows.Count, "A").End(xlUp).Row


    For i = 2 To ResultsRow

    If Cells(i, 5) > GreatVolume Then

    GreatVolume = Cells(i, 5)
    GreatTicker = Cells(i, 1)

    End If

    Next i

    For i = 2 To ResultsRow

    If Cells(i, 3) > GreatIncrease Then

    GreatIncrease = Cells(i, 3)
    GreatIncTicker = Cells(i, 1)

    End If

Next i

    GreatDecrease = Range("C2").Value

    For i = 2 To ResultsRow

    If Cells(i, 3) <= GreatDecrease Then

    GreatDecrease = Cells(i, 3)
    GreatDecTicker = Cells(i, 1)

    End If

    Next i


    For i = 2 To ResultsRow

    If Cells(i, 4) > GreatAvgChange Then

    GreatAvgChange = Cells(i, 4)
    GreatAvgTicker = Cells(i, 1)

    End If

    Next i

    Sheets("Results").Range("H2").Value = GreatVolume
    Sheets("Results").Range("I2").Value = GreatTicker

    Sheets("Results").Range("H5").Value = GreatIncrease
    Sheets("Results").Range("I5").Value = GreatIncTicker

    Sheets("Results").Range("H8").Value = GreatDecrease
    Sheets("Results").Range("I8").Value = GreatDecTicker

    Sheets("Results").Range("H10").Value = GreatAvgChange
    Sheets("Results").Range("I10").Value = GreatAvgTicker

    Sheets("Results").Range("C:C").NumberFormat = "0.00%"
    Sheets("Results").Range("H5").NumberFormat = "0.00%"
    Sheets("Results").Range("H8").NumberFormat = "0.00%"



End Sub



