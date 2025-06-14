# from fpdf import FPDF

# def create_report(internet, dns, download, upload, suggestions):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     pdf.cell(200, 10, txt="Smart Network Diagnostic Report", ln=True, align='C')
#     pdf.cell(200, 10, txt="", ln=True)

#     pdf.cell(200, 10, txt=f"Internet Connection: {'OK' if internet else 'FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"DNS Resolution: {'OK' if dns else 'FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"Download Speed: {download} Mbps", ln=True)
#     pdf.cell(200, 10, txt=f"Upload Speed: {upload} Mbps", ln=True)

#     pdf.cell(200, 10, txt="Suggestions:", ln=True)
#     for suggestion in suggestions:
#         pdf.cell(200, 10, txt=f"- {suggestion}", ln=True)

#     pdf.output("network_report.pdf")

# report.py
# from fpdf import FPDF

# def create_report(internet, dns, download, upload, suggestions):
#     # Debugging line to check if the function is being called
#     print("Generating PDF report...")  # This will print to the terminal where you run Streamlit

#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     # Add diagnostic results to PDF
#     pdf.cell(200, 10, txt=f"Internet: {'✅ OK' if internet else '❌ FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"DNS: {'✅ OK' if dns else '❌ FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"Download Speed: {download} Mbps", ln=True)
#     pdf.cell(200, 10, txt=f"Upload Speed: {upload} Mbps", ln=True)

#     pdf.cell(200, 10, txt="Suggestions:", ln=True)
#     for suggestion in suggestions:
#         pdf.cell(200, 10, txt=f"- {suggestion}", ln=True)

#     # Save PDF to a file
#     pdf.output("network_report.pdf")

#     # Display message and link to download the report
#     print("PDF report saved!")  # Debugging line
#     # Streamlit will show success message in the app
#     return "network_report.pdf"
# from fpdf import FPDF
# import logging

# logging.basicConfig(level=logging.DEBUG)

# def create_report(internet, dns, download, upload, suggestions):
#     logging.debug("Creating PDF report...")

#     pdf = FPDF()
#     pdf.set_auto_page_break(auto=True, margin=15)
#     pdf.add_page()

#     pdf.set_font("Arial", size=12, style='B')
#     pdf.cell(200, 10, txt="Network Diagnostic Report", ln=True, align="C")

#     pdf.ln(10)
#     pdf.set_font("Arial", size=12)
#     pdf.cell(200, 10, txt=f"Internet Status: {'✅ OK' if internet else '❌ FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"DNS Status: {'✅ OK' if dns else '❌ FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"Download Speed: {download} Mbps", ln=True)
#     pdf.cell(200, 10, txt=f"Upload Speed: {upload} Mbps", ln=True)

#     pdf.ln(10)
#     pdf.set_font("Arial", size=10)
#     pdf.cell(200, 10, txt="Suggestions:", ln=True)
#     for suggestion in suggestions:
#         pdf.cell(200, 10, txt=f"- {suggestion}", ln=True)

#     pdf.output("network_report.pdf")
#     logging.debug("PDF saved successfully as network_report.pdf")
# ---------The PDF library (`fpdf`) doesn’t understand emojis like ✅ or ❌ because it only supports basic characters (Latin-1). So, when you tried to include an emoji, it crashed.-----------


# from fpdf import FPDF

# def clean_text(text):
#     # Remove emojis and leading/trailing spaces
#     return text.replace("✅", "").replace("❌", "").replace("⚠️", "").strip()

# def create_report(internet, dns, download, upload, suggestions):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     pdf.cell(200, 10, txt="Smart Network Diagnostic Report", ln=True, align='C')
#     pdf.ln(10)

#     pdf.cell(200, 10, txt="Results:", ln=True)
#     pdf.cell(200, 10, txt=f"Internet: {'OK' if internet else 'FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"DNS: {'OK' if dns else 'FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"Download Speed: {download} Mbps", ln=True)
#     pdf.cell(200, 10, txt=f"Upload Speed: {upload} Mbps", ln=True)

#     pdf.ln(10)
#     pdf.cell(200, 10, txt="Suggestions:", ln=True)
#     for s in suggestions:
#         cleaned = clean_text(s)
#         pdf.multi_cell(0, 10, f"- {cleaned}")

#     pdf.output("network_report.pdf")
#---IMPROVED PDF---#


# from fpdf import FPDF
# import platform
# import socket
# from datetime import datetime

# class PDF(FPDF):
#     def header(self):
#         self.set_font("Arial", "B", 16)
#         self.cell(0, 10, "📡 Network Diagnostic Report", ln=True, align="C")

#     def footer(self):
#         self.set_y(-15)
#         self.set_font("Arial", "I", 8)
#         self.cell(0, 10, f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", align="C")

# def create_report(internet, dns, download, upload, suggestions):
#     pdf = PDF()
#     pdf.add_page()

#     pdf.set_font("Arial", "", 12)

#     # Timestamp and system info
#     pdf.cell(0, 10, f"Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
#     pdf.cell(0, 10, f"System: {platform.system()} {platform.release()}", ln=True)
#     pdf.cell(0, 10, f"Hostname: {socket.gethostname()}", ln=True)
#     pdf.cell(0, 10, f"Local IP: {socket.gethostbyname(socket.gethostname())}", ln=True)

#     pdf.ln(10)

#     # Diagnostic results
#     pdf.set_font("Arial", "B", 12)
#     pdf.cell(0, 10, "Results:", ln=True)
#     pdf.set_font("Arial", "", 12)
#     pdf.cell(0, 10, f"Internet: {'OK' if internet else 'FAIL'}", ln=True)
#     pdf.cell(0, 10, f"DNS: {'OK' if dns else 'FAIL'}", ln=True)
#     pdf.cell(0, 10, f"Download Speed: {download} Mbps", ln=True)
#     pdf.cell(0, 10, f"Upload Speed: {upload} Mbps", ln=True)

#     pdf.ln(10)

#     # Diagnosis summary
#     summary = ""
#     if internet and dns and download > 10:
#         summary = "✅ Your network appears to be working fine."
#     elif not internet:
#         summary = "❌ No Internet detected. Please check router or contact ISP."
#     elif download < 5:
#         summary = "⚠️ Slow Internet detected. Try switching networks or restarting router."
#     else:
#         summary = "⚠️ Some issues detected with DNS or speed."

#     pdf.set_font("Arial", "B", 12)
#     pdf.cell(0, 10, "Diagnosis Summary:", ln=True)
#     pdf.set_font("Arial", "", 12)
#     pdf.multi_cell(0, 10, summary)

#     pdf.ln(5)

#     # Suggestions
#     if suggestions:
#         pdf.set_font("Arial", "B", 12)
#         pdf.cell(0, 10, "Suggestions:", ln=True)
#         pdf.set_font("Arial", "", 12)
#         for s in suggestions:
#             # Remove emojis to avoid Unicode errors
#             s_clean = s.replace("✅", "").replace("❌", "").replace("⚠️", "").strip()
#             pdf.multi_cell(0, 10, f"- {s_clean}")

#     pdf.output("network_report.pdf")

# from fpdf import FPDF

# def create_report(results):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     pdf.set_title("Network Diagnostic Report")
#     pdf.cell(200, 10, txt="Network Diagnostic Report", ln=True, align="C")

#     pdf.ln(10)
#     pdf.cell(200, 10, txt=f"Internet: {results['internet_status']}", ln=True)
#     pdf.cell(200, 10, txt=f"DNS: {results['dns_status']}", ln=True)
#     pdf.cell(200, 10, txt=f"Download Speed: {results['download_speed']} Mbps", ln=True)
#     pdf.cell(200, 10, txt=f"Upload Speed: {results['upload_speed']} Mbps", ln=True)

#     pdf.ln(10)
#     pdf.multi_cell(0, 10, txt=f"Suggestions:\n{results['suggestions']}")

#     return pdf.output(dest='S').encode('latin1', 'ignore')  # Fixes Unicode issues by ignoring unsupported chars



#---workable code---#
# from fpdf import FPDF

# def clean_text(text):
#     # Remove emojis and leading/trailing spaces
#     return text.replace("✅", "").replace("❌", "").replace("⚠️", "").strip()

# def create_report(internet, dns, download, upload, suggestions):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     pdf.cell(200, 10, txt="Smart Network Diagnostic Report", ln=True, align='C')
#     pdf.ln(10)

#     pdf.cell(200, 10, txt="Results:", ln=True)
#     pdf.cell(200, 10, txt=f"Internet: {'OK' if internet else 'FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"DNS: {'OK' if dns else 'FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"Download Speed: {download} Mbps", ln=True)
#     pdf.cell(200, 10, txt=f"Upload Speed: {upload} Mbps", ln=True)

#     pdf.ln(10)
#     pdf.cell(200, 10, txt="Suggestions:", ln=True)
#     for s in suggestions:
#         cleaned = clean_text(s)
#         pdf.multi_cell(0, 10, f"- {cleaned}")

#     pdf.output("network_report.pdf")


# from fpdf import FPDF
# from datetime import datetime
# import platform
# import socket

# def clean_text(text):
#     """
#     Clean text by removing emojis and stripping extra spaces.
#     """
#     return text.replace("✅", "").replace("❌", "").replace("⚠️", "").strip()

# def create_report(internet, dns, download, upload, ping, suggestions):
#     """
#     Generates a detailed network diagnostic report in PDF format.
#     """
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     # Title and Timestamp
#     pdf.cell(200, 10, txt="Smart Network Diagnostic Report", ln=True, align='C')
#     pdf.ln(10)
#     pdf.cell(200, 10, txt=f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
#     pdf.ln(10)

#     # System Information
#     pdf.cell(200, 10, txt=f"System: {platform.system()} {platform.release()}", ln=True)
#     pdf.cell(200, 10, txt=f"Hostname: {socket.gethostname()}", ln=True)
#     pdf.cell(200, 10, txt=f"Local IP: {socket.gethostbyname(socket.gethostname())}", ln=True)
#     pdf.ln(10)

#     # Results Section
#     pdf.cell(200, 10, txt="Results:", ln=True)
#     pdf.cell(200, 10, txt=f"Internet: {'OK' if internet else 'FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"DNS: {'OK' if dns else 'FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"Download Speed: {download} Mbps", ln=True)
#     pdf.cell(200, 10, txt=f"Upload Speed: {upload} Mbps", ln=True)
#     pdf.cell(200, 10, txt=f"Ping: {ping} ms", ln=True)  # Add Ping information
#     pdf.ln(10)

#     # Suggestions Section
#     pdf.cell(200, 10, txt="Suggestions:", ln=True)
#     for s in suggestions:
#         cleaned = clean_text(s)  # Clean the suggestion text
#         pdf.multi_cell(0, 10, f"- {cleaned}")

#     # Save the PDF to a file
#     pdf.output("network_report.pdf")



# ---ping included---
# from fpdf import FPDF

# def clean_text(text):
#     # Remove emojis and leading/trailing spaces
#     return text.replace("✅", "").replace("❌", "").replace("⚠️", "").strip()

# def create_report(internet, dns, download, upload, ping, suggestions):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     # Title
#     pdf.cell(200, 10, txt="Smart Network Diagnostic Report", ln=True, align='C')
#     pdf.ln(10)

#     # Results section
#     pdf.cell(200, 10, txt="Results:", ln=True)
#     pdf.cell(200, 10, txt=f"Internet: {'OK' if internet else 'FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"DNS: {'OK' if dns else 'FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"Download Speed: {download} Mbps", ln=True)
#     pdf.cell(200, 10, txt=f"Upload Speed: {upload} Mbps", ln=True)
#     pdf.cell(200, 10, txt=f"Ping: {ping} ms", ln=True)  # Display Ping

#     pdf.ln(10)

#     # Suggestions section
#     pdf.cell(200, 10, txt="Suggestions:", ln=True)
#     for s in suggestions:
#         cleaned = clean_text(s)
#         pdf.multi_cell(0, 10, f"- {cleaned}")

#     # Output the PDF to a file
#     pdf.output("network_report.pdf")


#---improved pdf---#
# from fpdf import FPDF
# import platform
# import socket
# from datetime import datetime

# def clean_text(text):
#     return text.replace("✅", "").replace("❌", "").replace("⚠️", "").strip()

# def create_report(internet, dns, download, upload, ping, suggestions):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", "B", 14)
#     pdf.cell(0, 10, "Smart Network Diagnostic Report", ln=True, align='C')
    
#     pdf.set_font("Arial", "", 12)
#     pdf.ln(5)
#     pdf.cell(0, 10, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
#     pdf.cell(0, 10, f"System: {platform.system()} {platform.release()}", ln=True)
#     pdf.cell(0, 10, f"Hostname: {socket.gethostname()}", ln=True)
#     pdf.cell(0, 10, f"Local IP: {socket.gethostbyname(socket.gethostname())}", ln=True)

#     pdf.ln(10)
#     pdf.set_font("Arial", "B", 12)
#     pdf.cell(0, 10, "Results:", ln=True)
#     pdf.set_font("Arial", "", 12)
#     pdf.cell(0, 10, f"Internet: {'OK' if internet else 'FAIL'}", ln=True)
#     pdf.cell(0, 10, f"DNS: {'OK' if dns else 'FAIL'}", ln=True)
#     pdf.cell(0, 10, f"Download Speed: {round(download, 2)} Mbps", ln=True)
#     pdf.cell(0, 10, f"Upload Speed: {round(upload, 2)} Mbps", ln=True)
#     pdf.cell(0, 10, f"Ping: {round(ping, 2)} ms", ln=True)

#     # Summary
#     pdf.ln(10)
#     pdf.set_font("Arial", "B", 12)
#     pdf.cell(0, 10, "Diagnosis Summary:", ln=True)
#     pdf.set_font("Arial", "", 12)

#     if internet and dns and download >= 10:
#         summary = "Your network appears to be working well."
#     elif not internet:
#         summary = "No Internet detected. Check router or ISP."
#     elif download < 5:
#         summary = "Slow Internet. Try switching networks or restarting router."
#     else:
#         summary = "Some issues detected with DNS or speed."

#     pdf.multi_cell(0, 10, summary)

#     # Suggestions
#     if suggestions:
#         pdf.ln(5)
#         pdf.set_font("Arial", "B", 12)
#         pdf.cell(0, 10, "Suggestions:", ln=True)
#         pdf.set_font("Arial", "", 12)
#         for s in suggestions:
#             pdf.multi_cell(0, 10, f"- {clean_text(s)}")

#      pdf.output("network_report.pdf")




#---improved diagnosis summary---#
# from fpdf import FPDF
# from datetime import datetime
# import platform
# import socket

# def clean_text(text):
#     return text.replace("✅", "").replace("❌", "").replace("⚠️", "").strip()

# def create_report(internet, dns, download, upload, ping, suggestions, filename="network_report.pdf"):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     # Header info
#     pdf.cell(200, 10, txt="Smart Network Diagnostic Report", ln=True, align='C')
#     pdf.ln(10)

#     # Timestamp and system info
#     pdf.cell(200, 10, txt=f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
#     pdf.cell(200, 10, txt=f"System: {platform.system()} {platform.release()}", ln=True)
#     pdf.cell(200, 10, txt=f"Hostname: {socket.gethostname()}", ln=True)
#     try:
#         local_ip = socket.gethostbyname(socket.gethostname())
#         pdf.cell(200, 10, txt=f"Local IP: {local_ip}", ln=True)
#     except:
#         pdf.cell(200, 10, txt="Local IP: Not available", ln=True)

#     # Diagnostic results
#     pdf.ln(10)
#     pdf.cell(200, 10, txt="Results:", ln=True)
#     pdf.cell(200, 10, txt=f"Internet: {'OK' if internet else 'FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"DNS: {'OK' if dns else 'FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"Download Speed: {download} Mbps", ln=True)
#     pdf.cell(200, 10, txt=f"Upload Speed: {upload} Mbps", ln=True)
#     pdf.cell(200, 10, txt=f"Ping: {ping} ms", ln=True)

#     # Diagnosis Summary (dynamic)
#     summary_lines = []

#     if not internet:
#         summary_lines.append("No Internet detected. Please check your router or contact your ISP.")
#     elif download < 5:
#         summary_lines.append("Slow Internet. Try switching networks or restarting the router.")
#     elif not dns:
#         summary_lines.append("DNS issues detected. Consider changing your DNS server (e.g., to Google DNS).")
#     else:
#         summary_lines.append("Your network appears to be working fine.")

#     # Combine into a single string for PDF
#     summary_text = "\n".join(summary_lines)

#     # Add Diagnosis Summary
#     pdf.ln(10)
#     pdf.cell(200, 10, txt="Diagnosis Summary:", ln=True)
#     pdf.multi_cell(0, 10, clean_text(summary_text))

#     # Suggestions
#     if suggestions:
#         pdf.ln(5)
#         pdf.cell(200, 10, txt="Suggestions:", ln=True)
#         for s in suggestions:
#             pdf.multi_cell(0, 10, f"- {clean_text(s)}")

#     # Save the report to the specified filename
#     pdf.output(filename)


# from fpdf import FPDF
# from datetime import datetime
# import platform
# import socket

# def clean_text(text):
#     return text.replace("✅", "").replace("❌", "").replace("⚠️", "").strip()

# def create_report(internet, dns, download, upload, ping, suggestions, filename="network_report.pdf"):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     # Header info
#     pdf.cell(200, 10, txt="Smart Network Diagnostic Report", ln=True, align='C')
#     pdf.ln(10)

#     # Timestamp and system info
#     pdf.cell(200, 10, txt=f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True)
#     pdf.cell(200, 10, txt=f"System: {platform.system()} {platform.release()}", ln=True)
#     pdf.cell(200, 10, txt=f"Hostname: {socket.gethostname()}", ln=True)
#     try:
#         local_ip = socket.gethostbyname(socket.gethostname())
#         pdf.cell(200, 10, txt=f"Local IP: {local_ip}", ln=True)
#     except:
#         pdf.cell(200, 10, txt="Local IP: Not available", ln=True)

#     # Diagnostic results
#     pdf.ln(10)
#     pdf.cell(200, 10, txt="Results:", ln=True)
#     pdf.cell(200, 10, txt=f"Internet: {'OK' if internet else 'FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"DNS: {'OK' if dns else 'FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"Download Speed: {download} Mbps", ln=True)
#     pdf.cell(200, 10, txt=f"Upload Speed: {upload} Mbps", ln=True)
#     pdf.cell(200, 10, txt=f"Ping: {ping} ms", ln=True)

#     # Diagnosis Summary (dynamic)
#     summary_lines = []

#     if not internet:
#         summary_lines.append("No Internet detected. Please check your router or contact your ISP.")
#     elif download < 5:
#         summary_lines.append("Slow Internet. Try switching networks or restarting the router.")
#     elif not dns:
#         summary_lines.append("DNS issues detected. Consider changing your DNS server (e.g., to Google DNS).")
#     else:
#         summary_lines.append("Your network appears to be working fine.")

#     # Combine into a single string for PDF
#     summary_text = "\n".join(summary_lines)

#     # Add Diagnosis Summary
#     pdf.ln(10)
#     pdf.cell(200, 10, txt="Diagnosis Summary:", ln=True)
#     pdf.multi_cell(0, 10, clean_text(summary_text))

#     # Suggestions
#     if suggestions:
#         pdf.ln(5)
#         pdf.cell(200, 10, txt="Suggestions:", ln=True)
#         for s in suggestions:
#             pdf.multi_cell(0, 10, f"- {clean_text(s)}")

#     # Save the report to the specified filename
#     pdf.output(filename)

#     # Return the filename to display it in the success message
#     return filename



#---FINAL WORKABLE---#
# from fpdf import FPDF
# from datetime import datetime
# import platform
# import socket

# def clean_text(text):
#     return text.replace("✅", "").replace("❌", "").replace("⚠️", "").strip()

# def create_report(internet, dns, download, upload, ping, suggestions):
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)

#     now = datetime.now()
#     timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
#     filename_stamp = now.strftime("%Y%m%d_%H%M%S")

#     pdf.cell(200, 10, txt="Smart Network Diagnostic Report", ln=True, align='C')
#     pdf.ln(10)

#     # System info
#     pdf.cell(200, 10, txt=f"Generated on: {timestamp}", ln=True)
#     pdf.cell(200, 10, txt=f"System: {platform.system()} {platform.release()}", ln=True)
#     pdf.cell(200, 10, txt=f"Hostname: {socket.gethostname()}", ln=True)
#     pdf.cell(200, 10, txt=f"Local IP: {socket.gethostbyname(socket.gethostname())}", ln=True)
#     pdf.ln(10)

#     # Results
#     pdf.cell(200, 10, txt="Results:", ln=True)
#     pdf.cell(200, 10, txt=f"Internet: {'OK' if internet else 'FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"DNS: {'OK' if dns else 'FAIL'}", ln=True)
#     pdf.cell(200, 10, txt=f"Download Speed: {download} Mbps", ln=True)
#     pdf.cell(200, 10, txt=f"Upload Speed: {upload} Mbps", ln=True)
#     pdf.cell(200, 10, txt=f"Ping: {ping} ms", ln=True)
#     pdf.ln(10)

#     # Summary
#     pdf.cell(200, 10, txt="Diagnosis Summary:", ln=True)
#     if internet and dns and download > 10:
#         summary = "Your network appears to be working fine."
#     elif not internet:
#         summary = "No Internet detected. Please check router or contact ISP."
#     elif download < 5:
#         summary = "Slow Internet. Try switching networks or restarting router."
#     else:
#         summary = "Some issues detected with DNS or speed."
#     pdf.multi_cell(0, 10, summary)
#     pdf.ln(5)

#     # Suggestions
#     if suggestions:
#         pdf.cell(200, 10, txt="Suggestions:", ln=True)
#         for s in suggestions:
#             pdf.multi_cell(0, 10, f"- {clean_text(s)}")

#     # Unique filename per report
#     filename = f"network_report_{filename_stamp}.pdf"
#     pdf.output(filename)

#     return filename  # useful if you want to show or log the file path

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
