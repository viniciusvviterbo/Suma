# Suma

Cria resumos de textos com suas frases chave.

### Instalando Dependências

Clone esse repositório e execute:
```
pip3 install nltk beautifulsoup4 lxml
```
Para o correto funcionamento da biblioteca NLTK, execute:
```
python3
import nltk
nltk.download()
```
Em seguida, selecione a opção de download e instale os seguintes pacotes:
- averaged_perceptron_tagger
- floresta
- mac_morpho
- machado
- punkt
- stopwords
- wordnet
- words

### Uso

```
python3 Suma.py [-h] -f ARQUIVO_DE_TEXTO -n NÚMERO_DE_FRASES_DO_RESUMO
```

Informe o arquivo de texto (extensão '.txt') com o conteúdo que pretende resumir.

Exemplo:
```
python3 Suma.py -h
```

```
python3 Suma.py -f './texto.txt' -n 3
```

Inspirado [nesse artigo](https://medium.com/@viniljf/utilizando-processamento-de-linguagem-natural-para-criar-um-sumariza%C3%A7%C3%A3o-autom%C3%A1tica-de-textos-775cb428c84e)

**[GNU AGPL v3.0](https://www.gnu.org/licenses/agpl-3.0.html)**
