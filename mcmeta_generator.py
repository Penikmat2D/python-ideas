import json

def generate_pack_mcmeta(pack_format, description):
  mcmeta = {
    "pack": {
      "pack_format": pack_format,
      "description": description
    }
  }
  with open("pack.mcmeta", "w") as file:
    json.dump(mcmeta, file, indent=4)
    print("File pack.mcmeta telah berhasil dibuat")

try:
  pack_format: int(input("Masukkan kode paket sesuai versi MC yang diinginkan: "))
  description: input("Masukkan deskripsi paket sumber daya anda: ")

  generate_pack_mcmeta(pack_format, description)
except ValueError:
  print("Input pack_format harus berupa angka")
