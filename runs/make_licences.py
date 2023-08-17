import pandas as pd
import numpy as np

import logging
logger = logging.getLogger(__name__)

licenses = [
    "grbgetkey aa1cc64c-67d4-4da1-a083-0423d03e1783",
	"grbgetkey 1f5acd01-b274-4ffa-ae83-48ae81306399",
	"grbgetkey f3d10857-317c-4254-b6a9-68caa8cb1c60",
	"grbgetkey 32454719-c8c9-4073-a7d5-e42b8da1e3cc",
	"grbgetkey b7a11d1b-40ca-4900-a35b-8e4b49142235",
	"grbgetkey c7d7e681-5f30-46aa-9640-05018b930b4e",
	"grbgetkey 35afbae3-dc0c-48ce-bbdb-fd9601bc1597",
	"grbgetkey 33f2e5ee-f93f-4bf9-a885-30f684baaff3",
	"grbgetkey b1472d36-c77f-45bf-bada-74ee2ccae786",
	"grbgetkey 759eabf9-fb40-41c2-a135-df2ebc9360f2",
	"grbgetkey 2109f887-0672-42b4-9c3c-728368eeb9c2",
	"grbgetkey 9a17d54e-5f9a-46b1-80e9-5f38c2cfd988",
	"grbgetkey 23f28a93-f373-4c37-bba0-bcf0ea7195bc",
	"grbgetkey f0eadfaa-aa35-4584-92ab-a09a5a1a4f54",
	"grbgetkey 0ee4e398-fd74-4124-84f8-9e760c964d2d",
	"grbgetkey d25fbb58-a827-42bb-96b6-d81523a91262",
	"grbgetkey d6bab705-31f8-423c-bfb9-e8fba9dd40b5",
	"grbgetkey 13841d87-db47-4243-99c2-def4f2f42f88",
]

df = pd.DataFrame({
	"licences": licenses,
	"used": np.zeros(len(licenses)).astype(bool).tolist()})

df.to_csv("licence_storage.csv")

logger.info("Created licences!")
