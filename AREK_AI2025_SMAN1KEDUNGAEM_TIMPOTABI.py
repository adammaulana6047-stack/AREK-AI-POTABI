MERAH = "\033[91m"
HIJAU = "\033[92m"
KUNING = "\033[93m"
BIRU = "\033[94m"
CYAN = "\033[96m"
RESET = "\033[0m"

def parse_number(inp):
    """Bersihkan input angka seperti '1.000.000' atau '1,000,000' menjadi float."""
    s = str(inp).strip()
    s = s.replace("$", "").replace(" ", "")

    if s.count(",") > 0 and s.count(".") == 0:
        s = s.replace(",", ".")
    s = s.replace(",", "")  
    s = s.replace(".", "") if s.isdigit() else s 
    try:
        return float(s)
    except Exception:
        filt = "".join(ch for ch in s if ch.isdigit() or ch in ".-")
        return float(filt) if filt else None

def input_float(prompt):
    while True:
        raw = input(f"{KUNING}{prompt}{RESET}")
        val = parse_number(raw)
        if val is None:
            print(f"{MERAH}Input tidak valid. Masukkan angka, misal 15000 atau 15.000 atau 15,000.00{RESET}")
            continue
        if val < 0:
            print(f"{MERAH}Nilai tidak boleh negatif.{RESET}")
            continue
        return val

def input_choice(prompt, choices):
    while True:
        try:
            val = int(input(f"{KUNING}{prompt}{RESET}"))
            if val in choices:
                return val
            print(f"{MERAH}Pilihan tidak valid. Pilih salah satu: {choices}{RESET}")
        except ValueError:
            print(f"{MERAH}Masukkan angka bulat (contoh: 1, 2, atau 3).{RESET}")

print(f"{CYAN}=== Program Diskon Jalan Tol ==={RESET}")

harga_tol = input_float("Masukkan biaya tol ($): ")

print(f"\n{BIRU}Jenis Kendaraan:{RESET}")
print(f"{HIJAU}1. Golongan 1 (Mobil Pribadi){RESET}")
print(f"{HIJAU}2. Golongan 2 (Truk Kecil / Bus){RESET}")
print(f"{HIJAU}3. Golongan 3 (Truk Besar){RESET}")

golongan = input_choice("Masukkan golongan kendaraan (1/2/3): ", {1, 2, 3})

diskon_map = {1: 10, 2: 5, 3: 0}
diskon = diskon_map.get(golongan, 0)

potongan = harga_tol * (diskon / 100)
total_bayar = harga_tol - potongan

print(f"\n{CYAN}=== Hasil Perhitungan ==={RESET}")
print(f"{BIRU}Biaya tol sebelum diskon :{RESET} $ {harga_tol:,.2f}")
print(f"{BIRU}Diskon                    :{RESET} {diskon}%")
print(f"{BIRU}Potongan                  :{RESET} ${potongan:,.2f}")
print(f"{BIRU}Total bayar               :{RESET} $ {total_bayar:,.2f}")