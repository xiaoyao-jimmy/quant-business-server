DROP TABLE IF EXISTS fundamental;

CREATE TABLE IF NOT EXISTS fundamental (
    symbol TEXT PRIMARY KEY,
    date TEXT,
    fundamental_sign TEXT
);

CREATE UNIQUE INDEX idx_fundamental_symbol_date ON fundamental (symbol, date);