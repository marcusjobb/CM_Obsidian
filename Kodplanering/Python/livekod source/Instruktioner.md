
För att inkludera både extraherad information från `pom.xml` och dess källkod i det genererade Markdown-dokumentet, samt hantera andra filer med korrekt syntaxmarkering, kommer vi att anpassa planen enligt följande:

### Uppdaterad plan:

#### 1. **Filtrera och sortera filer:**
- För varje relevant mapp som innehåller "demo" eller "live" i namnet, filtrera och sortera filerna baserat på deras tillägg (.md, .properties, .env, .java, etc.) för att säkerställa att de läggs till i Markdown-dokumentet i önskad ordning.

#### 2. **Extrahera och presentera `pom.xml`:**
- Läs `pom.xml` för varje relevant projekt och extrahera grundläggande projektinformation som projekttyp, namn, version, beroenden, bygg-plugins och rapporter för att inkludera i början av Markdown-dokumentet som en översikt.
- Inkludera även hela innehållet i `pom.xml` i fillistan, presenterat inom ett kodblock märkt med ```xml för att visa XML-koden korrekt.

#### 3. **Generera Markdown-dokumentet:**
- För varje relevant projekt, skapa ett Markdown-dokument som innehåller:
  - Den extraherade projektinformationen från `pom.xml` i en välstrukturerad format.
  - Innehållet i den första .md-filen (t.ex. README.md) direkt i dokumentet.
  - En listad sektion för varje fil i den sorterade ordningen. Varje fils innehåll ska visas inom ett kodblock märkt med det lämpliga språket (t.ex. ```java för Java-koder, ```properties för properties-filer, etc.).

#### 4. **Spara och organisera Markdown-dokument:**
- Spara varje genererad Markdown-fil i en strukturerad mappbana enligt `outputfolder/{year}/{monthnumber}-{daynumber}-projectname` (utan "demo/live" i projektnamnet).

#### 5. **ZIP-arkivering:**
- Skapa en ZIP-fil för varje projekt som innehåller alla relevanta filer och spara den med namnformatet `{year}-{monthnumber}-{daynumber}-projectname` (utan "demo/live") i samma mapp som Markdown-filen.

### Tekniska överväganden:

- **Kodblock i Markdown:** Se till att alla kodblock är korrekt formaterade i Markdown-dokumentet för att garantera korrekt syntaxmarkering och läsbarhet.
- **Filhantering:** Använd pålitliga metoder för att läsa och skriva filer, speciellt när det gäller att hantera stora filer eller komplexa filstrukturer.
- **Effektivitet och prestanda:** Implementera scriptet på ett sätt som effektivt hanterar stora mängder filer och data, med lämplig felhantering och prestandaoptimeringar.

Denna anpassade plan bör tillgodose kravet på att både visa `pom.xml`-filer och annan källkod korrekt inom Markdown-dokumenten, samtidigt som viktig projektinformation extraheras och presenteras översiktligt. Om du är nöjd med denna plan kan vi fortsätta med implementationen.

[[Test av filtrering]]
