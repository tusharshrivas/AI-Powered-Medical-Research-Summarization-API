import requests

API_URL = "http://127.0.0.1:8000/summarize/"
API_KEY = "my_secure_api_key"


def send_report(report_text):
    """
    Simulate sending a medical report to the API with authentication.

    Parameters:
    - report_text (str): The medical report text.

    Returns:
    - None: Prints the response from the API.
    """
    headers = {"api_key": API_KEY}
    response = requests.post(API_URL, json={"report_text": report_text}, headers=headers)

    if response.status_code == 200:
        print("✅ Summarization Successful!")
        print("Summary:", response.json()["summary"])
    else:
        print("❌ Error:", response.json())


# Example: Sending a sample report
if __name__ == "__main__":
    sample_report = """Patient Name: John Doe
    Age: 62
    Gender: Male
    Chief Complaint: Severe chest pain, shortness of breath, dizziness.
    Medical History: Hypertension, Type 2 Diabetes, Hyperlipidemia. No prior history of myocardial infarction.
    Current Medications: Metformin, Amlodipine, Aspirin.
    Physical Examination:
    - Blood Pressure: 150/95 mmHg
    - Heart Rate: 110 bpm
    - Oxygen Saturation: 94%
    - ECG Findings: ST-segment elevations in leads II, III, and aVF, suggesting acute myocardial infarction.
    - Troponin Levels: Elevated (2.5 ng/mL)
    Diagnosis: Acute Inferior Myocardial Infarction
    Treatment Plan:
    1. Administer aspirin and clopidogrel.
    2. Immediate transfer to the cardiac catheterization lab for angioplasty.
    3. Start IV nitroglycerin and beta-blockers.
    4. Monitor troponin levels and perform echocardiography.
    """
    send_report(sample_report)
