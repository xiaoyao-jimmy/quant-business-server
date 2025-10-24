DROP TABLE IF EXISTS financial_statements;

CREATE TABLE IF NOT EXISTS financial_statements (
  symbol TEXT,
  period_ending_date TEXT,
  recent_month TEXT,
  file_date TEXT,
  accession_number TEXT,
  form_type TEXT,
  period_auditor TEXT,
  auditor_report_status TEXT,
  inventory_valuation_method TEXT,
  number_of_share_holders TEXT,
  period_type TEXT,
  total_risk_based_capital TEXT,
  income_file_date TEXT,
);

DROP TABLE IF EXISTS security_reference;

CREATE TABLE IF NOT EXISTS security_reference (
  security_symbol TEXT PRIMARY KEY,
  symbol TEXT,
  exchange_id TEXT,
  currency_id TEXT,
  ipo_date TEXT,
  is_depositary_receipt TEXT,
  depositary_receipt_ratio REAL,
  security_type TEXT,
  share_class_description TEXT,
  share_class_status TEXT,
  is_primary_share TEXT,
  is_dividend_reinvest TEXT,
  is_direct_invest TEXT,
  investment_id TEXT,
  ipo_offer_price REAL,
  delisting_date TEXT,
  delisting_reason TEXT,
  mic TEXT,
  common_share_sub_type TEXT,
  ipo_offer_price_range TEXT,
  exchange_sub_market_global_id TEXT,
  conversion_ration REAL,
  par_value REAL,
  trading_status TEXT,
  market_data_id TEXT,
  date TEXT
);

DROP TABLE IF EXISTS company_reference;

CREATE TABLE IF NOT EXISTS company_reference (
  company_id TEXT PRIMARY KEY,
  symbol TEXT,
  short_name TEXT,
  standard_name TEXT,
  legal_name TEXT,
  country_id TEXT,
  cik TEXT,
  company_status TEXT,
  fiscal_year_end INTEGER,
  industry_template_code TEXT,
  primary_share_class_id TEXT,
  primary_symbol TEXT,
  primary_exchange_id TEXT,
  business_country_id TEXT,
  legal_name_language_code TEXT,
  auditor TEXT,
  auditor_language_code TEXT,
  advisor TEXT,
  advisor_language_code TEXT,
  is_limited_partnership TEXT,
  is_reit TEXT,
  primary_mic TEXT,
  report_style INTEGER,
  yearof_establishment TEXT,
  is_limited_liability_company TEXT,
  expected_fiscal_year_end TEXT,
  date TEXT
);
