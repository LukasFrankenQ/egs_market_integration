import pandas as pd
import numpy as np

import logging
logger = logging.getLogger(__name__)

licenses = [
    "grbgetkey 63e50355-16f5-4de7-ad98-3b7fc77891dd",
	"grbgetkey 70ebcac9-37a8-45e4-a3f6-3d48693041cc",
	"grbgetkey bc17d9c3-5e33-43da-b394-9faf2d82a4c2",
	"grbgetkey e83f2e53-f0db-4f0c-9a21-fd8e3792f883",
	"grbgetkey 72cfac25-bb69-4174-b3cf-587064d0d819",
	"grbgetkey 88605347-b0c2-4c37-b5a3-14197c555557",
]

df = pd.DataFrame({
	"licences": licenses,
	"used": np.zeros(len(licenses)).astype(bool).tolist()})

df.to_csv("licence_storage.csv")

logger.info("Created licences!")
