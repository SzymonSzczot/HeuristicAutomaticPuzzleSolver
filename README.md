# HeuristicAutomaticPuzzleSolver
Aplikacja do układania puzzli na podstawie zdjęcia.
Wrzuć swój obraz
Podziel go na wybraną ilość kawałków
Przypisz kawałek do odpowiadającego miejsca za pomocą skryptu

Link do filmu z prezentacją działania: https://youtu.be/2cVUZNkV3CU



## 0. Wymagania

**Python w wersji 3.6+

Moduły Python:

*  opencv-python (cv2)
*  image_slicer
*  matplotlib


## 1. Działanie

Pracę z programem należy rozpocząć od podania ścieżki do obrazka, który chcemy przetwarzać(najlepiej w formacie jpg lub png). 
Następnie program zapyta nas o ilość "kawałków" na jakie chcemy podzielić obraz. Rozmiar tych kawałków jest obliczany automatycznie na podstawie rozmiarów oryginalnego obrazu. Każdy z kawałków jest zapisywany jako osobny plik. Zwracana jest także tablica zawierająca wszystkie kawałki. 

Kawałki używane są jako wzory. Program porównuje każdy wzór z obrazem oryginalnym i znajduje miejsce, które mu odpowiada. Miejsce to jest zaznaczane czerwonym prostokątem.

