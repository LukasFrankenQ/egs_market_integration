

#### 72 clusters, 2030

__elec__  -  __static__ -  1000  -  1500  -  2000  -  2500  -  3000
--------------------  yes --- yes ---  yes  ---     

__elec__  -  __flex__  ---  1000  -  1500  -  2000  -  2500  -  3000
-------------------  yes ---  yes  ---  yes  --- 

__chp__  -  __static__  -  1000  -  1500  -  2000  -  2500  -  3000 - 3500 - 4000 - 5000 - 6000
-------------------  yes  ---  yes ---  no  ---  yes  ---  yes  --- yes --- yes --- yes --- yes

__chp__  -  __flex__  ----  1000  - 1500  -  2000  -  2500  -  3000 - 3500 - 4000 - 5000 - 6000
--------------------  yes --- yes  ---  yes  ---  yes   ---   yes --- yes --- yes --- no --- no

__dh__  -  __static__  ---  1000  -  1500  -  2000  -  2500  -  3000 - 4000 - 5000 - 6000
--------------------  no  ---  yes ---  yes --- yes  ---  yes  --- yes ---- yes --- yes

__dh__  -  __flex__  ------  1000  -  1500  -  2000  -  2500  -  3000 - 4000 - 5000 - 6000
-------------------  no  -----  yes  ---  yes   ---   yes  --- yes --- yes --- yes --- yes



#### 72 clusters, 2050, dh progress sensitivity


__chp__  -  __flex__  ---- 0.0 -  0.25  - 0.5  -  0.75  -  1. 
-------------------  yes ----- yes  -----  yes  ---  yes   ----   yes

__dh__  -  __flex__  ----  0.0 - 0.25  - 0.5  -  0.75  -  1. 
-------------------  yes --- yea  -----  yes  ---  yes   ----   yes


### TO DO for final runs!

- Change investment year to 2050.
- Create consistency in cost heat distribution network between chp and dh.
- Double check cost of organic rankine cycle in config.
- Double check max hours of storage
- differentiate carrier between injection and production
- static capacity factors for generation?
- respect cascading of efficiency in the dh case
- should max_hours be adapted for 3h timesteps?\
- due to 125 generation capacity during discharge, should all cost be at injection well?


### Ideas jotted down

- Plot for CHP operation, where on the heat-elec diagram plant was operated
- Plot capacity change induced by flexible operation, versus change in energy provided by flexible operation.


###### On the cluster

to get medium fast exclude nodes 1f01, 1f02, 1j01
to get fast fast also exclude 1C19, 3c06, 3c05

example
- qsub -N ELST1000 -l h_vmem=64G -l h_rt=47:59:59 -l h=!(node1f01|node1f02|node1j01) ./main.sh