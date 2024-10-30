# Quran Random Verse Generator

This project fetches random verses from the Quran and generates a PDF document containing 365 randomly selected verses in Arabic. Each verse is displayed with its corresponding Surah name and Ayah number.

## Features

- Download verses from the Quran using the Alquran API.
- Randomly select 365 verses.
- Generate a PDF file formatted with the verses, including the Surah name and Ayah number.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `requests`
  - `json`
  - `random`
  - `pdfkit`
  
- You also need to install [wkhtmltopdf](https://wkhtmltopdf.org/) to generate PDFs.

## Installation

1. Clone the repository or download the project files.
2. Install the required Python libraries. You can do this by running:
   ```bash
   pip install requests pdfkit
