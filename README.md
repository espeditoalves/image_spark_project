- [image\_spark\_project](#image_spark_project)
  - [Tools used in this project](#tools-used-in-this-project)
  - [Project Structure](#project-structure)
- [Iniciando o docker nesse repositório:](#iniciando-o-docker-nesse-repositório)
  - [lista os containers:](#lista-os-containers)
  - [Iniciar o Contêiner Nomeando-o:](#iniciar-o-contêiner-nomeando-o)
  - [Reiniciar o Contêiner Existente:](#reiniciar-o-contêiner-existente)
  - [Iniciar jupyter notebook](#iniciar-jupyter-notebook)
- [Dentro do Docker: Ambiente do jupyter notebook web](#dentro-do-docker-ambiente-do-jupyter-notebook-web)
  - [Verificar os Kernels Disponíveis:](#verificar-os-kernels-disponíveis)
  - [Instalador do poetry](#instalador-do-poetry)
  - [ignorar o pacote raiz:](#ignorar-o-pacote-raiz)
  - [Instalar o Kernel do Poetry:](#instalar-o-kernel-do-poetry)
  - [Ativar o Ambiente virtual do poetry](#ativar-o-ambiente-virtual-do-poetry)
    - [Adicionar o Kernel do Poetry ao Jupyter:](#adicionar-o-kernel-do-poetry-ao-jupyter)

# image_spark_project

## Tools used in this project
* [hydra](https://hydra.cc/): Manage configuration files - [article](https://mathdatasimplified.com/stop-hard-coding-in-a-data-science-project-use-configuration-files-instead/)
* [pdoc](https://github.com/pdoc3/pdoc): Automatically create an API documentation for your project
* [pre-commit plugins](https://pre-commit.com/): Automate code reviewing formatting

* [Poetry](https://towardsdatascience.com/how-to-effortlessly-publish-your-python-package-to-pypi-using-poetry-44b305362f9f): Dependency management - [article](https://mathdatasimplified.com/poetry-a-better-way-to-manage-python-dependencies/)


## Project Structure

```bash
.
├── config                      
│   ├── main.yaml                   # Main configuration file
│   ├── model                       # Configurations for training model
│   │   ├── model1.yaml             # First variation of parameters to train model
│   │   └── model2.yaml             # Second variation of parameters to train model
│   └── process                     # Configurations for processing data
│       ├── process1.yaml           # First variation of parameters to process data
│       └── process2.yaml           # Second variation of parameters to process data
├── data            
│   ├── final                       # data after training the model
│   ├── processed                   # data after processing
│   └── raw                         # raw data
├── docs                            # documentation for your project
├── .gitignore                      # ignore files that cannot commit to Git
├── Makefile                        # store useful commands to set up the environment
├── models                          # store models
├── notebooks                       # store notebooks
│   ├── exploration
│   │   └── .gitkeep
│   ├── modeling
│   │   └── .gitkeep
│   ├── preprocessing
│   │   └── .gitkeep
│   └── reporting
│       └── .gitkeep
├── output                          # store outputs
│   ├── figures
│   │   └── .gitkeep
│   ├── predictions
│   │   └── .gitkeep
│   └── reports
│       └── .gitkeep
├── .pre-commit-config.yaml         # configurations for pre-commit
├── pyproject.toml                  # dependencies for poetry
├── README.md                       # describe your project
├── src                             # store source code
│   ├── __init__.py                 # make src a Python module 
│   ├── process.py                  # process data before training model
│   ├── train_model.py              # train model
│   └── utils.py                    # store helper functions
└── tests                           # store tests
    ├── __init__.py                 # make tests a Python module 
    ├── test_process.py             # test functions for process.py
    └── test_train_model.py         # test functions for train_model.py
```

# Iniciando o docker nesse repositório:

> SEM INICIAR O DOCKER DESCKTOP MANUALMENTE

**Em seguinda posso fazer o código abaixo ou o código renomeando o container.**

```bash
docker run -p 8888:8888 -v C:\Users\esped\Documents\Respositorio_git\Repositorio_projetos\image_spark_project:/home/jovyan/work jupyter/pyspark-notebook:spark-3.3.2
```

## lista os containers:

```bash 
docker ps
```

## Iniciar o Contêiner Nomeando-o:
```bash
docker run -p 8888:8888 -v /caminho/local/do/seu/projeto:/home/jovyan/work --name meu_container_base jupyter/pyspark-notebook:spark-3.3.2
```
Fazendo esse processo acima eu não preciso apagar o conteiner em execução e quando eu abrir o computador eu simplesmente uso os comandos abaixo para iniciar o container

## Reiniciar o Contêiner Existente:
```bash
docker start meu_container_base
docker attach meu_container_base
```

- Será necessário abrir terminal dentro do container: 
```bash
docker exec -it meu_container_base bash
```
## Iniciar jupyter notebook

```bash
jupyter notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

> Após esse processo irá surgir alguns logs com um link para abrir o jupyter notebook no navegador.

# Dentro do Docker: Ambiente do jupyter notebook web

No terminal do jupyter notebook web:

## Verificar os Kernels Disponíveis:
```bash
jupyter kernelspec list
```
## Instalador do poetry

[Poetry](https://python-poetry.org/docs/#installing-with-pipx)

## ignorar o pacote raiz:
Desativa o empacotamento do projeto, utilizando o Poetry apenas para gerenciamento de dependências

```bash
poetry install --no-root
```

## Instalar o Kernel do Poetry:
```bash
poetry add ipykernel
```

## Ativar o Ambiente virtual do poetry

```bash
poetry shell
```

### Adicionar o Kernel do Poetry ao Jupyter:

Após instalar o ipykernel no ambiente virtual do Poetry, você pode adicionar o kernel do Poetry ao Jupyter Notebook com o seguinte comando:

```bash
python -m ipykernel install --user --name=image-spark-project-py3.10 --display-name "Python (Poetry)"
```

* `--name=image-spark-project-py3.10`: Especifique o nome do ambiente virtual do Poetry que você deseja usar como base para o kernel.
* `--display-name "Python (Poetry)"`: Especifique o nome que deseja que apareça na lista de kernels do Jupyter Notebook.
Selecionar o Kernel do Poetry no Jupyter Notebook:
Depois de adicionar o kernel, você pode selecioná-lo ao criar um novo notebook ou alterar o kernel de um notebook existente:

Crie um novo notebook ou abra um notebook existente.
Vá para o menu **"Kernel"** e selecione **"Change Kernel"**.
Selecione **"Python (Poetry)"** ou o nome que você especificou ao adicionar o kernel do Poetry.

Agora, o notebook estará utilizando o kernel associado ao ambiente virtual do Poetry, garantindo que todas as dependências do seu projeto sejam utilizadas corretamente.

Esses passos devem ajudar a configurar e usar o kernel do Poetry no Jupyter Notebook dentro do seu ambiente Docker, garantindo que você esteja trabalhando com as dependências corretas do seu projeto.
