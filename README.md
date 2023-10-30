# Raspando Dados Da Internet Com Python
## Python Brasil 2023 - 31 / 10 / 2023

## Sobre o tutorial

A informação é abundante e está facilmente disponível na Internet. No entanto, a enorme quantidade de dados pode
ser esmagadora e demorada para navegar. É aí que entra a raspagem de dados - uma ferramenta poderosa usada para
extrair dados de sites e transformá-los em um formato utilizável.

Neste tutorial, exploraremos os fundamentos de raspagem de dados e como implementá-los usando Scrapy (um
framework Python). Quer você seja um analista de dados, programador ou pesquisador, este tutorial irá
equipá-lo com as habilidades fundamentais necessárias para criar seu próprio raspador e extrair informações
valiosas de sites.

## Antes do tutorial

Clone este repositório para ter acesso à apresentação e também à solução do código dos exercícios sugeridos:
[https://github.com/rennerocha/pybr2023-tutorial](https://github.com/rennerocha/pybr2023-tutorial)

Durante o tutorial espera-se que você tente resolver alguns pequenos exercícios usando
[Scrapy](https://scrapy.org), um framework de web scraping. Será a única biblioteca necessária para ser instalada
(quaisquer outras dependências deverão ser instaladas junto com ela).

Siga o [guia de instalação do Scrapy](https://docs.scrapy.org/en/latest/intro/install.html) de acordo com sua
plataforma e certifique-se de que você consegue executar a `versão do scrapy` em seu terminal e veja
`Scrapy 2.11.0` como resultado (sem erros).

Na plataforma Linux sugiro a utilização de um ambiente virtual. Se tudo estiver certo, só será necessário executar alguns
comandos para ter tudo funcionando e pronto para utilização:

```
$ git clone https://github.com/rennerocha/pybr2023-tutorial.git tutorial
$ cd tutorial
$ python3 -m venv .venv
$ source .venv/bin/activate
$ cd code
$ python -m pip install -r requirements
```

Em outras plataformas, siga a documentação oficial do Scrapy com o [guia de instatlação](https://docs.scrapy.org/en/latest/intro/install.html)
