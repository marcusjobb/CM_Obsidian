# Carolina – Feedback på Arbeten och Presentation

## Rapporter

Dina rapporter var exemplariskt skrivna. Det var enkelt att följa med i hur du tänkt kring ditt projekt. Du lyckades förklara projektet och dess syfte på ett tydligt och konkret sätt. Det märks att du har lagt ner mycket tid och energi på att göra rapporterna utförliga och förklarande.

## Presentation: Harmonibook

Din presentation om _Harmonibook_, som du utvecklat i samarbete med _Emmas massage_, var både inspirerande och genomtänkt. Trots lite tekniskt strul med ljudet lyckades du hålla en professionell nivå genom hela presentationen. Du visade god kännedom för PHP, CSS, och JavaScript, och du lyckades förklara ditt projekt på bra sätt. Du visade också att även om du inte gillade PHP och CSS så fick du till en grym produkt ändå.

**Om projektet:**

Harmonibook är en minimalistisk kalender- och bokningsapplikation som hjälper kunder och deras kunder att enkelt boka och omboka tider. Det är ett bra exempel på hur teknik kan användas för att förenkla vardagsrutiner och minska behovet av manuella arbetsmoment.

**Styrkor i presentationen:**

- Du visade tydligt hur du ser förbättringsmöjligheter i allt, vilket reflekterades i ditt arbete med Harmonibook.
- Enkelhet och användarvänlighet var i fokus, vilket är en styrka i ett sådant projekt.
- Du presenterade framtida uppdateringar, som att integrera Harmonibook som en **widget** eller via **JavaScript**, och du visade exempel på kod för att implementera detta. Dina kodförslag var användbara och visar att du har tänkt framåt i projektet.

Trots att du varit sjuk i två veckor lyckades du ändå hålla ihop projektet och presentera det på ett tydligt sätt. Det märktes också att du har gått igenom utmaningar med PHP och CSS men tagit dig igenom det med en positiv attityd.

## Opponering mot Samer

Din opponering mot Samer var väl förberedd och visade att du hade satt dig in i hans material. Du ställde bra frågor om både hans planering och kodning, vilket ledde till en konstruktiv diskussion. Dina frågor var relevanta och relaterade till hans projekt, och du bidrog med värdefull feedback. Dina frågor var skarpa och gav Samer en hel del att tänka på.

## Sammanfattning

Du har visat prov på både teknisk kompetens och förmåga att tänka framåt när det gäller vidareutveckling av ditt projekt. Din presentation var inspirerande, och din opponering visade på en god förmåga att analysera och ge konstruktiv kritik. Bra jobbat, och lycka till med framtida utveckling av Harmonibook!

## Tips:

Nackdelen med Iframe är att den kan misstas för ett virus, då den laddar innehåll från en annan server.

Alternativ till Iframe kan man ladda den via js och visa den på sidan
för att slippa att iframen, då den ibland kan anses vara en risk
då iframen kommer från en annan server.

```js
fetch("https://api.example.com/data") // Hämta data från server
  .then((response) => response.json()) // Gör om till json
  .then((data) => {
    // Skriv ut datan i din div kallad "content"
    document.getElementById("content").innerHTML = data.html;
  });
```

eller **htmlelement**

```js
fetch("https://api.example.com/data") // Hämta data från server
  .then((response) => response.text()) // Gör om till text
  .then((data) => {
    // Skriv ut datan i din div kallad "content"
    document.getElementById("content").innerHTML = data;
  });
```

eller **Web Components**

```js
fetch("https://api.example.com/data") // Hämta data från server
  .then((response) => response.text()) // Gör om till text
  .then((data) => {
    // Skapa ett template som ska innehålla datan
    const template = document.createElement("template");
    template.innerHTML = data; // Lägg in datan i template
    document
      .getElementById("content") // Hämta elementet med id "content"
      .appendChild(template.content.cloneNode(true)); // Lägg till template i content
  });
```

Hoppas någon av förrslagen funkar för dig!
