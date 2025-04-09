//complex_data_export_system.py
from abc import ABC, abstractmethod

# Step 1: Define the Implementor interface
class ExportFormat(ABC):
    @abstractmethod
    def export(self, data: dict):
        pass
# Step 2: Create Concrete Implementors for different formats
class CSVExporter(ExportFormat):
    def export(self, data: dict):
        csv_data = ",".join(data.keys()) + "\n" + ",".join(str(value) for value in data.values())
        print(f"Exporting as CSV:\n{csv_data}\n")
class JSONExporter(ExportFormat):
    def export(self, data: dict):
        import json
        json_data = json.dumps(data, indent=2)
        print(f"Exporting as JSON:\n{json_data}\n")
class PDFExporter(ExportFormat):
    def export(self, data: dict):
        # Simulating PDF export output
        print(f"Exporting as PDF:\n{' | '.join(f'{k}: {v}' for k, v in data.items())}\n")

# Step 3: Define the Abstraction
class DataExporter(ABC):
    def __init__(self, exporter: ExportFormat):
        self.exporter = exporter
    @abstractmethod
    def export_data(self, data: dict):
        pass
# Step 4: Create Refined Abstractions for different types of data
class SalesReportExporter(DataExporter):
    def export_data(self, data: dict):
        print("Exporting Sales Report:")
        self.exporter.export(data)
class InventoryReportExporter(DataExporter):
    def export_data(self, data: dict):
        print("Exporting Inventory Report:")
        self.exporter.export(data)

# Step 5 & 6: Client code
if __name__ == "__main__":
    sales_data = {"Month": "January", "Revenue": 15000, "Units Sold": 1200}
    inventory_data = {"Product": "Laptop", "Stock": 50, "Warehouse": "A1"}

    # Different export formats
    csv_exporter = CSVExporter()
    json_exporter = JSONExporter()
    pdf_exporter = PDFExporter()

    # Exporting sales report in multiple formats
    sales_csv = SalesReportExporter(csv_exporter)
    sales_json = SalesReportExporter(json_exporter)

    sales_csv.export_data(sales_data)
    sales_json.export_data(sales_data)

    # Exporting inventory report as PDF
    inventory_pdf = InventoryReportExporter(pdf_exporter)
    inventory_pdf.export_data(inventory_data)

//multi_channel_notification_system.py
from abc import ABC, abstractmethod

# Step 1: Define the Implementor interface
class NotificationChannel(ABC):
    @abstractmethod
    def send(self, message: str):
        pass
# Step 2: Create Concrete Implementors
class EmailChannel(NotificationChannel):
    def send(self, message: str):
        print(f"Sending Email: {message}")
class SMSChannel(NotificationChannel):
    def send(self, message: str):
        print(f"Sending SMS: {message}")
class SlackChannel(NotificationChannel):
    def send(self, message: str):
        print(f"Sending Slack message: {message}")
# Step 3: Define the Abstraction
class NotificationSender(ABC):
    def __init__(self, channel: NotificationChannel):
        self.channel = channel
    @abstractmethod
    def notify(self, message: str):
        pass
# Step 4: Create Refined Abstractions
class UrgentNotification(NotificationSender):
    def notify(self, message: str):
        self.channel.send(f"[URGENT] {message}")
class CasualNotification(NotificationSender):
    def notify(self, message: str):
        self.channel.send(f"[INFO] {message}")

# Step 5 & 6: Use in Client Code
if __name__ == "__main__":
    # Create different channel implementations
    email_channel = EmailChannel()
    sms_channel = SMSChannel()
    slack_channel = SlackChannel()

    # Pair them with different abstraction types
    urgent_email = UrgentNotification(email_channel)
    casual_sms = CasualNotification(sms_channel)
    urgent_slack = UrgentNotification(slack_channel)

    # Trigger notifications
    urgent_email.notify("System outage detected!")
    casual_sms.notify("Your order has been shipped.")
    urgent_slack.notify("Critical security update required.")
  
