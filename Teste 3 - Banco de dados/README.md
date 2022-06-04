Para esse teste eu achei que seria interessante fazer uma "limpeza" nos arquivos antes de importalos para o mysql
Visto que para o problema so precisava analisar especificamente uma descrição
Entao limpei o arquivo csv de ambos os anos retirando somente as linhas necessaria para a resolução do desafio
Isso diminui o total de linha de mais de 600 mil para um pouco mais de 8 mil linhas.
Otimizando assim, o carregamento dos dados e das consultas.
Ajudando tambem a simplificar minha consulta, já que nao precisaria fazer mais uso da condição da descrição "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR"
Basta inicializar o banco e rodar as 4 querys de consultas para receber os resultados:
Sendo elas, As 10 empresas que mais gastaram com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no ano de 2020
As 10 empresas que mais gastaram com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no ano de 2021
As 10 empresas que mais gastaram com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no ultimo trimestre do ano de 2021
As 10 empresas que mais gastaram com "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS  DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no ultimo trimestre do ano de 2020
O programa que fiz para limpar os arquivos tambem se encontra na pasta com o nome de 'File_cleaner.py'