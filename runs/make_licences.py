import pandas as pd
import numpy as np

import logging
logger = logging.getLogger(__name__)

licenses = [
"grbgetkey ffe68c1b-2e26-45cb-b706-4cf0a0e75202",
"grbgetkey 873fe5c4-ba05-4d07-976e-7678967bafa0",
"grbgetkey abbaddfd-fe48-4c1e-94f6-59b1b10c3af9",
"grbgetkey 66e7a00c-aabc-4449-b782-1bda30509a37",
"grbgetkey 59e02367-b2c2-4825-a1cb-b8c03e4ebd2e",
"grbgetkey 92b5e277-d83b-494f-9dab-674ac2f36757",
"grbgetkey d58f7ab1-746f-4865-b391-0b47aa895eb3",
"grbgetkey 1ae1f806-4849-498b-8fd0-4f8af5587e32",
"grbgetkey 70a0c87c-1ce8-4b47-8c33-9a3d1ebc46b3",
"grbgetkey d7ca63f1-3c75-4cef-8f45-a0e12ce860cb",
"grbgetkey 1934bb4f-316f-4299-befc-dcbc13a5cee5",
"grbgetkey 8d4c641a-a2e4-4992-9c0a-c30b3c9c7c1e",
"grbgetkey fcef81e1-6654-4671-a297-2946a8628052",
"grbgetkey bbcc617e-bba0-448c-a932-7c3864ab09c5",
"grbgetkey 6d25aa1b-d556-48c6-a784-856491af656b",
"grbgetkey a301a2bc-9bc1-46fd-b702-a498976d7e5e",
]

df = pd.DataFrame({
	"licences": licenses,
	"used": np.zeros(len(licenses)).astype(bool).tolist()})

df.to_csv("licence_storage.csv")

logger.info("Created licences!")
