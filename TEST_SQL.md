### 1. Для каждого клиента выведете магазин, в котором он совершил первую покупку, и ее дату.


`SELECT acc_id, whs_id, trn_date FROM warehouses JOIN transactions USING(whs_id) WHERE(acc_id, trn_date) IN ( SELECT acc_id, MIN(trn_date) AS trn_date FROM transactions GROUP BY acc_id) ORDER BY 1, 3`


### 2. Выведете клиентов, которые: - не посещали форматы «У Дома» и «Гипермаркет» более 8 недель; - формат «Авто» более 4 недель.


`SELECT acc_id FROM warehouses JOIN transactions USING(whs_id) WHERE acc_id in ( SELECT acc_id FROM ( SELECT acc_id FROM warehouses JOIN transactions USING(whs_id) WHERE ROUND((DATEDIFF(NOW(), trn_date) / 7), 0) > 8 AND frmt IN (2, 3) ) query_in WHERE ROUND((DATEDIFF(NOW(), trn_date) / 7), 0) > 4 AND frmt = 1 )`



### Выведете клиентов, у которых 80% чеков содержат от 10 шт. каждого товара в чеке.


`SELECT acc_id, SUM(mq >= 10) AS QNTY10, COUNT(*) AS ALL_TRANSACTIONS FROM ( SELECT trn_id, MIN(qnty) mq FROM products GROUP BY trn_id ) prod JOIN transactions ON transactions.trn_id = prod.trn_id GROUP BY acc_id HAVING QNTY10 > ALL_TRANSACTIONS * 0.8`
