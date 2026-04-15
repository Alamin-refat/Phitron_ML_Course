from google import genai
import os
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")

