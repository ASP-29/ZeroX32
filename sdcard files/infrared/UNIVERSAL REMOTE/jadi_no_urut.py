import os

def rename_ir_names(input_file, base_name="Power"):
    """Rename semua field `name:` dalam satu file IR."""
    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    counter = 1
    new_lines = []
    for line in lines:
        if line.strip().startswith("name:"):
            new_line = f"name: {base_name}_{counter}\n"
            new_lines.append(new_line)
            counter += 1
        else:
            new_lines.append(line)

    with open(input_file, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print(f"[OK] {input_file} | {counter-1} nama diganti.")


def menu():
    print("=== Flipper Zero IR Name Renamer ===")
    print("1. Scan file tunggal dalam folder")
    print("2. Proses semua file .ir dalam folder")
    print("3. Keluar")
    choice = input("Pilih menu: ").strip()
    return choice


def pick_file(folder):
    files = [f for f in os.listdir(folder) if f.lower().endswith(".ir")]
    if not files:
        print("❌ Tidak ada file .ir ditemukan di folder ini.")
        return None

    print("\nDaftar file IR:")
    for i, f in enumerate(files, start=1):
        print(f"{i}. {f}")

    while True:
        try:
            sel = int(input("Pilih file (nomor): ").strip())
            if 1 <= sel <= len(files):
                return os.path.join(folder, files[sel-1])
        except ValueError:
            pass
        print("⚠️ Pilihan tidak valid, coba lagi.")


def process_folder(folder, base_name):
    files = [f for f in os.listdir(folder) if f.lower().endswith(".ir")]
    if not files:
        print("❌ Tidak ada file .ir ditemukan di folder ini.")
        return
    for f in files:
        path = os.path.join(folder, f)
        rename_ir_names(path, base_name)


if __name__ == "__main__":
    base_name = input("Masukkan nama dasar (default: Power): ").strip() or "Power"
    folder = input("Masukkan folder path (kosongkan untuk current directory): ").strip() or "."

    while True:
        choice = menu()
        if choice == "1":
            file_path = pick_file(folder)
            if file_path:
                rename_ir_names(file_path, base_name)
        elif choice == "2":
            process_folder(folder, base_name)
        elif choice == "3":
            print("Keluar...")
            break
        else:
            print("⚠️ Menu tidak valid.\n")
