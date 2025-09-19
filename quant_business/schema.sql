# DROP TABLE IF EXISTS candlestick;

CREATE TABLE IF NOT EXISTS candlestick (
  symbol TEXT NOT NULL,
  date TEXT NOT NULL,
  candlestick_sign TEXT NOT NULL
);

ALTER TABLE candlestick ADD COLUMN IF NOT EXISTS candlestick_bullish_sign TEXT;
ALTER TABLE candlestick ADD COLUMN IF NOT EXISTS candlestick_bearish_sign TEXT;
CREATE UNIQUE INDEX IF NOT EXISTS idx_candlestick_symbol_date ON candlestick (symbol, date);