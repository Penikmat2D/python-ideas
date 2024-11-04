import sys

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb_color):
    return "#{:02x}{:02x}{:02x}".format(rgb_color[0], rgb_color[1], rgb_color[2])

while True:
    print("Pilih konversi: ")
    print("1. Hex ke RGB")
    print("2. RGB ke Hex")
    print("3. Keluar")
    choice = input("(1/2/3): ").strip().lower()

    if choice == "1":
        hex_color = input("Masukkan warna hex (misalnya #1abc9c): ")
        rgb_result = hex_to_rgb(hex_color)
        print(f"Hex #{hex_color} ke RGB: {rgb_result}")

    elif choice == "2":
        try:
            r = int(input("Masukkan nilai Red: "))
            g = int(input("Masukkan nilai Green: "))
            b = int(input("Masukkan nilai Blue: "))
            rgb_color = (r, g, b)
            hex_result =  rgb_to_hex(rgb_color)
            print(f"RGB {rgb_color} ke Hex: {hex_result}")
        except ValueError:
            print("Nilai tidak valid")

    elif choice == "3":
        print("Program selesai")
        sys.exit(0)

    else:
        print("Pilihan tidak valid")
