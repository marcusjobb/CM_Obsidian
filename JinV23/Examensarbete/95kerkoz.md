# 95kerkoz
### Feedback på Examensarbete för Kerim 

**Detaljer om projektet**

- **Projekt:** Word Guessing Game
- **Målgrupp:** Spelare som vill utmana sig själva och andra i ett ordgissningsspel 
- **Språk och teknik:** Python, TCP/IP-kommunikation, MongoDB
- **Mål:** Skapa ett server-klient-baserat spel där användare kan gissa ord via nätverkskommunikation
- **Teknologier:** Python, Pymongo, API 
- **Syfte:** Lära sig nätverksprogrammering och databashantering genom att skapa ett interaktivt spel 
- **Backend:** Python, Pymongo 
- **Frontend:** Python 
- **Databas:** MongoDB 
- **Övrigt:** Använde API för att hämta speldata och Pymongo för att interagera med databasen 

**Feedback på examensarbetet**

Kerim, ditt projekt "Word Guessing Game" är ett utmärkt exempel på hur man kan kombinera nätverksprogrammering med spelutveckling. Du har visat stor skicklighet i att skapa både en server och en klientapplikation som kommunicerar via TCP/IP, vilket gör det möjligt för spelare att delta från olika delar av världen. Att inkludera MongoDB för att hantera speldata och använda ett API för att hämta speldata visar på en djup förståelse för moderna teknologier och deras integration.

Din tekniska dokumentation är tydlig och ger en bra översikt över projektets syfte, arkitektur och de verktyg du använt. Du beskriver noggrant hur servern hanterar backend-logiken och hur klienten interagerar med användaren för att starta och köra spelet. Det är imponerande att se hur du har strukturerat ditt arbete och använt Pymongo för att interagera med databasen.

**Feedback på opposition**

Du svarade säkert och tydligt på frågorna under oppositionen, vilket visade att du har en god förståelse för ditt projekt och de teknologier du använt. Dina frågor under oppositionen var också genomtänkta och bidrog till en meningsfull diskussion.

**Förbättringspunkter**

- Du var medveten om några buggar och begränsningar i ditt projekt, såsom servern som stängde ned vid tomma strängar. Det är bra att du redan har identifierat dessa problem, och det skulle vara värdefullt att fortsätta arbeta på att lösa dem.
- Att utforska fler funktioner för spelhistorik och användaranpassningar skulle kunna ge ytterligare värde till ditt projekt. Det finns också potential att använda molnplattformar för att hosta servern och möjliggöra flera klienter samtidigt.

**Betyg**

Ditt arbete med "Word Guessing Game" visar på stor teknisk kompetens och en förmåga att lösa komplexa problem. Din dokumentation och planering var utförlig och väl genomtänkt. Ditt betyg är VG, ett mycket välförtjänt resultat för ditt hårda arbete. Bra jobbat!

---

## Anteckningar från redovisningen

Informerade om Python och dess historik
Python + Nätverk
Spel, 
TCP/IP baserad
Pluspoäng för kycklingen med Pip

Bra lärdom att du fick börja om och strukturera om, ibland får man göra så.
Bra att du utvärderade och la ner de delar du ansåg tog för långt tid eller som inte behövdes
bra beskrivning av hur nätverkskommunikationen körs

Demo
Bra demo, 

## Opponering av Samer

- *Hade du andra lösningar innan du bestämde dig?*
- Allt var tänkt från början, har dock andra brancher med olika lösningar
- *Varför kraschade servern vid tomma strängar*
- Det var en bugg som fick kollas, bra svarat, har bra koll
- While looparna stökade, är det en bra idé att ha en while loop i en server
- While loopar löste problemet temporärt
