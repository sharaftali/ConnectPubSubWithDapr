from dapr.ext.pubsub import DaprPubSub
import asyncio

async def publish_message():
    pubsub = DaprPubSub()

    # Publish a message to the specified topic
    topic_name = "report_topic"
    message_data = "Your message data"

    await pubsub.publish(topic_name, message_data)

    # Close the pubsub client
    await pubsub.close()

# Run the publish_message function
if __name__ == "__main__":
    asyncio.run(publish_message())

# dapr publish --pubsub pubsub --topic your-topic-name --data "Your message data"


def publish_message_with_():
    import requests
    import json

    dapr_publish_url = "http://localhost:3500/v1.0/publish/pubsub/your-topic-name"  # Replace with your Dapr sidecar's URL
    data = {
        "data": "Your message data",
        "metadata": {
            # You can include any metadata you need here
        }
    }
    payload = json.dumps(data)
    headers = {"Content-Type": "application/json"}

    response = requests.post(dapr_publish_url, data=payload, headers=headers)
    if response.status_code == 200:
        print("Message published successfully")
    else:
        print(f"Failed to publish message. Status code: {response.status_code}, Response content: {response.text}")
