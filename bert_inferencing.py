from transformers import pipeline

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

from parse_dict import *

PATH = "./RED.txt"
PART_OF_SPEECH = 1

def main():
    tokenizer = AutoTokenizer.from_pretrained("bert-base-cased-finetuned-mrpc")
    model = AutoModelForSequenceClassification.from_pretrained("bert-base-cased-finetuned-mrpc", return_dict=True)

    classes = ["is paronyms", "not paronyms"]

    items = parse_dict(PATH)

    for i in range(len(items)):
        words = items[i]
        if words[0] != PART_OF_SPEECH:
            continue
        for n in range(len(words[1])):
            for j in range(n+1, len(words[1])):
                w1 = words[1][n]#.encode("utf-8")
                w2 = words[1][j]#.encode("utf-8")
                par = tokenizer(w1, w2, return_tensors="pt")
                paraphrase_classification_logits = model(**par).logits
                paraphrase_results = torch.softmax(paraphrase_classification_logits, dim=1).tolist()[0]
                for i in range(1, len(classes)):
                    print(w1.encode("utf8").decode("cp1252"), w2.encode("utf8").decode("cp1252"), f"{classes[i]}: {int(round(paraphrase_results[i] * 100))}%")

if __name__ == "__main__":
    main()
