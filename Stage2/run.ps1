Write-Host -NoNewline "Bayes (1)"

py .\main.py .\weatherAUS.csv bayes
Write-Host -NoNewline "."


Write-Host ""
Write-Host -NoNewline "Knn (2)"

$neighbors = @(2, 5)

ForEach ($n in $neighbors)
{
    py .\main.py .\weatherAUS.csv knn -n $n
    Write-Host -NoNewline "."
}


Write-Host ""
Write-Host -NoNewline "NN (4)"

$layers = @(1, 10)
$iterations = @(500, 1000)

ForEach ($l in $layers)
{
    ForEach ($i in $iterations)
    {
        py .\main.py .\weatherAUS.csv svm -l $l -i $i
        Write-Host -NoNewline "."
    }
}


Write-Host ""
Write-Host -NoNewline "SVM (4)"

$kernels = @("rbf", "poly")
$regulations = @(0.1, 1)

ForEach ($k in $kernels)
{
    ForEach ($r in $regulations)
    {
        py .\main.py .\weatherAUS.csv svm -k $k -r $4
        Write-Host -NoNewline "."
    }
}
