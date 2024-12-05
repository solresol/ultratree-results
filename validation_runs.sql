PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE validation_runs (
                   validation_run_id integer primary key,
                   validation_start_time timestamp default current_timestamp,
                   validation_end_time timestamp,
                   description text not null,
                   model_file text not null,
                   model_table text not null,
                   model_node_count integer,
                   cutoff_date timestamp,
                   context_length integer,
                   validation_datafile text not null,
                   validation_table text not null,
                   output_table text not null,
                   number_of_data_points integer,
                   total_loss float,
                   average_depth float,
                   average_in_region_hits float
                );
INSERT INTO validation_runs VALUES(1,'2024-12-03 07:52:03',NULL,'Initial validation checking','/ultratree/language-model/tiny.sqlite','nodes',25,'2024-11-29 13:00:00+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',NULL,NULL,NULL,NULL);
INSERT INTO validation_runs VALUES(2,'2024-12-03 07:55:14','2024-12-03 07:55:18','Initial validation checking','/ultratree/language-model/tiny.sqlite','nodes',25,'2024-11-29 13:00:00+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1236.66015625,12.0,0.0);
INSERT INTO validation_runs VALUES(3,'2024-12-03 07:56:05','2024-12-03 07:56:57','Default daily 2024-11-30','/ultratree/language-model/tiny.sqlite','nodes',919,'2024-11-30 13:00:00+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1223.1953125,389.811175337186909,0.288375080282594731);
INSERT INTO validation_runs VALUES(4,'2024-12-03 08:11:06','2024-12-03 08:11:59','Default daily 2024-12-01','/ultratree/language-model/tiny.sqlite','nodes',1325,'2024-12-01 13:00:00+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1222.169921875,390.899807321772641,0.294797687861271695);
INSERT INTO validation_runs VALUES(5,'2024-12-03 08:12:31','2024-12-03 08:13:24','Default daily 2024-12-02','/ultratree/language-model/tiny.sqlite','nodes',1713,'2024-12-02 13:00:00+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1222.294921875,391.445086705202299,0.299293513166345559);
INSERT INTO validation_runs VALUES(6,'2024-12-03 09:48:24','2024-12-03 09:49:17','Default daily 2024-12-03','/ultratree/language-model/tiny.sqlite','nodes',2085,'2024-12-03 13:00:00+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1225.919921875,392.086062941554246,0.327552986512524069);
INSERT INTO validation_runs VALUES(7,'2024-12-03 13:00:01','2024-12-03 13:00:53','Default daily 2024-12-04','/ultratree/language-model/tiny.sqlite','nodes',2085,'2024-12-04 00:00:01+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1225.919921875,392.086062941554246,0.327552986512524069);
INSERT INTO validation_runs VALUES(8,'2024-12-04 13:00:01','2024-12-04 13:00:53','Default daily 2024-12-05','/ultratree/language-model/tiny.sqlite','nodes',2967,'2024-12-05 00:00:01+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1225.734375,393.136159280667925,0.330122029543994888);
INSERT INTO validation_runs VALUES(9,'2024-12-05 13:00:01','2024-12-05 13:01:08','Default daily 2024-12-06','/ultratree/language-model/tiny.sqlite','nodes',3625,'2024-12-06 00:00:01+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1223.623046875,394.070006422607605,0.337829158638407178);
COMMIT;
