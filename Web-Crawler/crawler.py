import os
import json
import webbrowser
import winsound
from datetime import datetime
from ArticleFetcher import ArticleFetcher

def generate_html_report(results, keyword):
    filename = f"Live_Report_{keyword if keyword else 'All'}.html"
    html = f"""
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="refresh" content="60">
        <style>
            body {{ font-family: 'Segoe UI', sans-serif; background: #1a1a1a; color: #eee; padding: 20px; }}
            h1 {{ color: #00ffcc; border-bottom: 2px solid #00ffcc; padding-bottom: 10px; }}
            table {{ width: 100%; border-collapse: collapse; background: #2d2d2d; margin-top: 20px; }}
            th, td {{ padding: 12px; border-bottom: 1px solid #444; text-align: left; }}
            th {{ background: #333; color: #00ffcc; }}
            tr:hover {{ background: #333; }}
            img {{ width: 80px; border-radius: 4px; }}
            .price {{ color: #ffcc00; font-weight: bold; font-size: 1.1em; }}
            .brand {{ color: #aaa; font-style: italic; }}
            a {{ color: #00ccff; text-decoration: none; font-weight: bold; }}
        </style>
    </head>
    <body>
        <h1>Live Monitoring: {keyword if keyword else 'Full Scan'}</h1>
        <p>Gefundene Artikel: {len(results)} | Letztes Update: {datetime.now().strftime('%H:%M:%S')}</p>
        <table>
            <thead><tr><th>Bild</th><th>Hersteller</th><th>Produkt (Link)</th><th>Preis</th></tr></thead>
            <tbody>"""
    
    for r in results:
        html += f"""
            <tr>
                <td><img src="{r.image}" onerror="this.src='https://via.placeholder.com/80?text=N/A'"></td>
                <td class="brand">{r.brand}</td>
                <td><a href="{r.url}" target="_blank">{r.title}</a></td>
                <td class="price">{r.price}</td>
            </tr>"""
    
    html += "</tbody></table></body></html>"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    return filename

def main():
    print("--- JARVIS CRAWLER v4.5 (MANUAL OVERRIDE ENABLED) ---")
    
    # 1. Eingabe-Parameter
    url = input("Ziel-URL (Enter für Mein-Deal.com): ").strip() or "https://www.mein-deal.com"
    keyword = input("Harter Filter (Keyword - Enter für alles): ").strip().lower()
    
    # NEU/RE-INTEGRIERT: Blacklist Abfrage
    blacklist_input = input("Blacklist (Begriffe mit Komma trennen - z.B. 'Halterung, Kabel'): ").strip().lower()
    blacklist = [item.strip() for item in blacklist_input.split(",")] if blacklist_input else []

    # 2. Selektoren-Abfrage (Manuelle Bestätigung)
    # Standard-Selektoren als Vorschlag
    sel = {"container": "article", "title": "h2", "next_btn": "a.next", "image": "img"}
    
    print("\n--- SELEKTOREN KONFIGURATION ---")
    print(f"Aktuelle Selektoren: {sel}")
    change_sel = input("Selektoren anpassen? (j/n): ").strip().lower()
    
    if change_sel == 'j':
        sel['container'] = input(f"Container ({sel['container']}): ") or sel['container']
        sel['title'] = input(f"Titel ({sel['title']}): ") or sel['title']
        sel['next_btn'] = input(f"Next-Button ({sel['next_btn']}): ") or sel['next_btn']
        sel['image'] = input(f"Image ({sel['image']}): ") or sel['image']

    # 3. Extraction
    fetcher = ArticleFetcher()
    results = []
    
    try:
        print(f"\n[*] Mission gestartet. Filter: {keyword if keyword else 'Keiner'} | Blacklist: {len(blacklist)} Begriffe")
        for article in fetcher.fetch(url, sel):
            full_text = (article.title + " " + article.brand).lower()
            
            # Harter Filter Check
            if not keyword or keyword in full_text:
                # Blacklist Check
                is_blacklisted = any(word in full_text for word in blacklist) if blacklist else False
                
                if not is_blacklisted:
                    results.append(article)
                    # Live-Update Dashboard
                    if len(results) % 5 == 0:
                        report = generate_html_report(results, keyword)
                        if len(results) == 5:
                            webbrowser.open(f"file://{os.path.abspath(report)}")
                        print(f"   [+] Treffer: {article.title[:50]}... ({len(results)} gesamt)")

    except KeyboardInterrupt:
        print("\n[!] Notfall-Halt durch Operator. Sichere Daten...")

    if results:
        final_report = generate_html_report(results, keyword)
        print(f"\n[*] Mission beendet. Finale Daten in {final_report}")
        webbrowser.open(f"file://{os.path.abspath(final_report)}")
        winsound.Beep(440, 200); winsound.Beep(660, 400)
    else:
        print("\n[!] Keine relevanten Daten gefunden.")

    input("\nSystem Standby. Enter zum Beenden...")

if __name__ == "__main__":
    main()