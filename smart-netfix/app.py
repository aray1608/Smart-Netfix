# import streamlit as st
# from connectivity import check_internet
# from dns_test import check_dns
# from speed_test import run_speedtest
# from suggestions import get_suggestions
# from report import create_report

# st.set_page_config(page_title="Smart Network Diagnostic Assistant")
# st.title("📡 Smart Network Diagnostic Assistant")

# if st.button("Run Diagnostics"):
#     internet = check_internet()
#     dns = check_dns()
#     download, upload = run_speedtest()
#     suggestions = get_suggestions(internet, dns, download)

#     st.subheader("Results:")
#     st.write(f"Internet: {'✅ OK' if internet else '❌ FAIL'}")
#     st.write(f"DNS: {'✅ OK' if dns else '❌ FAIL'}")
#     st.write(f"Download Speed: {download} Mbps")
#     st.write(f"Upload Speed: {upload} Mbps")

#     st.subheader("Suggestions:")
#     for s in suggestions:
#         st.write(f"- {s}")

#     if st.button("Generate PDF Report"):
#         create_report(internet, dns, download, upload, suggestions)
#         st.success("PDF report saved as `network_report.pdf`")


# /* since pdf wasnt generating */

# import streamlit as st
# from connectivity import check_internet
# from dns_test import check_dns
# from speed_test import run_speedtest
# from suggestions import get_suggestions
# from report import create_report

# st.set_page_config(page_title="Smart Network Diagnostic Assistant")
# st.title("📡 Smart Network Diagnostic Assistant")

# # Use session state to track diagnostics
# if "diagnostics_run" not in st.session_state:
#     st.session_state.diagnostics_run = False

# if st.button("Run Diagnostics"):
#     internet = check_internet()
#     dns = check_dns()
#     download, upload = run_speedtest()
#     suggestions = get_suggestions(internet, dns, download)

#     st.session_state.diagnostics_run = True
#     st.session_state.internet = internet
#     st.session_state.dns = dns
#     st.session_state.download = download
#     st.session_state.upload = upload
#     st.session_state.suggestions = suggestions

# if st.session_state.diagnostics_run:
#     st.subheader("Results:")
#     st.write(f"Internet: {'✅ OK' if st.session_state.internet else '❌ FAIL'}")
#     st.write(f"DNS: {'✅ OK' if st.session_state.dns else '❌ FAIL'}")
#     st.write(f"Download Speed: {st.session_state.download} Mbps")
#     st.write(f"Upload Speed: {st.session_state.upload} Mbps")

#     st.subheader("Suggestions:")
#     for s in st.session_state.suggestions:
#         st.write(f"- {s}")

#     if st.button("Generate PDF Report"):
#         create_report(
#             st.session_state.internet,
#             st.session_state.dns,
#             st.session_state.download,
#             st.session_state.upload,
#             st.session_state.suggestions,
#         )
#         st.success("PDF report saved as `network_report.pdf`")

#     with open("network_report.pdf", "rb") as file:
#         btn = st.download_button(
#             label="📄 Download Report",
#             data=file,
#             file_name="network_report.pdf",
#             mime="application/pdf"
#         )

#----NOW WE TRY TO MAKE THE DIAGNOSIS PROCESS FASTER. EARLIER (check_internet, check_dns, run_speedtest) 
# were executing one by one but now we run them parallely using
# multi-threading with concurrent.futures.ThreadPoolExecutor to run all diagnostics at the same time instead of one after another.-----#

# import streamlit as st
# from concurrent.futures import ThreadPoolExecutor
# from connectivity import check_internet
# from dns_test import check_dns
# from speed_test import run_speedtest
# from suggestions import get_suggestions

# # Run diagnostics in parallel
# def run_diagnostics():
#     with ThreadPoolExecutor() as executor:
#         future_internet = executor.submit(check_internet)
#         future_dns = executor.submit(check_dns)
#         future_speed = executor.submit(run_speedtest)
        
#         internet = future_internet.result()
#         dns = future_dns.result()
#         download, upload = future_speed.result()
        
#         suggestions = get_suggestions(internet, dns, download)
        
#         return internet, dns, download, upload, suggestions

# st.set_page_config(page_title="Smart Network Diagnostic Assistant")
# st.title("📡 Smart Network Diagnostic Assistant")

# if st.button("Run Diagnostics"):
#     internet, dns, download, upload, suggestions = run_diagnostics()

#     st.subheader("Results:")
#     st.write(f"Internet: {'✅ OK' if internet else '❌ FAIL'}")
#     st.write(f"DNS: {'✅ OK' if dns else '❌ FAIL'}")
#     st.write(f"Download Speed: {download} Mbps")
#     st.write(f"Upload Speed: {upload} Mbps")

#     st.subheader("Suggestions:")
#     for s in suggestions:
#         st.write(f"- {s}")
#---after improving pdf content, the generate button wasnt showing---#

# import streamlit as st
# from connectivity import check_internet
# from dns_test import check_dns
# from speed_test import run_speedtest
# from suggestions import get_suggestions
# from report import create_report

# st.set_page_config(page_title="Smart Network Diagnostic Assistant")
# st.title("📡 Smart Network Diagnostic Assistant")

# # Run diagnostics
# if st.button("Run Diagnostics"):
#     st.session_state.internet = check_internet()
#     st.session_state.dns = check_dns()
#     st.session_state.download, st.session_state.upload = run_speedtest()
#     st.session_state.suggestions = get_suggestions(
#         st.session_state.internet,
#         st.session_state.dns,
#         st.session_state.download,
#     )

# # Display results if available
# if "internet" in st.session_state:
#     st.subheader("Results:")
#     st.write(f"Internet: {'✅ OK' if st.session_state.internet else '❌ FAIL'}")
#     st.write(f"DNS: {'✅ OK' if st.session_state.dns else '❌ FAIL'}")
#     st.write(f"Download Speed: {st.session_state.download} Mbps")
#     st.write(f"Upload Speed: {st.session_state.upload} Mbps")

#     st.subheader("Suggestions:")
#     for s in st.session_state.suggestions:
#         st.write(f"- {s}")

#     if st.button("Generate PDF Report"):
#         create_report(
#             st.session_state.internet,
#             st.session_state.dns,
#             st.session_state.download,
#             st.session_state.upload,
#             st.session_state.suggestions,
#         )
#         st.success("✅ PDF report saved as `network_report.pdf`")
#---UNICODE ERROR + automatic pdf download change---#

# import streamlit as st
# from connectivity import check_internet
# from dns_test import check_dns
# from speed_test import run_speedtest
# from suggestions import get_suggestions
# from report import create_report

# st.set_page_config(page_title="Smart Network Diagnostic Assistant")
# st.title("📡 Smart Network Diagnostic Assistant")

# # Run Diagnostics button
# if st.button("Run Diagnostics"):
#     internet = check_internet()
#     dns = check_dns()
#     download, upload = run_speedtest()
#     suggestions = get_suggestions(internet, dns, download)

#     st.subheader("Results:")
#     st.write(f"Internet: {'✅ OK' if internet else '❌ FAIL'}")
#     st.write(f"DNS: {'✅ OK' if dns else '❌ FAIL'}")
#     st.write(f"Download Speed: {download} Mbps")
#     st.write(f"Upload Speed: {upload} Mbps")

#     st.subheader("Suggestions:")
#     for s in suggestions:
#         st.write(f"- {s}")

#     # Generate PDF report and allow download directly
#     if st.button("Generate PDF Report"):
#         pdf_content = create_report(internet, dns, download, upload, suggestions)
        
#         # Provide the download button for the generated PDF
#         st.download_button(
#             label="Download PDF Report",
#             data=pdf_content,
#             file_name="network_report.pdf",
#             mime="application/pdf"
#         )


# import streamlit as st
# from connectivity import check_internet
# from dns_test import check_dns
# from speed_test import run_speedtest
# from suggestions import get_suggestions
# from report import create_report

# # Streamlit page configuration
# st.set_page_config(page_title="Smart Network Diagnostic Assistant")
# st.title("📡 Smart Network Diagnostic Assistant")

# # Initialize session state for diagnostics results
# if "diagnostics_done" not in st.session_state:
#     st.session_state.diagnostics_done = False

# # Run diagnostics when the button is clicked
# if st.button("Run Diagnostics"):
#     internet = check_internet()
#     dns = check_dns()
#     download, upload = run_speedtest()
#     suggestions = get_suggestions(internet, dns, download)

#     # Save the results in session state
#     st.session_state.diagnostics_done = True
#     st.session_state.internet = internet
#     st.session_state.dns = dns
#     st.session_state.download = download
#     st.session_state.upload = upload
#     st.session_state.suggestions = suggestions

#     # Display the results
#     st.subheader("Results:")
#     st.write(f"Internet: {'✅ OK' if internet else '❌ FAIL'}")
#     st.write(f"DNS: {'✅ OK' if dns else '❌ FAIL'}")
#     st.write(f"Download Speed: {download} Mbps")
#     st.write(f"Upload Speed: {upload} Mbps")

#     st.subheader("Suggestions:")
#     for s in suggestions:
#         st.write(f"- {s}")

# # If diagnostics are done, show the "Generate PDF Report" button
# if st.session_state.diagnostics_done:
#     if st.button("Generate PDF Report"):
#         # Generate the report
#         pdf_content = create_report(
#             st.session_state.internet,
#             st.session_state.dns,
#             st.session_state.download,
#             st.session_state.upload,
#             st.session_state.suggestions
#         )
        
#         # Allow the user to download the PDF
#         st.download_button("Download PDF", data=pdf_content, file_name="network_report.pdf", mime="application/pdf")
#         st.success("PDF generated! Click the button to download.")

#---workable code---#

# import streamlit as st
# from connectivity import check_internet
# from dns_test import check_dns
# from speed_test import run_speedtest
# from suggestions import get_suggestions
# from report import create_report

# st.set_page_config(page_title="Smart Network Diagnostic Assistant")
# st.title("📡 Smart Network Diagnostic Assistant")

# # Run diagnostics
# if st.button("Run Diagnostics"):
#     st.session_state.internet = check_internet()
#     st.session_state.dns = check_dns()
#     st.session_state.download, st.session_state.upload = run_speedtest()
#     st.session_state.suggestions = get_suggestions(
#         st.session_state.internet,
#         st.session_state.dns,
#         st.session_state.download,
#     )

# # Display results if available
# if "internet" in st.session_state:
#     st.subheader("Results:")
#     st.write(f"Internet: {'✅ OK' if st.session_state.internet else '❌ FAIL'}")
#     st.write(f"DNS: {'✅ OK' if st.session_state.dns else '❌ FAIL'}")
#     st.write(f"Download Speed: {st.session_state.download} Mbps")
#     st.write(f"Upload Speed: {st.session_state.upload} Mbps")

#     st.subheader("Suggestions:")
#     for s in st.session_state.suggestions:
#         st.write(f"- {s}")

#     if st.button("Generate PDF Report"):
#         create_report(
#             st.session_state.internet,
#             st.session_state.dns,
#             st.session_state.download,
#             st.session_state.upload,
#             st.session_state.suggestions,
#         )
#         st.success("✅ PDF report saved as `network_report.pdf`")

# import streamlit as st
# from connectivity import check_internet
# from dns_test import check_dns
# from speed_test import run_speedtest
# from suggestions import get_suggestions
# from report import create_report

# st.set_page_config(page_title="Smart Network Diagnostic Assistant")
# st.title("📡 Smart Network Diagnostic Assistant")

# # Run diagnostics when the button is clicked
# if st.button("Run Diagnostics"):
#     # Store the results in session_state to keep the values persistent across interactions
#     st.session_state.internet = check_internet()
#     st.session_state.dns = check_dns()
#     st.session_state.download, st.session_state.upload, st.session_state.ping = run_speedtest()  # Assuming ping is also returned
#     st.session_state.suggestions = get_suggestions(
#         st.session_state.internet,
#         st.session_state.dns,
#         st.session_state.download,
#     )

# # Display the diagnostic results if available
# if "internet" in st.session_state:
#     st.subheader("Results:")
#     st.write(f"Internet: {'✅ OK' if st.session_state.internet else '❌ FAIL'}")
#     st.write(f"DNS: {'✅ OK' if st.session_state.dns else '❌ FAIL'}")
#     st.write(f"Download Speed: {st.session_state.download} Mbps")
#     st.write(f"Upload Speed: {st.session_state.upload} Mbps")
#     st.write(f"Ping: {st.session_state.ping} ms")  # Display ping

#     st.subheader("Suggestions:")
#     for s in st.session_state.suggestions:
#         st.write(f"- {s}")

#     # Generate PDF report when the button is clicked
#     if st.button("Generate PDF Report"):
#         # Call the function to create the PDF and pass the necessary information
#         create_report(
#             st.session_state.internet,
#             st.session_state.dns,
#             st.session_state.download,
#             st.session_state.upload,
#             st.session_state.ping,
#             st.session_state.suggestions,
#         )
#         st.success("✅ PDF report saved as `network_report.pdf`")


#---improved diagnosis---#
# import streamlit as st
# from connectivity import check_internet
# from dns_test import check_dns
# from speed_test import run_speedtest
# from suggestions import get_suggestions
# from report import create_report

# st.set_page_config(page_title="Smart Network Diagnostic Assistant")
# st.title("📡 Smart Network Diagnostic Assistant")

# # Run diagnostics
# if st.button("Run Diagnostics"):
#     st.session_state.internet = check_internet()
#     st.session_state.dns = check_dns()
#     st.session_state.download, st.session_state.upload, st.session_state.ping = run_speedtest()
#     st.session_state.suggestions = get_suggestions(
#         st.session_state.internet,
#         st.session_state.dns,
#         st.session_state.download,
#     )

# # Display results if available
# if "internet" in st.session_state:
#     st.subheader("Results:")
#     st.write(f"Internet: {'✅ OK' if st.session_state.internet else '❌ FAIL'}")
#     st.write(f"DNS: {'✅ OK' if st.session_state.dns else '❌ FAIL'}")
#     st.write(f"Download Speed: {st.session_state.download} Mbps")
#     st.write(f"Upload Speed: {st.session_state.upload} Mbps")
#     st.write(f"Ping: {st.session_state.ping} ms")

#     st.subheader("Suggestions:")
#     for s in st.session_state.suggestions:
#         st.write(f"- {s}")

#     if st.button("Generate PDF Report"):
#     # Call the function to create the PDF and pass the necessary information
#         filename = create_report(
#             st.session_state.internet,
#             st.session_state.dns,
#             st.session_state.download,
#             st.session_state.upload,
#             st.session_state.ping,
#             st.session_state.suggestions,
#         )
#         st.success(f"✅ PDF report saved as `{filename}`")

#---ping included---#
# import streamlit as st
# from services.connectivity import check_internet
# from services.dns_test import check_dns
# from services.speed_test import run_speedtest
# from services.suggestions import get_suggestions
# from report import create_report

# st.set_page_config(page_title="Smart Network Diagnostic Assistant")
# st.title("📡 Smart Network Diagnostic Assistant")

# # Run diagnostics when the button is clicked
# if st.button("Run Diagnostics"):
#     # Store the results in session_state to keep the values persistent across interactions
#     st.session_state.internet = check_internet()
#     st.session_state.dns = check_dns()
#     st.session_state.download, st.session_state.upload, st.session_state.ping = run_speedtest()  # Now correctly handles 3 values
#     st.session_state.suggestions = get_suggestions(
#         st.session_state.internet,
#         st.session_state.dns,
#         st.session_state.download,
#     )

# # Display the diagnostic results if available
# if "internet" in st.session_state:
#     st.subheader("Results:")
#     st.write(f"Internet: {'✅ OK' if st.session_state.internet else '❌ FAIL'}")
#     st.write(f"DNS: {'✅ OK' if st.session_state.dns else '❌ FAIL'}")
#     st.write(f"Download Speed: {st.session_state.download} Mbps")
#     st.write(f"Upload Speed: {st.session_state.upload} Mbps")
#     st.write(f"Ping: {st.session_state.ping} ms")  # Display ping

#     st.subheader("Suggestions:")
#     for s in st.session_state.suggestions:
#         st.write(f"- {s}")

#     # Generate PDF report when the button is clicked
#     if st.button("Generate PDF Report"):
#         # Call the function to create the PDF and pass the necessary information
#         filename = create_report(
#             st.session_state.internet,
#             st.session_state.dns,
#             st.session_state.download,
#             st.session_state.upload,
#             st.session_state.ping,
#             st.session_state.suggestions,
#         )
#         st.success(f"✅ PDF report saved as `{filename}`")

# import streamlit as st
# import requests
# from report import create_report  # Make sure report.py has this function

# st.set_page_config(page_title="Smart Network Diagnostic Assistant")
# st.title("📡 Smart Network Diagnostic Assistant")

# API_URL = "http://localhost:8000/api/v1/diagnostics/run"

# if st.button("Run Diagnostics"):
#     with st.spinner("Running diagnostics..."):
#         response = requests.post(API_URL, json={"test_type": "full"})
#         if response.status_code == 200:
#             result = response.json()["results"]
#             st.session_state.internet = result["internet"]
#             st.session_state.dns = result["dns"]
#             st.session_state.download = result["download"]
#             st.session_state.upload = result["upload"]
#             st.session_state.ping = result["ping"]
#             st.session_state.suggestions = result["suggestions"]
#         else:
#             st.error("❌ Diagnostics failed!")

# if "internet" in st.session_state:
#     st.subheader("Results:")
#     st.write(f"Internet: {'✅ OK' if st.session_state.internet else '❌ FAIL'}")
#     st.write(f"DNS: {'✅ OK' if st.session_state.dns else '❌ FAIL'}")
#     st.write(f"Download Speed: {st.session_state.download} Mbps")
#     st.write(f"Upload Speed: {st.session_state.upload} Mbps")
#     st.write(f"Ping: {st.session_state.ping} ms")

#     st.subheader("Suggestions:")
#     for s in st.session_state.suggestions:
#         st.write(f"- {s}")

#     if st.button("Generate PDF Report"):
#         filename = create_report(
#             st.session_state.internet,
#             st.session_state.dns,
#             st.session_state.download,
#             st.session_state.upload,
#             st.session_state.ping,
#             st.session_state.suggestions,
#         )
#         st.success(f"✅ PDF report saved as `{filename}`")

# import streamlit as st
# import requests
# from datetime import datetime
# from report import create_report

# st.set_page_config(page_title="Smart Network Diagnostic Assistant", layout="centered")
# st.title("📡 Smart Network Diagnostic Assistant")

# API_URL = "http://localhost:8000/api/v1/diagnostics/run"

# if st.button("Run Diagnostics"):
#     with st.spinner("Running diagnostics..."):
#         response = requests.post(API_URL, json={"test_type": "full"})
#         if response.status_code == 200:
#             result = response.json()["results"]
#             st.session_state.internet = result["internet"]
#             st.session_state.dns = result["dns"]
#             st.session_state.download = result["download"]
#             st.session_state.upload = result["upload"]
#             st.session_state.ping = result["ping"]
#             st.session_state.suggestions = result["suggestions"]
#             st.session_state.last_run = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         else:
#             st.error("❌ Diagnostics failed!")

# if "internet" in st.session_state:
#     st.success("✅ Diagnostics completed successfully.")
    
#     st.subheader("📊 Diagnostic Results")

#     st.markdown("### 🌐 Internet Connectivity")
#     if st.session_state.internet:
#         st.success("✅ Connected")
#     else:
#         st.error("❌ Not Connected")

#     st.markdown("### 🧭 DNS Resolution")
#     if st.session_state.dns:
#         st.success("✅ Working")
#     else:
#         st.error("❌ Failed")

#     st.markdown(f"### ⬇️ Download Speed\n\n**{st.session_state.download} Mbps**")
#     st.markdown(f"### ⬆️ Upload Speed\n\n**{st.session_state.upload} Mbps**")
#     st.markdown(f"### 📶 Ping\n\n**{st.session_state.ping} ms**")

#     st.markdown("### 🧠 Suggestions")
#     for s in st.session_state.suggestions:
#         st.success(s)

#     st.markdown(f"🕒 **Last Run:** {st.session_state.last_run}")

#     if st.button("📄 Generate PDF Report"):
#         filename = create_report(
#             st.session_state.internet,
#             st.session_state.dns,
#             st.session_state.download,
#             st.session_state.upload,
#             st.session_state.ping,
#             st.session_state.suggestions,
#         )
#         st.success(f"✅ PDF report saved as `{filename}`")

# import streamlit as st
# import requests
# from datetime import datetime
# from report import create_report

# st.set_page_config(page_title="Smart Network Diagnostic Assistant", layout="wide")
# st.title("📡 Smart Network Diagnostic Assistant")

# API_URL = "http://localhost:8000/api/v1/diagnostics/run"

# if st.button("▶️ Run Diagnostics"):
#     with st.spinner("Running diagnostics..."):
#         response = requests.post(API_URL, json={"test_type": "full"})
#         if response.status_code == 200:
#             result = response.json()["results"]
#             st.session_state.internet = result["internet"]
#             st.session_state.dns = result["dns"]
#             st.session_state.download = result["download"]
#             st.session_state.upload = result["upload"]
#             st.session_state.ping = result["ping"]
#             st.session_state.suggestions = result["suggestions"]
#             st.session_state.last_run = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         else:
#             st.error("❌ Diagnostics failed!")

# if "internet" in st.session_state:
#     st.success("✅ Diagnostics completed successfully.")
#     st.subheader("📊 Diagnostic Dashboard")

#     # 1. Top status row
#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown("### 🌐 Internet")
#         st.success("✅ Connected" if st.session_state.internet else "❌ Not Connected")
#     with col2:
#         st.markdown("### 🧭 DNS")
#         st.success("✅ Working" if st.session_state.dns else "❌ Failed")

#     # 2. Speed and ping row
#     col3, col4, col5 = st.columns(3)
#     with col3:
#         st.markdown("### ⬇️ Download")
#         st.metric(label="Speed", value=f"{st.session_state.download} Mbps")
#     with col4:
#         st.markdown("### ⬆️ Upload")
#         st.metric(label="Speed", value=f"{st.session_state.upload} Mbps")
#     with col5:
#         st.markdown("### 📶 Ping")
#         st.metric(label="Latency", value=f"{st.session_state.ping} ms")

#     # 3. Suggestions
#     st.markdown("### 🧠 Suggestions")
#     for s in st.session_state.suggestions:
#         st.success(s)

#     # 4. Footer
#     st.markdown(f"🕒 **Last Run:** {st.session_state.last_run}")

#     # 5. PDF Button
#     if st.button("📄 Generate PDF Report"):
#         filename = create_report(
#             st.session_state.internet,
#             st.session_state.dns,
#             st.session_state.download,
#             st.session_state.upload,
#             st.session_state.ping,
#             st.session_state.suggestions,
#         )
#         st.success(f"✅ PDF report saved as `{filename}`")


# import streamlit as st
# import requests
# from datetime import datetime
# from report import create_report

# st.set_page_config(page_title="Smart Network Diagnostic Assistant", layout="wide")
# st.title("📡 Smart Network Diagnostic Assistant")

# API_URL = "http://localhost:8000/api/v1/diagnostics/run"

# if st.button("▶️ Run Diagnostics"):
#     with st.spinner("Running diagnostics..."):
#         response = requests.post(API_URL, json={"test_type": "full"})
#         if response.status_code == 200:
#             result = response.json()["results"]
#             st.session_state.internet = result["internet"]
#             st.session_state.dns = result["dns"]
#             st.session_state.download = result["download"]
#             st.session_state.upload = result["upload"]
#             st.session_state.ping = result["ping"]
#             st.session_state.suggestions = result["suggestions"]
#             st.session_state.last_run = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         else:
#             st.error("❌ Diagnostics failed!")

# if "internet" in st.session_state:
#     st.success("✅ Diagnostics completed successfully.")
#     st.subheader("📊 Diagnostic Dashboard")

#     # 1. Connectivity Status
#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown("### 🌐 Internet")
#         st.success("✅ Connected" if st.session_state.internet else "❌ Not Connected")
#     with col2:
#         st.markdown("### 🧭 DNS")
#         st.success("✅ Working" if st.session_state.dns else "❌ Failed")

#     # 2. Speed & Ping
#     col3, col4, col5 = st.columns(3)
#     with col3:
#         st.markdown("### ⬇️ Download")
#         st.metric(label="Speed", value=f"{st.session_state.download} Mbps")
#     with col4:
#         st.markdown("### ⬆️ Upload")
#         st.metric(label="Speed", value=f"{st.session_state.upload} Mbps")
#     with col5:
#         st.markdown("### 📶 Ping")
#         st.metric(label="Latency", value=f"{st.session_state.ping} ms")

#     # 3. Suggestions
#     st.markdown("### 🧠 Suggestions")
#     for s in st.session_state.suggestions:
#         st.success(s)

#     # 4. Last Run
#     st.markdown(f"🕒 **Last Run:** {st.session_state.last_run}")

#     # 5. PDF Report Button
#     if st.button("📄 Generate PDF Report"):
#         filename = create_report(
#             st.session_state.internet,
#             st.session_state.dns,
#             st.session_state.download,
#             st.session_state.upload,
#             st.session_state.ping,
#             st.session_state.suggestions,
#         )
#         st.success(f"✅ PDF report saved as `{filename}`")






# import streamlit as st
# import requests
# from datetime import datetime
# from report import create_report

# st.set_page_config(page_title="Smart Network Diagnostic Assistant", layout="wide")
# st.title("📡 Smart Network Diagnostic Assistant")

# API_URL = "http://localhost:8000/api/v1/diagnostics/run"
# HISTORY_URL = "http://localhost:8000/api/v1/diagnostics/history"

# # --- Run Diagnostics ---
# if st.button("▶️ Run Diagnostics"):
#     with st.spinner("Running diagnostics..."):
#         response = requests.post(API_URL, json={"test_type": "full"})
#         if response.status_code == 200:
#             result = response.json()["results"]
#             st.session_state.internet = result["internet"]
#             st.session_state.dns = result["dns"]
#             st.session_state.download = result["download"]
#             st.session_state.upload = result["upload"]
#             st.session_state.ping = result["ping"]
#             st.session_state.suggestions = result["suggestions"]
#             st.session_state.last_run = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         else:
#             st.error("❌ Diagnostics failed!")

# # --- Results Display ---
# if "internet" in st.session_state:
#     st.success("✅ Diagnostics completed successfully.")
#     st.subheader("📊 Diagnostic Dashboard")

#     # 1. Connectivity Status
#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown("### 🌐 Internet")
#         st.success("✅ Connected" if st.session_state.internet else "❌ Not Connected")
#     with col2:
#         st.markdown("### 🧭 DNS")
#         st.success("✅ Working" if st.session_state.dns else "❌ Failed")

#     # 2. Speed & Ping
#     col3, col4, col5 = st.columns(3)
#     with col3:
#         st.markdown("### ⬇️ Download")
#         st.metric(label="Speed", value=f"{st.session_state.download} Mbps")
#     with col4:
#         st.markdown("### ⬆️ Upload")
#         st.metric(label="Speed", value=f"{st.session_state.upload} Mbps")
#     with col5:
#         st.markdown("### 📶 Ping")
#         st.metric(label="Latency", value=f"{st.session_state.ping} ms")

#     # 3. Suggestions
#     st.markdown("### 🧠 Suggestions")
#     for s in st.session_state.suggestions:
#         st.success(s)

#     # 4. Last Run
#     st.markdown(f"🕒 **Last Run:** {st.session_state.last_run}")

#     # 5. PDF Report Button
#     if st.button("📄 Generate PDF Report"):
#         filename = create_report(
#             st.session_state.internet,
#             st.session_state.dns,
#             st.session_state.download,
#             st.session_state.upload,
#             st.session_state.ping,
#             st.session_state.suggestions,
#         )
#         st.success(f"✅ PDF report saved as `{filename}`")

# # --- Diagnostics History ---
# st.subheader("📂 Previous Diagnostic Runs (Latest 5)")

# try:
#     history_response = requests.get(HISTORY_URL, params={"limit": 5})
#     if history_response.status_code == 200:
#         history = history_response.json()["history"]
#         for entry in history:
#             with st.expander(f"🕒 {entry['timestamp']}"):
#                 st.markdown(f"**🌐 Internet:** {'✅ Connected' if entry['internet'] else '❌ Not Connected'}")
#                 st.markdown(f"**🧭 DNS:** {'✅ Working' if entry['dns'] else '❌ Failed'}")
#                 st.markdown(f"**⬇️ Download:** {entry['download']} Mbps")
#                 st.markdown(f"**⬆️ Upload:** {entry['upload']} Mbps")
#                 st.markdown(f"**📶 Ping:** {entry['ping']} ms")
#                 st.markdown("**🧠 Suggestions:**")
#                 for s in entry["suggestions"]:
#                     st.markdown(f"- {s}")
#     else:
#         st.warning("⚠️ Could not load history.")
# except Exception as e:
#     st.error(f"❌ Error fetching history: {e}")








# import streamlit as st
# import requests
# from datetime import datetime
# from report import create_report
# import pytz
# from tzlocal import get_localzone

# st.set_page_config(page_title="Smart Network Diagnostic Assistant", layout="wide")
# st.title("📡 Smart Network Diagnostic Assistant")

# API_URL = "http://localhost:8000/api/v1/diagnostics/run"
# HISTORY_URL = "http://localhost:8000/api/v1/diagnostics/history"

# # --- Run Diagnostics ---
# if st.button("▶️ Run Diagnostics"):
#     with st.spinner("Running diagnostics..."):
#         response = requests.post(API_URL, json={"test_type": "full"})
#         if response.status_code == 200:
#             result = response.json()["results"]
#             st.session_state.internet = result["internet"]
#             st.session_state.dns = result["dns"]
#             st.session_state.download = result["download"]
#             st.session_state.upload = result["upload"]
#             st.session_state.ping = result["ping"]
#             st.session_state.suggestions = result["suggestions"]
#             st.session_state.last_run = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         else:
#             st.error("❌ Diagnostics failed!")

# # --- Results Display ---
# if "internet" in st.session_state:
#     st.success("✅ Diagnostics completed successfully.")
#     st.subheader("📊 Diagnostic Dashboard")

#     # 1. Connectivity Status
#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown("### 🌐 Internet")
#         st.success("✅ Connected" if st.session_state.internet else "❌ Not Connected")
#     with col2:
#         st.markdown("### 🧭 DNS")
#         st.success("✅ Working" if st.session_state.dns else "❌ Failed")

#     # 2. Speed & Ping
#     col3, col4, col5 = st.columns(3)
#     with col3:
#         st.markdown("### ⬇️ Download")
#         st.metric(label="Speed", value=f"{st.session_state.download} Mbps")
#     with col4:
#         st.markdown("### ⬆️ Upload")
#         st.metric(label="Speed", value=f"{st.session_state.upload} Mbps")
#     with col5:
#         st.markdown("### 📶 Ping")
#         st.metric(label="Latency", value=f"{st.session_state.ping} ms")

#     # 3. Suggestions
#     st.markdown("### 🧠 Suggestions")
#     for s in st.session_state.suggestions:
#         st.success(s)

#     # 4. Last Run
#     st.markdown(f"🕒 **Last Run:** {st.session_state.last_run}")

#     # 5. PDF Report Button
#     if st.button("📄 Generate PDF Report"):
#         filename = create_report(
#             st.session_state.internet,
#             st.session_state.dns,
#             st.session_state.download,
#             st.session_state.upload,
#             st.session_state.ping,
#             st.session_state.suggestions,
#         )
#         st.success(f"✅ PDF report saved as `{filename}`")

# # --- Diagnostics History ---
# st.subheader("📂 Previous Diagnostic Runs (Latest 5)")

# try:
#     history_response = requests.get(HISTORY_URL, params={"limit": 5})
#     if history_response.status_code == 200:
#         history = history_response.json()["history"]

#         from_zone = pytz.utc
#         to_zone = get_localzone()

#         for entry in history:
#             # Convert UTC string timestamp to local time
#             utc_time = datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=from_zone)
#             local_time = utc_time.astimezone(to_zone)
#             formatted_time = local_time.strftime("%Y-%m-%d %I:%M %p (%Z)")

#             with st.expander(f"🕒 {formatted_time}"):
#                 st.markdown(f"**🌐 Internet:** {'✅ Connected' if entry['internet'] else '❌ Not Connected'}")
#                 st.markdown(f"**🧭 DNS:** {'✅ Working' if entry['dns'] else '❌ Failed'}")
#                 st.markdown(f"**⬇️ Download:** {entry['download']} Mbps")
#                 st.markdown(f"**⬆️ Upload:** {entry['upload']} Mbps")
#                 st.markdown(f"**📶 Ping:** {entry['ping']} ms")
#                 st.markdown("**🧠 Suggestions:**")
#                 for s in entry["suggestions"]:
#                     st.markdown(f"- {s}")
#     else:
#         st.warning("⚠️ Could not load history.")
# except Exception as e:
#     st.error(f"❌ Error fetching history: {e}")


    #works fine till this point





















# import streamlit as st
# import requests
# from datetime import datetime
# from report import create_report
# import pytz
# from tzlocal import get_localzone

# # --- App Setup ---
# st.set_page_config(page_title="Smart Network Diagnostic Assistant", layout="wide")
# st.title("📡 Smart Network Diagnostic Assistant")

# API_URL = "http://localhost:8000/api/v1/diagnostics/run"
# HISTORY_URL = "http://localhost:8000/api/v1/diagnostics/history"

# # --- Hardcoded Login Credentials ---
# USERNAME = "admin"
# PASSWORD = "1234"

# # --- Login Section ---
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# if not st.session_state.logged_in:
#     st.subheader("🔐 Admin Login")
#     user = st.text_input("Username")
#     pwd = st.text_input("Password", type="password")
#     if st.button("Login"):
#         if user == USERNAME and pwd == PASSWORD:
#             st.session_state.logged_in = True
#             st.success("✅ Login successful")
#         else:
#             st.error("❌ Invalid credentials")
#     st.stop()  # Block rest of app if not logged in

# # --- Run Diagnostics ---
# if st.button("▶️ Run Diagnostics"):
#     with st.spinner("Running diagnostics..."):
#         response = requests.post(API_URL, json={"test_type": "full"})
#         if response.status_code == 200:
#             result = response.json()["results"]
#             st.session_state.internet = result["internet"]
#             st.session_state.dns = result["dns"]
#             st.session_state.download = result["download"]
#             st.session_state.upload = result["upload"]
#             st.session_state.ping = result["ping"]
#             st.session_state.suggestions = result["suggestions"]
#             st.session_state.last_run = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         else:
#             st.error("❌ Diagnostics failed!")

# # --- Results Display ---
# if "internet" in st.session_state:
#     st.success("✅ Diagnostics completed successfully.")
#     st.subheader("📊 Diagnostic Dashboard")

#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown("### 🌐 Internet")
#         st.success("✅ Connected" if st.session_state.internet else "❌ Not Connected")
#     with col2:
#         st.markdown("### 🧭 DNS")
#         st.success("✅ Working" if st.session_state.dns else "❌ Failed")

#     col3, col4, col5 = st.columns(3)
#     with col3:
#         st.markdown("### ⬇️ Download")
#         st.metric(label="Speed", value=f"{st.session_state.download} Mbps")
#     with col4:
#         st.markdown("### ⬆️ Upload")
#         st.metric(label="Speed", value=f"{st.session_state.upload} Mbps")
#     with col5:
#         st.markdown("### 📶 Ping")
#         st.metric(label="Latency", value=f"{st.session_state.ping} ms")

#     st.markdown("### 🧠 Suggestions")
#     for s in st.session_state.suggestions:
#         st.success(s)

#     st.markdown(f"🕒 **Last Run:** {st.session_state.last_run}")

#     if st.button("📄 Generate PDF Report"):
#         filename = create_report(
#             st.session_state.internet,
#             st.session_state.dns,
#             st.session_state.download,
#             st.session_state.upload,
#             st.session_state.ping,
#             st.session_state.suggestions,
#         )
#         st.success(f"✅ PDF report saved as `{filename}`")

# # --- Diagnostics History ---
# st.subheader("📂 Previous Diagnostic Runs (Latest 5)")

# try:
#     history_response = requests.get(HISTORY_URL, params={"limit": 5})
#     if history_response.status_code == 200:
#         history = history_response.json()["history"]

#         from_zone = pytz.utc
#         to_zone = get_localzone()

#         for entry in history:
#             utc_time = datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=from_zone)
#             local_time = utc_time.astimezone(to_zone)
#             formatted_time = local_time.strftime("%Y-%m-%d %I:%M %p (%Z)")

#             with st.expander(f"🕒 {formatted_time}"):
#                 st.markdown(f"**🌐 Internet:** {'✅ Connected' if entry['internet'] else '❌ Not Connected'}")
#                 st.markdown(f"**🧭 DNS:** {'✅ Working' if entry['dns'] else '❌ Failed'}")
#                 st.markdown(f"**⬇️ Download:** {entry['download']} Mbps")
#                 st.markdown(f"**⬆️ Upload:** {entry['upload']} Mbps")
#                 st.markdown(f"**📶 Ping:** {entry['ping']} ms")
#                 st.markdown("**🧠 Suggestions:**")
#                 for s in entry["suggestions"]:
#                     st.markdown(f"- {s}")
#     else:
#         st.warning("⚠️ Could not load history.")
# except Exception as e:
#     st.error(f"❌ Error fetching history: {e}")



# import streamlit as st
# import requests
# from datetime import datetime
# from report import create_report
# import pytz
# from tzlocal import get_localzone

# # --- Config ---
# st.set_page_config(page_title="Smart Network Diagnostic Assistant", layout="wide")
# st.title("📡 Smart Network Diagnostic Assistant")

# API_URL = "http://localhost:8000/api/v1/diagnostics/run"
# HISTORY_URL = "http://localhost:8000/api/v1/diagnostics/history"

# USERNAME = "admin"
# PASSWORD = "1234"

# # --- Session Init ---
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False
# if "page" not in st.session_state:
#     st.session_state.page = "login"

# # --- Login Page ---
# if not st.session_state.logged_in:
#     st.subheader("🔐 Admin Login")
#     user = st.text_input("Username")
#     pwd = st.text_input("Password", type="password")
#     if st.button("Login"):
#         if user == USERNAME and pwd == PASSWORD:
#             st.session_state.logged_in = True
#             st.session_state.page = "main"
#             st.rerun()  # Trigger UI refresh to show diagnostics page
#         else:
#             st.error("❌ Invalid credentials")
#     st.stop()

# # --- Logout Button ---
# if st.session_state.logged_in:
#     with st.sidebar:
#         if st.button("🚪 Logout"):
#             st.session_state.logged_in = False
#             st.session_state.page = "login"
#             st.rerun()

# # -----------------------
# # ✅ MAIN PAGE STARTS HERE
# # -----------------------

# # --- Run Diagnostics ---
# if st.button("▶️ Run Diagnostics"):
#     with st.spinner("Running diagnostics..."):
#         response = requests.post(API_URL, json={"test_type": "full"})
#         if response.status_code == 200:
#             result = response.json()["results"]
#             st.session_state.internet = result["internet"]
#             st.session_state.dns = result["dns"]
#             st.session_state.download = result["download"]
#             st.session_state.upload = result["upload"]
#             st.session_state.ping = result["ping"]
#             st.session_state.suggestions = result["suggestions"]
#             st.session_state.last_run = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         else:
#             st.error("❌ Diagnostics failed!")

# # --- Results Display ---
# if "internet" in st.session_state:
#     st.success("✅ Diagnostics completed successfully.")
#     st.subheader("📊 Diagnostic Dashboard")

#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown("### 🌐 Internet")
#         st.success("✅ Connected" if st.session_state.internet else "❌ Not Connected")
#     with col2:
#         st.markdown("### 🧭 DNS")
#         st.success("✅ Working" if st.session_state.dns else "❌ Failed")

#     col3, col4, col5 = st.columns(3)
#     with col3:
#         st.markdown("### ⬇️ Download")
#         st.metric(label="Speed", value=f"{st.session_state.download} Mbps")
#     with col4:
#         st.markdown("### ⬆️ Upload")
#         st.metric(label="Speed", value=f"{st.session_state.upload} Mbps")
#     with col5:
#         st.markdown("### 📶 Ping")
#         st.metric(label="Latency", value=f"{st.session_state.ping} ms")

#     st.markdown("### 🧠 Suggestions")
#     for s in st.session_state.suggestions:
#         st.success(s)

#     st.markdown(f"🕒 **Last Run:** {st.session_state.last_run}")

#     if st.button("📄 Generate PDF Report"):
#         filename = create_report(
#             st.session_state.internet,
#             st.session_state.dns,
#             st.session_state.download,
#             st.session_state.upload,
#             st.session_state.ping,
#             st.session_state.suggestions,
#         )
#         st.success(f"✅ PDF report saved as `{filename}`")

# # --- Diagnostics History ---
# st.subheader("📂 Previous Diagnostic Runs (Latest 5)")

# try:
#     history_response = requests.get(HISTORY_URL, params={"limit": 5})
#     if history_response.status_code == 200:
#         history = history_response.json()["history"]

#         from_zone = pytz.utc
#         to_zone = get_localzone()

#         for entry in history:
#             utc_time = datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=from_zone)
#             local_time = utc_time.astimezone(to_zone)
#             formatted_time = local_time.strftime("%Y-%m-%d %I:%M %p (%Z)")

#             with st.expander(f"🕒 {formatted_time}"):
#                 st.markdown(f"**🌐 Internet:** {'✅ Connected' if entry['internet'] else '❌ Not Connected'}")
#                 st.markdown(f"**🧭 DNS:** {'✅ Working' if entry['dns'] else '❌ Failed'}")
#                 st.markdown(f"**⬇️ Download:** {entry['download']} Mbps")
#                 st.markdown(f"**⬆️ Upload:** {entry['upload']} Mbps")
#                 st.markdown(f"**📶 Ping:** {entry['ping']} ms")
#                 st.markdown("**🧠 Suggestions:**")
#                 for s in entry["suggestions"]:
#                     st.markdown(f"- {s}")
#     else:
#         st.warning("⚠️ Could not load history.")
# except Exception as e:
#     st.error(f"❌ Error fetching history: {e}")


# import streamlit as st
# import requests
# from datetime import datetime
# from report import create_report
# import pytz
# from tzlocal import get_localzone

# # --- Config ---
# st.set_page_config(page_title="Smart Network Diagnostic Assistant", layout="wide")
# st.title("📡 Smart Network Diagnostic Assistant")

# API_URL = "http://localhost:8000/api/v1/diagnostics/run"
# HISTORY_URL = "http://localhost:8000/api/v1/diagnostics/history"

# USERNAME = "admin"
# PASSWORD = "1234"

# # --- Session Init ---
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False
# if "page" not in st.session_state:
#     st.session_state.page = "login"

# # --- Logout Button (Top-Right) ---
# logout_css = """
#     <style>
#         .logout-button {
#             position: absolute;
#             top: 20px;
#             right: 30px;
#             z-index: 100;
#         }
#     </style>
# """
# st.markdown(logout_css, unsafe_allow_html=True)
# logout_button = st.button("🚪 Logout", key="logout", help="Click to logout", type="primary")
# if logout_button:
#     st.session_state.logged_in = False
#     st.session_state.page = "login"
#     st.rerun()

# # --- Login Page ---
# if not st.session_state.logged_in:
#     st.subheader("🔐 Admin Login")
#     user = st.text_input("Username")
#     pwd = st.text_input("Password", type="password")
#     if st.button("Login"):
#         if user == USERNAME and pwd == PASSWORD:
#             st.session_state.logged_in = True
#             st.session_state.page = "main"
#             st.rerun()
#         else:
#             st.error("❌ Invalid credentials")
#     st.stop()

# # -----------------------
# # ✅ MAIN PAGE STARTS HERE
# # -----------------------

# # --- Run Diagnostics ---
# if st.button("▶️ Run Diagnostics"):
#     with st.spinner("Running diagnostics..."):
#         response = requests.post(API_URL, json={"test_type": "full"})
#         if response.status_code == 200:
#             result = response.json()["results"]
#             st.session_state.internet = result["internet"]
#             st.session_state.dns = result["dns"]
#             st.session_state.download = result["download"]
#             st.session_state.upload = result["upload"]
#             st.session_state.ping = result["ping"]
#             st.session_state.suggestions = result["suggestions"]
#             st.session_state.last_run = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         else:
#             st.error("❌ Diagnostics failed!")

# # --- Results Display ---
# if "internet" in st.session_state:
#     st.success("✅ Diagnostics completed successfully.")
#     st.subheader("📊 Diagnostic Dashboard")

#     col1, col2 = st.columns(2)
#     with col1:
#         st.markdown("### 🌐 Internet")
#         st.success("✅ Connected" if st.session_state.internet else "❌ Not Connected")
#     with col2:
#         st.markdown("### 🧭 DNS")
#         st.success("✅ Working" if st.session_state.dns else "❌ Failed")

#     col3, col4, col5 = st.columns(3)
#     with col3:
#         st.markdown("### ⬇️ Download")
#         st.metric(label="Speed", value=f"{st.session_state.download} Mbps")
#     with col4:
#         st.markdown("### ⬆️ Upload")
#         st.metric(label="Speed", value=f"{st.session_state.upload} Mbps")
#     with col5:
#         st.markdown("### 📶 Ping")
#         st.metric(label="Latency", value=f"{st.session_state.ping} ms")

#     st.markdown("### 🧠 Suggestions")
#     for s in st.session_state.suggestions:
#         st.success(s)

#     st.markdown(f"🕒 **Last Run:** {st.session_state.last_run}")

#     if st.button("📄 Generate PDF Report"):
#         filename = create_report(
#             st.session_state.internet,
#             st.session_state.dns,
#             st.session_state.download,
#             st.session_state.upload,
#             st.session_state.ping,
#             st.session_state.suggestions,
#         )
#         st.success(f"✅ PDF report saved as `{filename}`")

# # --- Diagnostics History ---
# st.subheader("📂 Previous Diagnostic Runs (Latest 5)")

# try:
#     history_response = requests.get(HISTORY_URL, params={"limit": 5})
#     if history_response.status_code == 200:
#         history = history_response.json()["history"]

#         from_zone = pytz.utc
#         to_zone = get_localzone()

#         for entry in history:
#             utc_time = datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=from_zone)
#             local_time = utc_time.astimezone(to_zone)
#             formatted_time = local_time.strftime("%Y-%m-%d %I:%M %p (%Z)")

#             with st.expander(f"🕒 {formatted_time}"):
#                 st.markdown(f"**🌐 Internet:** {'✅ Connected' if entry['internet'] else '❌ Not Connected'}")
#                 st.markdown(f"**🧭 DNS:** {'✅ Working' if entry['dns'] else '❌ Failed'}")
#                 st.markdown(f"**⬇️ Download:** {entry['download']} Mbps")
#                 st.markdown(f"**⬆️ Upload:** {entry['upload']} Mbps")
#                 st.markdown(f"**📶 Ping:** {entry['ping']} ms")
#                 st.markdown("**🧠 Suggestions:**")
#                 for s in entry["suggestions"]:
#                     st.markdown(f"- {s}")
#     else:
#         st.warning("⚠️ Could not load history.")
# except Exception as e:
#     st.error(f"❌ Error fetching history: {e}")










import streamlit as st
import requests
from datetime import datetime
from report import create_report
import pytz
from tzlocal import get_localzone

# --- Config ---
st.set_page_config(page_title="Smart Network Diagnostic Assistant", layout="wide")
st.title("📡 Smart Network Diagnostic Assistant")

API_URL = "http://localhost:8000/api/v1/diagnostics/run"
HISTORY_URL = "http://localhost:8000/api/v1/diagnostics/history"

USERNAME = "admin"
PASSWORD = "1234"

# --- Session Init ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"

# --- Logout Button (Top-Right Only After Login) ---
if st.session_state.logged_in:
    logout_css = """
        <style>
            .logout-container {
                position: absolute;
                top: 15px;
                right: 25px;
                z-index: 9999;
            }
        </style>
        <div class="logout-container">
            <form action="" method="post">
                <input type="submit" value="🚪 Logout" name="logout_btn" style="background-color:#f44336;color:white;border:none;padding:8px 14px;border-radius:6px;cursor:pointer;font-weight:bold;">
            </form>
        </div>
    """
    st.markdown(logout_css, unsafe_allow_html=True)

    if "logout_btn" in st.session_state:
        st.session_state.logged_in = False
        st.session_state.page = "login"
        st.rerun()

# --- Login Page ---
if not st.session_state.logged_in:
    st.subheader("🔐 Admin Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == USERNAME and pwd == PASSWORD:
            st.session_state.logged_in = True
            st.session_state.page = "main"
            st.rerun()
        else:
            st.error("❌ Invalid credentials")
    st.stop()

# -----------------------
# ✅ MAIN PAGE STARTS HERE
# -----------------------

# --- Run Diagnostics ---
if st.button("▶️ Run Diagnostics"):
    with st.spinner("Running diagnostics..."):
        response = requests.post(API_URL, json={"test_type": "full"})
        if response.status_code == 200:
            result = response.json()["results"]
            st.session_state.internet = result["internet"]
            st.session_state.dns = result["dns"]
            st.session_state.download = result["download"]
            st.session_state.upload = result["upload"]
            st.session_state.ping = result["ping"]
            st.session_state.suggestions = result["suggestions"]
            st.session_state.last_run = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            st.error("❌ Diagnostics failed!")

# --- Results Display ---
if "internet" in st.session_state:
    st.success("✅ Diagnostics completed successfully.")
    st.subheader("📊 Diagnostic Dashboard")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🌐 Internet")
        st.success("✅ Connected" if st.session_state.internet else "❌ Not Connected")
    with col2:
        st.markdown("### 🧭 DNS")
        st.success("✅ Working" if st.session_state.dns else "❌ Failed")

    col3, col4, col5 = st.columns(3)
    with col3:
        st.markdown("### ⬇️ Download")
        st.metric(label="Speed", value=f"{st.session_state.download} Mbps")
    with col4:
        st.markdown("### ⬆️ Upload")
        st.metric(label="Speed", value=f"{st.session_state.upload} Mbps")
    with col5:
        st.markdown("### 📶 Ping")
        st.metric(label="Latency", value=f"{st.session_state.ping} ms")

    st.markdown("### 🧠 Suggestions")
    for s in st.session_state.suggestions:
        st.success(s)

    st.markdown(f"🕒 **Last Run:** {st.session_state.last_run}")

    if st.button("📄 Generate PDF Report"):
        filename = create_report(
            st.session_state.internet,
            st.session_state.dns,
            st.session_state.download,
            st.session_state.upload,
            st.session_state.ping,
            st.session_state.suggestions,
        )
        st.success(f"✅ PDF report saved as `{filename}`")

# --- Diagnostics History ---
st.subheader("📂 Previous Diagnostic Runs (Latest 5)")

try:
    history_response = requests.get(HISTORY_URL, params={"limit": 5})
    if history_response.status_code == 200:
        history = history_response.json()["history"]

        from_zone = pytz.utc
        to_zone = get_localzone()

        for entry in history:
            utc_time = datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=from_zone)
            local_time = utc_time.astimezone(to_zone)
            formatted_time = local_time.strftime("%Y-%m-%d %I:%M %p (%Z)")

            with st.expander(f"🕒 {formatted_time}"):
                st.markdown(f"**🌐 Internet:** {'✅ Connected' if entry['internet'] else '❌ Not Connected'}")
                st.markdown(f"**🧭 DNS:** {'✅ Working' if entry['dns'] else '❌ Failed'}")
                st.markdown(f"**⬇️ Download:** {entry['download']} Mbps")
                st.markdown(f"**⬆️ Upload:** {entry['upload']} Mbps")
                st.markdown(f"**📶 Ping:** {entry['ping']} ms")
                st.markdown("**🧠 Suggestions:**")
                for s in entry["suggestions"]:
                    st.markdown(f"- {s}")
    else:
        st.warning("⚠️ Could not load history.")
except Exception as e:
    st.error(f"❌ Error fetching history: {e}")
