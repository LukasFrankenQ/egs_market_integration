import pandas as pd
import numpy as np

import logging
logger = logging.getLogger(__name__)

licenses = [
	"grbgetkey 130d46dc-6aae-42ad-a935-e212617f250b",
	"grbgetkey d7ce2d3e-2260-4a9b-a06d-cf0e18dfe2eb",
	"grbgetkey 9469eec7-6298-4e95-8148-dc40fd646369",
	"grbgetkey 5b8baeca-b746-40cc-9ed5-fc53f33d9da4",
	"grbgetkey fd2f5b68-438d-421d-b98f-ea4afa49cafe",
	"grbgetkey 66c1b46d-7cf1-4b5d-a344-58f65fac49f2",
	"grbgetkey 9145b0c7-1897-473f-9eeb-fb3042b8ac53",
	"grbgetkey f587b90f-4389-4fb8-ab21-c43cc86e976b",
	"grbgetkey 702f2b8a-a692-42c3-818c-6bd58faee738",
	"grbgetkey e3c21f15-dad6-4f62-880a-c722d71a9c57",
	"grbgetkey 6d679e65-b978-43ac-84dc-99fcbe182d09",
	"grbgetkey 5d9c65fb-cc0f-41a0-b31a-df8327defd61",
	"grbgetkey 5487c4c1-034a-4d1d-ae5a-4dbfe4c589a9",
	"grbgetkey b2bf9445-22d8-4c61-8c22-5dde3aa1c0bb",
	"grbgetkey e930d507-f34e-4c0f-ac1d-a2b4ac0a0004",
	"grbgetkey a736e9ed-5be8-4c88-b6cf-a44cef83a549",
	"grbgetkey 86930e1d-7d44-4872-8cd3-6afaccffade2",
	"grbgetkey 12c269dc-ce70-4ec5-8af2-f3944d8a0ef4",
	"grbgetkey 3af23811-c881-4c43-87fa-ccc585e0463b",
	"grbgetkey dd515635-9d0f-4889-bcd2-9b3426a31a09",
	"grbgetkey a1643af9-04d4-4dd1-97dd-b7c924ff11e9",
	"grbgetkey 9edacadc-fa1a-4b15-abce-bd615f48bdb1",
]

df = pd.DataFrame({
	"licences": licenses,
	"used": np.zeros(len(licenses)).astype(bool).tolist()})

df.to_csv("licence_storage.csv")

logger.info("Created licences!")
