CREATE TABLE user (
	username varchar(30) primary key NOT NULL
);

CREATE TABLE items(
	key int primary key NOT NULL;
	text varchar(30) NOT NULL,	
	status boolean,
	FOREIGN KEY(user) references user(username)
	);
