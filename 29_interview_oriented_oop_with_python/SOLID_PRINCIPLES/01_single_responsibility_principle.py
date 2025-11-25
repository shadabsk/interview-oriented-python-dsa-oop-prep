'''
Single Responsibility Principle (SRP) - Single class should be responsible
in doing a single job.
'''


class Invoice:
    def calculate_total(self):
        pass


class InvoiceRepository:
    def save(self, invoice):
        pass


class EmailService:
    def send_invoice(self, invoice):
        pass
