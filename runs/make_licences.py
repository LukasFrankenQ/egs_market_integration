import pandas as pd
import numpy as np

import logging
logger = logging.getLogger(__name__)

licenses = [
	"grbgetkey 42a2fe6d-c69e-427a-8ae5-266e0a0b2ec2",
	"grbgetkey 7995c197-b304-4a78-9431-f91122d642bd",
	"grbgetkey 2ac05bb5-f8e7-4ec2-80f7-50b2e8285855",
	"grbgetkey 2b5bc8d6-74da-480d-8130-b4a1a448f49c",
	"grbgetkey 2516a63e-8947-41e9-b479-fafc5b46db55",
	"grbgetkey 64ee2354-4260-46cd-87c2-635d74890d57",
	"grbgetkey 90a8a61a-0eca-401b-82d8-eadcd1b7faf5",
	"grbgetkey e30041fb-8277-4df0-ac33-2ea902b77b22",
	"grbgetkey 92b3af65-0aa1-471f-ad46-c9f39b198b27",
	"grbgetkey 14e0daab-e62c-4031-97ae-9c020b82abd9",
	"grbgetkey a8e2cade-8f51-4545-9787-3604489163dd",
	"grbgetkey 3428251c-90eb-4aa4-88b4-1f20a7350645",
	"grbgetkey 06adf6eb-2d41-484e-8d98-f327aa5f3eb0",
	"grbgetkey 8d84eebe-3d02-4ff0-b0c9-81607e8b7710",
	"grbgetkey 5fa5ab50-dc72-48ef-b778-af719d7653cd",
	"grbgetkey 788eba4c-b600-48b6-8e8d-1260ed67fc20",
	"grbgetkey 5ae94a0e-3b8a-4868-98aa-da08c5beaa05",
	"grbgetkey 32fe064b-83de-4d1b-9230-87a8fc17a3b0",
	"grbgetkey 8e66598f-d191-454b-9a06-fedb81c400ed",
	"grbgetkey 74020b00-755a-4f32-8124-fb930b71c838",
	"grbgetkey c9c62936-943e-43dc-ae5e-2d103492d300",
	"grbgetkey 2bdec785-cd49-4a87-bcee-4d84acdb2e5d",
	"grbgetkey fe24abc2-4ae4-4138-a8d5-0ffee85a1afb",
	"grbgetkey d1b99d07-8a45-4c36-a4f0-3fce30bb864a",
	"grbgetkey 1eac1baf-4442-4fc5-a6e1-c422f8e7d83e",
	"grbgetkey ff68ac7d-d739-4f35-95aa-10860553c1ef",
	"grbgetkey 934e6694-8c05-4a9a-9636-7bbac0c3e48b",
	"grbgetkey d8b9d890-de29-4372-8ad0-ca6989f439de",
	"grbgetkey 0a459656-3ca6-4af2-aae4-471f9cfeca14",
	"grbgetkey f747db10-1490-4d79-a0dc-f2aa604a2dc8",
	"grbgetkey 3c7fd367-11ee-4c0f-8f20-b794ac6ee947",
	"grbgetkey e07d6a85-e230-4d57-9ec3-63c0a48b8f54",
	"grbgetkey d0014a72-a7a4-4ebf-ba9c-8e77405269db",
	"grbgetkey fbb65103-c5f3-4f40-a647-c14df6d37c1f",
	"grbgetkey 53251768-c311-4ea2-aa31-246c6bcb3e30",
	"grbgetkey fec7fd9a-8e77-4867-b610-d0c9477b7eba",
	"grbgetkey 73a2f355-e6d2-4b49-964c-f1ded57045b2",
	"grbgetkey 5d2b3702-d4b3-4f09-86a1-5a0bfa83fd3c",
	"grbgetkey fc235fd8-876a-458b-a635-fb4f266f9713",
	"grbgetkey 3e0fcb17-a556-4e8d-9075-f037018d380d",
	"grbgetkey fd45f999-0ddc-410f-8086-2d692dcfc24c",
	"grbgetkey 4e6d08f4-199d-4163-9844-dcfdcc7c159f",
	"grbgetkey f848a38e-d1c3-402a-8cae-16b069f2fabe",
	"grbgetkey 04a38040-a01a-4733-b743-367ec82a8745",
	"grbgetkey 0e78ebc8-3b3e-4e2a-8bab-3c269d8b640b",
	"grbgetkey 843b6551-ce0c-4b9c-a7df-b5c8de85d9e9",
	"grbgetkey 564d6cb0-5022-4a80-86f5-d48d9e61f7b1",
	"grbgetkey 7382dc1c-6849-47af-8a22-a8439ce7bb60",
	"grbgetkey be7248a3-0b01-4fea-af74-cad16673ffb3",
	"grbgetkey 4b49e8d9-f6ec-435f-9818-a9851f484aab",
    "grbgetkey 7ac37c34-02e4-4790-b8e6-f6fbf89fa675",
	"grbgetkey 29325b96-e8e1-4232-9986-dedbb0ea4868",
	"grbgetkey 238c3e2e-304a-4811-b3c7-1b5723b32e4c",
	"grbgetkey 392db561-8e32-472e-9919-aee882a7106f",
	"grbgetkey 8ac519cf-4341-4503-9995-b1d909f4fcf0",
	"grbgetkey 0a46abf8-865a-4d48-b908-8b6865922375",
]

df = pd.DataFrame({
	"licences": licenses,
	"used": np.zeros(len(licenses)).astype(bool).tolist()})

df.to_csv("licence_storage.csv")

logger.info("Created licences!")
