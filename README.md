# API Pokewordle
> é basicamente uma cópia do pokewordle, só que pior.............. por enquanto................

## tecnologias usadas

Python
PostgreSQL
FastAPI
[Pokebase](https://github.com/PokeAPI/pokebase) / [PokéAPI](https://pokeapi.co/)

## "instalação"

1. clona o repositório
```bash
git clone essa-url
cd api-pokewordle
```

2. cria o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate
```

3. pega as dependencias
```bash
pip install -r requirements.txt
```

4. configura o .env com a sua conexao postgres
```bash
DATABASE_URL=postgresql://usuario:senha@localhost:5432/bando_de_dados
```

5. cria o banco de dados no seu postgres
```sql
CREATE DATABASE cardume_de_dados;
```

6. roda isso e parabéns a api vai estar rodando
```bash
python run.py
```

## endpoints em questão

1. sorteio de pokémon
envie uma requisição post vazia para POST http://127.0.0.1:8000/pkmn/sorteia

2. faça seu chute
envie uma requisição post com o nome de um pokémon para POST http://127.0.0.1:8000/pkmn/chute/{nome}

## versões

* 0.0.1
    * primeiro commit olha que legal