# Carolina

## Rapporter

Dina rapporter var exemplariskt skrivna, förklarade allt som behövdes för att förstå ditt projekt. Du hade en bra förklaring på ditt projekt och hur du tänkt kring det. Du hade en bra struktur på dina rapporter och det var lätt att följa med i ditt tänk.

## Presentation

Harmonibook - i samarbete med startup Emmas massage ( emmas.nu ). Lite krångel med ljudet under presentationen. Hatkärlek med planering.

Gillar att connecta med andra människor, ser förbättringsmöjligheter i allt. Då föddes ideén till Harmonibook. Med enkelhet och minimalism i fokus. Den kan användas som en kalender för att planera sin vardag.

Hjälpa kunder och kundernas kunder att boka och omboka tider. Förenklar hanteringen av bokningar så de slipper gå genom olika vägar för att boka.

Bra jobbat trots två veckors sjukdom.

Framtida uppdateringar:

- Att ha den som widget.
- Iframe för att kunna **bädda in** den på hemsidan.
  - alternativt kan man ladda den via js och visa den på sidan
    för att slippa att iframen, då den ibland kan anses vara en risk
    då iframen kommer från en annan server.
    ```js
    fetch("https://api.example.com/data")
      .then((response) => response.json())
      .then((data) => {
        document.getElementById("content").innerHTML = data.html;
      });
    ```
    eller **htmlelement**
    ```js
    fetch("https://api.example.com/data")
      .then((response) => response.text())
      .then((data) => {
        document.getElementById("content").innerHTML = data;
      });
    ```
    eller **Web Components**
    ```js
    fetch("https://api.example.com/data")
      .then((response) => response.text())
      .then((data) => {
        const template = document.createElement("template");
        template.innerHTML = data;
        document
          .getElementById("content")
          .appendChild(template.content.cloneNode(true));
      });
    ```

Bra svar baserade på erfarenhet, du visade klart att du lidit dig igenom PHP och CSS. bra svar på kniviga frågor.

## Opponering mot Samer

Bra frågor, om både hans plan och kodning. Samer svarade bra på frågorna. Som alltid var du väl förberedd på Samers material och ställde frågor som var relaterade till hans projekt.
