import env from 'dotenv'

env.config()

const test = process.env.BEARER_TOKEN
const test2 = process.env.API_KEY

console.log(test)
console.log(test2)
