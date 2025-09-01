DROP TABLE IF EXISTS candlestick;

CREATE TABLE candlestick (
  symbol TEXT NOT NULL,
  date TIMESTAMP NOT NULL,
  candlestick_sign TEXT NOT NULL
);