drop table if exists entries;
create table entries(
	id interger primary key autoncrement,
	title text not null,
	'text' text not null
);