/* Write your T-SQL query statement below */

with stocks_buy_sell as (
select stock_name,
       SUM(case when operation='buy' then price else 0 end) as StocksBuy,
       SUM(case when operation='sell' then price else 0 end) as StocksSell
from stocks
group by stock_name
)
select stock_name, 
       (StocksSell-StocksBuy) as capital_gain_loss
from stocks_buy_sell