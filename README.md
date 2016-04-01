# StormSecurityTest

# 1. Escreva um breve algoritmo que retorne o ​resto ​da divisão (operação matemática) de ​10​ por ​3 ​. Use a linguagem que você quiser. 

    def restOfDivision(n, m):
       return n % m;

    print restOfDivision(10, 3)

# 2. Algumas estruturas de dados são famosas, como a ​Pilha​, ​Fila​, ​Lista​, ​Dicionário​
 entre outras. 
a) Explique a diferença de funcionamento entre uma ​Pilha​ (Last In First Out) e uma ​Fila​ (First In First Out). 
    Em resumo, a fila usa a ordem de iserção para remover os itens adicionados. Ou seja, ao remover um item da fila ela remove o primeiro item adicionado. Enquanto que a pilha removerá o último a item adicionado.

    Na prática funciona da seguinte forma. Dada a seguinte fila [1, 2, 3]. Ao remover um item da fila, sobrará apenas [2,3]. Ou seja, o primeiro item adicionado foi removido. 
    Enquanto em uma pilha o comportamento é inverso. Dada uma pilha [1, 2, 3], ao remover um item, ela retornará [1,2] removendo o último item adicionado a lista.



(b) Dê 1 exemplo do mundo real, com o que você poderia representar, para ​cada​ uma destas estruturas.

    Para o envio de emails é legal utilizar filas. Quando temos uma demanda de envio de email maior que a capacidade de envio de nossos servidores. Podemos usar uma fila para gerenciar a sequencia de envio. Pois sempre serão enviados os emails de acordo com a sequencia que foram inseridos. Respeitando assim a fila.

    Para pilhas, acho interessante o exemplo do "git stash". Esse comando cria uma pilha de modificações que serão escondidas. Ao utilizar o comando git stash pop. Ele retorna o último item inserido na pilha. 


# 3. Imagine a seguinte estrutura de dados que contém os seguintes campos: 
 
    Classe ​Pessoa 
         String nome; 
         int idade; 
    fim 
 
# Você possui uma ordenada de objetos da classe ​Pessoa e um ​dicionário​, cuja chave é o ​nome da pessoa​.  
 
#### Sendo estas estruturas de dados preenchidas com o nome de uma família (Maria, José e João), para buscar pela idade de João, podemos dizer que é mais rápido, computacionalmente, fazê­-lo em um dicionário​ do que numa ​lista. ​Por quê?

    Quando selecionamos um determinado elemento em um dicionário. Ele possue uma busca baseada hash de strings para aquele elemento facilitando a indexação. Enquanto a lista percorrer sequencialmente todos os elementos anteriores ao número informado. O que à torna mais lenta quando trabalhamos com muitos elementos na coleção.
    
