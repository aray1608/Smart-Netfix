from fpdf import FPDF
from datetime import datetime
import platform
import socket

def clean_text(text):
    return text.encode("ascii", errors="ignore").decode().strip()  # Removes any emojis or non-ASCII

def create_report(internet, dns, download, upload, ping, suggestions):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    filename_stamp = now.strftime("%Y%m%d_%H%M%S")

    pdf.cell(200, 10, txt="Smart Network Diagnostic Report", ln=True, align='C')
    pdf.ln(10)

    # System info
    pdf.cell(200, 10, txt=f"Generated on: {timestamp}", ln=True)
    pdf.cell(200, 10, txt=f"System: {platform.system()} {platform.release()}", ln=True)
    pdf.cell(200, 10, txt=f"Hostname: {socket.gethostname()}", ln=True)
    pdf.cell(200, 10, txt=f"Local IP: {socket.gethostbyname(socket.gethostname())}", ln=True)
    pdf.ln(10)

    # Results
    pdf.cell(200, 10, txt="Results:", ln=True)
    pdf.cell(200, 10, txt=f"Internet: {'OK' if internet else 'FAIL'}", ln=True)
    pdf.cell(200, 10, txt=f"DNS: {'OK' if dns else 'FAIL'}", ln=True)
    pdf.cell(200, 10, txt=f"Download Speed: {download} Mbps", ln=True)
    pdf.cell(200, 10, txt=f"Upload Speed: {upload} Mbps", ln=True)
    pdf.cell(200, 10, txt=f"Ping: {ping} ms", ln=True)
    pdf.ln(10)

    # Summary
    pdf.cell(200, 10, txt="Diagnosis Summary:", ln=True)
    if internet and dns and download > 10:
        summary = "Your network appears to be working fine."
    elif not internet:
        summary = "No Internet detected. Please check router or contact ISP."
    elif download < 5:
        summary = "Slow Internet. Try switching networks or restarting router."
    else:
        summary = "Some issues detected with DNS or speed."
    pdf.multi_cell(0, 10, clean_text(summary))
    pdf.ln(5)

    # Suggestions
    if suggestions:
        pdf.cell(200, 10, txt="Suggestions:", ln=True)
        for s in suggestions:
            pdf.multi_cell(0, 10, f"- {clean_text(s)}")

    filename = f"network_report_{filename_stamp}.pdf"
    pdf.output(filename)

    return filename
