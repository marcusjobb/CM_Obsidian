# Powerfighters

### **Utvärdering av PowerFighters**

**Gruppmedlemmar:**

- **Hugo**
- **Niklas**
- **Ali-Reza**
- **Amir**

### **Kodgranskning**

#### **Testklasser**

- **PlayerTest.cs (Amir):**  
    Testerna är välgjorda och testar grundläggande funktioner som spelarens namn och inventariehantering. StringWriter används för att fånga konsolutmatning, vilket är en bra lösning. Dock kunde fler tester ha skrivits, exempelvis för exception cases och valideringar.
    
- **ItemTest.cs (Amir):**  
    Grundläggande tester är på plats och hanterar visning av föremålsinformation och boxhantering. Det är tydligt att fokus låg på att säkerställa rätt utmatning och logik, men några tester för edge cases saknas här också.
    
- **GameEngineTest.cs (Hugo):**  
    Här syns Hugos skicklighet tydligt. Testerna täcker spelmotorns funktioner på ett imponerande sätt, och det märks att stor vikt har lagts vid robusthet och användarupplevelse.
    

#### **Övriga klasser**

- **CommandHandler.cs (Niklas):**  
    En exceptionellt välgjord klass. Här syns tydligt hur Niklas har arbetat för att skapa en flexibel och återanvändbar lösning. Bra användning av mockning för att testa input, men som nämnt i rapporterna kan framtida utmaningar med språkhjälpmedel behöva hanteras. 
    
- **Data-klasserna (Ali-Reza):**  
    Klasserna för datahantering är funktionella, men vissa saknar kommentarer och kunde vara mer självdokumenterande. Det verkar som att komplexiteten i början av projektet gjorde att vissa delar av designen fick strömlinjeformas senare. Detta är förståeligt, men det är viktigt att prioritera refaktorisering nästa gång.
    

#### **Övriga observationer**

- Flera tomma testfiler följde med i inlämningen. Dessa borde ha rensats bort innan inlämning.
- Bristen på enhetlighet i kodformatet är märkbar, exempelvis gällande tomma rader och formattering. Detta är ett område för förbättring för hela gruppen.

---

### **Arbetsinsatser och reflektioner**

- **Hugo:**  
    Enastående arbete med att sammanföra hela projektet. Hugo har axlat en ledarroll och knutit samman de lösa trådarna. Detta arbete är ovärderligt och har tydligt bidragit till projektets _framgång_. Fantastiskt jobbat! Du var som Spindelmannen i nätet... eller nåt sånt.
    
- **Niklas:**  
    Mycket gediget arbete på menyer och inputhantering. Niklas visar stor skicklighet i att skapa robust kod, och det märks att han bidragit starkt, särskilt i projektets senare skeden.
    
- **Ali-Reza:**  
    Bidragit med många idéer och initialt designarbete, men det framgår att tidspressen gjorde att flera funktioner och klasser inte kunde realiseras fullt ut. Viktigt att fokusera på att avsluta arbetet mer strukturerat nästa gång. Även om du kanske planerade för stort låt det inte hindra din fantasi inför framtida projekt.  Just nu hade ni inte tid till det, men i framtida projekt kan det ändras. Då kommer du att skapa fantastiska saker. Planera stort, sikta mot stjärnorna så att om du failar åtminstone når trädtoppen, som man brukar säga.  
    
- **Amir:**  
    Har bidragit med tester för Player- och Item-klasserna, men deltagandet verkar ha varit sporadiskt. Det är viktigt att öka engagemanget och närvaron i framtida projekt. Förståeligt för att du haft mycket att komma ifatt med, i framtida projekt kommer saker och ting att flyta på mycket bättre ska du se.
    

---

### **Testklasser**

1. **InputHandlerTest.cs**  
    Fantastisk testklass! Hanterar både giltig och ogiltig inmatning med mockade objekt. Testerna är robusta och tydliga, och timeout-implementeringen är ett bra skydd mot oändliga loopar. Den här klassen är som en perfekt julklapp – genomtänkt, funktionell och precis vad man ville ha! Tummen upp! 🎁
    
2. **ItemTests\UnitTest1.cs**  
    Tom. Precis som en julstrumpa som saknar godis. Den borde inte ha varit med i inlämningen. Vi uppskattar tanken, men nästa gång hoppas vi på lite innehåll!
    
3. **PowerFightersXmas.Test\Test1.cs**  
    Ännu en tom testfil – som en tom presentask under granen. Bra att den är där, men vad innehåller den egentligen? Inget denna gång. Ack...
    
4. **PlaceholderTest.cs**  
    Helt tom. Är det en placeholder? Är det en kolbit? Har Krampus varit framme? Det känns som att tomten säger: “Din julklapp kommer… nästa år”. En snabb kommentar om syftet hade klargjort detta. Eller ta bort den bara.
    
5. **LogicTests\CommandHandlerTests.cs**  
    En riktig julstjärna! Testerna täcker viktiga kommandon som “go” och “take”. Det är som att ha Rudolf som guidar tomtens släde – tydligt, pålitligt och funktionellt. Bra jobbat!
    
6. **LogicTests\GameEngineTests.cs**  
    Bra tester för GameEngine! Det är som att testa om tomtens släde lyfter och landar smidigt. Spelets huvudloop är stabil och redo att leverera julstämning. Ett genomtänkt och robust jobb här.
    
7. **LogicTests\GameStateTests.cs**  
    Stickprovstesterna i denna klass känns som att kolla om granen är rätt dekorerad. Testerna säkerställer att spelaren kan navigera mellan rum och hantera föremål. Mycket bra!
    
8. **PowerFightersXmas.Test\InputHandlerTest.cs**  
    En tvilling till den första InputHandlerTest. Dubbel julklapp? Kanske lite onödigt om de är identiska, men en reserv är alltid bra om den fyller en funktion.
    
9. **PowerFightersXmasTest\TestSaveAndLoadPlayer.cs**  
    Den här testklassen är som att packa in och packa upp julklappar – allt fungerar smidigt och utan rivna paket! Det är tydligt att spar- och laddningsfunktionerna är prioriterade och robusta. Bra gjort!
    

---

### **Sammanfattning**

Powerfighters har levererat ett grymt coolt spel med en tydlig arbetsfördelning. Dock framgår det tydligt från både rapporter och kod att gruppens samarbete ibland saknade struktur, vilket gjorde att Hugo fick ta en ledarroll och knyta samman projektet. Detta är imponerande, men samtidigt ett förbättringsområde för gruppen som helhet. 

Powerfighters har trots vissa utmaningar med arbetsfördelningen. Koden är imponerande i sin struktur och funktionalitet, särskilt tack vare Niklas och Hugos insatser. Förbättringar inom dokumentation och kommunikation kan ytterligare höja kvaliteten i framtida projekt. Bra jobbat! 🎉