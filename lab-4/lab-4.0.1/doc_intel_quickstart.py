# import libraries
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeResult
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest

# Replace hardcoded endpoint and key with environment variables
endpoint = os.getenv("DOCUMENT_INTELLIGENCE_ENDPOINT")
key = os.getenv("DOCUMENT_INTELLIGENCE_KEY")

# helper functions
def get_words(page, line):
    result = []
    for word in page.words:
        if _in_span(word, line.spans):
            result.append(word)
    return result


def _in_span(word, spans):
    for span in spans:
        if word.span.offset >= span.offset and (
            word.span.offset + word.span.length
        ) <= (span.offset + span.length):
            return True
    return False


def analyze_layout():
    # sample document
    formUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-layout.pdf"

    document_intelligence_client = DocumentIntelligenceClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-layout", AnalyzeDocumentRequest(url_source=formUrl)
    )

    result: AnalyzeResult = poller.result()

    if result.styles and any([style.is_handwritten for style in result.styles]):
        print("Document contains handwritten content")
    else:
        print("Document does not contain handwritten content")

    for page in result.pages:
        print(f"----Analyzing layout from page #{page.page_number}----")
        print(
            f"Page has width: {page.width} and height: {page.height}, measured with unit: {page.unit}"
        )

        if page.lines:
            for line_idx, line in enumerate(page.lines):
                words = get_words(page, line)
                print(
                    f"...Line # {line_idx} has word count {len(words)} and text '{line.content}' "
                    f"within bounding polygon '{line.polygon}'"
                )

                for word in words:
                    print(
                        f"......Word '{word.content}' has a confidence of {word.confidence}"
                    )

        if page.selection_marks:
            for selection_mark in page.selection_marks:
                print(
                    f"Selection mark is '{selection_mark.state}' within bounding polygon "
                    f"'{selection_mark.polygon}' and has a confidence of {selection_mark.confidence}"
                )

    if result.tables:
        for table_idx, table in enumerate(result.tables):
            print(
                f"Table # {table_idx} has {table.row_count} rows and "
                f"{table.column_count} columns"
            )
            if table.bounding_regions:
                for region in table.bounding_regions:
                    print(
                        f"Table # {table_idx} location on page: {region.page_number} is {region.polygon}"
                    )
            for cell in table.cells:
                print(
                    f"...Cell[{cell.row_index}][{cell.column_index}] has text '{cell.content}'"
                )
                if cell.bounding_regions:
                    for region in cell.bounding_regions:
                        print(
                            f"...content on page {region.page_number} is within bounding polygon '{region.polygon}'"
                        )

    print("----------------------------------------")


def analyze_invoice():
    # sample document
    invoiceUrl = "https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/sample-invoice.pdf"

    document_intelligence_client = DocumentIntelligenceClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )

    poller = document_intelligence_client.begin_analyze_document(
        "prebuilt-invoice", AnalyzeDocumentRequest(url_source=invoiceUrl)
    )
    invoices = poller.result()

    if invoices.documents:
        for idx, invoice in enumerate(invoices.documents):
            print(f"--------Analyzing invoice #{idx + 1}--------")
            vendor_name = invoice.fields.get("VendorName")
            if vendor_name:
                print(
                    f"Vendor Name: {vendor_name.get('content')} has confidence: {vendor_name.get('confidence')}"
                )
            vendor_address = invoice.fields.get("VendorAddress")
            if vendor_address:
                print(
                    f"Vendor Address: {vendor_address.get('content')} has confidence: {vendor_address.get('confidence')}"
                )
            vendor_address_recipient = invoice.fields.get("VendorAddressRecipient")
            if vendor_address_recipient:
                print(
                    f"Vendor Address Recipient: {vendor_address_recipient.get('content')} has confidence: {vendor_address_recipient.get('confidence')}"
                )
            customer_name = invoice.fields.get("CustomerName")
            if customer_name:
                print(
                    f"Customer Name: {customer_name.get('content')} has confidence: {customer_name.get('confidence')}"
                )
            customer_id = invoice.fields.get("CustomerId")
            if customer_id:
                print(
                    f"Customer Id: {customer_id.get('content')} has confidence: {customer_id.get('confidence')}"
                )
            customer_address = invoice.fields.get("CustomerAddress")
            if customer_address:
                print(
                    f"Customer Address: {customer_address.get('content')} has confidence: {customer_address.get('confidence')}"
                )
            customer_address_recipient = invoice.fields.get("CustomerAddressRecipient")
            if customer_address_recipient:
                print(
                    f"Customer Address Recipient: {customer_address_recipient.get('content')} has confidence: {customer_address_recipient.get('confidence')}"
                )
            invoice_id = invoice.fields.get("InvoiceId")
            if invoice_id:
                print(
                    f"Invoice Id: {invoice_id.get('content')} has confidence: {invoice_id.get('confidence')}"
                )
            invoice_date = invoice.fields.get("InvoiceDate")
            if invoice_date:
                print(
                    f"Invoice Date: {invoice_date.get('content')} has confidence: {invoice_date.get('confidence')}"
                )
            invoice_total = invoice.fields.get("InvoiceTotal")
            if invoice_total:
                print(
                    f"Invoice Total: {invoice_total.get('content')} has confidence: {invoice_total.get('confidence')}"
                )
            due_date = invoice.fields.get("DueDate")
            if due_date:
                print(
                    f"Due Date: {due_date.get('content')} has confidence: {due_date.get('confidence')}"
                )
            purchase_order = invoice.fields.get("PurchaseOrder")
            if purchase_order:
                print(
                    f"Purchase Order: {purchase_order.get('content')} has confidence: {purchase_order.get('confidence')}"
                )
            billing_address = invoice.fields.get("BillingAddress")
            if billing_address:
                print(
                    f"Billing Address: {billing_address.get('content')} has confidence: {billing_address.get('confidence')}"
                )
            billing_address_recipient = invoice.fields.get("BillingAddressRecipient")
            if billing_address_recipient:
                print(
                    f"Billing Address Recipient: {billing_address_recipient.get('content')} has confidence: {billing_address_recipient.get('confidence')}"
                )
            shipping_address = invoice.fields.get("ShippingAddress")
            if shipping_address:
                print(
                    f"Shipping Address: {shipping_address.get('content')} has confidence: {shipping_address.get('confidence')}"
                )
            shipping_address_recipient = invoice.fields.get("ShippingAddressRecipient")
            if shipping_address_recipient:
                print(
                    f"Shipping Address Recipient: {shipping_address_recipient.get('content')} has confidence: {shipping_address_recipient.get('confidence')}"
                )
            print("Invoice items:")
            for idx, item in enumerate(invoice.fields.get("Items").get("valueArray")):
                print(f"...Item #{idx + 1}")
                item_description = item.get("valueObject").get("Description")
                if item_description:
                    print(
                        f"......Description: {item_description.get('content')} has confidence: {item_description.get('confidence')}"
                    )
                item_quantity = item.get("valueObject").get("Quantity")
                if item_quantity:
                    print(
                        f"......Quantity: {item_quantity.get('content')} has confidence: {item_quantity.get('confidence')}"
                    )
                unit = item.get("valueObject").get("Unit")
                if unit:
                    print(
                        f"......Unit: {unit.get('content')} has confidence: {unit.get('confidence')}"
                    )
                unit_price = item.get("valueObject").get("UnitPrice")
                if unit_price:
                    unit_price_code = (
                        unit_price.get("valueCurrency").get("currencyCode")
                        if unit_price.get("valueCurrency").get("currencyCode")
                        else ""
                    )
                    print(
                        f"......Unit Price: {unit_price.get('content')}{unit_price_code} has confidence: {unit_price.get('confidence')}"
                    )
                product_code = item.get("valueObject").get("ProductCode")
                if product_code:
                    print(
                        f"......Product Code: {product_code.get('content')} has confidence: {product_code.get('confidence')}"
                    )
                item_date = item.get("valueObject").get("Date")
                if item_date:
                    print(
                        f"......Date: {item_date.get('content')} has confidence: {item_date.get('confidence')}"
                    )
                tax = item.get("valueObject").get("Tax")
                if tax:
                    print(
                        f"......Tax: {tax.get('content')} has confidence: {tax.get('confidence')}"
                    )
                amount = item.get("valueObject").get("Amount")
                if amount:
                    print(
                        f"......Amount: {amount.get('content')} has confidence: {amount.get('confidence')}"
                    )
            subtotal = invoice.fields.get("SubTotal")
            if subtotal:
                print(
                    f"Subtotal: {subtotal.get('content')} has confidence: {subtotal.get('confidence')}"
                )
            total_tax = invoice.fields.get("TotalTax")
            if total_tax:
                print(
                    f"Total Tax: {total_tax.get('content')} has confidence: {total_tax.get('confidence')}"
                )
            previous_unpaid_balance = invoice.fields.get("PreviousUnpaidBalance")
            if previous_unpaid_balance:
                print(
                    f"Previous Unpaid Balance: {previous_unpaid_balance.get('content')} has confidence: {previous_unpaid_balance.get('confidence')}"
                )
            amount_due = invoice.fields.get("AmountDue")
            if amount_due:
                print(
                    f"Amount Due: {amount_due.get('content')} has confidence: {amount_due.get('confidence')}"
                )
            service_start_date = invoice.fields.get("ServiceStartDate")
            if service_start_date:
                print(
                    f"Service Start Date: {service_start_date.get('content')} has confidence: {service_start_date.get('confidence')}"
                )
            service_end_date = invoice.fields.get("ServiceEndDate")
            if service_end_date:
                print(
                    f"Service End Date: {service_end_date.get('content')} has confidence: {service_end_date.get('confidence')}"
                )
            service_address = invoice.fields.get("ServiceAddress")
            if service_address:
                print(
                    f"Service Address: {service_address.get('content')} has confidence: {service_address.get('confidence')}"
                )
            service_address_recipient = invoice.fields.get("ServiceAddressRecipient")
            if service_address_recipient:
                print(
                    f"Service Address Recipient: {service_address_recipient.get('content')} has confidence: {service_address_recipient.get('confidence')}"
                )
            remittance_address = invoice.fields.get("RemittanceAddress")
            if remittance_address:
                print(
                    f"Remittance Address: {remittance_address.get('content')} has confidence: {remittance_address.get('confidence')}"
                )
            remittance_address_recipient = invoice.fields.get(
                "RemittanceAddressRecipient"
            )
            if remittance_address_recipient:
                print(
                    f"Remittance Address Recipient: {remittance_address_recipient.get('content')} has confidence: {remittance_address_recipient.get('confidence')}"
                )

    print("----------------------------------------")


if __name__ == "__main__":
    # Uncomment to run the layout analysis
    # analyze_layout()
    
    # Uncomment to run the invoice analysis
    analyze_invoice()
