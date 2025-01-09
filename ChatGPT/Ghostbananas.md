# Ghostbananas

Kul spel!

Kollade igenom koden, mest testerna och hittade en del mystiska saker.

**GhostBananasTestProjekt**
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


Testerna här är bra, men de är oftast positiva. Ni testar om man kan gå “right” när rummet har en utgång “right” men vad händer om rummet har “right” och jag går “left”?

testerna kollar om stickproven stämmer vilket gör att storyn alltid kommer att ha samma startpunkt. 







**GameDisplayTest.cs** är tom
- 