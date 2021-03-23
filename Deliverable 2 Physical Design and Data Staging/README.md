This folder provides some original scripts of data staging, however many records (even some dimensions/tables) in database were modified/deleted for optimal performance of OLAP queries.

Late Version Changes:

Test_date, Onset_date, report_date, and specimen_date dimensions/tables are replaced by a role-playing dimension named by "Date"

Data from all tables before 2020-11-01 were considered irrelavant or trivial at the time, thus they were removed.
