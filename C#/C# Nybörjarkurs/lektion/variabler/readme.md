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