# Comandos internos do Databricks

| Comando | Definição |
| ------ | ------ |
| %fs help | Acessa o comando HELP |
| %fs ls / | Lista as pasta |
| dbutils.fs.ls("/) | Lista as pastas |
| %fs mkdirs name | Cria uma nova pasta chamada name |
| %fs ls /FileStore/ | Mostra as pastas no dir /FireStore/ |
| %fs cp /FireStore/tables/path/arquivo /FireStore/path_dir/copia_arquivo | Copia um arquivo de uma pasta para outra |
| %fs mv /FileStore/path/arquivo /FireStore/path/arquivo2 | Renomear um arquivo |
| %fs rm /FileStore/path/arquivo | Remove o arquivo |
| fs rm -r /FileStore/path/ | Remove uma pasta |
| [%%bash find /path - name "*.csv | grep 'fai*.*'] | Realiza uma busca na pasta /path por arquivos .csv |
