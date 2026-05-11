#else and finally
#else runs aif no error occurrend, finally always runs-great for cleanup

try:
    result = 100 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
else:
    print(f"Success {result}")
finally:
    print("This Always run")  # clean up code here



#Catching multiple errors + custom Messages

def safe_open(filepath):
    try:
        with open(filepath, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"[!] not fount! {filepath}")
    except PermissionError:
        print(f"[!] Access denied! {filepath}")
    except Exception as e:
        print(f"[!] Unexpected: {e}")
    return None

safe_open("C//user")