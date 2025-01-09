# Ghostbananas

Kul spel!

Kollade igenom koden, mest testerna och hittade en del mystiska saker.


**GhostBananasTestProjekt**
- GameConsoleHelperTest.cs - Att använda en stringwriter för att hantera outputs… genialt! Kul check med hur långt tid testet tar.
- IsgrottansHjartaTest.cs - bra test av klassen
- **ItemTest.cs** är tom - den saknar kod, vill man vara petig kan man kolla så att constructor och properties gör det de ska göra
- **NPC.cs** är också tom
- **PepparkaksBynTest.cs** bra och specifik testande
- **PlayerTest.cs** är tom
- **PolarkylansSkogTest.cs** är bra, den tar stickprov på klassen
- **RoomTest.cs** är tom
- **RudolfsHedTest.cs** tar också stickprov
- **TomteLandTest.cs** tar också stickprov
- **CommandHandler.cs** Wow… den är exemplarisk! Riktigt snyggt jobbat där! Smart planerat att mocka inputdelen. Dock kan det bli problem om ni får för er att göra så att spelet fungerar i olika språk ;)
- **GameEngineTest.cs** Det första som lockar min uppmärksamhet där är public void Test1() med innehållet Assert.False(false); … OK… vad är poängen med denna?
- **GameStateTest.cs** Bra stickprovstester.
- InputHandlerTest.cs denna älskar jag bara, det är sjukt krångligt att testa inputs men denna lösning är hur bra som helst.
- MainMenuTest.cs lika snyggt som förra, bra lösning för att kontrollera inputs och därmed styra menyn från koden! Najs!!!
- UnitTest1.cs - ännu en tom fil
- MainMenuTest.UnitTest1.cs - tom fil
- MariaTestClass.UnitTest1.cs - Filnamnet ska alltid vara likadan som klassens namn. Grymt att du har StringWriter för att fånga in outputs. OMG StringAsserts också, nu blir jag lyrisk, jag glömmer alltid att använda dem, men man ska använda rätt assert till rätt typ! Bra gjort!
- **GameDisplayTest.cs** är tom men… Den har en kommentar att koden kommer senare. Helt OK att lämna det så!
- Bonusmaterial hade en massa bortkommenterad kod, men ingen förklaring till varför. Antingen skriver man en kommentar om varför det är bortkommenterad eller så tar man bort den före inläming eller Pull-request.

**Vad kunde ha gjorts bättre**
- Många tomma filer som inte borde ha kommit med i inlämningen.
- Några av klasserna hade inga tomrader mellan metoderna och någon klass hade flera tomrader i slutet, innan sista klamret.
- Tänk på att alltid snygga upp och refaktorera innan inlämning (eller pull request)

**Allt bra i slutändan**
Testerna kollar om stickproven stämmer vilket gör att storyn alltid kommer att ha samma startpunkt. 
 