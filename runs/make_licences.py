import pandas as pd
import numpy as np

import logging
logger = logging.getLogger(__name__)

licenses = [
	"grbgetkey 3b68259c-2742-411f-8a48-81169c3fe40c",
	"grbgetkey cde7d92b-f4ad-4766-a12b-b404d0c5bb0c",
	"grbgetkey a7f13fab-001a-4ae1-9220-a7f8ebc5b456",
	"grbgetkey 30001c26-88f2-11ed-84fc-0242ac120002",
	"grbgetkey aa1cc64c-67d4-4da1-a083-0423d03e1783",
	"grbgetkey f3d10857-317c-4254-b6a9-68caa8cb1c60",
	"grbgetkey 32454719-c8c9-4073-a7d5-e42b8da1e3cc",
	"grbgetkey c7d7e681-5f30-46aa-9640-05018b930b4e",
	"grbgetkey b9b9e96a-ba8c-49a3-ad2a-91b9e3034f39",
	"grbgetkey 67a0f9b4-5ee8-4b6b-bc18-64aac828e097",
]

df = pd.DataFrame({
	"licences": licenses,
	"used": np.zeros(len(licenses)).astype(bool).tolist()})

df.to_csv("licence_storage.csv")

logger.info("Created licences!")
