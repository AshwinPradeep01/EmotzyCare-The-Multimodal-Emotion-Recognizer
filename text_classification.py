import torch
from transformers import BertModel, BertTokenizer
from record import audio_input


# Load the saved model and tokenizer
bertmodel = torch.load('emotzy_model.pth',map_location=torch.device('cpu'))
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

tokenizer.save_pretrained('tokenizer.json')

# Load the tokenizer
from transformers import BertTokenizer

tokenizer = BertTokenizer.from_pretrained('tokenizer.json')

def get_emotion(review_text):
    encoded_review = tokenizer.encode_plus(review_text, max_length=512,
                                          add_special_tokens=True, return_token_type_ids = False,
                                          padding=True,
                                          return_attention_mask=True,
                                          truncation=True,
                                          return_tensors='pt')
    input_ids = encoded_review['input_ids']
    attention_mask = encoded_review['attention_mask']
    output = bertmodel(input_ids,attention_mask)
    logits = output.logits
    probs =(torch.nn.functional.softmax(logits, dim=1))
    prediction = int(torch.argmax(output.logits))
    pred_dict ={
        0:"angry",
        1:"frustrated",
        2:"happy",
        3:"neutral",
        4:"sad"
    }
    prediction = pred_dict[prediction]
    print(f"Review text:{review_text}")
    print(f"Sentiment:{prediction}")

res = audio_input()

review_text2 = "I m on cloud nine feeling so delighted"
get_emotion(res)