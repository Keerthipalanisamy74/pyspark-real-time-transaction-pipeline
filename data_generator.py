import csv
import random
import time

with open("transactions.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id","user_id","amount","timestamp"])

    for i in range(1000):
        transaction_id = i
        user_id = random.randint(1000, 2000)
        amount = round(random.uniform(10, 5000),2)
        timestamp = time.time()

        writer.writerow([transaction_id,user_id,amount,timestamp])
        time.sleep(0.1)
