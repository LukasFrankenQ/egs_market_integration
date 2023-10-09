import pandas as pd
import numpy as np

import logging
logger = logging.getLogger(__name__)

licenses = [
	"grbgetkey dd070277-2ffd-4ec1-a60a-f0b555d55612",
	"grbgetkey fda2b041-6b29-49ba-93e1-fbe003c26017",
	"grbgetkey d662ab7c-f1a5-4fc5-b737-2e948e73c2a5",
	"grbgetkey f1ef68ca-b319-4849-942b-36031d8f9e2e",
	"grbgetkey 42a2fe6d-c69e-427a-8ae5-266e0a0b2ec2",
	"grbgetkey 256c07fc-2fa7-4f72-bcf0-381265096558",
	"grbgetkey f58a305a-90dc-46a1-a793-bbe7a2aed6e1",
	"grbgetkey 7995c197-b304-4a78-9431-f91122d642bd",
	"grbgetkey 2ac05bb5-f8e7-4ec2-80f7-50b2e8285855",
	"grbgetkey 2b5bc8d6-74da-480d-8130-b4a1a448f49c",
	"grbgetkey 2516a63e-8947-41e9-b479-fafc5b46db55",
	"grbgetkey 64ee2354-4260-46cd-87c2-635d74890d57",
	"grbgetkey 90a8a61a-0eca-401b-82d8-eadcd1b7faf5",
	"grbgetkey 62a9088a-0aaf-4d9e-9a25-7172a2d497b1",
	"grbgetkey c5b24f51-22fd-4a05-b9f3-1fbcfb9d784a",
	"grbgetkey 04123d07-2191-4c56-8408-f2608f50233c",
	"grbgetkey 1ba2a977-d529-405e-9ab1-e3930ac138bf",
	"grbgetkey 7c197ec7-9d5a-4a1c-acd7-b588490ce720",
	"grbgetkey 8b084a1f-b413-4df9-82dc-0d88905d4c86",
	"grbgetkey bff19b57-6096-4869-9515-ce10c21c613c",
	"grbgetkey fb5185af-1b2a-4dee-8375-0f9abe6057db",
	"grbgetkey dfd00df3-ed9f-40b9-a60b-83c0ddf4806f",
	"grbgetkey e30041fb-8277-4df0-ac33-2ea902b77b22",
	"grbgetkey 92b3af65-0aa1-471f-ad46-c9f39b198b27",
	"grbgetkey 0328ab1c-c22d-4086-803c-9cc312beafe4",
	"grbgetkey c96e1769-56af-4e6f-a4c7-b3a125f999c3",
	"grbgetkey 52838c68-fb68-45e7-a037-1649568c4a52",
	"grbgetkey 14e0daab-e62c-4031-97ae-9c020b82abd9",
	"grbgetkey ea26d2dc-aec0-412b-b64d-849c75375445",
	"grbgetkey 66eead50-2a24-489d-a1fd-a22a90234585",
	"grbgetkey f452c85e-8a53-4253-9448-45d1af5c70f6",
	"grbgetkey e0e5e0f6-43cb-425c-9bf0-6919214a6a17",
	"grbgetkey a8e2cade-8f51-4545-9787-3604489163dd",
	"grbgetkey 3428251c-90eb-4aa4-88b4-1f20a7350645",
	"grbgetkey 8d03d6a6-3d5e-4e52-8004-51211e5ad594",
	"grbgetkey 78062a5d-fcdf-4925-9fc3-127ccd67c7bd",
	"grbgetkey 84e90c18-000c-463b-b1f9-c4d58d7376ea",
	"grbgetkey 60595340-9d26-4f6d-9126-146a5ca2934c",
	"grbgetkey 06adf6eb-2d41-484e-8d98-f327aa5f3eb0",
	"grbgetkey 8d84eebe-3d02-4ff0-b0c9-81607e8b7710",
	"grbgetkey 7c7e20e9-cd5a-4a44-9328-3659039950f1",
	"grbgetkey 79a4bd42-3e3f-4003-aada-ad462c1abec1",
	"grbgetkey 8bba39f8-4a53-45f0-9ce6-1ab310e7b5a9",
	"grbgetkey 9fcef608-cb27-4cbe-a5b3-2cd782d66753",
	"grbgetkey 5e380aa6-d388-4de7-be52-4597fe28cc7a",
	"grbgetkey eafb0955-6a1d-49cc-af9d-3b546967e18f",
	"grbgetkey 072357a1-53f5-4806-9099-9835eb20285f",
	"grbgetkey b1922d3b-ed35-4af8-8385-5382d2e13605",
	"grbgetkey 4d4bceb8-cfa4-4aa7-8e9a-c51ddd6b3123",
	"grbgetkey 61e9fb92-daa9-4208-9269-e38445157954",
    "grbgetkey f97949b4-3841-45a9-890d-8056a3abea6e",
	"grbgetkey 307cc7b0-f615-4f6f-8e42-756ca76f5f1a",
]

df = pd.DataFrame({
	"licences": licenses,
	"used": np.zeros(len(licenses)).astype(bool).tolist()})

df.to_csv("licence_storage.csv")

logger.info("Created licences!")
