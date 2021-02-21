from transformers import BertTokenizer, BertModel
from sentence_transformers import util
import torch
import torch.nn as nn

from parse_dict import *
import xlrd, xlwt

PATH = "./RED.txt"
PART_OF_SPEECH = 3
FORMAT = "mean"

def main():
    tokenizer = BertTokenizer.from_pretrained("DeepPavlov/rubert-base-cased")
    model = BertModel.from_pretrained("DeepPavlov/rubert-base-cased")
    cos = nn.CosineSimilarity(dim=1, eps=1e-6)
 #   items = parse_dict(PATH)
    counter = 0

    tmp = xlwt.Workbook()
    f = tmp.add_sheet("Worksheet")
    s = "aa"
    while s != "":
        s = input().strip().split()
        par1 = tokenizer.encode(s[0], return_tensors="pt")
        par2 = tokenizer.encode(s[1], return_tensors="pt")
        out1 = torch.mean(model(par1, output_hidden_states=True)[0], 1)
        out2 = torch.mean(model(par2, output_hidden_states=True)[0], 1)
        sin =  util.pytorch_cos_sim(out1, out2)

        f.write(counter, 0, s[0])
        f.write(counter, 1, s[1])
        f.write(counter, 3, sin.item())
        counter += 1
        print(s[0], s[1], sin.item())
    tmp.save("results_unknown_news.xls")
    #print(w1, w2, sin.item())

if __name__ == "__main__":
    main()
