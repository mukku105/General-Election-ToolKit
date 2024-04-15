-- SQLite
SELECT 
    sum(voters_turnout.turnout_male_1) as tm_1, 
    sum(voters_turnout.turnout_male_1_sangha) as tm_1_sangha,
    sum(voters_turnout.turnout_male_2) as tm_2,
    sum(voters_turnout.turnout_male_2_sangha) as tm_2_sangha,
    sum(voters_turnout.turnout_male_3) as tm_3,
    sum(voters_turnout.turnout_male_3_sangha) as tm_3_sangha,
    sum(voters_turnout.turnout_male_4) as tm_4,
    sum(voters_turnout.turnout_male_4_sangha) as tm_4_sangha,
    sum(voters_turnout.turnout_male_5) as tm_5,
    sum(voters_turnout.turnout_male_5_sangha) as tm_5_sangha,
    sum(voters_turnout.turnout_male_6) as tm_6,
    sum(voters_turnout.turnout_male_6_sangha) as tm_6_sangha,
    sum(voters_turnout.turnout_male_pc) as tm_pc,

    sum(voters_turnout.turnout_female_1) as tf_1, 
    sum(voters_turnout.turnout_female_1_sangha) as tf_1_sangha, 
    sum(voters_turnout.turnout_female_2) as tf_2,
    sum(voters_turnout.turnout_female_2_sangha) as tf_2_sangha,
    sum(voters_turnout.turnout_female_3) as tf_3,
    sum(voters_turnout.turnout_female_3_sangha) as tf_3_sangha,
    sum(voters_turnout.turnout_female_4) as tf_4,
    sum(voters_turnout.turnout_female_4_sangha) as tf_4_sangha,
    sum(voters_turnout.turnout_female_5) as tf_5,
    sum(voters_turnout.turnout_female_5_sangha) as tf_5_sangha,
    sum(voters_turnout.turnout_female_6) as tf_6,
    sum(voters_turnout.turnout_female_6_sangha) as tf_6_sangha,
    sum(voters_turnout.turnout_female_pc) as tf_pc,

    sum(voters_turnout.turnout_other_1) as to_1, 
    sum(voters_turnout.turnout_other_1_sangha) as to_1_sangha, 
    sum(voters_turnout.turnout_other_2) as to_2,
    sum(voters_turnout.turnout_other_2_sangha) as to_2_sangha,
    sum(voters_turnout.turnout_other_3) as to_3,
    sum(voters_turnout.turnout_other_3_sangha) as to_3_sangha,
    sum(voters_turnout.turnout_other_4) as to_4,
    sum(voters_turnout.turnout_other_4_sangha) as to_4_sangha,
    sum(voters_turnout.turnout_other_5) as to_5,
    sum(voters_turnout.turnout_other_5_sangha) as to_5_sangha,
    sum(voters_turnout.turnout_other_6) as to_6,
    sum(voters_turnout.turnout_other_6_sangha) as to_6_sangha,
    sum(voters_turnout.turnout_other_pc) as to_pc,

    sum(polling_station.electors_male) as em,
    sum(polling_station.electors_male_sangha) as em_sangha,
    sum(polling_station.electors_female) as ef,
    sum(polling_station.electors_female_sangha) as ef_sangha,
    sum(polling_station.electors_other) as eo,
    sum(polling_station.electors_other_sangha) as eo_sangha,
    sum(polling_station.electors_total) as et,
    sum(polling_station.electors_total_sangha) as et_sangha
FROM 
    polling_station 
LEFT JOIN voters_turnout
ON polling_station.ps_code = voters_turnout.fk_polling_station_code
WHERE fk_assembly_const_no = 14