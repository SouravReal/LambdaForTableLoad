import boto3
db_name = ["aananda_lakshmi", "abbnew", "abbottind", "abbpower_projectssil", "acclimited", "ADAG_RBNL", "ADAG_RCAP", "ADAG_RCOMM", "ADAG_RHFL", "ADAG_RINFR", "ADAG_RNEL", "adag_rpower", "ADAG_RPOWER", "adani", "adbirlafin", "adityabirla_sunlifeamcl", "affle_ipl", "agarwal_floatglassil", "agro", "agrotechfl", "ail", "airan", "akshoptifibre", "alirox", "allsec", "ALPHAGEO", "alstom", "amberent", "ambition_mica", "amd", "amfebconl", "amin_tanneryl", "anjanicem", "anupam_rasayanil", "aplnew", "apollo_tyresl", "appml", "aptech", "aptus_valuehfilfv2", "archid_decor", "archid", "arihantil", "ashok_masala", "asianeast", "asiannorth", "asianwest", "asl", "aslind", "asmtech", "atlanta", "b3mindia", "bajajauto", "bajajautofin", "bajajcorp", "bajajfinserv", "bajajholding", "balaji", "balarampur", "balkrishna", "balmerlawrie", "bambino", "bandhan_bank", "bang", "bangsoft", "bellacasa_fashion", "belnew", "beml", "bgil", "bgnmetals", "bharat_roadnl", "bharat_wireropes", "bhartinfra", "bhoruka", "biocon", "birla", "bnagarwood", "bnr", "bob", "bombayburmah", "bombaydyeing", "bommid", "bpl", "brigade", "britannia", "bse", "bstran", "btvl", "CANARA", "capacite_ipl", "capitalind_finltd", "carbonew", "care", "castrol_indial", "cccl", "cel", "celestial", "cerebra", "cfleng", "cgcel", "chalet_hotels", "chemplast_sanmarl", "chola", "cini", "cipla", "cleducate_new", "commeng", "coromandel", "coxkings_fsl", "coxnkings", "cpcl", "crisil", "cubehighways_trustinvit", "dabur", "dalmia_bharatrefral", "darshan_ornal", "dbl", "dcbnew", "dcmsil_new", "deccan", "deccanpoly", "deepakfpc", "denetworks", "devyani_intll", "dhyaani_marblez", "diamond", "digicontentl", "disl", "divi", "dixon_techil", "dlfnew", "dlinknew", "dodladairy", "dpcorp", "dqent", "dynamatic", "eastern_logicainfowayl18", "easytrip_plan", "eclerx", "eidnew", "electro", "electronics_mil", "elin_electronics", "enil", "epcind", "equitas_smallfbl", "escorts", "ethos_ltd", "euro_indiaffl", "fine_organicil", "fino_paymentsbankl", "finolexcables", "finolexind", "fintech", "fit", "fivestar_busfin", "flora_textiles", "fortishealthcare", "fortismalar", "fortunenew", "foursoft", "gabnew", "galaprint", "gandhi", "ganga_pharma", "gatpro", "gautam_gemsl", "gayatri_highways", "general_icil", "gg_engineeringl", "gichousing", "glenmark_lifesl", "glennew", "global_healthpleqcla", "gmrferro", "gmrinfra", "gmrpower_urbaninfra", "godrej_agrovet", "godrej", "goenka", "gofashion_indiapl", "gokaldas", "gowralfl", "gppl", "grameen_financial", "granules_india", "grasim", "gravita", "greatescl", "greavescot", "grinfra_projl", "gujarat_gas", "gujpetro", "gujrat_narmadavfcl", "gulflubricant", "gulfoilnew", "gvkpower", "gxpharma", "hal", "handson", "happiest_mindstpl12", "hblnife", "hdfc_amcl", "hdfclife", "hdil", "healthcare_global", "hero", "hexawaretech", "hfl", "himat", "hindfluro", "hindmotors", "hindujaglob", "hindujaven", "hindustan_aeronautics", "hindzinc", "hll", "hmtltd", "hmvl", "homefirst_financecil", "hpleletricpl", "htmedia_new", "husyscl", "ibr", "ibsinfra", "ibspower", "ibullshousing", "ibwsl", "icici_prudential", "icici_securities", "icicibank", "icicilombard", "idbi", "idfc", "idfcbank", "ielnew", "igl", "india_pesticidesl_23", "indiabulls_enterprises", "indiagreen", "indiagrid_trust", "indiancard", "indianenergy", "indigo", "infosys", "innovent", "intertec", "iocl", "irbinfra", "irbinvit", "ishan_intll", "ismtltd", "itdc", "itt", "iventure", "ivrclnew", "jagran", "jaypeeinfra", "jcl", "jetair", "jfllife_sciencesl", "jindal", "jindalinvestment", "jkb", "jmfinltd", "jswholdings", "jtpcl", "jupiter_infomedia", "justdial", "jvsl", "kaarya_fsl", "kale", "kartik_investments", "kenvi_jewelsl", "kernex", "kesar_indial", "kew", "kispat", "kmfeqt", "kms_medisurgi", "kpitengineering", "krebsbio", "krone", "krsnaa_diagnosticspl", "kshitij_polylinel", "kskenergy", "ksl", "larsentoubro", "laserdot", "lauruslabs", "laxmi_goldornahl", "lemontree", "licofindia", "LICOFINDIA", "linde_india", "lnttechsl", "lokesh", "lumax", "lux", "madhucon", "mafatlal", "mahascooter", "mahfin", "mahlifedev", "majesco", "manav_infrapl", "mangalam_seeds", "mankind_pharma28", "manpasand", "maruti", "mascon", "masl", "mastek", "matrimony", "maytas", "mcx", "mdinductocl", "medplus_healthslfv2", "meera_ind", "merck", "mholi", "millitoons", "mindspace_businessparks", "mirza", "mmltd", "modi", "moschip", "mothersn", "motherson_sumiwil", "mrotek", "mspsteel", "mtar_techpl", "mukand", "mukandpref", "music_broadcast", "nalco", "nanavati_venturespl", "narayanahrud", "narmada_agrobasel", "navigantcal", "navinfil", "nccblue", "nccfinance", "nccltd", "ndtv", "nectar", "net4india", "newgen_softl", "newlandlab", "nitesh", "nocil", "noida", "nouritrans_eximl", "nucleus", "nvbnew", "odisha_cement", "oilindia", "onelifecal", "onmobile", "opal_luxury", "opto", "oracle_fssl", "orient_cement", "orient_electric", "orient_paperil", "ortelcomm", "ortinlab", "padmalay", "palm_jewelsl", "pankajpoly", "paragmilk", "parin_furniture", "pasari", "pcjewel", "pcleqt", "pennarind", "penta_gold", "perfect_infraengl", "pfcl", "pfizer", "pgelectro", "philipslil", "phillips_dail", "phillips", "photancap", "piind", "pokarna", "polycab", "polyplex", "power_mechpl", "powergrid", "prabhat_dairy", "prataap_snacks", "premierexp", "prithvi", "psl", "psp_projects", "ptcindia", "pudumjee_paper", "pudumjee", "pulsar_intlltd", "punj", "pvpven", "pvr", "raasient_new", "radico_khaitan", "rainbow", "raincom", "ramkey", "ratravel_tech", "ravidist", "ravindra_energy", "relaxo", "reliance_nippon", "religare", "relstruct_buildcon", "renuka", "repco_home", "rfl", "riddhi_steel", "ro_jewelsl", "routesms", "rss", "rtechnologies", "rtechnova", "sagar", "sagarcem", "salasarext", "salsteel", "samor_realityl", "sasken", "sayaji", "sbilife", "scandent", "sequent_scientific", "sesagoa", "shalby", "shankara_iml", "sharda_cropchem", "shashwat_furnishingsl", "sheetal_coolpl", "sheshadri_ind", "shilpa", "shiva_cementl", "shoppers", "shriram_propertiesl", "shristiinfra", "shyam_metalicsel", "siddharth_esl", "sipm", "sirca_paintsil", "sk_intlexportl", "skanska", "smartlink", "smgoldl", "softsol", "solnew", "sona", "sonaforg", "sonata", "sotl", "spandana", "splind", "sps", "sqlstar", "sreenath_invcl", "srei_equity", "srfltd", "srfpolymers", "srirama", "ssp", "starhealth", "starpaper", "stdind", "stove_kraftpl", "strides", "subex_ltd", "sula_vineyardspl", "sunrise_efficientml", "sunrise_indtl", "suntv", "supertan", "surana", "suranaven", "suratex", "suryaamba", "suryachakra", "suryajyoti", "suryalata", "suryalcot", "suryavspin", "suryoday_mfl", "suven_18", "suvenew", "suzlon_rights", "suzlon", "syngene_intl", "talbros", "tanla", "tarsons", "tbl", "tci_developers", "tci_express", "tci", "tcnsccl_fv2", "teamleasesl", "terasoft", "texmaco", "texmacorail", "texmopipe", "thermex", "thomas", "tifinancial_fv1", "torent", "transport_corp", "tribhovandas", "trident_ltd", "trident_texofabl", "trigyntech", "triveni", "ttk", "tubeindia_fv1", "tulip", "uco", "ufo_moviezil", "uhzaveril", "ujjivan_smallfbl", "ujjivan", "ultratech", "UNION_BANK", "universal_autofoundry", "universusphoto", "upal", "utiasset", "utinew", "vascon", "vatech", "vedant_fashionspleqfv1", "veekayem_fashionappl", "veeram_ornaments", "veeraminfra", "veerkrupa_jewellersl", "venus_pipestubesl", "veranda_learningspl", "vertozadv", "vgl", "vijaya_diagnosticcl", "vintage", "visakaind_fv2", "visasteel", "vishal_bearings", "vishal", "vmartretail", "vppil", "vrl_logistics", "vstind", "vtmltd", "wendt", "wipro", "wonder_fibromatsl", "wonderla", "xelpmoc_dtl", "yesbank", "yuken", "zenotech", "zensartech", "zentech", "zodiac"]

table_name = ["all_benpos", "alldiv", "alldiv_bank", "benmast", "certno1", "certno2", "certno3", "certno4", "certno5", "certno6", "cs_cerdet", "cs_tran", "ddmast", "dividend_f15g_master", "dividend_master", "ecsrejmast", "holder_phone", "holder1", "holder10", "holder12", "holder2", "holder3", "holder4", "holder4_nonall", "holder5", "holder6", "holder7", "holder9", "iepf_alldiv", "Iepf_alldiv_bank", "Iepf_benmast", "iepf_claim_master", "iepf_claim_master_dividend", "iepf_claim_master_shares", "iepf_final_master", "LockinMast", "nominee", "nominee_opt_out", "ns_cerdet", "ns_tran", "paid_tran", "PledgeMast", "post_cl5a_mast", "postcert", "postretn", "queryrlmast", "querytran1", "querytran2", "querytran3", "querytran4", "querytran5", "querytran6", "querytran7", "querytran8", "refund", "webdiff", "webmis"]

def load_table_from_s3_to_athena(bucket_name, object_key, db_nam, columns_final):
  table_name = db_nam+"_"+object_key
  """Loads a table from S3 to Athena.

  Args:
    bucket_name: The name of the S3 bucket that contains the table data.
    object_key: The key of the S3 object that contains the table data.
    table_name: The name of the Athena table to load the data into.
  """

  ath_client = boto3.client("athena")

  # Create the Athena query to load the data.
  query = """
    CREATE EXTERNAL TABLE {table_name}
    (
      {columns_final}
    )
    STORED AS PARQUET
    LOCATION 'bucket_name'
    TBLPROPERTIES ('skip.header.line.count'='1')
  """.format(
      table_name=table_name,
      bucket_name=bucket_name,
      object_key=object_key,
  )

  # Run the Athena query.
  ath_client.start_query_execution(QueryExecutionId=query)

def initial_step_s3():
  s3_client = boto3.client("s3")
  bucket = ["s3://kfintech-crg-landing/fl/corpreg/"+db+"/dbo/" for db in db_name ]
  for bn in bucket:
    db_nam = ''

    for dbn in db_name:
      if dbn in bn:
        db_nam = dbn
    
    object_list = s3_client.list_objects(Bucket = bn)
    for obj in object_list:
      object_data = obj["Body"].read().decode("utf-8")
      columns = object_data.split(",")[0:-1] #here the columns variable contains list of all the columns in the particular table
      columns_string = "\""
      for ele in columns:
        columns_string += ele+"\" string, \n\"" #here the columns name are stored like how it should be in the create table command with a trailing , and an enter element
      
      columns_final = columns_string[:-4]

      load_table_from_s3_to_athena(bn, obj, db_nam, columns_final)


if __name__ == "__main__":
  initial_step_s3()
  # bucket_name = "my-bucket"
  # object_key = "my-table.parquet"
  # table_name = "my_table"
  # load_table_from_s3_to_athena(bucket_name, object_key, table_name)