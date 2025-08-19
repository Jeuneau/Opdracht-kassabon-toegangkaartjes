class Tarief:
    def ToonTarief(self):
        import json
        # Definieer de tarieven in een dictionary
        # en converteer deze naar een JSON-string
        x = {
            "De tarieven voor de toegang tot het pretpark zijn als volgt:": "",
            "Jonger dan 4 jaar": "gratis",
            "4 t/m 18 jaar": 5, 
            "19 t/m 65 jaar": 10,
            "65-plussers": 8,
            "Bij 5 personen of meer krijgt u 5 euro korting.": ""
            }

        y = json.dumps(x, indent = 4)   
        print(y) 
        