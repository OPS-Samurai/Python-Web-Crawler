# Jarvis Web Crawler v4.0 (Autonomic & Stealth)

Ein modularer, hochgradig flexibler Web-Crawler, entwickelt für die effiziente Extraktion von Daten aus Blogs und News-Portalen. Das System verfügt über eine automatische Strukturanalyse und ein interaktives Dashboard.

## 🚀 Features

* **Auto-Discovery**: Analysiert die Zielseite vorab und schlägt passende CSS-Selektoren vor.
* **Stealth-Modus**: Integrierte Cool-Down-Phasen (Throttling) nach 100 Seiten zur Vermeidung von IP-Sperren.
* **Präzisions-Filter**: Kombination aus hartem Keyword-Filter und optionaler Blacklist.
* **Blackbox-Logging**: Detaillierte Fehlerprotokolle (`crawler_errors.log`) und HTML-Dumps bei Fehlern zur forensischen Analyse.
* **HTML Dashboard**: Automatisierte Erstellung eines interaktiven Dark-Mode Berichts mit Thumbnails und Direktlinks zum Angebot.

## 🛠 Installation

### 1. **Repository klonen:**
   ```bash
   git clone [https://github.com/IHR_BENUTZERNAME/CrawlerPython.git](https://github.com/IHR_BENUTZERNAME/CrawlerPython.git)
   cd CrawlerPython
   ```
### Virtuelle Umgebung erstellen:

```bash
python -m venv .venv
.\.venv\Scripts\Activate
```

Abhängigkeiten installieren:

```bash
pip install -r requirements.txt
```

## 📖 Nutzung
Starten Sie das Hauptskript:

```bash
python crawler.py
```
Das System führt Sie durch den Prozess:

URL eingeben: Zieladresse (z.B. mein-deal.com).

Filter setzen: Keywords für die Suche festlegen.

Blacklisted Keywords: Keywords für die Blacklist festlegen. 

Recon akzeptieren: Die vorgeschlagenen Selektoren bestätigen.

Dashboard sichten: Nach 10 Treffern öffnet sich automatisch der HTML-Report.

## 📁 Projektstruktur
crawler.py: Hauptsteuerung, Filterlogik und Dashboard-Generator.

ArticleFetcher.py: Die Crawling-Engine inkl. Stealth-Mechanismen.

CrawledArticle.py: Datenklasse für die Artikelstruktur.

requirements.txt: Benötigte Python-Bibliotheken (requests, beautifulsoup4).
