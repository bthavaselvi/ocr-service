#  ACCOUNT_NUMBER = "ACCOUNT_NUMBER"
#     ADDRESS = "ADDRESS"
#     ADDRESS_BLOCK = "ADDRESS_BLOCK"
#     AMOUNT_DUE = "AMOUNT_DUE"
#     AMOUNT_PAID = "AMOUNT_PAID"
#     CITY = "CITY"
#     COUNTRY = "COUNTRY"
#     CUSTOMER_NUMBER = "CUSTOMER_NUMBER"
#     DELIVERY_DATE = "DELIVERY_DATE"
#     DISCOUNT = "DISCOUNT"
#     DUE_DATE = "DUE_DATE"
#     GRATUITY = "GRATUITY"
#     INVOICE_RECEIPT_DATE = "INVOICE_RECEIPT_DATE"
#     INVOICE_RECEIPT_ID = "INVOICE_RECEIPT_ID"
#     NAME = "NAME"
#     ORDER_DATE = "ORDER_DATE"
#     OTHER = "OTHER"
#     PAYMENT_TERMS = "PAYMENT_TERMS"
#     PO_NUMBER = "PO_NUMBER"
#     PRIOR_BALANCE = "PRIOR_BALANCE"
#     RECEIVER_ABN_NUMBER = "RECEIVER_ABN_NUMBER"
#     RECEIVER_ADDRESS = "RECEIVER_ADDRESS"
#     RECEIVER_GST_NUMBER = "RECEIVER_GST_NUMBER"
#     RECEIVER_NAME = "RECEIVER_NAME"
#     RECEIVER_PAN_NUMBER = "RECEIVER_PAN_NUMBER"
#     RECEIVER_PHONE = "RECEIVER_PHONE"
#     RECEIVER_VAT_NUMBER = "RECEIVER_VAT_NUMBER"
#     SERVICE_CHARGE = "SERVICE_CHARGE"
#     SHIPPING_HANDLING_CHARGE = "SHIPPING_HANDLING_CHARGE"
#     STATE = "STATE"
#     STREET = "STREET"
#     SUBTOTAL = "SUBTOTAL"
#     TAX = "TAX"
#     TAX_PAYER_ID = "TAX_PAYER_ID"
#     TOTAL = "TOTAL"
#     VENDOR_ABN_NUMBER = "VENDOR_ABN_NUMBER"
#     VENDOR_ADDRESS = "VENDOR_ADDRESS"
#     VENDOR_GST_NUMBER = "VENDOR_GST_NUMBER"
#     VENDOR_NAME = "VENDOR_NAME"
#     VENDOR_PAN_NUMBER = "VENDOR_PAN_NUMBER"
#     VENDOR_PHONE = "VENDOR_PHONE"
#     VENDOR_URL = "VENDOR_URL"
#     VENDOR_VAT_NUMBER = "VENDOR_VAT_NUMBER"
#     ZIP_CODE = "ZIP_CODE"
from dataclasses import dataclass
from response.Address import Address
from response.LineItem import LineItem
class ReceiptSummary:
   address: Address
   accountNumber: str
   amountDue: float
   amountPaid: float
   customerNumber: str
   discount: float
   gratuity: float
   name: str
   invoiceReceiptDate: str
   orderDate: str
   