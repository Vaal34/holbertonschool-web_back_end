import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});
  
client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error}`);
});

async function setSchool() {
    await client.hset('HolbertonSchools', 'Portland', 50, redis.print);
    await client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
    await client.hset('HolbertonSchools', 'New York', 20, redis.print);
    await client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
    await client.hset('HolbertonSchools', 'Cali', 40, redis.print);
    await client.hset('HolbertonSchools', 'Paris', 2, redis.print);
    
    await client.hgetall('HolbertonSchools', function(err, object) {
        console.log(object);
    });
}

setSchool();
