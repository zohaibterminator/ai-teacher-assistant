from datasets import Dataset, load_dataset
from dotenv import load_dotenv

def getData():
    comp_sci = load_dataset("zohaibterminator/9th-grade-comp-sci", split="train")
    phys     = load_dataset("zohaibterminator/9th-grade-phys", split="train")
    chem     = load_dataset("zohaibterminator/9th-grade-chem", split="train")

    try:
        yield (comp_sci, phys, chem)
    finally:
        print("Data Loaded Successfully")