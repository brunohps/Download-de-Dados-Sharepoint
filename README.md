# PT-Br
# Download de Dados Sharepoint
Script Python que faz downloads dos repósitórios salvos no sharepoint

### Requisitos:
#### - Python;
#### - Credenciais do seu site:ID do Cliente (Site Sharepoint) / Segredo do Cliente (Site SharePoint).

🔗Download Python: https://www.python.org/downloads/

🔗Download Script: https://github.com/brunohps/Download-de-Dados-Sharepoint/blob/main/DownloadSharePoint.py

# ID do Cliente | Segredo do Cliente

## Passo 1 — Gere credenciais do seu site SharePoint

Antes de começarmos a obter arquivos do SharePoint, precisamos gerar as credenciais necessárias do seu site do SharePoint. Essas credenciais nos permitirão autenticar e acessar o SharePoint de forma programática.

Faça login no seu site do SharePoint com privilégios administrativos.
Navegue até a página de registro do aplicativo SharePoint. Normalmente, você pode simplesmente adicionar `/_layouts/15/appregnew.aspx`  após o nome do seu site no URL.

Por exemplo: 
`https://{instance}.sharepoint.com/sites/{sitename}/_layouts/15/appregnew.aspx`

### Crie um novo registro de aplicativo.
Esta etapa pode variar um pouco dependendo da versão e configuração do SharePoint. Siga as ações no instantâneo abaixo e armazene o ID do cliente e o segredo do cliente em um local seguro.

![git_credencial](https://github.com/brunohps/Download-de-Dados-Sharepoint/assets/52177106/2e7be3d1-a083-483e-a3b2-f85ba964d8e7)

![image](https://github.com/brunohps/Download-de-Dados-Sharepoint/assets/52177106/cc8055c2-4a12-4a0e-b26a-566cc999aa94)

Depois que o aplicativo for criado, navegue até a página de configurações do aplicativo para conceder permissões. Normalmente, o URL é a página do site com `/_layouts/15/appinv.aspx`.
Por exemplo: 

`https://{instance}.sharepoint.com/sites/{sitename}/_layouts/15/appinv.aspx`

- Primeiramente, preencha o "`Id do Aplicativo:`" (ou seja, o Client id que você acabou de gerar na página de registro do aplicativo).
- Clique na parte inferior de pesquisa ao lado da caixa de texto e todas as informações, incluindo “Título”, “Domínio do aplicativo” e “URL de redirecionamento” serão preenchidas automaticamente se o ID do aplicativo puder ser encontrado.
- Cole o texto abaixo em `XML de solicitação de permissão:`. Por último, clique em Criar para conceder a permissão.

```bash
<AppPermissionRequests AllowAppOnlyPolicy="true">
<AppPermissionRequest Scope="http://sharepoint/content/sitecollection" Right="FullControl"/>
</AppPermissionRequests>
```
![git_credencial_app](https://github.com/brunohps/Download-de-Dados-Sharepoint/assets/52177106/315a28f4-7fcd-4bf6-9fd1-90efe7e07c3f)

```bash
<!-- Para o escopo em nível de locatário, o XML de solicitação de permissão tem a seguinte aparência: --> 

<AppPermissionRequests AllowAppOnlyPolicy="true">
<AppPermissionRequest Scope="http://sharepoint/content/tenant" Right="FullControl"/>
</AppPermissionRequests>
```
![git_confiar_credencial](https://github.com/brunohps/Download-de-Dados-Sharepoint/assets/52177106/b7a718e6-405e-42f6-b7a3-41987889fe00)

Após tudo configurado, basta executar o script `DownloadSharePoint.py`  e preencher os campos solicitados.

🚨🚨🚨 Por padrão o script está mapeando inicialmente a pasta `Documentos Compartilhados`, então quando solicitado o caminho da pasta que deseja baixar, deve usa o caminho a partir da pasta `Documentos Compartilhados`.

#### Exemplo: se a pasta estiver em `Documentos\TesteDownload\pasta2`. 
![image](https://github.com/brunohps/Download-de-Dados-Sharepoint/assets/52177106/46019105-b1dd-4d9f-ac36-83e189a4d760)

Deve-se informar apenas `TesteDownload\pasta2` quando solicitado o caminho da pasta que deseja baixar.

```bash
Digite a URL do site do SharePoint: https://{instance}.sharepoint.com/sites/{sitename}
Digite o ID do Cliente: 058******************************
Digite o Segredo do Cliente: bslqiT**********************************
Digite o caminho da pasta que deseja baixar: TesteDownload\pasta2

Digite o nome da pasta ou arquivo que deseja baixar: teste_diretory1
Digite o caminho da pasta que deseja salvar: c:/info
Baixando conteúdo de: pasta2
Apenas a pasta 'teste_diretory1' será baixada.
```

__________________________________________________________________________________________________________
#EN-Us
# Download Sharepoint Data
Python script that downloads from repositories saved in sharepoint

### Requirements:
#### - Python;
#### - Credentials for your site: Client ID (Sharepoint Website) / Client Secret (SharePoint Website).

🔗Download Python: https://www.python.org/downloads/

🔗Download script: https://github.com/brunohps/Download-de-Dados-Sharepoint/blob/main/DownloadSharePoint.py

# Customer ID | Customer Secret

## Step 1 — Generate credentials for your SharePoint site

Before we start getting files from SharePoint, we need to generate your SharePoint site credentials. These credentials will not allow you to authenticate and access SharePoint programmatically.

Log in to your SharePoint site with administrative privileges.
Navigate to the SharePoint app registration page. Typically, you can simply add `/_layouts/15/appregnew.aspx` after your site name in the URL.

For example:
`https://{instance}.sharepoint.com/sites/{sitename}/_layouts/15/appregnew.aspx`

### Create a new application registration.
This step may vary slightly depending on your SharePoint version and configuration. Follow the actions in the snapshot below and store the client ID and client secret in a secure location.

![git_credencial](https://github.com/brunohps/Download-de-Dados-Sharepoint/assets/52177106/2e7be3d1-a083-483e-a3b2-f85ba964d8e7)

![image](https://github.com/brunohps/Download-de-Dados-Sharepoint/assets/52177106/cc8055c2-4a12-4a0e-b26a-566cc999aa94)

Once the app is created, navigate to the app's settings page to grant permissions. Typically, the URL is a website page with `/_layouts/15/appinv.aspx`.
For example:

`https://{instance}.sharepoint.com/sites/{sitename}/_layouts/15/appinv.aspx`

- First, fill in the "`Application Id:`" (that is, the Client id you just generated on the application registration page).
- Click the bottom of the search next to the text box and all information including “Title”, “App Domain” and “Redirect URL” will be automatically filled in if the App ID can be found.
- Paste the text below into `Permission request XML:`. Lastly, click Create to grant the permission.

```bash
<AppPermissionRequests AllowAppOnlyPolicy="true">
<AppPermissionRequest Scope="http://sharepoint/content/sitecollection" Right="FullControl"/>
</AppPermissionRequests>
```
![git_credencial_app](https://github.com/brunohps/Download-de-Dados-Sharepoint/assets/52177106/315a28f4-7fcd-4bf6-9fd1-90efe7e07c3f)

```bash
<!-- For tenant-level scope, the permission request XML looks like this: -->

<AppPermissionRequests AllowAppOnlyPolicy="true">
<AppPermissionRequest Scope="http://sharepoint/content/tenant" Right="FullControl"/>
</AppPermissionRequests>
```
![git_confiar_credencial](https://github.com/brunohps/Download-de-Dados-Sharepoint/assets/52177106/b7a718e6-405e-42f6-b7a3-41987889fe00)

After everything is configured, simply run the `DownloadSharePoint.py` script and fill in the requested fields.

🚨🚨🚨 By default the script is initially mapping the `Shared Documents` folder, so when asked for the path of the folder you want to download, you must use the path from the `Shared Documents` folder.

#### Example: if the folder is in `Documents\TesteDownload\folder2`.
![image](https://github.com/brunohps/Download-de-Dados-Sharepoint/assets/52177106/46019105-b1dd-4d9f-ac36-83e189a4d760)

You should only enter `TesteDownload\pasta2` when asked for the path of the folder you want to download.

```bash
Digite a URL do site do SharePoint: https://{instance}.sharepoint.com/sites/{sitename}
Digite o ID do Cliente: 058******************************
Digite o Segredo do Cliente: bslqiT**********************************
Digite o caminho da pasta que deseja baixar: TesteDownload\pasta2

Digite o nome da pasta ou arquivo que deseja baixar: teste_diretory1
Digite o caminho da pasta que deseja salvar: c:/info
Baixando conteúdo de: pasta2
Apenas a pasta 'teste_diretory1' será baixada.
```
