def check_service(name, status):
    if status == "OK":
        print(f"[OK] - {name}")
    else:
        print(f"[WRONG] - {name}")
