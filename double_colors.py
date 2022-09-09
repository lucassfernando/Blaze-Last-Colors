import json
from time import sleep
import requests



def start_last_colors():

    try:

        while True:

            URL_LINK_BLAZE = 'https://blaze.com/api/roulette_games/recent'

            information = requests.get(URL_LINK_BLAZE)

            if information.status_code == 200:

                results_colors = json.loads(information.text)

                color, roll, server_seed = results_colors[0]['color'], results_colors[0]['roll'], results_colors[0]['server_seed']
                
                ''' 0 = WHITE
                    1 = RED
                    2 = BLACK '''
                    
                if color == 0:
                    color = 'WHITE'

                elif color == 1:
                    color = 'RED'

                else:
                    color = 'BLACK'

                if server_seed not in list_server_seed:

                    print(f"COLOR: {color} | ROLL: {roll}")
                    list_server_seed.append(server_seed)
                    sleep(20)

                else:
                    continue
            
            else:
                continue

    except Exception as error:

        with open('ERROR_LOG.txt', 'a') as error_log:
            error_log.writelines(f"ERRO: {error} | STATUS CODE: {information.status_code} ")

list_server_seed = []
start_last_colors()