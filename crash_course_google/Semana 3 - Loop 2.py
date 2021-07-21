'''Digamos que você dirige uma liga de basquete local em sua cidade.
Você tem quatro equipes que vão jogar um contra o outro na liga, tanto em casa como fora.
Guardaste os nomes das equipas numa lista, como esta.
Queremos escrever um script que produzirá todos os emparelhamentos de equipe possíveis.
Para isso, a ordem dos nomes importa porque para cada jogo,
o primeiro nome será a equipe da casa e o segundo nome é a equipe ausente.
Claro, o que não queremos é ter uma equipa a jogar contra si mesma.
Então, que declaração precisamos usar para evitar isso? Para fazer isso,
precisamos usar um condicional que garante que apenas imprimimos o emparelhamento quando os nomes são diferentes.
Veja o que isso parece. Para a equipe da casa em equipes, para a equipe fora em equipes.
Se a equipe da casa não é igual à equipe ausente, imprimir equipe da casa versus equipe ausente. Sucesso!'''

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + ' vs ' + away_team)