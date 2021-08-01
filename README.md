## tutorial para rodar o projeto

## pré-requisitos para rodar o código
- versões do python: 3.6, 3.7, 3.8
- tqdm
- stable_baselines
- gym-retro
- tensorflow
- ffmpeg

## comandos para instalação
- pip install tensorflow
- pip install stable_baselines
- pip install tqdm
- pip install gym-retro

## passo a passo para instalar a ROM do Street Fighter 2
- extraia o arquivo zip StreetFighterIISpecialChampionEdition-Genesis.zip
- copie os arquivos da pasta extraida
- cole dentro do diretório : C:\Users\{SEU USUARIO}\AppData\Local\Programs\Python\Python38\Lib\site-packages\retro\data\stable\StreetFighterIISpecialChampionEdition-Genesis
- navegue até a pasta raiz do projeto e digite o seguinte comando : "python -m retro.import StreetFighterIISpecialChampionEdition-Genesis"

## passo a passo para instalar o ffmpeg

- link para tutorial de instalação : https://pt.wikihow.com/Instalar-o-FFmpeg-no-Windows

## como rodar o código
- dentro do diretório do projeto, digite no terminal "python play.py"
- OBS: o resultado do treinamento vai vir como um documento com a extensão .bk2

## como visualizar o resultado gerado
- dentro do diretório do projeto, digite no terminal "python3 -m retro.scripts.playback_movie nomeDoArquivo-000000.bk2"
- fazendo o que foi pedido na linha acima, vai ser gerado um arquivo MP4 de uma luta da IA contra a máquina. O arquivo tem o mesmo nome do arquivo .BK2
