from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.client_credential import ClientCredential
from office365.sharepoint.files.file import File

site_url = 'https://predilectacombr.sharepoint.com/sites/DadosT.I-PREDILECTA'
app_principal = {
    'client_id': 'ba282d4d-1330-4b5b-85f7-444d6ef6442f',
    'client_secret': 'a+njfWzLO3QSmV1gD95abXW3J8pmyU0bjzmLdNRKhFA=',
}

output_folder = "C:\\INFO\\"

# Autenticação
credentials = ClientCredential(app_principal['client_id'], app_principal['client_secret'])
ctx = ClientContext(site_url).with_credentials(credentials)

# Carregar a pasta no SharePoint
folder_url = "/sites/DadosT.I-PREDILECTA/Documentos Compartilhados/TesteDownload"
folder = ctx.web.get_folder_by_server_relative_url(folder_url)
ctx.load(folder)
ctx.execute_query()

# Listar os arquivos na pasta
files = folder.files
ctx.load(files)
ctx.execute_query()

# Baixar cada arquivo para o diretório local
for file in files:
    file_name = file.properties["Name"]
    file_stream = File.open_binary(ctx, file.properties["ServerRelativeUrl"])
    with open(output_folder + file_name, "wb") as local_file:
        local_file.write(file_stream.content)

print("Pasta 'TesteDownload' baixada para: " + output_folder)
