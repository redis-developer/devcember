import { Client, Repository } from 'redis-om';
import animalSchema from './animal.js';

import fs from 'fs';
import csvStreamReader from 'csv-reader';

async function loadAnimals() {
  const csvStream = fs.createReadStream('animal_data.csv', 'utf8');
  const client = new Client();
  await client.open();

  const repository = new Repository(animalSchema, client);

  csvStream.pipe(
    new csvStreamReader({
      parseNumbers: true,
      parseBooleans: true,
      trim: true
    })
  ).on('data', async (row) => {
    const animal = repository.createEntity();

    animal.name = row[0];
    animal.species = row[1];
    animal.age = row[2];
    animal.weight = row[3];
    animal.sex = row[4];
    animal.fee = row[5];
    animal.children = row[6];
    animal.otherAnimals = row[7];
    animal.description = row[8];

    const id = await repository.save(animal);
    console.log(`Loaded ${animal.name} the ${animal.species} as ${id}.`);
  }).on('end', async () => {
    await repository.createIndex();
    await client.close();
    console.log('Loaded all of the animals!');
  });
}

loadAnimals();
