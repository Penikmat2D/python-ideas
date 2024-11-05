import requests

def get_exchange_rate(from_currency, to_currency):
    api_key = 'a6e2872c01b1604125383272' 
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_currency}/{to_currency}'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        return data["conversion_rate"]
    else:
        print("Error:", data.get("error-type", "Tidak diketahui"))
        return None

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate:
        converted_amount = amount * rate
        print(f"{amount} {from_currency} sama dengan {converted_amount:.2f} {to_currency}")
    else:
        print("Gagal mendapatkan kurs. Pastikan kode mata uang benar dan API key valid.")

def main():
    print("Aplikasi Konverter Mata Uang")
    
    while True:
        from_currency = input("Masukkan kode mata uang awal (contoh: USD): ").upper()
        to_currency = input("Masukkan kode mata uang tujuan (contoh: IDR): ").upper()
        try:
            amount = float(input("Masukkan jumlah uang yang akan dikonversi: "))
            convert_currency(amount, from_currency, to_currency)
        except ValueError:
            print("Input jumlah tidak valid. Harap masukkan angka.")

        repeat = input("Ingin melakukan konversi lain? (y/n): ").lower()
        if repeat != 'y':
            print("Terima kasih telah menggunakan aplikasi konverter mata uang.")
            break

if __name__ == "__main__":
    main()
