USE insurance_dw;

-- =====================================
-- Insurance Claims Data Warehouse
-- Analytical SQL Queries
-- =====================================

-- 1. Total Claims
SELECT COUNT(*) AS Total_Claims
FROM fact_claim;

-- 2. Total Claim Amount
SELECT SUM(amount) AS Total_Claim_Amount
FROM fact_claim;

-- 3. Average Claim Amount
SELECT AVG(amount) AS Average_Claim_Amount
FROM fact_claim;

-- 4. Claims by Status
SELECT
    status,
    COUNT(*) AS Total_Claims
FROM fact_claim
GROUP BY status;

-- 5. Claims by Type
SELECT
    claim_type,
    COUNT(*) AS Total_Claims
FROM fact_claim
GROUP BY claim_type;

-- 6. Top 10 Highest Claims
SELECT *
FROM fact_claim
ORDER BY amount DESC
LIMIT 10;
