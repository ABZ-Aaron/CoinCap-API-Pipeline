CREATE SCHEMA IF NOT EXISTS crypto;
CREATE TABLE IF NOT EXISTS crypto.assets (
	id VARCHAR(50) NOT NULL,
	rank INTEGER,
	symbol VARCHAR(50),
	name VARCHAR(50),
	supply NUMERIC,
	max_supply NUMERIC,
	market_cap NUMERIC,
	volume_24hr NUMERIC,
	price NUMERIC,
	change_per_24hr NUMERIC,
	volume_we_24hr NUMERIC,
	update_utc TIMESTAMP WITH TIME ZONE
);