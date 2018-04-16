# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 10:52:42 2017

@author: wc57661
"""

import pyspark


pyspark
sqlCtx = SQLContext(sc)
df = sqlCtx.read.format("com.databricks.spark.avro").load("/data/gftrrhrn/managed/CCAR14A_EA_TEST/GC20/CCAR14A_ENRICHED_ACCOUNT/batch_id=1009451")
df.registerTempTable("base");



sqlCtx.sql("select sum(PAYMENT_MISSED_COUNT), min(PAYMENT_MISSED_COUNT), max(PAYMENT_MISSED_COUNT), count(1) from base").show()

sqlCtx.sql("select sum(ARM_INITIAL_RATE_PERIOD), min(ARM_INITIAL_RATE_PERIOD), max(ARM_INITIAL_RATE_PERIOD), count(1) from base").show()

sqlCtx.sql("select sum(NUMBER_OF_BORROWERS), min(NUMBER_OF_BORROWERS), max(NUMBER_OF_BORROWERS), count(1) from base").show()
