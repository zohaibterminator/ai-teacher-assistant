from colpali_engine.models import ColQwen2, ColQwen2Processor
from dotenv import load_dotenv
import os
load_dotenv()

def getEncoder():
    model = ColQwen2.from_pretrained(
        "vidore/colqwen2-v0.1", # model name
        torch_dtype=torch.bfloat16, # load the model in 16-bit precision
        device_map="cuda:0", # load the model in GPU
    )
    processor = ColQwen2Processor.from_pretrained("vidore/colqwen2-v0.1") # load the model's vision encoder

    try:
        yield (model, processor)
    finally:
        print("Embedding Model Loaded Successfully")