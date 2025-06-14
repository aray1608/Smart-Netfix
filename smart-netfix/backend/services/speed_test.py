# import speedtest

# def run_speedtest():
#     st = speedtest.Speedtest()
#     download = st.download() / 1e6  # Convert to Mbps
#     upload = st.upload() / 1e6
#     return round(download, 2), round(upload, 2)

# speed_test.py

# import speedtest

# def run_speedtest():
#     st = speedtest.Speedtest()
#     st.get_best_server()

#     # download = st.download() / 1_000_000  # Convert to Mbps
#     # upload = st.upload() / 1_000_000      # Convert to Mbps
#     download = round(st.download() / 1_000_000, 2)
#     upload = round(st.upload() / 1_000_000, 2)
#     ping = int(st.results.ping)               # Get ping value in ms

#     return download, upload, ping


# import speedtest

# def run_speedtest():
#     st = speedtest.Speedtest()
#     st.get_best_server()
#     download_speed = round(st.download() / 1_000_000, 2)  # Mbps
#     upload_speed = round(st.upload() / 1_000_000, 2)      # Mbps
#     ping = round(st.results.ping, 2)                      # ms
#     return download_speed, upload_speed, ping


# import speedtest

# def run_speedtest():
#     try:
#         st = speedtest.Speedtest()
#         st.get_best_server()
#         download_speed = st.download() / 1_000_000
#         upload_speed = st.upload() / 1_000_000
#         ping = st.results.ping

#         if download_speed == 0.0 or upload_speed == 0.0 or ping == 0.0:
#             raise Exception("Speed test failed or returned zero values.")

#         return {
#             "download": round(download_speed, 2),
#             "upload": round(upload_speed, 2),
#             "ping": round(ping, 2)
#         }

#     except Exception as e:
#         return {
#             "download": -1,
#             "upload": -1,
#             "ping": -1,
#             "error": str(e)
#         }


import speedtest

def run_speedtest():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1_000_000
        upload_speed = st.upload() / 1_000_000
        ping = st.results.ping

        if download_speed == 0.0 or upload_speed == 0.0 or ping == 0.0:
            raise Exception("Speed test failed or returned zero values.")

        return {
            "download": round(download_speed, 2),
            "upload": round(upload_speed, 2),
            "ping": round(ping, 2)
        }

    except Exception as e:
        return {
            "download": -1,
            "upload": -1,
            "ping": -1,
            "error": str(e)
        }

    


