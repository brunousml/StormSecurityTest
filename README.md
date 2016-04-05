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


### 5. Escreva um algoritmo qualquer para inverter uma String recebida como parâmetro. Use pseudo código ou a linguagem que você quiser. Não use funções prontas. 

```
função inverterString(str):
   stringInvertida = '';
   para letra em str faça:
      stringInvertida = letra + stringInvertida
   fim
   
   retornar stringInvertida
fim

```


### 6 Em um projeto de um aplicativo, existe uma classe chamada GoogleAnalytics, cuja função é enviar marcações (ex:eventos, screen views, etc) para a ferramenta de analytics do Google. Esta classe é utilizada em muitos pontos diferentes do projeto. A cada instanciação da GoogleAnalytics, é feito um setup que envolve uma série de atividades e que só deveriam acontecer uma única vez. Você foi encarregado de implementar esta classe. Que solução de design  você daria para garantir que a instanciação da GoogleAnalytics, ocorra apenas uma única vez, ao longo de toda execução do aplicativo? 

   Acredito que para este caso o padrão de projetos "Singleton" oferece o necessário para atender este requisito.

### 7 Usando os conceitos de orientação a objetos, dê sua sugestão para um modelo que expresse os conceitos destacados em negrito e seus relacionamentos: 
 
_Em um Prédio comercial, existem duas Empresas. Uma delas é a Storm Security e a outra é a Storm Defense. A Storm Security possui em seu quadro de Funcionários, Pessoas alocadas em diversos Departamentos. Um deles é o de Tecnologia e Informação (TI). No departamento de TI, você encontra alguns funcionários que são bastante flexíveis e dependendo da situação ou projeto, conseguem assumir um papel  de Desenvolvedor e Database Administrator (DBA) Outros funcionários são especialistas e desempenham um papel exclusivo de Desenvolvedor._

```
class building{
   id
   name
}

class company{
   id
   name 
   building_id
}

class department{
   id
   name
   company_id
}

class employment{
   id
   name
   department_id
   ...
}

class dev extends employment{
   employment_id
   skills
   ...
}

class dba extends employment{
   employment_id
   skills
   ..
}
```


### 8 O conceito de Model­View­Controller (MVC) é um padrão de design amplamente conhecido e implementado em diversos frameworks. Diga o que você entende por MVC com suas palavras.

O modelo MVC como o próprio nome diz, separa a arquitetura em 3 grandes camadas Modelo, Visão e Controlador. 

O modelo tem por obrigação gerenciar toda a persistência de dados e interação com banco de dados. Conexões, querys, entre outras interações.

No meio do caminho fica a camada de controle, que é o cerébro da aplicação. Nela inclui-mos as regras de negócio. para que ele possa acionar o modelo, recuperar os dados, e digerir antes de retornar a camada de visualização.

Por fim a camada de visualização esta encarregada de exibir os dados retornados pelo controlador para o cliente.

### 9 No desenvolvimento de aplicativos, é comum a necessidade de consumo de Web Services, para fazer o download/envio de dados úteis para aplicação. Em uma empresa de TI, o desenvolvimento do app e do backend, onde fica a implementação dos serviços, fica sob responsabilidade de pessoas diferentes e que trabalham em ritmos diferentes. Um cenário comum, é a necessidade de uso do serviços para avançar na codificação do app, porém, nem sempre eles se encontram prontos para tal.  
_O que você faria para contornar esta situação e avançar no desenvolvimento do app, tentando diminuir essa dependência do desenvolvedor de backend?_

Penso em 2 saídas para essa situação:

Primeiro: Podemos definir as URLs e os dados que elas retornarão. Assim podemos criar as rotas retornando dados estáticos, de acordo com o que o front necessita naquele momento. Ao final da implementação de backend, podemos trocar o retorno estático pelo retorno da aplicação de backend. 

Segundo: Com a utilização de aplicação como firebase, podemos criar uma banco de dados para desenvolvimento, baseado em webservice. Isso retornará os dados que o front precisa para continuar o seu trabalho. 

O importante nestes exemplos, é que definindo um padrão de URLs e dados, podemos trabalhar em paralelo, diminuindo a dependência de Frontend e Backend durante o desenvolvimento de aplicações.
