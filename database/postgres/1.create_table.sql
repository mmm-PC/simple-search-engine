CREATE TABLE "posts" (
  "id" serial PRIMARY KEY,
  "rubrics" VARCHAR(32) ARRAY NOT NULL,
  "text" TEXT DEFAULT '',
  "created_date" TIMESTAMP NOT NULL);