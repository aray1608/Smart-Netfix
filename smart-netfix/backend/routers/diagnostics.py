# # from fastapi import APIRouter
# # from pydantic import BaseModel
# # from backend.services.connectivity import check_internet
# # from backend.services.dns_test import check_dns
# # from backend.services.speed_test import run_speedtest
# # from backend.services.suggestions import get_suggestions

# # router = APIRouter()

# # class DiagnosticRequest(BaseModel):
# #     test_type: str  # currently only 'full' is used

# # @router.post("/run")
# # def run_diagnostics(request: DiagnosticRequest):
# #     if request.test_type == "full":
# #         internet = check_internet()
# #         dns = check_dns()
# #         download, upload, ping = run_speedtest()
# #         suggestions = get_suggestions(internet, dns, download)

# #         return {
# #             "results": {
# #                 "internet": internet,
# #                 "dns": dns,
# #                 "download": download,
# #                 "upload": upload,
# #                 "ping": ping,
# #                 "suggestions": suggestions,
# #             }
# #         }
# #     else:
# #         return {"error": "Invalid test type"}


# from fastapi import APIRouter
# from fastapi.responses import JSONResponse
# from backend.services.connectivity import check_internet
# from backend.services.dns_test import check_dns
# from backend.services.speed_test import run_speedtest
# from backend.services.suggestions import get_suggestions

# router = APIRouter()

# # @router.post("/api/v1/diagnostics/run")

# def run_diagnostics(payload: dict):
#     print("📡 Received diagnostics request...")

#     try:
#         internet = check_internet()
#         print("✅ Internet:", internet)
#     except Exception as e:
#         print("❌ Internet check error:", e)
#         internet = False

#     try:
#         dns = check_dns()
#         print("✅ DNS:", dns)
#     except Exception as e:
#         print("❌ DNS check error:", e)
#         dns = False

#     try:
#         download, upload, ping = run_speedtest()
#         print("✅ Speedtest - DL:", download, "UL:", upload, "Ping:", ping)
#     except Exception as e:
#         print("❌ Speedtest error:", e)
#         download, upload, ping = 0.0, 0.0, 0.0

#     try:
#         suggestions = get_suggestions(internet, dns, download, upload, ping)
#         print("🧠 Suggestions:", suggestions)
#     except Exception as e:
#         print("❌ Suggestions error:", e)
#         suggestions = ["An unknown error occurred during diagnostics."]


#     return JSONResponse(content={
#         "results": {
#             "internet": internet,
#             "dns": dns,
#             "download": download,
#             "upload": upload,
#             "ping": ping,
#             "suggestions": suggestions,
#         }
#     })


# from fastapi import APIRouter
# from fastapi.responses import JSONResponse
# from backend.services.connectivity import check_internet
# from backend.services.dns_test import check_dns
# from backend.services.speed_test import run_speedtest
# from backend.services.suggestions import get_suggestions

# router = APIRouter()

# @router.post("/run")  # ✅ Route fixed
# def run_diagnostics(payload: dict = {}):
#     print("📡 Received diagnostics request...")

#     try:
#         internet = check_internet()
#         print("✅ Internet:", internet)
#     except Exception as e:
#         print("❌ Internet check error:", e)
#         internet = False

#     try:
#         dns = check_dns()
#         print("✅ DNS:", dns)
#     except Exception as e:
#         print("❌ DNS check error:", e)
#         dns = False

#     try:
#         download, upload, ping = run_speedtest()
#         print("✅ Speedtest - DL:", download, "UL:", upload, "Ping:", ping)
#     except Exception as e:
#         print("❌ Speedtest error:", e)
#         download, upload, ping = 0.0, 0.0, 0.0

#     try:
#         suggestions = get_suggestions(internet, dns, download, upload, ping)
#         print("🧠 Suggestions:", suggestions)
#     except Exception as e:
#         print("❌ Suggestions error:", e)
#         suggestions = ["An unknown error occurred during diagnostics."]

#     return JSONResponse(content={
#         "results": {
#             "internet": internet,
#             "dns": dns,
#             "download": download,
#             "upload": upload,
#             "ping": ping,
#             "suggestions": suggestions,
#         }
#     })


# from fastapi import APIRouter
# from fastapi.responses import JSONResponse
# from backend.services.connectivity import check_internet
# from backend.services.dns_test import check_dns
# from backend.services.speed_test import run_speedtest
# from backend.services.suggestions import get_suggestions

# router = APIRouter()

# @router.post("/run")
# def run_diagnostics(payload: dict = {}):
#     print("📡 Received diagnostics request...")

#     try:
#         internet = check_internet()
#         print("✅ Internet:", internet)
#     except Exception as e:
#         print("❌ Internet check error:", e)
#         internet = False

#     try:
#         dns = check_dns()
#         print("✅ DNS:", dns)
#     except Exception as e:
#         print("❌ DNS check error:", e)
#         dns = False

#     try:
#         speed_results = run_speedtest()
#         download = speed_results["download"]
#         upload = speed_results["upload"]
#         ping = speed_results["ping"]
#         print("✅ Speedtest - DL:", download, "UL:", upload, "Ping:", ping)
#     except Exception as e:
#         print("❌ Speedtest error:", e)
#         download, upload, ping = -1, -1, -1

#     try:
#         suggestions = get_suggestions(internet, dns, download, upload, ping)
#         print("🧠 Suggestions:", suggestions)
#     except Exception as e:
#         print("❌ Suggestions error:", e)
#         suggestions = ["An unknown error occurred during diagnostics."]

#     return JSONResponse(content={
#         "results": {
#             "internet": internet,
#             "dns": dns,
#             "download": download,
#             "upload": upload,
#             "ping": ping,
#             "suggestions": suggestions,
#         }
#     })


# from fastapi import APIRouter
# from fastapi.responses import JSONResponse
# from backend.services.connectivity import check_internet
# from backend.services.dns_test import check_dns
# from backend.services.speed_test import run_speedtest
# from backend.services.suggestions import get_suggestions
# from backend.db.database import db  # <-- MongoDB client
# from datetime import datetime

# router = APIRouter()

# @router.post("/run")
# def run_diagnostics(payload: dict = {}):
#     print("📡 Received diagnostics request...")

#     try:
#         internet = check_internet()
#         print("✅ Internet:", internet)
#     except Exception as e:
#         print("❌ Internet check error:", e)
#         internet = False

#     try:
#         dns = check_dns()
#         print("✅ DNS:", dns)
#     except Exception as e:
#         print("❌ DNS check error:", e)
#         dns = False

#     try:
#         speed_results = run_speedtest()
#         download = speed_results["download"]
#         upload = speed_results["upload"]
#         ping = speed_results["ping"]
#         print("✅ Speedtest - DL:", download, "UL:", upload, "Ping:", ping)
#     except Exception as e:
#         print("❌ Speedtest error:", e)
#         download, upload, ping = -1, -1, -1

#     try:
#         suggestions = get_suggestions(internet, dns, download, upload, ping)
#         print("🧠 Suggestions:", suggestions)
#     except Exception as e:
#         print("❌ Suggestions error:", e)
#         suggestions = ["An unknown error occurred during diagnostics."]

#     # Save to MongoDB
#     record = {
#         "internet": internet,
#         "dns": dns,
#         "download": download,
#         "upload": upload,
#         "ping": ping,
#         "suggestions": suggestions,
#         "timestamp": datetime.utcnow(),
#     }
#     db["diagnostic_history"].insert_one(record)

#     return JSONResponse(content={
#         "results": {
#             "internet": internet,
#             "dns": dns,
#             "download": download,
#             "upload": upload,
#             "ping": ping,
#             "suggestions": suggestions,
#         }
#     })


# @router.get("/history")
# def get_diagnostics_history(limit: int = 10):
#     history = list(db["diagnostic_history"]
#                    .find()
#                    .sort("timestamp", -1)
#                    .limit(limit))
#     for item in history:
#         item["_id"] = str(item["_id"])
#         item["timestamp"] = item["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
#     return {"history": history}




from fastapi import APIRouter
from fastapi.responses import JSONResponse
from backend.services.connectivity import check_internet
from backend.services.dns_test import check_dns
from backend.services.speed_test import run_speedtest
from backend.services.suggestions import get_suggestions
from backend.db.database import db
from datetime import datetime

router = APIRouter()

@router.post("/run")
def run_diagnostics(payload: dict = {}):
    print("📡 Received diagnostics request...")

    try:
        internet = check_internet()
        print("✅ Internet:", internet)
    except Exception as e:
        print("❌ Internet check error:", e)
        internet = False

    try:
        dns = check_dns()
        print("✅ DNS:", dns)
    except Exception as e:
        print("❌ DNS check error:", e)
        dns = False

    try:
        speed_results = run_speedtest()
        download = speed_results["download"]
        upload = speed_results["upload"]
        ping = speed_results["ping"]
        print("✅ Speedtest - DL:", download, "UL:", upload, "Ping:", ping)
    except Exception as e:
        print("❌ Speedtest error:", e)
        download, upload, ping = -1, -1, -1

    try:
        suggestions = get_suggestions(internet, dns, download, upload, ping)
        print("🧠 Suggestions:", suggestions)
    except Exception as e:
        print("❌ Suggestions error:", e)
        suggestions = ["An unknown error occurred during diagnostics."]

    # Save to MongoDB
    record = {
        "internet": internet,
        "dns": dns,
        "download": download,
        "upload": upload,
        "ping": ping,
        "suggestions": suggestions,
        "timestamp": datetime.utcnow(),
    }
    db["diagnostic_history"].insert_one(record)

    return JSONResponse(content={
        "results": {
            "internet": internet,
            "dns": dns,
            "download": download,
            "upload": upload,
            "ping": ping,
            "suggestions": suggestions,
        }
    })


@router.get("/history")
def get_diagnostics_history(limit: int = 10):
    history = list(
        db["diagnostic_history"]
        .find()
        .sort("timestamp", -1)
        .limit(limit)
    )
    for item in history:
        item["_id"] = str(item["_id"])  # convert ObjectId to string
        item["timestamp"] = item["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
    return {"history": history}
