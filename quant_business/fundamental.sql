DROP TABLE IF EXISTS company_reference;

CREATE TABLE IF NOT EXISTS company_reference (
  company_id TEXT PRIMARY KEY,
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
  expected_fiscal_year_end TEXT
);
