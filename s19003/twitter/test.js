// import Twitter from 'twitter-v2'
import dotenv from 'dotenv'
import Twitter from 'twitter-v2'
dotenv.config()

const client = new Twitter({
  consumer_key: process.env.API_KEY,
  consumer_secret: process.env.API_SECRET,
  access_token_key: process.env.ACCESS_TOKEN,
  access_token_secret: process.env.ACCESS_SECRET
})
