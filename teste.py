import urllib.request
import json

url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=ef5d9fe14bd68061311051bc1554074e"

try:
    resposta = urllib.request.urlopen(url)
    dados = json.load(resposta)
    
    for filme in dados['results'][:10]:
        titulo = filme['title']
        popularidade = filme['popularity']
        data_lancamento = filme['release_date']
        print(f"Título: {titulo}, Popularidade: {popularidade}, Data de Lançamento: {data_lancamento}")
except Exception as e:
    print(f"Erro ao acessar a API: {e}")
