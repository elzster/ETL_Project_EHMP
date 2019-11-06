-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "aaa_gas_prices" (
    "current_avg" text   NOT NULL,
    "regular_gas" float   NOT NULL,
    "mid_grade_gas" float   NOT NULL,
    "premium_gas" float   NOT NULL,
    "diesel_gas" float   NOT NULL,
    "e85_gas" float   NOT NULL
);

CREATE TABLE "fuelly_fuelup_log" (
    "user" text   NOT NULL,
    "year" int   NOT NULL,
    "make" text   NOT NULL,
    "model" text   NOT NULL,
    "mpg" float   NOT NULL,
    CONSTRAINT "pk_fuelly_fuelup_log" PRIMARY KEY (
        "make","model"
     )
);

CREATE TABLE "car_stats" (
    "make" text   NOT NULL,
    "model" text   NOT NULL,
    "unit_sales" float   NOT NULL,
    "vehicle_type" text   NOT NULL,
    "msrp_price" float   NOT NULL,
    "horsepower" float   NOT NULL,
    "curb_weight" float   NOT NULL,
    "fuel_capacity" float   NOT NULL,
    "mpg" float   NOT NULL,
    CONSTRAINT "pk_car_stats" PRIMARY KEY (
        "fuel_capacity"
     )
);

ALTER TABLE "car_stats" ADD CONSTRAINT "fk_car_stats_make" FOREIGN KEY("make")
REFERENCES "fuelly_fuelup_log" ("");

ALTER TABLE "car_stats" ADD CONSTRAINT "fk_car_stats_model" FOREIGN KEY("model")
REFERENCES "fuelly_fuelup_log" ("");

