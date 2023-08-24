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

## Links e Fontes:
- https://pt.wikipedia.org/wiki/Tf%E2%80%93idf
- https://youtu.be/zLMEnNbdh4Q
