import pandas as pd
import numpy as np

import logging
logger = logging.getLogger(__name__)

licenses = [
    "grbgetkey d0c17ef4-784e-49c1-95ac-3731a780daa4",
	"grbgetkey 88668cd6-c2a3-4760-acc9-27c7741fc145",
	"grbgetkey 085f3881-9b5c-4270-8287-1608da12cc81",
	"grbgetkey 24fa0ee1-9a91-46ae-9952-ad6bb84cea07",
	"grbgetkey 3b4a89aa-ba4a-49e7-974e-b12d571160b3",
	"grbgetkey a3cc0718-c14f-4f24-9db8-ab83bb8efaff",
	"grbgetkey 7e1ecd17-64e4-4399-8135-ef8485e415d4",
	"grbgetkey e5ee02e0-6444-44c0-a5d1-9616b3c7da8d",
	"grbgetkey 767aee65-a66f-486d-94d9-6482443bba1a",
]

df = pd.DataFrame({
	"licences": licenses,
	"used": np.zeros(len(licenses)).astype(bool).tolist()})

df.to_csv("licence_storage.csv")

logger.info("Created licences!")
