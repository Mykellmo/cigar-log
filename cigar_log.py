import json
import os

LOG_FILE = "cigar_log.json"

# Load existing cigar log
def load_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    return []

# Save cigar log
def save_log(log):
    with open(LOG_FILE, "w") as f:
        json.dump(log, f, indent=4)

# Add a cigar
def add_cigar():
    name = input("Cigar name: ")
    brand = input("Brand: ")
    rating = input("Rating (1-10): ")
    notes = input("Notes: ")

    cigar = {
        "name": name,
        "brand": brand,
        "rating": rating,
        "notes": notes
    }

    log = load_log()
    log.append(cigar)
    save_log(log)
    print(f"✅ Saved {name} by {brand}!\n")

# View all cigars
def view_cigars():
    log = load_log()
    if not log:
        print("📭 No cigars logged yet.\n")
        return
    
    for i, cigar in enumerate(log, start=1):
        print(f"{i}. {cigar['name']} ({cigar['brand']}) - Rating: {cigar['rating']}")
        print(f"   Notes: {cigar['notes']}\n")

# Menu
def main():
    while True:
        print("=== Cigar Log ===")
        print("1. Add a cigar")
        print("2. View all cigars")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_cigar()
        elif choice == "2":
            view_cigars()
        elif choice == "3":
            print("👋 Exiting Cigar Log. Enjoy your smoke!")
            break
        else:
            print("❌ Invalid choice, try again.\n")

if __name__ == "__main__":
    main()
