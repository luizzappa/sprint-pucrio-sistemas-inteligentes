# Backend: Pinguins de palmer

Esse é o projeto de backend do MVP da pós-gradução de Engenharia de Software da PUC-Rio. Ele foi desenvolvido em flask e tem por objetivo expor uma rest API que possui um modelo embarcado que realizará a predição da espécie de um pinguim com base nas características fornecidas.

## Instalação

Primeiramente faz-se necessária a instalação das bibliotecas utilizadas

```bash
pip install -r requirements.txt
```

## Execução

Após a instalação, o projeto pode ser iniciado com o comando abaixo:

```bash
flask --app app run
```

## Testes automatizados

Para execução dos testes automatizados que asseguram que o modelo atenda os requisitos de desempenho, execute o comando:

```bash
pytest -v test_modelo.py
```
