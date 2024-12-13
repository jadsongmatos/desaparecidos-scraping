
Este projeto de pessoas desaparecidas, envolvendo coleta de dados, processamento de dados, integração de sistemas de informações geográficas (GIS) e formulários para catalogação de dados de pessoas desaparecidas.

Abaixo está um resumo detalhado e uma explicação da estrutura de diretórios fornecida e dos arquivos destacados. Este panorama visa ajudá-lo a entender o propósito e o conteúdo dos arquivos, bem como os trechos de código relevantes e suas funcionalidades.

Pontos chave sobre a estrutura:

- Foi feito vários notebooks (`sc.ipynb`, `map.ipynb`, `cidades.ipynb`, `namus.ipynb`) para análise de dados, extração de APIs e manipulação de dados geoespaciais.
- Arquivos como `Form.md` e `Aula.md` incluem notas, formulários e instruções relacionadas ao contexto das pessoas desaparecidas.
- Arquivos como `mapa.qgz`, `mapa-local.qgz` e `mapa-local.qgs` são arquivos de projeto QGIS.
- `Unique_Hex_Colors.csv` e `mapa.ipynb` são dados geoespaciais e geológicos, referências de cores.

---

## Arquivos Destacados e Seus Conteúdos

### 1. `casos.csv`

O arquivo `casos.csv` é um CSV que contém informações detalhadas sobre indivíduos desaparecidos. Ele inclui:

- **Métricas de Saúde e Fitness**: Índice de Massa Corporal (IMC), Taxa Metabólica Basal (TMB), gordura corporal, entre outras.
- **Atributos Pessoais**: Sexo, idade, altura e peso dos desaparecidos.
- **Atributos Codificados**: Um grande conjunto de campos binários ou numericamente codificados que descrevem circunstâncias específicas do desaparecimento, como características físicas ("O desaparecido tem cabelo longo?") ou informações demográficas ("O desaparecido é Brasileiro?").
- **Datas Importantes**: Datas de nascimento e de desaparecimento.

A estrutura do arquivo organiza os dados por colunas, onde a primeira linha contém os descritores dos atributos e as linhas subsequentes representam cada indivíduo. Este formato facilita a análise quantitativa e categórica dos casos de desaparecimento, permitindo identificar padrões e realizar estudos detalhados sobre as características e circunstâncias dos desaparecidos.

### 2. `namus.js`

Um arquivo JavaScript que utiliza `axios` para solicitar dados da API do NamUs (National Missing and Unidentified Persons System, um banco de dados baseado nos EUA). O script:

- Define parâmetros para paginação (`take`, `skip`).
- Faz uma requisição POST para a API do NamUs para buscar dados de pessoas não identificadas.
- Itera através de todas as páginas para buscar todos os registros e registra o progresso.
- O código visa baixar e armazenar dados do NamUs para análise posterior.

### 3. `Form.md`

Este documento em Markdown apresenta um questionário detalhado acompanhado de instruções para a identificação das características geológicas do último local onde uma pessoa desaparecida foi vista. As perguntas estão organizadas em categorias específicas, incluindo:

1. **Tipo de Rocha**: Avalia a presença de camadas, dureza, textura arenosa e fósseis nas rochas.
2. **Formações Geológicas Visíveis**: Investiga a existência de montanhas, falésias, formações arqueadas e sinais de atividade vulcânica.
3. **Características Relacionadas à Água e Gelo**: Identifica corpos d'água próximos e evidências de formações glaciais.
4. **Recursos Naturais e Outros**: Examina a presença de minerais metálicos, gemas e cristais nas rochas.

Além das perguntas, o documento inclui uma tabela de mapeamento para interpretar as respostas, facilitando a identificação das possíveis características geológicas do local com base nas observações fornecidas. Este formulário faz parte de um pipeline de coleta de dados padronizado, destinado a reunir informações precisas sobre o ambiente do desaparecimento e o último avistamento da pessoa.

Adicionalmente, o documento fornece links para diversas calculadoras online relacionadas à saúde e felicidade, explorando também atributos psicofísicos dos indivíduos envolvidos.

### 5. `map.ipynb`

Este notebook:

- Utiliza bibliotecas Python (`pandas`, `pycountry`, `rasterio`, `duckdb`, `tqdm`) para processar dados geoespaciais e textuais.
- Processar dados de pessoas desaparecidas integrados com consultas espaciais, vinculando-os a um mapa geológico `mapa.tif`.
- Busca características geológicas relacionadas ao último avistamento.

### 7. `Unique_Hex_Colors.csv`

Um CSV com códigos de cores hexadecimais e características geológicas associadas. Usado para mapear cores em uma camada de mapa geológico a certos tipos de rochas, tipos de crosta ou épocas geológicas. Cada entrada possui uma cor hex, um "Tipo de Crosta", "Tipo de Rocha" e período de idade geológica.

### 8. `namus.ipynb`

Outro notebook Jupyter:

- Utiliza `requests`, `tenacity` para tentativas de reenvio e `requests_cache`.
- Conecta ao `duckdb` e busca dados da API do NamUs.
- Cria uma tabela DuckDB `MissingPersons` e armazena registros recuperados.
- Este notebook automatiza o download e o armazenamento de dados de pessoas desaparecidas da API do NamUs em um banco de dados local DuckDB para análise posterior.

### 9. `Aula.md`

Este documento Markdown aborda a questão crítica das pessoas desaparecidas no Brasil, destacando a gravidade do problema com mais de 100 mil casos registrados anualmente. Ele apresenta uma análise das causas mais comuns de desaparecimento, sustentada por estatísticas detalhadas de 2019 a 2021.

O documento serve como um guia abrangente para o desenvolvimento de ferramentas e processos destinados a melhorar a investigação e resolução de casos de pessoas desaparecidas. Ele reúne informações essenciais, recursos legais, estatísticas e exemplos de casos para fornecer uma base sólida para profissionais e organizações envolvidas nesse desafio. Ao centralizar esse conhecimento, o documento visa otimizar a cooperação entre setores, aumentar a sensibilização pública e utilizar tecnologias modernas para acelerar a localização das desaparecidas.

### 12. `ideias.md`

Este documento Markdown apresenta um brainstorming de ideias voltadas para aprimorar a divulgação e a busca por pessoas desaparecidas. A proposta central é desenvolver uma plataforma que funcione como um ambiente de trabalho colaborativo para detetives, oferecendo ferramentas avançadas como inteligência artificial para envelhecimento e reconhecimento facial. A plataforma visa priorizar casos com base em algoritmos específicos, garantir a verificação colaborativa das informações e implementar sistemas de proteção contra abusos.

Além das funcionalidades tecnológicas, a plataforma incluirá recursos como mapas interativos, alertas e notificações, fóruns comunitários e integração com redes sociais para ampliar a visibilidade dos casos. Estratégias de financiamento propostas envolvem anúncios, campanhas de crowdfunding, doações, assinaturas para detetives e apoio de comunidades religiosas. A plataforma também facilitará a criação e distribuição de panfletos, o cadastro detalhado de desaparecidos e a utilização de tecnologias de localização e vigilância para auxiliar nas investigações.

Desafios identificados incluem a manutenção da interoperabilidade e padrões abertos, a descoberta de conteúdo em uma rede descentralizada e a escalabilidade do sistema para garantir um desempenho consistente. O objetivo final é criar uma ferramenta eficaz para localizar pessoas desaparecidas, apoiar detetives em suas investigações e engajar a comunidade na busca, aumentando assim as chances de sucesso na resolução dos casos.
## Conclusão

Este diretório contém um projeto multifacetado que combina ciência de dados, GIS e pesquisa investigativa em casos de pessoas desaparecidas. Os arquivos destacados contribuem de maneira diferente: alguns buscam dados de APIs, outros armazenam ou processam esses dados, e formulários. A integração com GIS (via projetos QGIS e dados raster) a exploração de dados que combina demográficos, saúde, comportamentais e dados geológicos vinculados a incidentes de desaparecimento.