BEGIN TRANSACTION;

INSERT INTO users VALUES 
 ('user-1','user-1@example.com','User 1','{hash_password[newtest1]}',1,'223366895','user-1@example.com','bilbao'),
 ('user-2','user-2@example.com','User 2','{hash_password[newtest1]}',0,'55689854','user-2@example.com','casco viejo'),
 ('user-3','user-3@example.com','User 3','{hash_password[newtest1]}',0,'55568842','user-3@example.com','barakaldo'),
 ('user-4','user-4@example.com','User 4','{hash_password[newtest1]}',0,'2662266558',,'user-4@example.com','muskiz');

COMMIT;
