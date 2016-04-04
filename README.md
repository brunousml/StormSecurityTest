# StormSecurityTest

### 1. Escreva um breve algoritmo que retorne o ​resto ​da divisão (operação matemática) de ​10​ por ​3 ​. Use a linguagem que você quiser. 

``` python
def restOfDivision(n, m):
   return n % m;

print restOfDivision(10, 3)
``` 

### 2. Algumas estruturas de dados são famosas, como a Pilha, Fila, Lista, Dicionário entre outras. 
_a) Explique a diferença de funcionamento entre uma ​Pilha​ (Last In First Out) e uma ​Fila​ (First In First Out)._
    
    Em resumo, a fila usa a ordem de iserção para remover os itens adicionados. Ou seja, ao remover um item da fila ela remove o primeiro item adicionado. Enquanto que a pilha removerá o último a item adicionado

    Na prática funciona da seguinte forma. Dada a seguinte fila [1, 2, 3]. Ao remover um item da fila, sobrará apenas [2,3]. Ou seja, o primeiro item adicionado foi removido. 
    Enquanto em uma pilha o comportamento é inverso. Dada uma pilha [1, 2, 3], ao remover um item, ela retornará [1,2] removendo o último item adicionado a lista.



_(b) Dê 1 exemplo do mundo real, com o que você poderia representar, para ​cada​ uma destas estruturas._

    Para o envio de emails é legal utilizar filas. Quando temos uma demanda de envio de email maior que a capacidade de envio de nossos servidores. Podemos usar uma fila para gerenciar a sequencia de envio. Pois sempre serão enviados os emails de acordo com a sequencia que foram inseridos. Respeitando assim a fila.

    Para pilhas, acho interessante o exemplo do "git stash". Esse comando cria uma pilha de modificações que serão escondidas. Ao utilizar o comando git stash pop. Ele retorna o último item inserido na pilha. 


### 3. Imagine a seguinte estrutura de dados que contém os seguintes campos: 
 
``` python
    Classe ​Pessoa 
         String nome; 
         int idade; 
    fim 
``` 
 
_Você possui uma ordenada de objetos da classe ​Pessoa e um ​dicionário​, cuja chave é o ​nome da pessoa. Sendo estas estruturas de dados preenchidas com o nome de uma família (Maria, José e João), para buscar pela idade de João, podemos dizer que é mais rápido, computacionalmente, fazê-lo em um dicionário do que numa lista. Por quê?_

    Quando selecionamos um determinado elemento em um dicionário. Ele possue uma busca baseada hash de strings para aquele elemento facilitando a indexação. Enquanto a lista percorrer sequencialmente todos os elementos anteriores ao número informado. O que à torna mais lenta quando trabalhamos com muitos elementos na coleção.
    
# 4. Dados os dois algoritmos (​maior_numero ​ e ​meu_algoritmo ​) diga: 
 _(a) Qual a ​complexidade de tempo de execução ​(ex: O[log n], O[n!] ...)_
 
 _(b) Desenhe sua ​curva de crescimento assintótico​ (tempo de execução x tamanho da entrada)._ 
 
 _(c) O vetor ​números​, possui o mesmo tamanho ​N, ​ na chamada de ambas as funções, qual delas terminará primeiro?_

```python
função maior_numero(vetor números) 
     int maior = numeros[0]; 
     para i = 0 até tamanho(números) faça 
          se numeros[i] > maior então 
               maior = numeros[i]; 
     fim 
 
     retorna maior; 
fim 
 ```
```python 
função meu_algoritmo(vetor numeros) 
     int soma = 0; 
     para i de 0  até tamanho(números) faça 
          para j de 0 até tamanho(números) faça 
               soma = soma +numeros[i] + numeros[j] 
          fim 
     fim 
 
     retorna soma; 
fim 
```
# 5. Escreva um algoritmo qualquer para inverter uma String recebida como parâmetro. Use pseudo código ou a linguagem que você quiser. Não use funções prontas. 

```
função inverterString(str):
   stringInvertida = '';
   para letra em str faça:
      stringInvertida = letra + stringInvertida
   fim
   
   retornar stringInvertida
fim

```
