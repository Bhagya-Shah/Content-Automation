# import openai

# # Set up OpenAI API credentials
# openai.api_key = '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'

# # Generate marketing response and subject based on the provided review
# def generate_marketing_response(review):
#     subject_prompt = "Subject:"
#     subject_response = openai.Completion.create(
#         engine="text-davinci-003",  # Use GPT-3.5 model
#         prompt=subject_prompt,
#         max_tokens=100,  # Adjust as needed
#         temperature=0.5  # Adjust as needed
#     )
#     subject = subject_response.choices[0].text.strip()
    
#     prompt = "Review: " + review + "\nSubject: " + subject + "\nResponse:"
#     response = openai.Completion.create(
#         engine="text-davinci-003",  # Use GPT-3.5 model
#         prompt=prompt,
#         max_tokens=450,  # Adjust as needed
#         temperature=0.7  # Adjust as needed
#     )
#     generated_text = response.choices[0].text.strip().replace("Response:", "")
#     return subject, generated_text

# # Example usage
# review_input = "The food at this restaurant is outstanding! Every dish I've tried has been bursting with flavor and made with the freshest ingredients."
# subject_output, response_output = generate_marketing_response(review_input)
# print("Subject:", subject_output)
# print("Response:", response_output)


# import os
# import openai

# openai.api_key = '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'
# def gettext(review):
#     response = openai.Completion.create(
#     model="text-davinci-003",
#     prompt=f"Write a food review response as a marketing text to review : {review}+.",
#     temperature=0.7,
#     max_tokens=600,
#     top_p=1,
#     frequency_penalty=0,
#     presence_penalty=0
#     )
#     return response
# review=""

import openpyxl
import requests

# List of materials (replace with your own list of materials)
materials = [
    "MEDIUM CHAIN MONO-DIGLYCERIDE CAPMUL MCM",
    "TRI-N-BUTYL TINCHLORIDE",
    "Optimus Vaseline Petroleum Jelly MRP 10",
    "MEASLES VACCINE 10 DOSE VIAL (5ML) (S36)",
    "AlbuterolSulfate Inh Aerosol 90mcg",
    "Leuprolide acetate injection 22.5mg/vial",
    "Endura Mass Weight Gainer-Chocolate–500g",
    "OMNIGEL 10 GM",
    "Pirfenidone 267mg Cap 270s",
    "DOLU+LAMI+TENOTAB50/300/300MG90(WHO)E/S",
    "SITAGLIPTIN 100MG TABS28S(CHEMO-CIP-UK)",
    "POLIOMYELITIS VACCINE – 20 DOSE VIAL 50S",
    "Endura Mass Weight Gainer - Banana–500 g",
    "IMATIB 100CAPS 1 X 10'S(AJ MIR-PK)",
    "SORAFENIB TOSYLATE",
    "ETHICS PARA 120MG/5ML ORAL SUSP 200ML(NZ)",
    "ABIRATERONE 500MG 4X14T (AIZ-CIP-UK)",
    "LUMET TABLETS",
    "COFSILS GingerLemon JAR_22+2 Strips Free",
    "AMLO BESY TAB USP 10MG 1000'S(QUALLENT)",
    "Prolyte Gluco-D++ Regular 75+50gm(125g)"
]

# Create an Excel workbook and select the active sheet
wb = openpyxl.Workbook()
sheet = wb.active

# Set the headers in the Excel sheet
headers = ["Material", "Active Ingredient", "Family Belongs To", "Dosage Form", "End Use"]
sheet.append(headers)

# Iterate over each material
for material in materials:
    # Generate a chat completion for the material using the ChatGPT API
    prompt = f"write active ingredient, family belongs to, dosage form, and end use of {material}"
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": "Bearer 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",
            "Content-Type": "application/json"
        },
        json={"messages": [{"role": "system", "content": "/start"}, {"role": "user", "content": prompt}]}
    )
    data = response.json()

    # Extract the completion from the API response
    completion = data["choices"][0]["message"]["content"]

    # Extract the individual fields from the completion
    active_ingredient = ""
    family_belongs_to = ""
    dosage_form = ""
    end_use = ""

    # Parse the completion to extract the required information
    lines = completion.split("\n")
    for line in lines:
        if "Active Ingredient:" in line:
            active_ingredient = line.split(":")[1].strip()
        elif "Family Belongs To:" in line:
            family_belongs_to = line.split(":")[1].strip()
        elif "Dosage Form:" in line:
            dosage_form = line.split(":")[1].strip()
        elif "End Use:" in line:
            end_use = line.split(":")[1].strip()

    # Add the extracted information to the Excel sheet
    row_data = [material, active_ingredient, family_belongs_to, dosage_form, end_use]
    sheet.append(row_data)

# Save the Excel file
wb.save("material_info.xlsx")

