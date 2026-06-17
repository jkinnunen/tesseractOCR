# TesseractOCR



* Tekijät: Rui Fontes, Ângelo Abrantes ja Abel Passos do Nascimento nuorempi
* Yhteensopivuus: NVDA 2026.1 ja uudemmat



## Tiedot

Tämä lisäosa käyttää ilmaista ja avoimen lähdekoodin Tesseract OCR -moottoria tekstintunnistuksen suorittamiseen kuvatiedostolle (kuten PDF, JPG tai TIF) tarvitsematta avata sitä.
Tunnistuksen tuloksen sisältävä tekstitiedosto tallennetaan samaan kansioon alkuperäisen tiedoston kanssa samalla nimellä, mutta .txt-tunnisteella.
Lisäosalla voidaan myös suorittaa tekstintunnistus paperiasiakirjoille WIA-yhteensopivien skannereiden avulla.
Tulokset näytetään käyttäjän Tiedostot-kansioon tallennettavassa OCR.txt-tiedostossa.
Lisäosa pystyy myös poimimaan tekstin saavutettavista PDF-tiedostoista XPDF-työkalujen avulla.
NVDA:n asetusvalintaikkunaan on lisätty TesseractOCR-kategoria, jossa voit muuttaa seuraavia asetuksia:

* Tunnistuksessa käytettävät kielet
* Tunnistettavat asiakirjamuodot
* Kysytäänkö PDF-asiakirjan salasanaa. Jos tämä asetus on valittuna ja PDF-ää ei ole suojattu salasanalla, paina Enter salasanaa pyytävässä valintaikkunassa.
* Määritä skannerin tarkkuus väliltä 150–400 pistettä tuumalla.
* Paperin suunnan tunnistus
* Tunnistuksen edistymistä ilmaisevat merkkiäänet

Lisäosaan sisältyviä englantia ja portugalia lukuun ottamatta tunnistuskielet ladataan ja asennetaan niitä valittaessa.
Huom: Tekstintunnistus kestää sitä kauemmin, mitä enemmän tunnistuskieliä on valittuna.
Tämän vuoksi suosittelemme, että käytät vain tarvitsemiasi kieliä.
Huomaa myös, että tunnistuksen laatu saattaa vaihdella sen mukaan, missä järjestyksessä kielet ovat.
Tästä syystä kannattaa kokeilla järjestää kielet eri tavalla, jos tunnistuksen tulos ei ole tyydyttävä.



## Pikanäppäimet

Oletuskomennot ovat:
Win+Ctrl+W: Skannaa skannerissa olevan asiakirjan ja suorittaa sille tekstintunnistuksen
Win+Ctrl+R: Suorittaa tekstintunnistuksen valitulle asiakirjalle
Win+Ctrl+T: Poimii tekstin saavutettavasta PDF-tiedostosta
Win+Ctrl+C: Peruuttaa skannauksen
Huom: Komentoa on käytettävä ennen lisäsivujen skannausta kysyvän valintaikkunan ilmestymistä.

Tunnistetun tekstin sisältävä tekstitiedosto avautuu jonkin ajan kuluttua.

Näitä komentoja on mahdollista muuttaa Näppäinkomennot-valintaikkunan TesseractOCR-osiossa.



## Tunnetut ongelmat

* Kun \"Asiakirjan tyyppi\" -yhdistelmäruudusta valitaan \"Useita\"-vaihtoehto, tunnistettuun tekstiin tulee todennäköisesti paljon tyhjiä rivejä.
Tämä on tunnettu ongelma Tesseractissa, eikä toistaiseksi ole löytynyt sellaista ratkaisua, jota käytettäessä tiedoston käsittely ei kestäisi kauan.



## Tuetut kielet

Tämä versio tukee seuraavia kieliä:

* afrikaans
* albania
* amhara
* arabia
* armenia
* assami
* azeri (latinalainen)
* baski
* valkovenäjä
* bengali
* bosnia
* bretoni
* bulgaria
* burma
* katalaani/valencia
* cebuano
* cherokee
* kiina (yksinkertaistettu)
* kiina (perinteinen)
* korsika
* kroatia
* tšekki
* tanska
* saksa
* divehi
* hollanti (flaami)
* dzongkha
* englanti
* esperanto
* viro
* fääri
* filipino
* suomi
* ranska
* galicia
* georgia
* kreikka
* gudžarati
* haitilainen kreoli
* heprea
* hindi
* unkari
* islanti
* indonesia
* inuktitut
* iiri
* italia
* jaava
* japani
* kannada
* kazakki
* keski-khmer
* kirgiisi
* korea
* kurdi (kurmandži)
* lao
* latina
* latvia
* liettua
* luxemburg
* makedonia
* malaiji
* malajalam
* malta
* maori
* marathi
* matemaattiset yhtälöt
* mongoli
* nepali
* norja
* oksitaani
* orija
* pandžabi
* paštu
* persia
* puola
* portugali
* ketšua
* romania/moldova
* venäjä
* sanskrit
* gaeli
* serbia (latinalainen)
* slovakki
* sloveeni
* sindhi
* sinhali
* espanja
* sunda
* swahili
* ruotsi
* syyria
* tadžikki
* tamili
* tataari
* telugu
* thai
* tiibet
* tigrinja
* tonga
* turkki
* uiguuri
* ukraina
* urdu
* uzbekki (latinalainen)
* vietnam
* kymri
* länsifriisi
* jiddiš
* joruba



## Tuetut kuvamuodot

Tämä lisäosa tukee seuraavia tiedostotyyppejä:

* PDF
* JPG
* TIF
* PNG
* BMP
* PNM
* PBM
* PGM
* JP2
* GIF
* JFIF
* JPEG
* TIFF
* SPIX
* WebP

