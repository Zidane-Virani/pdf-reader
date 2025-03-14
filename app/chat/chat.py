from app.chat.models import ChatArgs
from app.chat.vector_stores import retriever_map
from app.chat.llms import llm_map
from app.chat.memories import memory_map
from app.chat.chains.retrieval import StreamingConversationalRetrievalChain
from app.chat.llms.chatopenai import build_llm
from app.chat.memories.sql_memory import build_memory
from langchain.chat_models import ChatOpenAI
from app.web.api import (
    set_conversation_components, 
    get_conversation_components
)
import random
#from app.chat.tracing.langfuse import langfuse


def select_component(
    component_type, component_map, chat_args
):
    components = get_conversation_components(
        chat_args.conversation_id
    )
    previous_component = components[component_type]
    if previous_component:
        builder = component_map[previous_component]
        return previous_component, builder(chat_args)
    else:
        random_name = random.choice(list(component_map.keys()))
        builder = component_map[random_name]
        return random_name, builder(chat_args)

def build_chat(chat_args: ChatArgs):
    
    retriever_name, retriever = select_component(
        "retriever", 
        retriever_map,
        chat_args
    )
    
    llm_name, llm = select_component(
        "llm",
        llm_map,
        chat_args
    )
    
    memory_name, memory = select_component(
        "memory",
        memory_map,
        chat_args
    )
    
    set_conversation_components(
        conversation_id= chat_args.conversation_id,
        llm = llm_name,
        retriever = retriever_name,
        memory = memory_name 
    )
    

    condense_question_llm = ChatOpenAI(streaming = False)
    
    # trace = langfuse.trace(
    #     CreateTrace(
    #         id = chat_args.conversation_id,
    #         metadata = chat_args.metadata
    #     )
    # )
    
    return StreamingConversationalRetrievalChain.from_llm(
        llm=llm,
        memory=memory,
        condense_question_llm = condense_question_llm,
        retriever=retriever,  # Fixed typo,
       # callbacks = [trace.getNewHandler()]
    )
