def get_suggestions(internet, dns, download_speed, upload_speed, ping):
    suggestions = []

    if not internet:
        suggestions.append("❌ No Internet connection. Check your router or try reconnecting.")
    elif not dns:
        suggestions.append("❌ DNS issue detected. Try using a public DNS like 8.8.8.8 (Google).")
    elif download_speed == -1 and upload_speed == -1:
        suggestions.append("⚠️ Speed test failed. Please check your internet connection and try again.")
    elif download_speed < 5:
        suggestions.append("⚠️ Slow Internet detected (< 5 Mbps). Try restarting your router or switching networks.")
    else:
        suggestions.append("✅ All systems are working fine!")

    return suggestions
