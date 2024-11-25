# **Mineração de Sentenças para Aprendizado de Idiomas**

## **Visão Geral**
Este projeto automatiza a criação de flashcards para Anki, auxiliando estudantes de idiomas a aprender vocabulário e sentenças de maneira eficiente. Utilizando uma combinação de processamento de linguagem natural (NLP) e técnicas de aprendizado de máquina, o código processa um texto em inglês, extrai vocabulário e sentenças relevantes, traduz para o português e gera guias de pronúncia, transcrições fonéticas (IPA) e arquivos de áudio associados.

Os flashcards gerados são salvos no formato `.apkg`, prontos para importação no Anki, uma ferramenta popular de estudos baseada em flashcards. O resultado inclui dois decks:
1. **Deck de Vocabulário**: Focado em palavras-chave do texto.
2. **Deck de Sentenças**: Focado em frases significativas extraídas do texto.

---

## **Importância**
O aprendizado eficaz de um idioma exige:
- **Recordação ativa**: Praticar vocabulário e o uso de sentenças.
- **Habilidades de escuta**: Associar palavras à pronúncia correta.
- **Compreensão contextual**: Aprender vocabulário no contexto de frases.

Esta ferramenta atende a todas essas necessidades ao:
- Extrair e classificar o vocabulário e as sentenças mais importantes de textos reais.
- Fornecer traduções e transcrições fonéticas precisas.
- Gerar áudio para aprimorar as práticas de escuta e pronúncia.

---

## **Funcionalidades**
### 1. **Extração Automática de Vocabulário**
- Identifica as palavras mais relevantes usando o algoritmo TF-IDF.
- Remove palavras comuns (stopwords) para focar em termos únicos ou significativos.

### 2. **Mineração de Sentenças**
- Segmenta o texto em sentenças.
- Fornece exemplos contextuais para o uso do idioma.

### 3. **Flashcards Multi-Modais**
Cada flashcard inclui:
- A palavra ou frase em **inglês**.
- Sua **tradução para o português**.
- **Guias de pronúncia** nos formatos ARPAbet e IPA.
- Um **arquivo de áudio** gerado com o Google Text-to-Speech (gTTS).

### 4. **Criação de Decks Personalizados**
- Dois decks separados:
  - Deck de vocabulário para palavras individuais.
  - Deck de sentenças para aprendizado contextual.
- Formatação clara e profissional para facilitar os estudos.

---

## **Instalação**
Para executar o projeto, você precisará de Python 3.x e das seguintes bibliotecas:
```bash
pip install deep-translator pronouncing gruut gTTS genanki nltk scikit-learn
```
## **Como Usar**
1. **Insira o Texto**:
   - Substitua o texto de exemplo no código por qualquer texto em inglês de sua escolha.
   - **Exemplo**: Artigos de notícias, trechos de livros ou materiais de estudo personalizados.

2. **Execute o Script**:
   - O código processará o texto, extraindo palavras e sentenças e gerando dois arquivos `.apkg`.

3. **Importe no Anki**:
   - Abra o Anki e importe os arquivos `.apkg` gerados.
   - Comece a estudar!

---

## **Como Funciona**
### **Etapa 1: Processamento de Texto**
- O texto de entrada é pré-processado para remover números e segmentado em palavras e sentenças.

### **Etapa 2: Extração de Vocabulário**
- TF-IDF é aplicado para identificar as palavras mais importantes.
- As palavras são traduzidas para o português e acompanhadas de fonética e áudio.

### **Etapa 3: Segmentação de Sentenças**
- As sentenças são extraídas e processadas para gerar informações fonéticas e áudio.

### **Etapa 4: Geração de Flashcards**
- Cada palavra e sentença é formatada em flashcards Anki usando `genanki`.
- Arquivos de áudio associados são incluídos no pacote.

---

## **Aplicações**
- **Aprendizado de Idiomas**: Aprenda vocabulário e habilidades auditivas com conteúdo real.
- **Professores**: Crie rapidamente materiais de estudo para seus alunos.
- **Autodidatas**: Personalize decks a partir de qualquer fonte de texto.

---

## **Limitações**
- O código foca na tradução de inglês para português; para outros idiomas, são necessárias pequenas adaptações.
- A geração de pronúncia ARPAbet pode ser limitada para palavras complexas ou incomuns.

---

## **Melhorias Futuras**
- Suporte a outros idiomas e fontes de texto.
- Aperfeiçoamento da precisão das transcrições fonéticas com técnicas avançadas de NLP.
- Integração com APIs para entrada dinâmica de texto (ex.: web scraping).

---

## **Contribuindo**
Contribuições são bem-vindas para melhorar a funcionalidade e expandir o suporte a idiomas! Envie *issues* ou *pull requests* para o repositório.

---

## **Licença**
Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.