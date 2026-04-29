from datetime import datetime       # used to print the datetime
# Method 2:
def capture_log(**kwargs):

    timestamp = datetime.now()
    log_line = ", ".join(f"{key} = {value}" for key, value in kwargs.items())
    log_line = f"{timestamp} | {log_line}"
    with open("python_logs.txt","a") as file:
        file.write(log_line  + "\n")

    print("log saved successfully!")

capture_log(status = "Done", status_code = 101, message = "Job run successfully")