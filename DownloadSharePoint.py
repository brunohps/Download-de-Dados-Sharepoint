import importlib.util
import subprocess
import sys
import os

def install(package):
    """Instala uma biblioteca via pip"""
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Lista de bibliotecas necessárias
libraries = ["office365-rest-python-client", "tqdm"]

# Verificar e instalar bibliotecas ausentes
for lib in libraries:
    if importlib.util.find_spec(lib) is None:
        print(f"A biblioteca '{lib}' não está instalada. Instalando...")
        install(lib)
        print(f"A biblioteca '{lib}' foi instalada com sucesso!")
        
if os.name == 'nt':
    os.system('cls')  # Comando para limpar a tela no Windows
else:
    os.system('clear')  # Comando para limpar a tela em sistemas Unix-like
        
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential
from office365.sharepoint.files.file import File
from office365.sharepoint.folders.folder import Folder
import os
import urllib.parse
from tqdm import tqdm

# Solicitar informações do usuário
site_url = input("Digite a URL do site do SharePoint: ")
client_id = input("Digite o ID do Cliente: ")
client_secret = input("Digite o Segredo do Cliente: ")
# Extrair a parte do URL após ".sharepoint.com" e adicionar "/Documentos Compartilhados"
parsed_url = urllib.parse.urlparse(site_url)
folder_url = parsed_url.path + "/Documentos Compartilhados"
folder_caminho = input("Digite o caminho da pasta que deseja baixar: ")
diretory_url = folder_url + "/" + folder_caminho


print(diretory_url)

item_name = input("Digite o nome da pasta ou arquivo que deseja baixar: ")
output_folder = input("Digite o caminho da pasta que deseja salvar: ")
app_principal = {
    'client_id': client_id,
    'client_secret': client_secret,
}

# Autenticação
credentials = ClientCredential(app_principal['client_id'], app_principal['client_secret'])
ctx = ClientContext(site_url).with_credentials(credentials)

# Obter a pasta
folder = ctx.web.get_folder_by_server_relative_url(diretory_url)
ctx.load(folder)
ctx.execute_query()

print("Baixando conteúdo de:", folder.properties["Name"])

# Função para baixar recursivamente arquivos de uma pasta
def download_files_from_folder(folder, output_folder):
    files = folder.files
    ctx.load(files)
    ctx.execute_query()

    for file in tqdm(files, desc="Baixando arquivos"):
        file_stream = File.open_binary(ctx, file.properties["ServerRelativeUrl"])
        with open(output_folder + "\\" + file.properties["Name"], "wb") as local_file:
            local_file.write(file_stream.content)
        tqdm.write("Arquivo '{}' baixado para: {}".format(file.properties["Name"], output_folder))

    # Recursivamente, baixar arquivos de todas as subpastas
    subfolders = folder.folders
    ctx.load(subfolders)
    ctx.execute_query()

    for subfolder in subfolders:
        subfolder_name = subfolder.properties["Name"]
        tqdm.write("Entrando na subpasta:", subfolder_name)
        # Criar a pasta no diretório de saída
        os.makedirs(output_folder + "\\" + subfolder_name, exist_ok=True)
        # Recursivamente, baixar arquivos da subpasta
        download_files_from_folder(subfolder, output_folder + "\\" + subfolder_name)

# Extrair apenas o nome da pasta alvo
item_name_parts = item_name.split("/")
target_folder_name = item_name_parts[-1]

# Verificar se o item é uma pasta
if folder.properties["Name"] == target_folder_name:
    print("Apenas a pasta '{}' será baixada.".format(target_folder_name))
    # Criar a pasta no diretório de saída
    os.makedirs(output_folder + "\\" + target_folder_name, exist_ok=True)
    # Baixar recursivamente arquivos da pasta
    download_files_from_folder(folder, output_folder + "\\" + target_folder_name)
else:
    # Verificar se o próximo item é uma pasta ou arquivo
    subfolders = folder.folders
    ctx.load(subfolders)
    ctx.execute_query()
        
    files = folder.files
    ctx.load(files)
    ctx.execute_query()

    # Verificar se o item foi encontrado
    if any(item.properties["Name"] == item_name for item in subfolders) or any(item.properties["Name"] == item_name for item in files):
        # Verificar se o item é uma pasta
        for subfolder in subfolders:
            if subfolder.properties["Name"] == target_folder_name:
                print("Apenas a pasta '{}' será baixada.".format(target_folder_name))
                # Criar a pasta no diretório de saída
                os.makedirs(output_folder + "\\" + target_folder_name, exist_ok=True)
                # Baixar recursivamente arquivos da subpasta
                download_files_from_folder(subfolder, output_folder + "\\" + target_folder_name)
                break
            # Verificar se o item é uma subpasta de TesteDownload
            elif subfolder.properties["Name"] == item_name_parts[0]:
                print("Entrando na subpasta:", subfolder.properties["Name"])
                # Criar a pasta no diretório de saída
                os.makedirs(output_folder + "\\" + subfolder.properties["Name"], exist_ok=True)
                # Recursivamente, baixar arquivos da subpasta
                download_files_from_folder(subfolder, output_folder + "\\" + subfolder.properties["Name"])
                break

        for file in tqdm(files, desc="Baixando arquivos"):
            if file.properties["Name"] == item_name:
                file_stream = File.open_binary(ctx, file.properties["ServerRelativeUrl"])
                with open(output_folder + "\\" + file.properties["Name"], "wb") as local_file:
                    local_file.write(file_stream.content)
                tqdm.write("Arquivo '{}' baixado para: {}".format(file.properties["Name"], output_folder))
                break
        else:
            print("Pasta '{}' não encontrada na pasta informada.".format(target_folder_name))

# Loop para permitir o download de mais pastas ou arquivos dentro do mesmo caminho informado
while True:
    continuar = input("Deseja baixar mais alguma pasta ou arquivo neste caminho? (s/n): ")
    if continuar.lower() == 'n':
        break
    elif continuar.lower() == 's':
        # Solicitar o nome da próxima pasta ou arquivo
        folder_caminho = input("Digite o caminho da pasta que deseja baixar: ")
        diretory_url = folder_url + "/" + folder_caminho

        # Obter a pasta
        folder = ctx.web.get_folder_by_server_relative_url(diretory_url)
        ctx.load(folder)
        ctx.execute_query()
        
        item_name = input("Digite o nome da próxima pasta ou arquivo que deseja baixar: ")

        # Verificar se o próximo item é uma pasta ou arquivo
        subfolders = folder.folders
        ctx.load(subfolders)
        ctx.execute_query()

        files = folder.files
        ctx.load(files)
        ctx.execute_query()

        # Verificar se o item foi encontrado
        if any(item.properties["Name"] == item_name for item in subfolders) or any(item.properties["Name"] == item_name for item in files):
            # Verificar se o item é uma pasta
            for subfolder in subfolders:
                if subfolder.properties["Name"] == item_name:
                    print("Apenas a pasta '{}' será baixada.".format(item_name))
                    
                    # Criar a pasta no diretório de saída
                    os.makedirs(output_folder + "\\" + item_name, exist_ok=True)
                    # Baixar recursivamente arquivos da pasta
                    download_files_from_folder(subfolder, output_folder + "\\" + item_name)
                    break
            # Verificar se o item é um arquivo
            for file in files:
                if file.properties["Name"] == item_name:
                    file_stream = File.open_binary(ctx, file.properties["ServerRelativeUrl"])
                    with open(output_folder + "\\" + file.properties["Name"], "wb") as local_file:
                        local_file.write(file_stream.content)
                    print("Arquivo '{}' baixado para: {}".format(file.properties["Name"], output_folder))
                    break
        else:
            print("Pasta ou arquivo '{}' não encontrado na pasta informada.".format(item_name))
