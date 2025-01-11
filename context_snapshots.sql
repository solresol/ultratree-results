PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE context_snapshots (
	context_snapshot_id integer primary key,
	filename text not null,
	when_captured timestamp default current_timestamp
);
INSERT INTO context_snapshots VALUES(1,'/ultratree/language-model/sense-annotated1.sqlite','2025-01-09 13:03:09');
INSERT INTO context_snapshots VALUES(2,'/ultratree/language-model/sense-annotated2.sqlite','2025-01-09 13:06:42');
INSERT INTO context_snapshots VALUES(3,'/ultratree/language-model/sense-annotated3.sqlite','2025-01-09 13:10:05');
INSERT INTO context_snapshots VALUES(4,'/ultratree/language-model/sense-annotated4.sqlite','2025-01-09 13:13:19');
INSERT INTO context_snapshots VALUES(5,'/ultratree/language-model/sense-annotated5.sqlite','2025-01-09 13:16:39');
INSERT INTO context_snapshots VALUES(6,'/ultratree/language-model/unannotated-model1.sqlite','2025-01-09 13:37:25');
INSERT INTO context_snapshots VALUES(7,'/ultratree/language-model/sense-annotated1.sqlite','2025-01-10 13:02:48');
INSERT INTO context_snapshots VALUES(8,'/ultratree/language-model/sense-annotated2.sqlite','2025-01-10 13:05:57');
INSERT INTO context_snapshots VALUES(9,'/ultratree/language-model/sense-annotated3.sqlite','2025-01-10 13:09:04');
INSERT INTO context_snapshots VALUES(10,'/ultratree/language-model/sense-annotated4.sqlite','2025-01-10 13:11:52');
INSERT INTO context_snapshots VALUES(11,'/ultratree/language-model/sense-annotated5.sqlite','2025-01-10 13:11:52');
INSERT INTO context_snapshots VALUES(12,'/ultratree/language-model/unannotated-model1.sqlite','2025-01-10 13:19:56');
COMMIT;
