import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailReportDispatcher:
    """
    Sends Builder Core summaries, key metrics, and milestone visual reports via email.
    """

    def __init__(self):
        self.recipient = "james@fullpotential.com"
        self.sender = "builder-core@system.ai"

    def format_report(self, summary):
        return f"""
        <h2>Builder Core Weekly Report</h2>
        <p><strong>Total Cycles:</strong> {summary['total_cycles']}</p>
        <p><strong>Diagnostics Run:</strong> {summary['diagnostics']}</p>
        <p><strong>Improvement Plans:</strong> {summary['plans_made']}</p>
        <p><strong>Last Action:</strong> {summary['last_action']}</p>
        <p><strong>Coverage:</strong> {summary['coverage']}</p>
        <hr>
        <p>This report includes all recent activity from the Builder Core self-evolution loop.</p>
        """

    def send_email(self, summary):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Builder Core Weekly Report"
        msg['From'] = self.sender
        msg['To'] = self.recipient

        html_content = self.format_report(summary)
        msg.attach(MIMEText(html_content, 'html'))

        # NOTE: Actual SMTP config omitted for privacy/safety
        # Simulating successful send
        return {
            "status": "Email queued",
            "to": self.recipient,
            "subject": msg['Subject']
        }

# Example usage (will be wired into scheduler later):
# dispatcher = EmailReportDispatcher()
# summary = core_log_hub.summarize()
# dispatcher.send_email(summary)
