# Crytpo-Arbitrage

**Crypto-arbitrage** refers to the practice of exploiting price differences for a cryptocurrency (or other digital assets) across different exchanges or trading platforms. The goal of crypto-arbitrage is to buy the cryptocurrency at a lower price on one exchange and sell it at a higher price on another exchange, thereby making a profit from the price disparity.

Here's a simplified example of how crypto-arbitrage works:

1. **Identifying Opportunity**: Let's say Bitcoin is trading at $50,000 on Exchange A and $51,000 on Exchange B.

2. **Buying**: A trader would purchase Bitcoin at the lower price of $50,000 on Exchange A.

3. **Transferring**: The trader would then transfer the purchased Bitcoin from Exchange A to Exchange B, which might involve transaction fees and some time for the transfer to be confirmed on the blockchain.

4. **Selling**: Once the Bitcoin arrives on Exchange B, the trader sells it at the higher price of $51,000.

5. **Profit**: The trader has now made a profit of $1,000 ($51,000 - $50,000), minus any transaction fees and transfer costs.

For simplicity, we are assuming transaction fees and transfer costs as 0

---
### How to run the code?
1. Download all the files on your system
2. Install all the required modules from requirements.txt
```
pip install -r requirements.txt
```
3. Download and install MongoDB Compass from [here](https://downloads.mongodb.com/compass/mongodb-compass-1.39.2-win32-x64.exe)
4. Connect the MongoDB connection via
```
mongodb://localhost:27017
```
5. Create a folder **instance** and a file within the folser with name **secret_keys.py**. 
Create a variable `CMC_API_KEY`and paste your API Key.
***(Don't forget to paste your CoinMarketCap API Key)***
7. Now go to the root directory of the app and run this command:
```
flask run
```
8. The flask app will be started. There are 2 important api endpoints. 
- First one is '/home': This is where magic happens. Go to `locahost:5000/home` on your browser. If everything has been installed as per the instructions above, home page will look something like this:
![home page](https://drive.google.com/file/d/1YViVns0JzKs9i5PYAAecSi5S7aNr-i-G/view)
- Second one is '/history': This is to show the historical data which has been stored in the DB. Open postman and go to `localhost:5000/history`. In the auth section, select basic auth and input these credentials. 
```
username: kushagra
password: algotest
```
- If everything has been installed as per the instructions above, you will get all the historical data (only when profit is not null) that has been stored in the DB.
