# To run this code you need to install the following dependencies:
# pip install google-genai

import os
from google import genai
from google.genai import types


def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-3-flash-preview"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text="""INSERT_INPUT_HERE"""),
            ],
        ),
    ]
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="HIGH",
        ),
        system_instruction=[
            types.Part.from_text(text="""Vous êtes un expert en Vision par Ordinateur et en Micro-finance. 
Votre mission est d'analyser une capture d'écran d'historique de transactions mobile (Orange Money, MTN, etc.).

ÉTAPES :
1. OCR : Extrayez chaque transaction visible (Date, Type, Montant).
2. ANALYSE : Calculez un \"Score de Confiance\" (0-100) basé sur la régularité des revenus et le sérieux des dépenses.
3. CONSEIL : Générez un plan d'épargne hebdomadaire réaliste.

RÉPONSE STRICTE EN JSON :
{
  \"statut\": \"Analyse réussie\",
  \"donnees_extraites\": [{\"date\": \"\", \"type\": \"\", \"montant\": 0}],
  \"score_confiance\": {
    \"note\": 0,
    \"justification\": \"\"
  },
  \"plan_epargne\": {
    \"montant_hebdo\": 0,
    \"objectif_3_mois\": 0,
    \"conseil_cle\": \"\"
  }
}"""),
        ],
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if text := chunk.text:
            print(text, end="")

if __name__ == "__main__":
    generate()


