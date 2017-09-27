USE GAP_AnalyticDB;
GO

--Retrieve ecological system boundary info for one system.
WITH ESPAD AS (
SELECT lu_boundary_gap_landfire.boundary, lu_boundary_gap_landfire.count,
       lu_boundary_gap_landfire.gap_landfire, lu_boundary.value, lu_boundary.padus1_4, 
       padus1_4.revoid, padus1_4.gap_sts
FROM lu_boundary_gap_landfire INNER JOIN lu_boundary ON lu_boundary.value = lu_boundary_gap_landfire.boundary
   					          INNER JOIN padus1_4 ON lu_boundary.padus1_4 = padus1_4.revoid),

--Retrieve ecological system name and code
ECOSYS AS (
SELECT g.ecosys_lu, g.value
FROM gap_landfire as g
WHERE g.ecosys_lu = 'South Florida Bayhead Swamp')

--Group records from joined data views by count
SELECT ESPAD.gap_sts, sum(ESPAD.count) AS cells
FROM ECOSYS INNER JOIN ESPAD ON ECOSYS.value = ESPAD.gap_landfire
GROUP BY ESPAD.gap_sts