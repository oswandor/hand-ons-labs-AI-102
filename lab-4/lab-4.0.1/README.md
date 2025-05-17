# Azure AI Document Intelligence Quickstart Guide
# -----------------------------------------

This quickstart demonstrates how to use Azure AI Document Intelligence (formerly Form Recognizer) 
to extract data from documents using the Python SDK.

## Prerequisites

- Azure subscription - Create one for free at https://azure.microsoft.com/free/
- Python 3.7 or later
- Document Intelligence resource in Azure portal
- pip installed with the Azure AI Document Intelligence client library:
  `pip install azure-ai-documentintelligence==1.0.0b4`

## Setting up

1. Create a Document Intelligence resource in the Azure portal
2. Get your endpoint and key from the resource
3. Update the `endpoint` and `key` variables in the `doc_intel_quickstart.py` file

## Features demonstrated in this sample:

1. **Layout Analysis** - Extract text, tables, selection marks, and more from documents
   - Text extraction with bounding areas
   - Table structure recognition
   - Selection mark detection

2. **Prebuilt Invoice Analysis** - Extract common fields from invoices
   - Vendor and customer information
   - Invoice details (dates, amounts, etc.)
   - Line items and totals

## Running the sample

1. Make sure you've installed the required libraries:
   ```
   pip install azure-ai-documentintelligence==1.0.0b4
   ```

2. Update the endpoint and key in the script

3. Run the script:
   ```
   python doc_intel_quickstart.py
   ```

4. By default, the invoice analysis is enabled. 
   To run the layout analysis, uncomment the `analyze_layout()` line in the main section.

## Learn more

- [Document Intelligence Documentation](https://learn.microsoft.com/azure/ai-services/document-intelligence/)
- [API Reference](https://learn.microsoft.com/python/api/azure-ai-documentintelligence/)
