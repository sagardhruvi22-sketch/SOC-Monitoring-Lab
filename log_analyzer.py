with open("sample.log", "r") as file:
    logs = file.readlines()

failed_logins = 0

for log in logs:
    if "Failed login" in log:
        failed_logins += 1

print("Failed Login Attempts:", failed_logins)

if failed_logins > 1:
    print("ALERT: Suspicious Activity Detected")
