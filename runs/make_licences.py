import pandas as pd
import numpy as np

import logging
logger = logging.getLogger(__name__)

licenses = [
	"grbgetkey a1643af9-04d4-4dd1-97dd-b7c924ff11e9",
	"grbgetkey 9edacadc-fa1a-4b15-abce-bd615f48bdb1",
	"grbgetkey ab12d03c-63c6-4c59-bab2-0d10340eb684",
	"grbgetkey b41efcbc-52f8-48c5-8eec-a9d583cfb651",
	"grbgetkey f64b2ecd-b11a-4cc1-94ca-9ff5a162f474",
	"grbgetkey 3f1c78ba-672f-4e5c-8c87-a7df7c54451d",
	"grbgetkey c3dd6140-a670-42b8-9a19-f64370a66c09",
	"grbgetkey 1e1bcc5f-5d4a-4ea5-9b4e-154b9b47ddf3",
	"grbgetkey 2d661014-e0b4-47b2-9572-ef3892806f9c",
]

df = pd.DataFrame({
	"licences": licenses,
	"used": np.zeros(len(licenses)).astype(bool).tolist()})

df.to_csv("licence_storage.csv")

logger.info("Created licences!")
