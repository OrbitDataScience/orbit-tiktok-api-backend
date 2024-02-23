import pandas as pd
import requests
import json
import csv
from datetime import datetime

# Converte o timestamp do epoch para o formato de data e hora.
def converte_para_data(epoch_timestamp):
    date_time = datetime.fromtimestamp(epoch_timestamp)
    formatted_date = date_time.strftime('%d-%m-%Y %H:%M:%S')  # Formato: YYYY-MM-DD HH:MM:SS
    
    return formatted_date

def salvar_csv(dados, nome_arquivo):
    # Converter o dicionário para DataFrame
    df = pd.DataFrame.from_dict(dados, orient='index')

    # Salvar o DataFrame em um arquivo CSV
    df.to_csv(nome_arquivo + '.csv', sep=';', index_label='Video')

# Busca as postagens do TikTok com base nos filtros
def search_tiktok(keyword, region, sort, count, dataPostagem):
    headers = {
        "X-RapidAPI-Key": "88b5804da0mshaec086ad3147560p16ac64jsn608ec3c7f56c",
        "X-RapidAPI-Host": "tiktok-video-no-watermark10.p.rapidapi.com"
    }

    # Inicializa a variável de controle do loop e o cursor para a paginação da API.
    has_more = True
    cursor = "0"

    # Lista para armazenar os dados coletados de cada resposta da API.
    responses_list = []
    # Loop continua enquanto houver mais páginas de dados a serem coletadas.
    while has_more:

        url = "https://tiktok-video-no-watermark10.p.rapidapi.com/index/Tiktok/searchVideoListByKeywords"
        querystring = {"keywords":keyword,"cursor":cursor,"region":region,"publish_time":dataPostagem,"count":count,"sort_type":sort}

        response = requests.get(url, headers=headers, params=querystring)
        json_response = response.json()
       
        # Adiciona os dados da resposta atual à lista de todas as respostas.
        responses_list.append(json_response['data'])

        # Atualiza a variável 'has_more' com o valor correspondente da resposta para determinar se há mais páginas a serem solicitadas.
        has_more = json_response['data']['hasMore']
        # Atualiza o cursor com o valor correspondente da resposta para a próxima paginação.
        cursor = json_response['data']['cursor']

    # Calcula o número de páginas de dados coletados.
    pages = cursor // 30

    return filtrar_json(responses_list, pages)

# Filtra os dados coletados da API do TikTok e salva em um arquivo CSV.
def filtrar_json(dados_json, pages):
        count = 0
        info = {}

        # Loop para percorrer cada página de dados.
        for i in range(pages):
            # Loop para percorrer cada vídeo da página atual.
            for video in dados_json[i]['videos']:
                nickname = video['author']['nickname'].replace(" ", "")
                code_video = video['video_id']
                link = f'https://www.tiktok.com/@{nickname}/video/{code_video}'
                visualizations = video['play_count']
                like = video['digg_count']
                downloads = video['download_count']
                comments = video['comment_count']
                shares = video['share_count']
                id_user = video['author']['id']
                region = video['region']
                time = video['create_time']
                title = video['title']
                # Adiciona os dados do vídeo atual ao dicionário 'info'.
                info[f'Vídeo: {count}'] = {
                    'Link' : link,
                    'Visualizações' : visualizations,
                    'Curtidas' : like,
                    'Comentários' : comments,
                    'Downloads' : downloads,
                    'Compartilhamentos' : shares,
                    'Data' : converte_para_data(time),
                    'ID Usuário' : id_user,
                    'Região' : region,
                    'Título' : title
                    }

                count += 1
        # Salva os dados coletados em um arquivo CSV.
        salvar_csv(info, 'tiktok_data')

        return info
