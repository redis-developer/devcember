import { Client, Entity, Repository, Schema } from 'redis-om';

class Animal extends Entity { };

const animalSchema = new Schema(Animal, {
  name: { type: 'string' },
  species: { type: 'string' },
  age: { type: 'number' },
  weight: { type: 'number' },
  sex: { type: 'boolean' },
  fee: { type: 'number' },
  children: { type: 'boolean' },
  otherAnimals: { type: 'boolean' },
  description: { type: 'string', textSearch: true }
}, {
  dataStructure: 'HASH'
});

export default animalSchema;