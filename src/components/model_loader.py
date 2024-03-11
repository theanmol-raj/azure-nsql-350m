
from src.exception import CustomException
from dataclasses import dataclass
from transformers import AutoTokenizer, AutoModelForCausalLM
import os
import sys


@dataclass
class NsqlModelConfig :
    checkpoint = 'NumbersStation/nsql-350M'

class NsqlModel :
    def __init__(self) -> None:
        self.checkpoint = NsqlModelConfig()
        self.tokenizer = AutoTokenizer.from_pretrained(self.checkpoint.checkpoint)
        self.model = AutoModelForCausalLM.from_pretrained(self.checkpoint.checkpoint)

    def save_model_locally(self):
        try:
            file_path = os.path.dirname(os.path.join('artifacts','model'))
            os.makedirs(file_path,exist_ok=True)
            self.model.save_model('model')
        except Exception as e:
            raise CustomException(e,sys)
        
    def predict(self,prompt : str =''):
        if prompt == '' :
            return -1

        input_ids = self.tokenizer(prompt, return_tensors="pt").input_ids
        
        generated_ids = self.model.generate(input_ids, max_length=500)
        return self.tokenizer.decode(generated_ids[0], skip_special_tokens=True)



