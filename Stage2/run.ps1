Write-Host -NoNewline "Bayes (1) "

py .\main.py .\weatherAUS.csv bayes
Write-Host -NoNewline "."


Write-Host ""
Write-Host -NoNewline "Knn (3) "

$neighbors = @(2, 4, 6)

ForEach ($n in $neighbors)
{
    py .\main.py .\weatherAUS.csv knn -n $n
    Write-Host -NoNewline "."
}


Write-Host ""
Write-Host -NoNewline "NN (6) "

$layers = @(1, 10, 20)
$iterations = @(100, 500, 1000)

ForEach ($l in $layers)
{
    ForEach ($i in $iterations)
    {
        py .\main.py .\weatherAUS.csv svm -l $l -i $i
        Write-Host -NoNewline "."
    }
}


Write-Host ""
Write-Host -NoNewline "SVM (6) "

$kernels = @("rbf", "poly", "sigmoid")
$regulations = @(0.1, 0.5, 5)

ForEach ($k in $kernels)
{
    ForEach ($r in $regulations)
    {
        py .\main.py .\weatherAUS.csv svm -k $k -r $4
        Write-Host -NoNewline "."
    }
}
