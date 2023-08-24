import datetime
import ft_dt
import query


if __name__ == "__main__":
    # Salvando um backup // Pode trocar por outro método de organização
    data_atual = datetime.date.today()
    file_saved = f'{data_atual}_backup'
    
    # Chamando o primeiro script
    freq = ft_dt.SearchEngine('../search_engine/dados.json', file_saved)
    freq.process_data()
    freq.save_result()
    
    # Será necessário procurar o caminho para enviar como 'index_file_path', no caso, uma chamada ao banco de dados
    index_file_path = file_saved
    
    # Inputs para definir os paramentros da busca
    max_results = input('Qual é o max_results?')
    query_keywords = input("Qual é a palavra?")
    
    # Chamando o segundo script
    query = query.Query(index_file_path, max_results, query_keywords)
    query.process_index()
    query.display_results()
    
    