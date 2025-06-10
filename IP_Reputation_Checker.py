import requests

API_KEY = "YOUR_API_KEY"
ip = input ("Enter a suspected IP address: ")

url = "https://api.abuseipdb.com/api/v2/check"

querystring = {
    "ipAddress": ip,
    "maxAgeInDays": "90" 
}

headers = {
    "Accept": "application/json",
    "Key": API_KEY
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    result=response.json()["data"]
    print(f"\n[+] IP: {result["ipAddress"]}")
    print(f"[+] Abuse Score: {result["abuseConfidenceScore"]}/100")
    print(f"[+] Country: {result["countryCode"]}")
    print(f"[+] Domain: {result["domain"]}")
    print(f"[+] Total Reports: {result["totalReports"]}")
    print(f"[+] Last Reported:{result["lastReportedAt"]}")

else:
    print("[-] Error:", response.status_code)


