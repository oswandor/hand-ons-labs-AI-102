# Sample form for testing the Document Intelligence service

This directory contains a sample form that can be used to test the Document Intelligence service.

## Using the sample form

The sample form located in this folder can be used to test Document Intelligence functionality. You can:

1. Use it as a test form for the prebuilt model
2. Include it as part of your training set when training custom models

## Training your own models

To train a custom model, you need:

1. At least 5 forms of the same type/layout
2. At least 5 filled instances of each field you want to extract
3. Both training and test forms should have similar layouts

### Best practices for custom model training

- Use clear, high-quality scans
- Make sure field labels are consistent across forms
- Include variations in how forms are filled out
- Include both blank and filled forms
- Train with representative samples of what you'll process in production

### Upload your training data

Training data should be uploaded to an Azure Blob Storage container. You'll need:

1. A Storage Account in Azure
2. A container with your training documents
3. A SAS URL to securely access the container
4. Minimum of 5 forms of the same type

## Processing results

After analyzing forms, you can work with:

- Key-value pairs extracted from the form
- Tables detected in the document
- Text content with position information
- Field values with confidence scores

Keep in mind that custom models may require fine-tuning for optimal performance.
