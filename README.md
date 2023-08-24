# Search_Engine_TF_IDF
Repo que contém o básico senão o necessário para substituir o Elastic Search para uma versão mais flexível de busca.

## Como calcular o TF-IDF:
Existem 3 termos que são importantes na área do NLP:
- Term Frequency (TF): Que diz a frequência de um termo em relação ao documento inteiro.
- Document Frequency (DF): Que é a frequência de um termo de um documento em específico.
- Inverse Document Frequency (IDF): Esse é o valor que alcançamos ao calcular DF com a fórmula:
>>> IDF = LOG[(#N od doc) / (#N of doc containing the word (DF))]

## Matemática Aplicada à Texto:
> Usando o TF-IDF (Term-Frequency + Inverse Document Frequency), nós podemos conseguir o peso de cada palavra em relação ao documento inteiro (que se houver um DB, então ao records do banco de dados passados). Esses pesos então serão computados como 'score' e a fórmula para tal é,
>>> SCORE = TF * IDF

## Nomeando os arquivos:
- /teste : Pasta que contém os testes para ambos os arquivos (ft_dt.py e query.py).
- ft_dt.py : Extrai as palavras e aplicada a lógica matemática.
- query.py : recebe o json do ft_dt com as respostas e sorteia por score o resultado final.
- main.py : arquivo principal, ou administrador dos métodos.

## Links e Fontes:
- https://pt.wikipedia.org/wiki/Tf%E2%80%93idf
- https://youtu.be/zLMEnNbdh4Q

## Resultado:
- Qual é o max_results? 3
- Qual é a palavra? fonte de dados
![image](https://github.com/Ingrid-0906/Search_Engine_TF_IDF/assets/92744210/51befacb-e454-4b4f-9ca2-7fa520cab3f7)
