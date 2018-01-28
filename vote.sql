drop table if exists wx_vote_info;
CREATE TABLE wx_vote_info (
  vote_id INTEGER PRIMARY KEY autoincrement,
  timestamp integer NOT Null,
  initiator string NOT NULL,
  items string NOT null,
  valid INT NOT NULL,
);

drop table if exists wx_vote_user;
CREATE TABLE wx_vote_user (
  id INTEGER PRIMARY KEY autoincrement,
  timestamp integer NOT Null,
  FOREIGN KEY
);
