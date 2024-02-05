# Textová hra

## Jak hrát
Třída `Game` obsahuje seznam instancí objektu dialogů.
Dialogy jsou navzájem provázány pomocí seznamu `options` v každé insanci objektu Dialogue.
Tento seznam obsahuje *"odkazy"* na různé možnosti pokračování, v podobě jejich indexů v poli dialogů.
Formát definice pokračování dialogu: `Text možnosti": index v poli}]`.

Hráč vybírá možnosti zadáním jejího čísla do inputu.
Takhle se prochází postupně vybrané možnosti, dokud

1. seznam `options` příslušného dialogu je prázdný, hra končí a vypisuje se hláška,
2. hráč ztratí veškeré svoje životy,
3. nebo vybraná možnost přesahuje kapacitu pole, což znamená, že je potřeba jí dodělat.

## Základní workflow schéma fungování
![schéma] ()
