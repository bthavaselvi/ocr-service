from common.DocumentType import DocumentType
from service.OCRService import BusinessCardService,InvoiceService,IDService,GeneralDocumentService

class OCRServiceFactory:
    @staticmethod 
    def create_OCR_service(document_type):
        if document_type == DocumentType.BUSINESS_CARD.value :
            return  BusinessCardService()
        elif document_type == DocumentType.INVOICE.value:
            return InvoiceService()
        elif document_type == DocumentType.ID.value:
            return IDService()
        elif document_type == DocumentType.GENERAL.value:
            return GeneralDocumentService()
        else:
            raise Exception('Invalid document type')