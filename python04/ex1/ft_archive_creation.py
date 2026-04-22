def write_archive(filename: str) -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
    print(f"Initializing new storage unit: {filename}")
    file = open(filename, "w")
    print("Storage unit created successfully...\n")
    print("Inscribing preservation data...")
    file.write("[ENTRY 001] New quantum algorithm discovered\n")
    file.write("[ENTRY 002] Efficiency increased by 347%\n")
    file.write("[ENTRY 003] Archived by Data Archivist trainee\n")
    print("[ENTRY 001] New quantum algorithm discovered")
    print("[ENTRY 002] Efficiency increased by 347%")
    print("[ENTRY 003] Archived by Data Archivist trainee\n")
    file.close()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    write_archive("new_discovery.txt")
