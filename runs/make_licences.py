import pandas as pd
import numpy as np

import logging
logger = logging.getLogger(__name__)

licenses = [
	"grbgetkey 300e8b96-40f1-42fe-aa94-bde4e7296751",
	"grbgetkey 37b5f866-3b4a-4eb4-99eb-097fafae5752",
	"grbgetkey 20f4c118-fc79-46b7-952c-b39867cc2837",
	"grbgetkey 980f7c5e-32d6-4fcb-bc99-1442726e36ea",
	"grbgetkey 7a7293eb-127f-48e8-97d7-801b693ed3e6",
	"grbgetkey 7cb8f6fa-4bc9-405b-bacf-a22220a26235",
	"grbgetkey 4e22ac08-4f0f-4fed-84d0-6248300c9fbd",
	"grbgetkey cfb66bba-b061-4a52-ab03-cb4239b98378",
	"grbgetkey 44a9b6d8-7ed6-41cc-81b0-536d417bd0d1",
	"grbgetkey 14fbed5c-40a8-4f04-80d7-954627f4ca76",
	"grbgetkey 136a7033-c78d-446a-ba61-784a95c10fb5",
	"grbgetkey 1b71b9e9-af8b-4202-ab23-1cd21748984f",
	"grbgetkey 130d46dc-6aae-42ad-a935-e212617f250b",
]

df = pd.DataFrame({
	"licences": licenses,
	"used": np.zeros(len(licenses)).astype(bool).tolist()})

df.to_csv("licence_storage.csv")

logger.info("Created licences!")
