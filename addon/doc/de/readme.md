# TesseractOCR

* Autoren: Rui Fontes, Ângelo Abrantes und Abel Passos do Nascimento Jr.
* [stabile Version] herunterladen[1]
* Kompatibilität: NVDA-Version 2019.3 und höher

## Information

Dieses Add-on verwendet die kostenlose und Open-Source-OCR-Engine (Texterkennung) Tesseract, um eine optische Zeichenerkennung an einem Bilddokument durchzuführen, sei es PDF, JPG, TIF oder andere, ohne dass das Dokument geöffnet werden muss.

Das Ergebnis wird in einem Textdokument mit demselben Namen wie das Original, aber mit der Erweiterung .txt im selben Ordner gespeichert.

Es ermöglicht auch den Zugriff auf WIA-kompatible Scanner, um OCR auf einem Papierdokument durchzuführen. In diesem Fall wird das Dokument mit dem Ergebnis im Ordner „Dokumente“ des Benutzers mit dem Namen OCR.txt abgelegt.

Schließlich können Sie Text aus einem barrierefreien PDF abrufen und ihn im Notepad anzeigen.

## Einstellungen 

Im NVDA-Menü „Einstellungen“ wird ein Abschnitt „TesseractOCR“ hinzugefügt, in dem Sie Folgendes konfigurieren können:

- Sprachen, die bei der Erkennung verwendet werden sollen.
- die Art der zu erkennenden Dokumente.
- ob nach einem Passwort für das PDF gefragt werden soll oder nicht. Wenn diese Option ausgewählt ist und die PDF-Datei kein Passwort hat, drücken Sie einfach die Eingabetaste im Dialogfeld, in dem Sie nach dem Passwort gefragt werden.
- den WIA-Scanner auswählen.
-  Die Scannerauflösung kann zwischen 150 und 400 DPP eingestellt werden.

Mit Ausnahme von Portugiesisch und Englisch, die bereits im Add-on enthalten sind, werden die restlichen Sprachen heruntergeladen und installiert, wenn eine Sprache ausgewählt wird, die noch nicht im Add-on vorhanden ist.

Dies muss mit Deutsch einmal gemacht werden, damit die Erweiterung ordnungsgemäß funktioniert.

Beachten Sie, dass der OCR-Vorgang länger dauert, wenn Sie die Anzahl der ausgewählten Erkennungssprachen erhöhen. Wir empfehlen daher, nur die erforderlichen Sprachen zu verwenden.

Beachten Sie außerdem, dass die Qualität der Erkennung je nach Reihenfolge der Sprachen variieren kann. Wenn das Erkennungsergebnis nicht zufriedenstellend ist, können Sie daher eine andere Reihenfolge  versuchen.

## Befehle

Die Standardbefehle sind:

* Windows+Strg+w – Zum Scannen und Erkennen eines Dokuments mit dem Scanner;
* Windows+Strg+r – Zum Erkennen der ausgewählten Datei;
* Windows+Strg+t – Um Text aus einer barrierefreien PDF-Datei abzurufen.
* Windows+Strg+c – Um den Scanvorgang abzubrechen.

Hinweis: Es muss gewartet  werden, bevor das Dialogfeld mit der Frage erscheint, ob Sie weitere Seiten scannen möchten!

Warten Sie dann einfach, bis die Datei ocr.txt mit dem erkannten Text angezeigt wird.

Diese Befehle können im Dialogfeld „Befehle definieren“ im Abschnitt „TesseractOCR“ geändert werden.

## Bekannte Probleme

* Wenn Sie im Kombinationsfeld „Dokumenttyp“ die Option "Verschiedene" auswählen, enthält der erkannte Text wahrscheinlich viele Leerzeilen
Dies ist ein bekanntes Tesseract-Problem, und ohne dass es viel Verarbeitungszeit in Anspruch nimmt, haben wir noch keine Lösung gefunden. Aber wir haben trotzdem nicht aufgegeben!

## Unterstützte Sprachen

Die in dieser Version unterstützten Sprachen sind:

* Afrikaans
* Albanisch
* Amharisch
* Arabisch
* Armenisch
* Assamesisch
* Aserbaidschanisch (Latein)
* Baskisch
* Weißrussisch
* Bengali
* Bosnisch
* Bretonisch
* Bulgarisch
* Burnese
* Katalanisch/Valencianisch
* Cebuano
* Cherokee
* Vereinfachtes Chinesisch
* Traditionelles Chinesisch
*Korsisch
* Kroatisch
* Tschechisch
* Dänisch
* Deutsch
* Dhivehi
* Niederländisch (Flämisch)
* Dzongkha
* Englisch
* Esperanto
* Estnisch
* Färöisch
* Philippinisch
* Finnisch
* Französisch
* Galizisch
* Georgisch
* Griechisch
* Gujarat
* Haitianisch
* Hebräisch
* Hindi
* Ungarisch
* Isländisch
* Indonesisch
* Inuktitut
* Irisch
* Italienisch
* Javanisch
* Japanisch
* Kannada
* Kasachisch
* Khmer (Zentral)
* Kirgisisch
* Koreanisch
* Kurmanji Kurdisch
* Laotisch
* Latein
* Lettisch
* Litauisch
* Luxemburgisch
* Mazedonisch
* Malaiisch
* Malayalam
* Maltesisch
* Maori
* Marathi
* Mathematische Gleichungen
* Mongolisch
* Nepalesisch
* Norwegisch
* Okzitanisch
* Oriya
* Panjabi
* Afghanisch
* Persisch
* Polnisch
* Portugiesisch
* Quechua
* Rumänisch/Moldauisch
* Russisch
* Sanskrit
* Schottisch-Gälisch
* Serbisch (Latein)
* Slowakisch
* Slowenisch
* Sindi
* Singhalesisch
* Spanisch
* Sundanesisch
* Suaheli
* Schwedisch
* Syrisch
* Tadschikisch
* Tamil
* Zahnstein
* Telugu
* Thailändisch
* Tibetisch
* Tigrinien
* Tonganisch
* Türkisch
* Uigur
* Ukrainisch
* Urdu 
* Usbekisch (Latein)
* Vietnamesisch
* Walisisch
* Westfriesisch
* Jiddisch
* Yoruba

## Unterstützte Bildtypen

Dieses Add-on unterstützt die folgenden Dateitypen:

* PDF
* jpg
* tiff
* png
* bmp
* pnm
* pbm
* pgm
* jp2
* gif
* jfif
* jpeg
* tiff
* spix
* webp

## Deutsche Übersetzung 

 Diese Übersetzung wurde vom NVDA-Team im [BFW Würzburg][2] erstellt.

[1]: https://github.com/ruifontes/tesseractOCR/releases/download/2025.06.14/tesseractOCR-2025.06.14.nvda-addon

[2]: https://www.bfw-wuerzburg.de