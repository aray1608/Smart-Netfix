# import argparse
# import requests

# API_URL = "http://localhost:8000/api/v1/diagnostics/run"

# def run_diagnostics():
#     print(">>\nRunning diagnostics...")
#     try:
#         response = requests.post(API_URL, json={"test_type": "full"})
#         response.raise_for_status()
#         data = response.json()

#         print(f"✅ Internet: {data.get('internet')}")
#         print(f"✅ DNS: {data.get('dns')}")
#         print(f"⬇️ Download: {data.get('download')} Mbps")
#         print(f"⬆️ Upload: {data.get('upload')} Mbps")
#         print(f"📶 Ping: {data.get('ping')} ms")
#         print("🧠 Suggestions:")
#         for s in data.get("suggestions", []):
#             print(f" - {s}")
#     except Exception as e:
#         print("❌ Error during diagnostics:", e)

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser(description="Smart Network Diagnostic CLI")
#     parser.add_argument('--run-diagnostics', action='store_true', help='Run full diagnostics')

#     args = parser.parse_args()

#     if args.run_diagnostics:
#         run_diagnostics()


# import requests

# def run_diagnostics():
#     print(">>\nRunning diagnostics...")

#     try:
#         response = requests.post("http://localhost:8000/api/v1/diagnostics/run", json={})
#         response.raise_for_status()
#         data = response.json().get("results", {})

#         print(f"✅ Internet: {data.get('internet')}")
#         print(f"✅ DNS: {data.get('dns')}")
#         print(f"⬇️ Download: {data.get('download')} Mbps")
#         print(f"⬆️ Upload: {data.get('upload')} Mbps")
#         print(f"📶 Ping: {data.get('ping')} ms")

#         print("🧠 Suggestions:")
#         for s in data.get("suggestions", []):
#             print(f" - {s}")

#     except requests.exceptions.RequestException as e:
#         print(f"❌ Error during diagnostics: {e}")

# if __name__ == "__main__":
#     import sys
#     if "--run-diagnostics" in sys.argv:
#         run_diagnostics()


# import argparse
# import requests

# def run_diagnostics():
#     print(">>\nRunning diagnostics...")
#     try:
#         response = requests.post("http://localhost:8000/api/v1/diagnostics/run")
#         response.raise_for_status()
#         data = response.json().get("results", {})

#         print(f"✅ Internet: {data.get('internet')}")
#         print(f"✅ DNS: {data.get('dns')}")
#         print(f"⬇️ Download: {data.get('download')} Mbps")
#         print(f"⬆️ Upload: {data.get('upload')} Mbps")
#         print(f"📶 Ping: {data.get('ping')} ms")

#         print("🧠 Suggestions:")
#         for suggestion in data.get("suggestions", []):
#             print(f" - {suggestion}")

#     except Exception as e:
#         print("❌ Error during diagnostics:", e)

# if __name__ == "__main__":
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--run-diagnostics", action="store_true", help="Run full network diagnostics")
#     args = parser.parse_args()

#     if args.run_diagnostics:
#         run_diagnostics()


import argparse
import requests
from report import create_report

def run_diagnostics(generate_pdf=False):
    print(">>\nRunning diagnostics...")
    try:
        response = requests.post("http://localhost:8000/api/v1/diagnostics/run")
        response.raise_for_status()
        data = response.json().get("results", {})

        print(f"✅ Internet: {data.get('internet')}")
        print(f"✅ DNS: {data.get('dns')}")
        print(f"⬇️ Download: {data.get('download')} Mbps")
        print(f"⬆️ Upload: {data.get('upload')} Mbps")
        print(f"📶 Ping: {data.get('ping')} ms")

        print("🧠 Suggestions:")
        for suggestion in data.get("suggestions", []):
            print(f" - {suggestion}")

        if generate_pdf:
            filename = create_report(
                data.get("internet"),
                data.get("dns"),
                data.get("download"),
                data.get("upload"),
                data.get("ping"),
                data.get("suggestions")
            )
            print(f"\n📄 PDF report saved as `{filename}`")

    except Exception as e:
        print("❌ Error during diagnostics:", e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-diagnostics", action="store_true", help="Run full network diagnostics")
    parser.add_argument("--pdf", action="store_true", help="Generate PDF report along with diagnostics")
    args = parser.parse_args()

    if args.run_diagnostics:
        run_diagnostics(generate_pdf=args.pdf)
    else:
        parser.print_help()
