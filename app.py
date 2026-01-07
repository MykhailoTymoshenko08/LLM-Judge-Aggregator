import os

from dotenv import load_dotenv
load_dotenv()
API_KEY=os.getenv("API_KEY")

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def get_langchain_answer(model_name, user_text):
    llm = ChatOpenAI(
        model = model_name,
        openai_api_key = API_KEY,
        base_url = "https://openrouter.ai/api/v1",
        max_tokens = 200
    )

    #prompt = ChatPromptTemplate("{topic}")
    prompt = ChatPromptTemplate.from_template("{topic}")
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    result = chain.invoke({"topic": user_text})
    return f"✅{result}"




def judge_answers(user_text, answer1, answer2, model):
    llm = ChatOpenAI(
        model=model,
        openai_api_key=API_KEY,
        base_url="https://openrouter.ai/api/v1",
        max_tokens=500  
    )
    judge_template = """
    Ти — експерт, який аналізує відповіді AI.
    
    Питання: {question}
    
    ВІДПОВІДЬ 1:
    {answer1}
    
    ВІДПОВІДЬ 2:
    {answer2}
    
    Твоє завдання:
    1. Порівняй ці дві відповіді
    2. Вибери найкращі частини з кожної
    3. Створи одну ідеальну відповідь
    4. Будь об'єктивним та точним
    
    ФІНАЛЬНА ВІДПОВІДЬ:
    """
    
    prompt = ChatPromptTemplate.from_template(judge_template)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    result = chain.invoke({
        "question": user_text,
        "answer1": answer1,
        "answer2": answer2
    })
    return f"✅{result}"



def main():
    models = [
        "meta-llama/llama-3.3-70b-instruct:free",
        "google/gemma-3-27b-it:free"
    ]
    judge_model = "mistralai/devstral-2512:free"
    user_input = input("Enter your request: ")

    answer1 = get_langchain_answer(models[0], user_input)
    answer2 = get_langchain_answer(models[1], user_input)   
    print("\n" + "="*50)
    print("Original answers:")
    print(f"Model 1: {answer1}")
    print("\n" + "="*50)
    print(f"Model 2: {answer2}")
    print("\n" + "="*50)
    print("\n" + "="*50)

    final_answer = judge_answers(user_input, answer1, answer2, judge_model)
    print("\n" + "="*50)
    print("Final answer:")
    print(final_answer)


if __name__ == "__main__":
    main()