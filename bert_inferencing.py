from transformers import BertTokenizer, BertModel
from sentence_transformers import util
import torch
import torch.nn as nn

from parse_dict import *

import xlrd, xlwt
PATH = "./RED.txt"
PART_OF_SPEECH = 3

def main():
    tokenizer = BertTokenizer.from_pretrained("DeepPavlov/rubert-base-cased")
    model = BertModel.from_pretrained("DeepPavlov/rubert-base-cased")
    cos = nn.CosineSimilarity(dim=1, eps=1e-6)
    items = parse_dict(PATH)
    counter = 0

    tmp = xlwt.Workbook()
    f = tmp.add_sheet("Worksheet")
    
    for i in range(len(items)):
        words = items[i]
        if words[0] != PART_OF_SPEECH:
            continue
        for n in range(len(words[1])):
            for j in range(n+1, len(words[1])):
                w1 = words[1][n]#.encode("utf-8")
                w2 = words[1][j]#.encode("utf-8")
                par1 = tokenizer.encode(w1, return_tensors="pt")
                par2 = tokenizer.encode(w2, return_tensors="pt")
                out1 = torch.mean(model(par1, output_hidden_states=True)[0], 1)
                out2 = torch.mean(model(par2, output_hidden_states=True)[0], 1)
                sin =  util.pytorch_cos_sim(out1, out2)
                f.write(counter, 0, w1)
                f.write(counter, 1, w2)
                f.write(counter, 3, sin.item())
                counter += 1
                print(w1, w2, sin.item())
 #   f.close()
    tmp.save("results_adj.xls")
    #print(w1, w2, sin.item())

if __name__ == "__main__":
    main()
