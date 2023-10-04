import asyncio
import os
from dapr.ext.pubsub import DaprPubSub

async def message_handler(data, metadata):
    # Handle the incoming message
    print(f"Received message: {data.decode('utf-8')}")

pubsub = DaprPubSub()
pubsub.register_topic_handler("your-topic-name", message_handler)

asyncio.run(pubsub.start())
