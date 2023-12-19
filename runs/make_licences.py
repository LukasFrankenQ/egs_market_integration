import pandas as pd
import numpy as np

import logging
logger = logging.getLogger(__name__)

licenses = [
	"grbgetkey 9112222f-c2dd-4932-91f2-7cd29b342bf5",
	"grbgetkey 868a3317-3f57-4200-9632-e03eb3a2728d",
	"grbgetkey 6be9853f-edc7-443a-b310-41337293450d",
	"grbgetkey de153697-9e7e-45b2-b316-522fb853abd7",
	"grbgetkey e8836e74-bf75-47c8-bf2f-7a304ba3feef",
	"grbgetkey 9dd6b3d3-8abd-44c3-8fc0-0758667028dc",
]

df = pd.DataFrame({
	"licences": licenses,
	"used": np.zeros(len(licenses)).astype(bool).tolist()})

df.to_csv("licence_storage.csv")

logger.info("Created licences!")
