**Deploy Command**

``kubectl apply -f pubsub.yaml -n namespace``

**note**: No need to configure the pub/sub localhost with in the same cluster. 

publish with bash 
``dapr publish --pubsub pubsub --topic your-topic-name --data "Your message data"``
