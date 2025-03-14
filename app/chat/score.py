from app.chat.redis import client
import random

def random_component_by_score(component_type, component_map):
    if component_type not in ["llm", "memory", "retriever"]:
        raise ValueError("Invalid Component Type")
    
    values = client.hgetall(f"{component_type}_score_values")
    counts = client.hgetall(f"{component_type}_score_counts") 
    
    names = component_map.keys()
    
    ratings = {}
    
    
    for name in names:
        score = int(values.get(name,1))
        count = int(counts.get(name,1))
        avg = score/count
        ratings[name] = max(avg,0.1)
        
    sum_scores = sum(ratings.values())
    random_val = random.uniform(0,sum_scores)
    cumulative = 0
    for name,score in ratings.items():
        cumulative += score
        if random_val <= cumulative:
            return name

def score_conversation(
    conversation_id: str, score: float, llm: str, retriever: str, memory: str
) -> None:
    score = min(max(score,0),1)
    
    client.hincrby("llm_score_values", llm,score)
    client.hincrby("llm_score_counts", llm,1)
    
    client.hincrby("retriever_score_values", retriever,score)
    client.hincrby("retriever_score_counts", retriever,1)
    
    client.hincrby("memory_score_values", memory,score)
    client.hincrby("memory_score_counts", memory,1)


def get_scores():
    aggregate = {"llm":{}, "retriever": {}, "memory":{}}
    
    for component_type in aggregate.keys():
        values = client.hgetall(f"{component_type}_score_values")
        counts = client.hgetall(f"{component_type}_score_counts") 
        
        names = values.keys()
        
        for name in names:
            score = int(values.get(name,1))
            count = int(counts.get(name,1))
            avg = score/count
            aggregate[component_type][name] = [avg]
