import uuid
import requests

# Trace context is represented as a dictionary
trace_context = {
    "trace_id": str(uuid.uuid4()),  # Generate a new trace ID
    "span_id": str(uuid.uuid4()),   # Generate a new span ID for the first span
}

# Service A sends a request to service B
response = requests.get("http://service-b/endpoint", headers={"Trace-Context": trace_context})

# Service B sends a request to service C
response = requests.get("http://service-c/endpoint", headers={"Trace-Context": trace_context})

# Service C returns a response to service B
# Service B adds a new span ID to the trace context and sends the response back to service A
trace_context["span_id"] = str(uuid.uuid4())
response = requests.post("http://service-a/endpoint", headers={"Trace-Context": trace_context}, json=response.json())

# Service A processes the response and logs the trace context for later analysis
print(trace_context)
