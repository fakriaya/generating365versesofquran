import requests
import json
import random
import pdfkit

# Étape 1 : Télécharger le texte du Coran en arabe depuis l'API Alquran.cloud
response = requests.get("http://api.alquran.cloud/v1/quran/ar.alafasy")
quran_data = response.json()["data"]["surahs"]

# Étape 2 : Extraire les informations des versets
verses = []
for surah in quran_data:
    for ayah in surah["ayahs"]:
        verses.append({
            "surah_number": surah["number"],
            "surah_name": surah["name"],  # Added Surah name
            "ayah": ayah["number"],
            "text": ayah["text"]
        })

# Optionnel : Sauvegarder les versets dans un fichier JSON pour vérification
with open("quran_arabic.json", "w", encoding="utf-8") as file:
    json.dump(verses, file, ensure_ascii=False, indent=2)
print("Téléchargement et sauvegarde terminés dans quran_arabic.json")

# Étape 3 : Sélectionner aléatoirement 365 versets
random_verses = random.sample(verses, 365)

# Étape 4 : Formater le contenu pour la génération du PDF
html_content = """
<html>
<head>
    <meta charset="UTF-8"> <!-- Add this line for character encoding -->
    <style>
        body {
            font-family: 'Noto Naskh Arabic', 'Arial', sans-serif;
            direction: rtl; /* Right-to-left text direction */
        }
    </style>
</head>
<body>
    <h1>365 Versets Aléatoires du Coran</h1>
"""
for verse in random_verses:
    surah_number = verse["surah_number"]
    surah_name = verse["surah_name"]  # Get the Surah name
    ayah_number = verse["ayah"]
    text = verse["text"]
    html_content += f"<p><b>Surah {surah_number} ({surah_name}), Ayah {ayah_number}:</b> {text}</p>"
html_content += "</body></html>"

# Étape 5 : Générer le PDF en spécifiant le chemin de wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

# Définir les options pour le PDF
options = {
    'dpi': 300,
    'print-media-type': ''
}

# Générer le PDF avec les options spécifiées
pdfkit.from_string(html_content, "365_versets_aleatoires_du_coran.pdf", configuration=config, options=options)

print("PDF généré sous le nom 365_versets_aleatoires_du_coran.pdf")
