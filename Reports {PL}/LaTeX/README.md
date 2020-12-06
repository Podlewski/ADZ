# ADZ - LaTeX

## Etap2

Pliki PNG nie znajdują się na repozytorium. Wygenerują się automatycznie dzięki skryptowi `run.ps1` - należy je następnie przekiopować do folderu `resources\stage2\` i podzielić w podfoldery od nazw nazw (z polskimi znakami).

W celu umożliwienia kompliacji z obrazkami należy przełączyć flagę `\setkeys{Gin}{draft=True}` na `\setkeys{Gin}{draft=False}`, do znalezienia przed każdą sekcją zawierającą wykresy dla miar. Overleaf w wersji darmowej nie przydziela wystarczjąco dużo zasobów w celu wygenerowania pliku PDF w minuę z 176(!) wykresami, dlatego prawdopodobnie konieczna będzie przynajmniej dwukrrotna generacja plików. 