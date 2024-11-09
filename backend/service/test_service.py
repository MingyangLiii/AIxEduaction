import os
import sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
from config.configuration import get_config
from util.generate_id import generate_id
from util.extract_table_of_content import *
from entity.textbook import Textbook
from model.database_connection import DatabaseConnection
from service.generator import Generator
from service.generate_pipeline import GenerationPipeline
from llm.agent import Agent
from openai import OpenAI



if  __name__ == "__main__":
    client = OpenAI(api_key=get_config()["api_key"])
    agent = Agent(client)
    db = DatabaseConnection()
    genai = Generator(agent=agent)

    course_name = "MPC 控制算法"
    user_req = "我想要学习MPC控制算法， 我是一个新手，帮我在短时间内快速学习，不要太多内容。"

    pipeline = GenerationPipeline(agent)
    pipeline.generate_textbook(course_name=course_name, user_requirement=user_req)
    