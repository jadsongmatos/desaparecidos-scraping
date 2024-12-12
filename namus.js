import axios from "axios"

async function start() {
  const allResults = [];
  const take = 10000; // Número de registros por requisição
  let skip = 0;       // Inicializa o skip
  let totalCount = 0; // Contagem total de registros

  // Configuração básica da requisição
  const requestConfig = {
    method: 'post',
    maxBodyLength: Infinity,
    url: 'https://www.namus.gov/api/CaseSets/NamUs/UnidentifiedPersons/Search',
    headers: { 
      'Content-Type': 'application/json',
    },
    data: {
      "predicates": [],
      "take": take,
      "skip": skip,
      "projections": [
        "idFormatted",
        "caseNumber",
        "dateFound",
        "estimatedAgeFrom",
        "estimatedAgeTo",
        "cityOfRecovery",
        "countyDisplayNameOfRecovery",
        "stateOfRecovery",
        "sex",
        "raceEthnicity",
        "modifiedDateTime",
        "namus2Number",
        "stateDisplayNameOfRecovery"
      ],
      "orderSpecifications": [
        {
          "field": "dateFound",
          "direction": "Descending"
        }
      ]
    }
  };

  try {
    // Primeira requisição para obter a contagem total
    const firstResponse = await axios.request(requestConfig);
    const firstData = firstResponse.data;

    totalCount = firstData.count;
    allResults.push(...firstData.results);

    console.log(`Obtidos ${firstData.results.length} de ${totalCount} registros.`);

    skip += take;

    // Calcular o número de requisições necessárias
    const totalRequests = Math.ceil(totalCount / take);
    
    // Realizar as requisições restantes
    for (let i = 1; i < totalRequests; i++) {
      // Atualizar o parâmetro skip para a próxima página
      requestConfig.data.skip = skip;

      const response = await axios.request(requestConfig);
      const data = response.data;

      allResults.push(...data.results);
      console.log(`Obtidos ${allResults.length} de ${totalCount} registros.`);

      skip += take;
    }

    console.log('Todos os dados foram baixados com sucesso.');
    // Aqui você pode processar `allResults` conforme necessário
    // Por exemplo, salvar em um arquivo:
    // const fs = require('fs');
    // fs.writeFileSync('dados.json', JSON.stringify(allResults, null, 2));
    
  } catch (error) {
    console.error('Ocorreu um erro ao baixar os dados:', error);
  }
}

start();
