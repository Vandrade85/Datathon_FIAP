# Datathon - Fiap
 Datathon é o trabalho final para a pós na FIAP de Data Analytics

 Site com o trabalho: https://datathonfiap.streamlit.app/

### Relatório: Análise dos Dados Educacionais - ONG Passos Mágicos

#### Introdução
O presente relatório visa apresentar uma análise detalhada dos dados educacionais de estudantes atendidos pelo programa Passos Mágicos nos anos de 2020, 2021 e 2022. O objetivo principal é avaliar o impacto do programa no desenvolvimento dos estudantes, com foco nos indicadores de desempenho e evolução ao longo do período analisado.

A proposta analítica visa não apenas identificar as principais métricas e indicadores de desempenho, mas também fornecer insights sobre a evolução dos alunos e destacar as áreas onde o impacto da ONG é mais evidente.

#### Carregamento e Preparação dos Dados
Os dados utilizados na análise foram retirados diretamente dos registros educacionais e socioeconômicos disponibilizados pela ONG Passos Mágicos. Como primeira etapa, realizamos a limpeza e preparação dos dados:

- **Conversão de colunas**: as colunas numéricas foram convertidas para o formato adequado para cálculos e visualizações.
- **Filtragem de colunas**: selecionamos as colunas mais relevantes para a análise.
- **Tratamento de valores ausentes**: linhas com dados faltantes foram removidas para garantir a integridade da análise.

#### Análise Anual (2020, 2021, 2022)
Para cada ano analisado, foram criados DataFrames específicos, com foco em colunas relevantes como desempenho acadêmico, participação no programa e dados socioeconômicos.

- **Distribuição de dados**: gráficos de barras foram utilizados para visualizar a distribuição dos alunos por diferentes categorias (como fases e turmas).
- **Indicadores de desempenho**: destacamos a evolução de métricas como o Indicador de Desenvolvimento Educacional (INDE), permitindo uma visão clara da evolução dos alunos ao longo do tempo.

#### Evolução dos Indicadores
Um dos focos principais foi a evolução de métricas importantes, como o INDE, ao longo dos três anos. Observamos:

- **Gráficos de linha e barras**: utilizados para destacar tendências e mudanças ao longo do tempo.
- **Correlação entre variáveis**: investigamos as relações entre diferentes indicadores usando matrizes de correlação, identificando fatores que mais influenciam o desempenho dos alunos.

#### Análise de Destaque
Os alunos foram divididos em dois grupos: "melhores desempenhos" e "em desenvolvimento". Com base nesta segmentação, realizamos análises comparativas:

- **Grupos de destaques**: comparamos métricas como o Índice de Evolução Geral (IEG), o Índice de Desempenho Acadêmico (IDA) e o Índice de Participação Voluntária (IPV) entre os dois grupos.
- **Impacto do tempo de participação**: identificamos uma correlação positiva entre o tempo de participação no programa e a melhoria no desempenho dos alunos.

#### Visualizações
Para facilitar a interpretação dos dados, criamos uma série de visualizações:

- **Gráficos de barras horizontais**: usados para comparar o desempenho entre os grupos.
- **Heatmaps**: para identificar rapidamente correlações fortes entre variáveis.

#### Conclusão
A análise dos dados dos alunos do programa Passos Mágicos revelou um impacto positivo no desenvolvimento dos estudantes ao longo dos três anos. A correlação entre o tempo de participação no programa e o desempenho educacional foi um dos principais destaques, reforçando a importância da continuidade no apoio oferecido pelo programa. Com base nessas informações, é possível orientar futuras decisões educacionais e otimizar ainda mais o impacto do programa.

Para obter análises ainda mais precisas, seria ideal contar com uma base de dados padronizada entre todas as escolas e que incluísse informações tanto de alunos participantes quanto de não participantes do programa, dentro da mesma instituição. Dessa forma, seria possível identificar com maior clareza os aspectos em que o programa realmente promove um impacto significativo no desenvolvimento educacional e pedagógico dos alunos.


## Instalação do pacote - MVP Streamlit 
Clone o repositório e instale as dependências:
```bash
git clone https://github.com/Vandrade85/Fiap_Datathon.git
cd Fiap_Datathon
pip install -r requirements.txt

