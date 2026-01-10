# Python-Tools

Dieses Repository beherbergt eine Sammlung von Python-Skripten, die für diverse Automatisierungs- und Sicherheitsaufgaben konzipiert wurden. Die Tools umfassen Funktionen zum Exportieren von Git-Repository-Informationen, Netzwerk-Scans sowie Web-Crawling zur Extraktion von Artikeldaten.

## Installation

Um die Skripte in diesem Repository nutzen zu können, müssen die erforderlichen Python-Abhängigkeiten installiert werden. Es wird dringend empfohlen, eine virtuelle Umgebung zu verwenden.

1.  **Virtuelle Umgebung erstellen und aktivieren (Optional, aber empfohlen):**

    ```bash
    python -m venv venv
    # Auf Windows:
    .\venv\Scripts\activate
    # Auf Linux/macOS:
    . venv/bin/activate
    ```

2.  **Abhängigkeiten installieren:**

    Navigieren Sie in das entsprechende Unterverzeichnis und installieren Sie die dort gelisteten Abhängigkeiten. Für den Web-Crawler:

    ```bash
    cd Web-Crawler
    pip install -r requirements.txt
    ```

    Für `Automation-Helpers/GitExporttoyaml.py` könnte `PyYAML` erforderlich sein, falls nicht bereits global installiert:

    ```bash
    pip install PyYAML
    ```

## Skripte & Funktionen

| Dateiname                               | Funktion                                            | Beschreibung                                                                                                                                                             |
| :-------------------------------------- | :-------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Automation-Helpers/GitExporttoyaml.py` | Git-Informationen nach YAML exportieren             | Sammelt detaillierte Informationen (wie aktuellen Branch und Remote-URL) von Git-Repositories und exportiert diese strukturiert in eine YAML-Datei.                     |
| `Network-Scanner/netscan.py`            | Einfacher TCP Port-Scanner                          | Ein schlanker Python-basierter Port-Scanner, der verwendet wird, um offene TCP-Ports auf einem angegebenen Zielhost zu identifizieren.                                  |
| `Web-Crawler/ArticleFetcher.py`         | Artikel-Fetcher für Web-Crawler                     | Eine Klasse, die für das Abrufen von Webseiteninhalten und das Parsen spezifischer Daten (z.B. Titel, Marke, Preis) mittels definierter Selektoren zuständig ist. |
| `Web-Crawler/CrawledArticle.py`         | Datenmodell für gecrawlte Artikel                   | Definiert eine `dataclass` zur standardisierten Speicherung von extrahierten Artikelinformationen wie Titel, Marke, Preis, Bild-URL und Artikel-URL.                 |
| `Web-Crawler/crawler.py`                | Interaktiver Web-Crawler                            | Ein umfassender Web-Crawler, der Webseiten interaktiv durchsucht, Artikelinformationen extrahiert und diese in einem generierten HTML-Bericht zusammenfasst.            |

## Ordnerstruktur

```
.
├── Automation-Helpers
│   ├── GitExporttoyaml.py
│   └── README.md
├── Network-Scanner
│   ├── netscan.py
│   └── README.md
├── Web-Crawler
│   ├── ArticleFetcher.py
│   ├── CrawledArticle.py
│   ├── crawler.py
│   ├── README.md
│   └── requirements.txt
├── .gitignore
├── GEMINI_TASK.txt
├── README.md
└── .git
```