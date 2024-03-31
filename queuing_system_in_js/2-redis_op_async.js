import redis from 'redis';
import util from 'util';

const client = redis.createClient();
const getAsync = util.promisify(client.get).bind(client);

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

function setNewSchool(schoolName, value){
  client.set(schoolName, value, (error, reply) => {
    redis.print(`Reply: ${reply}`);
  });
};

async function displaySchoolValue(schoolName) {
    try {
        const foundValue = await getAsync(schoolName);
        console.log(foundValue);
    } catch (error) {
        console.error(error);
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');