import pandas as pd
import numpy as np

import logging
logger = logging.getLogger(__name__)

licenses = [
    "grbgetkey 17832a74-2add-4f93-ad8f-26eb8f38c730",
	"grbgetkey ccfa6b53-747b-4f4c-826c-8da9d7a57bbf",
	"grbgetkey 78cbc89c-7cd9-4810-a7fa-7f2c8ee23c41",
	"grbgetkey 5f291124-6b36-49b1-84c9-86f81bdff7fb",
	"grbgetkey 07c84477-398c-4f7f-8cd7-c3711575761b",
	"grbgetkey a58b1a42-cdb5-4418-8287-85b7e0ac4345",
	"grbgetkey 8f0fad60-c99d-4b59-a29a-951e20ad34b1",
	"grbgetkey e638332b-c0c0-4866-9c1e-79d8ed3accf0",
	"grbgetkey 528cf718-83ae-4060-9767-f8c6fc319d4b",
	"grbgetkey 7e31ca52-dc82-458f-a36a-65a8378c1e60",
	"grbgetkey 70385a53-e8c8-4754-896e-c059029bed15",
	"grbgetkey 67004cf4-5aa2-4d16-aa94-72cc0962bb77",
	"grbgetkey 5392abfc-dda5-46c7-b942-27d0f0c84866",
	"grbgetkey 3055280f-b994-4f3b-9d9a-d54c9e98a692",
	"grbgetkey 1496f8bd-0c27-4269-b4d2-8d7b40717973",
	"grbgetkey 8ca465ad-14ad-4e90-898c-dbf358e80c98",
	"grbgetkey 0025912d-28df-4362-8cd5-a30b0a48389c",
	"grbgetkey 02b13ec7-ec9f-424c-a934-5a5701c58c1c",
	"grbgetkey 96ca4c85-08e0-41f3-86c3-b52db61a80cd",
]

df = pd.DataFrame({
	"licences": licenses,
	"used": np.zeros(len(licenses)).astype(bool).tolist()})

df.to_csv("licence_storage.csv")

logger.info("Created licences!")
