from astropy.io import fits

# Caminho para o arquivo FITS
file_path = '/home/meteoro/Documentos/treinoM104/master_flat.fits'

# Abrir o arquivo FITS
with fits.open(file_path) as hdu_list:
    # Exibir informações sobre os HDUs (Header Data Units)
    hdu_list.info()

    # Acessar o cabeçalho da primeira HDU
    header = hdu_list[0].header
    print("\nCabeçalho da Primeira HDU:")
    for key in header.keys():
        print(f"{key}: {header[key]}")

    # Acessar os dados da imagem da primeira HDU
    image_data = hdu_list[0].data
    print("\nDados da Imagem:")
    print(type(image_data))  # Exibir o tipo de image_data
    print(image_data.shape)  # Exibir a forma dos dados da imagem

    # Modificar o cabeçalho
    #header['OBJECT'] = "EUSGURI"  # Atualizar o valor da chave OBJECT
    #header['RA'] =     
    #header['DEC'] = 
    #header['OBJCTRA'] =
    #header['OBJCTDEC'] =
    #header['RADECSRC'] = "site com informacao do objeto ra e dec"
    #header['EXPTIME'] = 15
    #header['IMAGETYP'] = 'LIGHT'
    #header['FILTER'] = 'v'
    #header['NAXIS1'] = 775
    
         
# Escrever os dados e o cabeçalho em um novo arquivo FITS
output_file = '/home/meteoro/Documentos/treinoM104/master_flat.fits'
fits.writeto(output_file, image_data, header, overwrite=True)

print(f"\nArquivo FITS atualizado salvo como: {output_file}")
