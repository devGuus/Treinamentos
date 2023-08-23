def contarLetra(texto):
  qtdCaracteres = 0
# Garantindo que não vai contar os espaços
  for caractere in texto:
    if caractere != " ":
      qtdCaracteres += 1
  return qtdCaracteres 

def contarPalavra(texto):
  # Dividindo o texto em palavras
  palavras = texto.split()  
  # Contando a quantidade de palavras
  qtd_palavras = len(palavras)  
  return qtd_palavras

def contarFrase(texto):
  qtdFrase = 0
  for carac in texto:
    if (carac == "." or carac=="!" or carac=="?"):
      qtdFrase += 1
  return qtdFrase

def coleman_liau(letras, palavras, frases ):
  L = ((letras / palavras) * 100)
  S = ((frases / palavras) * 100)
  CLI = 0.0588 * L - 0.296 * S - 15.8
  return CLI

# Recebendo texto:
entradaTexto = input("Digite o seu texto: ")
# Salvando os resultados em variaveis para o código ficar mais limpo
carac = contarLetra(entradaTexto)
plvrs = contarPalavra(entradaTexto)
frss = contarFrase(entradaTexto)
nota = coleman_liau(carac, plvrs, frss)
# Imprimimos a quantidade de Caracteres:
print(f"Possuem {carac} caracteres no seu texto;")
print(f"Possuem {plvrs} palavras nessa frase; ")
print(f"Possuem {frss} frases; ")
print(f"O resumo tem a nota {nota:.1f}")