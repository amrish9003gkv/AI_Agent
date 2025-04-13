import os
from dotenv import load_dotenv
from twilio.rest import Client
from elevenlabs import generate, save, set_api_key
#from elevenlabs import generate
#print(generate)

# Load environment variables from .env file
load_dotenv()

# Set Google Application Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Twilio credentials
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")

print("TWILIO_ACCOUNT_SID:", os.getenv("TWILIO_ACCOUNT_SID"))
print("TWILIO_AUTH_TOKEN:", os.getenv("TWILIO_AUTH_TOKEN"))
print("TWILIO_PHONE_NUMBER:", os.getenv("TWILIO_PHONE_NUMBER"))

# Validate Twilio credentials
if not account_sid or not auth_token or not twilio_phone_number:
    raise ValueError("One or more Twilio environment variables are missing.")

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Make a call
call = client.calls.create(
    to="+919634019003",  # Replace with a verified number
    from_=twilio_phone_number,
    url="http://demo.twilio.com/docs/voice.xml"  # Can be dynamic
)

print("Call initiated:", call.sid)





set_api_key(os.getenv("ELEVENLABS_API_KEY"))

audio = generate(
    text="Hello, this is an AI-generated voice.",
    voice="Rachel",
    model="eleven_monolingual_v1"
)
save(audio, "output.wav")
