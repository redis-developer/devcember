import { Client, Repository } from 'redis-om';
import animalSchema from './animal.js';

async function queryAnimals() {
  const client = new Client();
  await client.open();

  const repository = new Repository(animalSchema, client);

  const matchingAnimals = await repository.search()
    .where('species').equals('dog')
    .and('sex').equals('m')
    .and('age').is.greaterThan(3).returnAll();

  console.log(matchingAnimals);  
  await client.close();
}

queryAnimals();
