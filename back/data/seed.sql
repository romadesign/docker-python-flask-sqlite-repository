BEGIN TRANSACTION;

INSERT INTO users VALUES 
 ('user1','user1@example.com','User 1','{hash_password[user1]}',1,'223366895','user1@example.com','bilbao'),
 ('user2','user2@example.com','User 2','{hash_password[user2]}',0,'55689854','user2@example.com','casco viejo'),
 ('user3','user3@example.com','User 3','{hash_password[user3]}',0,'55568842','user3@example.com','barakaldo'),
 ('user4','user4@example.com','User 4','{hash_password[user4]}',0,'2662266558',,'user4@example.com','muskiz');

COMMIT;
