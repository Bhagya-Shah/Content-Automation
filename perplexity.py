import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("gpt2")
tokenizer = AutoTokenizer.from_pretrained("gpt2")

def calper(text2):
    inputs_wiki_text = tokenizer(text2, return_tensors = "pt")
    loss = model(input_ids = inputs_wiki_text["input_ids"], labels = inputs_wiki_text["input_ids"]).loss
    ppl = torch.exp(loss)
    print(f'{ppl:.2f}')
    return f'Perplexity Score : {ppl:.3f}'


calper("Subject: We're sorry for falling short of your expectation. We apologize for the atmosphere issues you experienced during your recent visit to our restaurant. As a chef, I understand the importance of creating a welcoming and comfortable environment for our guests. We take your feedback seriously and will work to improve our atmosphere to ensure that you have a pleasant dining experience when visiting us.  Thank you for bringing this to our attention, and we look forward to serving you better in the future.")