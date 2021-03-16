------------------------------------------------------------------------------
select count(1)
from (
select distinct a.CountryCode,b.*  from result_clusters b 
inner join countries_all a 
on a.CountryName=b.CountryName
)

select count(1) from result_clusters

------------------------------------------------------------------------------
select * from (
select distinct CountryName, CountryCode, 'J'
from countries_all
where CountryCode in 
	(select CntA from clusters_dates
	group by Conc, CntA
	having count(Clust_dte) =1 
	)  )
inner join 
(select distinct CountryName, CountryCode, 'J'
from countries_all
where CountryCode in 
	(select CntB from clusters_dates
	group by Conc, CntB
	having count(Clust_dte) =1 
	))

------------------------------------------------------------------------------
select distinct CountryName from countries_all
where CountryCode 
in (
select CntA from clusters_dates union select CntB from clusters_dates)
 
------------------------------------------------------------------------------
