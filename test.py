db_name = ["aananda_lakshmi", "abbnew", "abbottind", "abbpower_projectssil", "acclimited", "ADAG_RBNL", "ADAG_RCAP", "ADAG_RCOMM", "ADAG_RHFL", "ADAG_RINFR", "ADAG_RNEL", "adag_rpower", "ADAG_RPOWER", "adani", "adbirlafin", "adityabirla_sunlifeamcl", "affle_ipl", "agarwal_floatglassil", "agro", "agrotechfl", "ail", "airan", "akshoptifibre", "alirox", "allsec", "ALPHAGEO", "alstom", "amberent", "ambition_mica", "amd", "amfebconl", "amin_tanneryl", "anjanicem", "anupam_rasayanil", "aplnew", "apollo_tyresl", "appml", "aptech", "aptus_valuehfilfv2", "archid_decor", "archid", "arihantil", "ashok_masala", "asianeast", "asiannorth", "asianwest", "asl", "aslind", "asmtech", "atlanta"]
bucket = ["s3://kfintech-crg-landing/fl/corpreg/"+db+"/dbo/" for db in db_name ]
# for i in bucket:
#     print( i)
# for bn in bucket:

#     db_nam = ''

#     for dbn in db_name:
#       if dbn in bn:
#         db_nam = dbn
#     print(bn," ", db_nam)

columns = ['empid', 'name', 'salary', 'department', 'email']
columns_list = (*columns)
print(columns_list)



# "SCHEME"	 string,
# "KFIN PLAN" string,
# "AMC PLANID"	 string,
# "ACNO"	 string,
# "IHNO"	 string,
# "TRTYPE"	 string,
# "TRDT"	 string,
# "INVESTOR_NAME"	"PAN_NO"	 string,
# "CITY"	 string,
# "STATE"	 string,
# "COUNTRY"	 string,
# "STATUS"	 string,
# "BANKTYPE"	 string,
# "AGENTNAME"	 string,
# "COMMITMENTAMOUNT"	 string,
# "VALUEDATE"	 string,
# "NAVDT"	 string,
# "INITIAL_CONTRIBUTION"	 string,
# "SETUP_FEES"	 string,
# "GST"	 string,
# "STAMP_DUTY"	 string,
# "ALLOTMENT_AMOUNT"	 string,
# "NAV"	 string,
# "UNITS"	 string,
# "Topup_CONTRIBUTION"	 string,
# "SETUP_FEES"	 string,
# "STAMP_DUTY"	 string,
# "ALLOTMENT_AMOUNT"	 string,
# "UNITS"	 string,
# "Net contribution received"	 string,
# "Issued Units"	 string,
# "Principal repayment till date"	 string,
# "Units redeemed till date"	 string,
# "Outstanding Principal as on date"	 string,
# "Balance units as on date" string,


# bn = 's3://kfintech-crg-landing/fl/corpreg/aananda_lakshmi/dbo/'
# if 'aananda_lakshmi' in bn:
#     print(True)