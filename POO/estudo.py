"""
1- Linguagem de maquina;
2- Linguagem de montagem (Asembly);
3- Linguagem de alto nivel (FORTRAN);
4- Linguagem estruturada (ALGOL);
    *Muita repetição de codigo;
    *Codigo mal organizado;
    *Codigo de dificil entendimento;
    *Muitos erros (BUGS);
5- Programação orientada a objetos (POO);

POO:

Objeto: É algo que encapsula dados (variaveis e atributos) que o programa vai manipular, e os codigos 
(Funções ou métodos) correspondentes a esses dados;

Classe: Derfine os elemtnos de um conjunto de objetos (Atributos e métodos). Funciona como
uma fabrica de objetos, criando instancias dos mesmos;
  *Instancia: Java: Carro c = new carro()
              Python: c = carro()
  *Comunicação: envio de mensagem de um objeto para outro objeto (Chamada de metodo, ou de função);

Abstração: um objeto representa alguma coisa do mundo real, e os atributos, caracteristicas dessa coisa;

Variavel do objeto: É uma variavel que muda de instancia para instancia, ex: diametro de uma bola;

Variavel de classe: É uma variavel que não muda nas instancias, ex: formato da bola(redonda);
  *Se mudar a variavel de classe, vai mudar todas as intancias, pois ela esta ligada a todas;


PYTHON:

class Bola;
  conta_bolas = 0 #Variavel de classe

  def __INIT__(self, diametro);
    self.diametro = diametro #Variavel objeto
    Bola.conta_bola += 1 #Acessar variavel de classe (chama a funçao da classe e dps a variavel)


HERANÇA: (Especialização = subclasses // generalização = superclasses)
  - Subclasses ou Superclasses;
  - É um mecanismo que serve para evitar duplicação de codigo;
  - Ele pega elementos repetidos em determinadas classes, e coloca eles uma uma classe a cima;
  - "É um", classe pato e classe ave, pato subclasse (É uma ave);
  - Quando usar?
    *Para organizar abstrações;
    *Para acrescentar um novo comportamento(atributo ou metodo);
    *alterar um metodo/comportamento;

PYTHON:

class x: #Superclasse(Mãe)
  def __INIT__(self):

class y(x) #Subclasse(Filho)

OBSERVAÇÃO:

lado = [0 for i in range(x)] #Cria uma lista com x elementos, e todos com valar 0;

lado = [float(input("Digite o tamanho do lado: + str(i+1), for i in range(x)] #Percorre uma lista pedindo o valor de cada lado;

ARQUITETURA DE SOFTWARE:
  - Principais elementos que compoem um sistema de software e os inter-relacionamentos
  entre eles;
  - Modelar: Representação simplificada de alguma coisa que elimina caracteristicas 
  e atributos menos importantes (Abstrair);

UML(Unified modelling language)
  - Linguagem para visualização;
  - Especificar;
  - Documentar;
  - Construir;
  - OBS: Diagrama de classe, objeto(ESTRUTURAIS) // Diagrama de sequencia(COMPORTAMENTAIS)
  - Diagrama de classe:
    * Atributo/Modulo + = publico
    * Atributo/Modulo - = privado
    * Modulo # = So pode ser acessado pela propria classse, ou subclasse;
    * Agregar (losangulo) = um objeto é composto por mais de 0 de outro objeto 
      (instituto é composto (possui) por departamentos);
    * Composição (losangulo fechado) = um objeto é composto por mais de 0 de outro objeto, 
      mas o outro objeto depende do primeiro para existir;


Linguagem interpretada X Linguagem compilada:
  - Interpretada: Codigo fonte >> Interpretador >> Saída;
  - Compilada: Codigo fonte >>  Compliador >> Código objeto >> executor >> saida
  - Hibrida: Antes de iniciar a execução, o compilador traduz aquilo para bytecode,
    e ao iniciar o programa o interpretador le os bytecode um a um;

Filosofia de Java:
  - Uma linguagem que tem o objetivo de fazer um unico codigo, funcionar em deiferentes SO,
    nos outros casos, é necessario trancrever o programa para o SO que vc qr ultilizar, 
    caso nn seje oq vc programou primeiro;
  - Maquina virtual de java;

"""