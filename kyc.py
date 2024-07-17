#! python3
import pyperclip

collect_data = True
result = ""

def assemble_result(date, time, manual_au, manual_nz, manual_uk, refresh_au, greeting="Bom dia"):
    return f"{greeting}!\n\n{date}\nManual KYC\n\nBR Time ({time})\n AU -> {manual_au}\n NZ -> {manual_nz}\n UK -> {manual_uk}\n\n{date}\nKYC Refresh\n\nBR Time ({time})\n AU -> {refresh_au}\n"

while collect_data:
    date = input("Inform date: ")
    time = input("Inform time: ")

    print("\nManual KYC")
    manual_au = input("AU: ")
    manual_nz = input("NZ: ")
    manual_uk = input("UK: ")

    print("\nKYC Refresh")
    refresh_au = input("AU: ")

    result = assemble_result(date, time, manual_au, manual_nz, manual_uk, refresh_au)

    print(f"\n{result}\n")

    is_correct = input("Is this correct [y/n]? ")
    correct_possibilities = "yYsSdDjJ"

    if is_correct in correct_possibilities:
        collect_data = False

pyperclip.copy(result)
print("\nKYC Numbers copied to the clipboard")
input("Press any key to close application")

