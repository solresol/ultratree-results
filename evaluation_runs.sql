PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE evaluation_runs (
                   evaluation_run_id integer primary key,
                   evaluation_start_time timestamp default current_timestamp,
                   evaluation_end_time timestamp,
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
INSERT INTO evaluation_runs VALUES(1,'2024-12-03 07:52:03',NULL,'Initial validation checking','/ultratree/language-model/tiny.sqlite','nodes',25,'2024-11-29 13:00:00+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',NULL,NULL,NULL,NULL);
INSERT INTO evaluation_runs VALUES(2,'2024-12-03 07:55:14','2024-12-03 07:55:18','Initial validation checking','/ultratree/language-model/tiny.sqlite','nodes',25,'2024-11-29 13:00:00+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1236.66015625,12.0,0.0);
INSERT INTO evaluation_runs VALUES(3,'2024-12-03 07:56:05','2024-12-03 07:56:57','Default daily 2024-11-30','/ultratree/language-model/tiny.sqlite','nodes',919,'2024-11-30 13:00:00+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1223.1953125,389.811175337186909,0.288375080282594731);
INSERT INTO evaluation_runs VALUES(4,'2024-12-03 08:11:06','2024-12-03 08:11:59','Default daily 2024-12-01','/ultratree/language-model/tiny.sqlite','nodes',1325,'2024-12-01 13:00:00+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1222.169921875,390.899807321772641,0.294797687861271695);
INSERT INTO evaluation_runs VALUES(5,'2024-12-03 08:12:31','2024-12-03 08:13:24','Default daily 2024-12-02','/ultratree/language-model/tiny.sqlite','nodes',1713,'2024-12-02 13:00:00+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1222.294921875,391.445086705202299,0.299293513166345559);
INSERT INTO evaluation_runs VALUES(6,'2024-12-03 09:48:24','2024-12-03 09:49:17','Default daily 2024-12-03','/ultratree/language-model/tiny.sqlite','nodes',2085,'2024-12-03 13:00:00+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1225.919921875,392.086062941554246,0.327552986512524069);
INSERT INTO evaluation_runs VALUES(7,'2024-12-03 13:00:01','2024-12-03 13:00:53','Default daily 2024-12-04','/ultratree/language-model/tiny.sqlite','nodes',2085,'2024-12-04 00:00:01+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1225.919921875,392.086062941554246,0.327552986512524069);
INSERT INTO evaluation_runs VALUES(8,'2024-12-04 13:00:01','2024-12-04 13:00:53','Default daily 2024-12-05','/ultratree/language-model/tiny.sqlite','nodes',2967,'2024-12-05 00:00:01+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1225.734375,393.136159280667925,0.330122029543994888);
INSERT INTO evaluation_runs VALUES(9,'2024-12-05 13:00:01','2024-12-05 13:01:08','Default daily 2024-12-06','/ultratree/language-model/tiny.sqlite','nodes',3625,'2024-12-06 00:00:01+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1223.623046875,394.070006422607605,0.337829158638407178);
INSERT INTO evaluation_runs VALUES(10,'2024-12-06 03:04:45','2024-12-06 03:04:49','First node','/ultratree/language-model/tiny.sqlite','nodes',1,'2024-11-29 12:16:40+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1236.6669921875,0.0,0.0);
INSERT INTO evaluation_runs VALUES(11,'2024-12-06 03:05:47','2024-12-06 03:05:51','Half-hour mark','/ultratree/language-model/tiny.sqlite','nodes',7,'2024-11-29 12:30:00+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1236.66796875,3.0,0.0);
INSERT INTO evaluation_runs VALUES(12,'2024-12-06 13:00:01','2024-12-06 13:00:58','Default daily 2024-12-07','/ultratree/language-model/tiny.sqlite','nodes',4227,'2024-12-07 00:00:01+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1222.7080078125,394.533076429030188,0.338471419396274897);
INSERT INTO evaluation_runs VALUES(13,'2024-12-07 13:00:01','2024-12-07 13:00:55','Default daily 2024-12-08','/ultratree/language-model/tiny.sqlite','nodes',4751,'2024-12-08 00:00:01+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1221.591796875,394.994219653179186,0.339755940912010279);
INSERT INTO evaluation_runs VALUES(14,'2024-12-08 13:00:01','2024-12-08 13:00:54','Default daily 2024-12-09','/ultratree/language-model/tiny.sqlite','nodes',5337,'2024-12-09 00:00:01+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1221.5341796875,395.652536929993573,0.341682723185613379);
INSERT INTO evaluation_runs VALUES(15,'2024-12-09 13:00:02','2024-12-09 13:00:55','Default daily 2024-12-10','/ultratree/language-model/tiny.sqlite','nodes',6137,'2024-12-10 00:00:01+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1221.302734375,396.575465639049468,0.343609505459216424);
INSERT INTO evaluation_runs VALUES(16,'2024-12-10 13:00:01','2024-12-10 13:00:54','Default daily 2024-12-11','/ultratree/language-model/tiny.sqlite','nodes',7091,'2024-12-11 00:00:01+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1222.7939453125,397.476557482337852,0.345536287732819524);
INSERT INTO evaluation_runs VALUES(17,'2024-12-11 13:00:01','2024-12-11 13:01:07','Default daily 2024-12-12','/ultratree/language-model/tiny.sqlite','nodes',7745,'2024-12-12 00:00:01+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1222.908203125,397.884393063583843,0.346820809248554906);
INSERT INTO evaluation_runs VALUES(18,'2024-12-12 13:00:01','2024-12-12 13:00:53','Default daily 2024-12-13','/ultratree/language-model/tiny.sqlite','nodes',8443,'2024-12-13 00:00:01+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1223.150390625,398.357739242132311,0.348747591522158006);
INSERT INTO evaluation_runs VALUES(19,'2024-12-13 13:00:01','2024-12-13 13:00:53','Default daily 2024-12-14','/ultratree/language-model/tiny.sqlite','nodes',8885,'2024-12-14 00:00:01+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1224.283203125,398.600513808606308,0.350674373795761051);
INSERT INTO evaluation_runs VALUES(20,'2024-12-14 13:00:01','2024-12-14 13:00:54','Default daily 2024-12-15','/ultratree/language-model/tiny.sqlite','nodes',9827,'2024-12-15 00:00:01+00:00',16,'/ultratree/language-model/validation.sqlite','training_data','inferences',1557,1224.267578125,398.935773924213208,0.350674373795761051);
INSERT INTO evaluation_runs VALUES(21,'2024-12-15 02:17:12','2024-12-15 02:18:05','Default daily 2024-12-15','/ultratree/language-model/tiny.sqlite','nodes',10209,'2024-12-15 13:17:12+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1224.267578125,399.087989723827888,0.350674373795761051);
INSERT INTO evaluation_runs VALUES(22,'2024-12-15 02:18:05','2024-12-15 02:18:11','Default daily 2024-12-15','/ultratree/language-model/sense-annotated2.sqlite','nodes',53,'2024-12-15 13:18:05+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1237.390625,25.9775208734746314,0.0301862556197816309);
INSERT INTO evaluation_runs VALUES(23,'2024-12-15 02:18:11','2024-12-15 02:18:17','Default daily 2024-12-15','/ultratree/language-model/sense-annotated3.sqlite','nodes',57,'2024-12-15 13:18:11+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1238.171875,27.8420038535645488,0.0115606936416184965);
INSERT INTO evaluation_runs VALUES(24,'2024-12-15 02:18:17','2024-12-15 02:18:24','Default daily 2024-12-15','/ultratree/language-model/sense-annotated4.sqlite','nodes',65,'2024-12-15 13:18:17+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1237.46875,31.9755940912010281,0.00192678227360308282);
INSERT INTO evaluation_runs VALUES(25,'2024-12-15 02:18:24','2024-12-15 02:18:31','Default daily 2024-12-15','/ultratree/language-model/sense-annotated5.sqlite','nodes',61,'2024-12-15 13:18:24+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1236.6767578125,29.8497109826589586,0.0109184328837508021);
INSERT INTO evaluation_runs VALUES(26,'2024-12-15 02:18:31','2024-12-15 02:18:38','Default daily for unnotated data model #1 2024-12-15','/ultratree/language-model/unannotated-model1.sqlite','nodes',77,'2024-12-15 13:18:31+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1237.4296875,38.0,0.0);
INSERT INTO evaluation_runs VALUES(27,'2024-12-15 13:00:01','2024-12-15 13:00:53','Default daily 2024-12-16','/ultratree/language-model/tiny.sqlite','nodes',10289,'2024-12-16 00:00:01+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1224.267578125,399.123956326268455,0.35131663455362877);
INSERT INTO evaluation_runs VALUES(28,'2024-12-15 13:00:53','2024-12-15 13:01:01','Default daily 2024-12-16','/ultratree/language-model/sense-annotated2.sqlite','nodes',83,'2024-12-16 00:00:53+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1225.9921875,40.2646114322414874,0.0590879897238278731);
INSERT INTO evaluation_runs VALUES(29,'2024-12-15 13:01:01','2024-12-15 13:01:11','Default daily 2024-12-16','/ultratree/language-model/sense-annotated3.sqlite','nodes',113,'2024-12-16 00:01:01+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1240.6318359375,55.023763648041104,0.0610147719974309596);
INSERT INTO evaluation_runs VALUES(30,'2024-12-15 13:01:11','2024-12-15 13:01:23','Default daily 2024-12-16','/ultratree/language-model/sense-annotated4.sqlite','nodes',139,'2024-12-16 00:01:11+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1223.85546875,67.828516377649322,0.0719332048811817531);
INSERT INTO evaluation_runs VALUES(31,'2024-12-15 13:01:23','2024-12-15 13:01:34','Default daily 2024-12-16','/ultratree/language-model/sense-annotated5.sqlite','nodes',129,'2024-12-16 00:01:23+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1233.62890625,63.3474630700064196,0.016698779704560053);
INSERT INTO evaluation_runs VALUES(32,'2024-12-15 13:01:34','2024-12-15 13:01:43','Default daily for unnotated data model #1 2024-12-16','/ultratree/language-model/unannotated-model1.sqlite','nodes',121,'2024-12-16 00:01:34+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1237.43359375,60.0,0.0);
INSERT INTO evaluation_runs VALUES(33,'2024-12-15 21:16:07','2024-12-15 21:16:11','Default daily 2024-12-16','/ultratree/language-model/sense-annotated1.sqlite','nodes',1,'2024-12-16 08:16:07+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1236.6669921875,0.0,0.0);
INSERT INTO evaluation_runs VALUES(34,'2024-12-15 21:16:11','2024-12-15 21:16:19','Default daily 2024-12-16','/ultratree/language-model/sense-annotated2.sqlite','nodes',83,'2024-12-16 08:16:11+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1225.9921875,40.2646114322414874,0.0590879897238278731);
INSERT INTO evaluation_runs VALUES(35,'2024-12-15 21:16:19','2024-12-15 21:16:29','Default daily 2024-12-16','/ultratree/language-model/sense-annotated3.sqlite','nodes',113,'2024-12-16 08:16:19+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1240.6318359375,55.023763648041104,0.0610147719974309596);
INSERT INTO evaluation_runs VALUES(36,'2024-12-15 21:16:29','2024-12-15 21:16:40','Default daily 2024-12-16','/ultratree/language-model/sense-annotated4.sqlite','nodes',139,'2024-12-16 08:16:29+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1223.85546875,67.828516377649322,0.0719332048811817531);
INSERT INTO evaluation_runs VALUES(37,'2024-12-15 21:16:40','2024-12-15 21:16:52','Default daily 2024-12-16','/ultratree/language-model/sense-annotated5.sqlite','nodes',129,'2024-12-16 08:16:40+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1233.62890625,63.3474630700064196,0.016698779704560053);
INSERT INTO evaluation_runs VALUES(38,'2024-12-15 21:16:52','2024-12-15 21:17:01','Default daily for unnotated data model #1 2024-12-16','/ultratree/language-model/unannotated-model1.sqlite','nodes',123,'2024-12-16 08:16:52+00:00',16,'/ultratree/language-model/testdata.sqlite','training_data','inferences',1557,1236.90625,61.0,0.0);
COMMIT;