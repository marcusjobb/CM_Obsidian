# Variabler

Variabler är det som vi använder mest inom programmering. En variabel är ett värde som kan förändras (dess innehåll varierar, därav namnet).

Man kan se variabler som behållare av data. Dess innehåll kan förändras men det kommer alltid att vara av samma sorts data. Ungefär som en sockerskål eller salt och pepparkar. Man häller alltid socker i sockerskålen, alltid salt i ett saltkar och alltid peppar i en pepparkar.

I C# har vi olika typer av data vi kan stoppa in i våra variabler. Här är en lista på de vanligaste.

| Datatyp | Typ                                 | Exempel                     | Kommentar                            |
| :------- | :----------------------------------- | :--------------------------- | :------------------------------------ |
| byte    | Små tal                             | 0 - 255                     | Liten men effektiv                   |
| short   | Lite större än byte                 | -32,768 to 32,767           | Snabb men kort                       |
| int     | heltal                              | 4, 8, 15, 16, 23, 42        | Snabbaste nummertypen                |
| long    | Stora heltal                        | 9999999999                  | Långsammare än int                   |
| float   | decimaltal (4 bytes)                | 3.1415                      | Snabbare än double                   |
| double  | fler decimaltal (8 bytes)           | 3.1415                      | Dubbelt så stor som float, långsam   |
| decimal | Många decimaltal                    | 3.1415                      | Exakt men långsammast                |
| char    | ett tecken                          | ‘A’, ‘C’,‘D’,‘C’            | Bara ett tecken, får aldrig vara tom |
| string  | text, egentligen en lång rad tecken | “quoth the raven nevermore” | Vanlig text                          |
|         |                                     |                             |                                      |

När vi skapar en variabel för att använda i vårt program säger vi att vi instansierar variabeln, alltså att vi skapar en instans av variabeln. Detta gör vi genom att ange typen av variabel vi ska ha, i detta fall ett heltal (int) och sedan namnet på variabeln.

```cs 
// Instansierar variabler
int xCoordinate;
int yCoordinate;
```

När vi ger våra variabler ett värde kallas det att vi tilldelar den ett värde. Vi använder nu namnet till variabeln för att tilldela den ett värde.
```cs 
// Tilldelar värden till variabler
xCoordinate = 10;
yCoordinate = 15;
```

Som du ser, så behöver vi inte ange typen igen, för variabeln vet redan vad den ska ha för typ, då vi angav det vid instansieringen.

Men för enkelhetens skull så gör vi oftast instansiering och tilldelning i samma rad.
```cs 
// Instansierar variabler
string namn = "Bruce";
string efternamn ="Wayne";
```

Orsaken till att vi gör detta är att vi nu kan skriva program som räknar ut positioner baserade på x och y koordinaterna vi angav, och sedan skriva ut

```cs
Console.WriteLine($"{namn} {efternamn} befinner sig på coordinaterna {xCoordinate},{yCoordinate}")
```

Detta i sin tur betyder att vi kan med enkelhet ändra namn, efternamn, x, y koordinater utan att behöva ändra särskilt mycket i vårt program.

Namnet på variabeln är det som vi kommer att använda för att arbeta med det värde som variabeln har. På samma sätt som vi tilldelar personer eller myndigheter telefonnummer. 

En butik blev rånad, ring polisen! Då vet vi att man menar 112. Fram till 2008 var numret 90000. Vi kan alltså uppdatera vår kod genom att bara ändra i en rad.
```cs 
// int polis = 90000; -- Gamla numret, gäller inte längre
int polis = 112;
Make_Phonecall(polis);
```

Jag är hungrig! Beställ en pizza! 
Pizzerian närmast Campus Mölndal är Pizzeria Mums, alltså ringer vi dit!
```cs
int pizzeriaMums = 031400034;
string favPizza = "Tartufo";
orderPizza(pizzeriaMums, favPizza);
```

Vi tar ett annat exempel, vi ska räkna ut åldern på en person. För detta ska vi använda oss av en färdig typ som finns i C# kallad DateTime. DateTime håller koll på dagens datum och tid så exakt den kan (baserat på datorns interna klocka).

För att kunna se skillnaden i dagar mellan två datum måste vi skapa ett datumobjekt, men det är tack och lov väldigt enkelt. Koden kan se lite skrämmande ut men den är ganska logisk och lätt att följa.
```cs 
// Deklarera variabler
string name="Finn Wolfhard";
int year = 2002;
int month = 12;
int day = 23;

// Ta reda på dagens datum
DateTime today = DateTime.Now;

// Skapa ett datumobjekt med födelsedatan
DateTime birthday = new DateTime(year, month, day);

// Beräkna antal dagar som skiljer från födelsedagen till nu och dela med 365.25
int age = (int)((today - birthday).TotalDays/365.25);

Console.WriteLine($"{name} är {age} år gammal");
```

Tack vare variablerna kan du nu lätt ändra det till ditt namn och din födelsedata i deklarationsdelen, resten av programmet kan köra precis som den är.