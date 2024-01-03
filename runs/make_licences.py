import pandas as pd
import numpy as np

import logging
logger = logging.getLogger(__name__)

licenses = [
    "grbgetkey 29586845-df26-4d11-9514-1446b0500048",
	"grbgetkey fc8ca1df-7de2-4f10-bfa1-e7cc69076bc5",
	"grbgetkey c9b83b6a-2ea8-4030-a384-4ea5bf618181",
	"grbgetkey 51702d84-4f7c-42b4-bbbf-5f5e8ae816c0",
	"grbgetkey f10d030f-e101-423b-9c83-bb25fb421b05",
	"grbgetkey e8188ee2-4798-4a61-a92b-085acbc5bad6",
	"grbgetkey 9f5ffa46-85eb-4892-b915-a02eea3b85da",
	"grbgetkey a56070fd-5ea7-470a-b139-f71e40b80029",
	"grbgetkey ad819b23-9764-4a2c-9aa9-5edaac8862ba",
	"grbgetkey 300e8b96-40f1-42fe-aa94-bde4e7296751",
	"grbgetkey 37b5f866-3b4a-4eb4-99eb-097fafae5752",
	"grbgetkey 20f4c118-fc79-46b7-952c-b39867cc2837",
]

df = pd.DataFrame({
	"licences": licenses,
	"used": np.zeros(len(licenses)).astype(bool).tolist()})

df.to_csv("licence_storage.csv")

logger.info("Created licences!")
