import pandas as pd
import numpy as np

import logging
logger = logging.getLogger(__name__)

licenses = [
    "grbgetkey faecb389-b950-478e-8c81-ac915c205655",
	"grbgetkey fc30480e-fdae-4da0-81a3-80f0cf0be8d6",
	"grbgetkey 67a0f9b4-5ee8-4b6b-bc18-64aac828e097",
	"grbgetkey f3e788b3-ee5a-40fe-a575-a2bba9b55aab",
	"grbgetkey 83f7acf7-c378-49ab-b450-7f15b6be742a",
	"grbgetkey 1609e55d-93e6-4a56-98fb-ea2ea0348990",
	"grbgetkey e6c79067-2490-4a07-b973-a1eb3843d30a",
	"grbgetkey dc669901-a823-455a-b7f1-32d3fd59b99b",
	"grbgetkey 15decb79-a7ac-4e8f-89ea-5df952e20e25",
	"grbgetkey 8071d579-b611-4154-8329-ed6f7d19f289",
	"grbgetkey 1f83b932-34ab-4b71-95d5-0570fb23679d",
	"grbgetkey 2e00bc00-d3a5-4297-a7f4-903ccf752d82",
	"grbgetkey 12040f08-1194-4fbb-8e32-33db55af5775",
	"grbgetkey c05b45d2-8a8d-4688-a789-76751d078273",
	"grbgetkey 1fd3eccc-6a13-439a-8d02-0ea60d06fa89",
	"grbgetkey a4ee179d-72b3-4277-bbc2-473ab0a1b46e",
	"grbgetkey 2f0c0b1d-0fdb-4079-baf2-c6ed6dd89a5e",
	"grbgetkey f050f2a3-54e8-4d4a-8ff4-9f9e004b14de",
	"grbgetkey 0af90ac2-b73b-4c90-8ee9-cfe32cec9610",
	"grbgetkey 2feea501-c139-418f-a8e2-8e9da5356459",
	"grbgetkey ac4d4016-ab9e-4ee7-8fe5-995fec56b8e2",
	"grbgetkey dbe16e4f-f3db-4662-ac22-9a8e6cc02fd8",
]


df = pd.DataFrame({
	"licences": licenses,
	"used": np.zeros(len(licenses)).astype(bool).tolist()})

df.to_csv("licence_storage.csv")

logger.info("Created licences!")
