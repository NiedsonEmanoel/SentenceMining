# -*- coding: utf-8 -*-
"""Gerador de Flashcards com Foco em Vocabulário e Sentenças."""

# Importação de bibliotecas
from gtts import gTTS
from collections import Counter
import re
import genanki
import pronouncing
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from deep_translator import GoogleTranslator
from gruut import sentences

# Configuração inicial
nltk.download('stopwords')  # Baixar stopwords do NLTK, caso necessário
tradutor = GoogleTranslator(source="en", target="pt")  # Tradutor Inglês -> Português

# Modelo Anki para os flashcards
modelo = genanki.Model(
    1234567890,  # ID único do modelo
    'Modelo Português-Inglês',
    fields=[
        {'name': 'PalavraEmPortugues'},
        {'name': 'PalavraEmIngles'},
        {'name': 'Pronuncia'},
        {'name': 'IPA'},
        {'name': 'Audio'},
    ],
    templates=[
        {
            'name': 'Cartão de Vocabulário',
            'qfmt': '<div class="back"><b>{{PalavraEmPortugues}}</b></div>',
            'afmt': '''
                <div class="back">{{FrontSide}}</div>
                <div class="back">
                    <hr>
                    <p><b>Tradução:</b> {{PalavraEmIngles}}</p>
                    <p><b>Pronúncia:</b> {{Pronuncia}}</p>
                    <p><b>IPA:</b> {{IPA}}</p>
                    <p>{{Audio}}</p>
                </div>
            ''',
        },
    ],
    css="""
        .front {
            font-size: 30px;
            text-align: center;
            font-family: 'Arial', sans-serif;
        }
        .back {
            font-size: 20px;
            font-family: 'Verdana', sans-serif;
            text-align: center;
            line-height: 1.6;
        }
        b { color: #E74C3C; }
        hr { border: 1px solid #BDC3C7; }
        audio { display: block; margin-top: 10px; }
    """
)

# Função para remover números de strings
def remover_numeros(texto):
    """
    Remove todos os números de uma string.

    Args:
        texto (str): Texto original.

    Returns:
        str: Texto sem números.
    """
    return re.sub(r'\d+', '', texto)

# Função para extrair palavras importantes com TF-IDF
def palavras_importantes_tfidf(texto, n):
    """
    Extrai as palavras mais importantes de um texto usando TF-IDF.

    Args:
        texto (str): Texto de entrada.
        n (int): Número de palavras a extrair.

    Returns:
        list: Lista das n palavras mais relevantes.
    """
    documentos = [texto]  # TF-IDF aceita múltiplos documentos
    stop_words = stopwords.words('english')  # Stopwords em inglês

    # Criação do vetor TF-IDF
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    X = vectorizer.fit_transform(documentos)

    # Obter importância das palavras
    importancia = dict(zip(vectorizer.get_feature_names_out(), X.toarray().sum(axis=0)))
    palavras_importantes = sorted(importancia.items(), key=lambda x: x[1], reverse=True)
    return palavras_importantes[:n]

# Função para gerar áudio e informações de pronúncia
def gerar_info_pronuncia(palavra):
    """
    Gera a pronúncia, IPA e áudio para uma palavra.

    Args:
        palavra (str): Palavra de entrada.

    Returns:
        dict: Informações geradas.
    """
    try:
        pronuncia = pronouncing.phones_for_word(palavra.lower())[0]
        pronuncia = remover_numeros(pronuncia).replace(' ', '|').replace('1', "[+]").replace('0', "[-]")
    except IndexError:
        pronuncia = ""

    IPA = ""
    try:
        sentence_list = list(sentences(palavra, lang="en-us"))
        for sent in sentence_list:
            for word in sent.words:
                if word.phonemes and word.phonemes[0] != '‖':
                    IPA = "".join(word.phonemes)
    except:
        IPA = ""

    # Gerar áudio
    audio_file = f"{palavra}.mp3"
    gTTS(text=palavra, lang='en', slow=False).save(audio_file)

    return {
        'pronuncia': pronuncia,
        'IPA': IPA,
        'audio': audio_file
    }

# Processar palavras e criar flashcards
def processar_palavras(texto, num_palavras, modelo, titulo):
    """
    Cria flashcards com base em palavras importantes do texto.

    Args:
        texto (str): Texto de entrada.
        num_palavras (int): Número de palavras a processar.
        modelo (genanki.Model): Modelo Anki.
        titulo (str): Título do deck.

    Returns:
        genanki.Package: Pacote do deck gerado.
    """
    palavras = palavras_importantes_tfidf(texto, num_palavras)
    deck = genanki.Deck(10929038, f"Idiomas::🇺🇸::{titulo}::Palavras")
    pacote = genanki.Package(deck)

    for palavra, _ in palavras:
        traducao = tradutor.translate(palavra)
        info = gerar_info_pronuncia(palavra)

        note = genanki.Note(
            model=modelo,
            fields=[
                traducao,  # Frente
                palavra,   # Verso
                info['pronuncia'],  # Pronúncia
                info['IPA'],        # IPA
                f'[sound:{info["audio"]}]'  # Áudio
            ]
        )
        deck.add_note(note)
        pacote.media_files.append(info['audio'])

    return pacote

# Texto de exemplo
texto = """..."""  # Coloque o texto aqui
titulo = "Special counsel Jack Smith drops cases"
pacote = processar_palavras(texto, 500, modelo, titulo)

# Salvar o pacote
pacote.write_to_file('pt_en_words.apkg')