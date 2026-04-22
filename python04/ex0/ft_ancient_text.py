

def read_vault(filename: str) -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print(f"Accessing Storage Vault: {filename}")
    try:
        file = open(filename, "r")
        content = file.read()
        file.close()
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(content)
        print()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    read_vault("ancient_fragment.txt")
