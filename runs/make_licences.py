import pandas as pd
import numpy as np

import logging
logger = logging.getLogger(__name__)

licenses = [
	"grbgetkey 4c426f95-3d59-4cd1-a0d8-29f3b59995a1",
	"grbgetkey d519ea5f-d5c0-488d-a3fb-d157f8123033",
	"grbgetkey 38c2d7b3-be59-4371-bd2c-474a3310e165",
]

df = pd.DataFrame({
	"licences": licenses,
	"used": np.zeros(len(licenses)).astype(bool).tolist()})

df.to_csv("licence_storage.csv")

logger.info("Created licences!")
