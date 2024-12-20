# Filip

## Presentation: Expensa

Budgetapp för att hålla koll på sina utgifter. Skapad tillsamans med Mathias. Brainstormade varandras idéer och skapade en gemensam vision.
Förenkla och göra ekonomin enklare. Målgruppen är personer som vill ha koll på sin ekonomi.

Med OCR skannas kvitton och läggs in i appen. Då kan man jämföra med budgeten och se hur mycket som diffar. Man kan även se det i grafform.

Frontend: React och Typescript. Reacr navigation, react native animated, react native
Backend: Node.js/Express.
Databas: MSSQL på Azure.
TypeOrm för att koppla ihop databasen med backend.
Blob storage för att lagra bilder.
JWT för att autentisera användare.

Funktioner

- dokumentuppladdning
- Sökfunktion
- Visualisering av data
- Budgetöversikt

Backend:

- OCR-tolkning
- JWT-autentisering
- Refreshtoken hantering
- Databashantering

Tabeller i databasen:

- User - användare
- Project - projekt
- Expense - utgifter
- Category - kategorier
- Receipt - kvitton
- Invoice - fakturor
- Receipt_items - Köpta varor på kvitton

Vidareutveckling

- Export till Excel eller PDF
- Samarbetsläge
- Kategorisering av utgifter
- Förbättrad analys av utgifter och budget, inklusive interaktiva grafer och insikter

Du svarade på frågorna med tydlig erfarenhet av projektet och teknikerna. Azure frågan svarade du jättebra på.

Flutter kom aldrig på fråga. React Native var det självklara valet. Najs att ni vill släppa ut den på marknaden. Stödsamtal med varandra, då det kändes omöjligt att göra det själv.

## Opponering mot Sven

- Frågade om inlärningskurvan.
  - Ägarskapsmodellen är annorlunda, ta en dag i taget och förstå en bit i taget.
  - Syntaxen är inte alls som Java
  - Det är hopplöst att lära sig i längden utan AI och Copilot.
- Tidskrävande?
  - Parsing av data tog tid, hitta mönster i datan.
  - Började med en enkel version som sedan byggdes om till miljövariabler (globala variabler).
- Om du haft mer tid, vad skulle förbättras eller läggas till?
  - Inget gui, älskar terminalen.
- Kan du hämta statistik från andra sporter?
  - hela den jobbiga parsningen måste göras om, men annars ja
