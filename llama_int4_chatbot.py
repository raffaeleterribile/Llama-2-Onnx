""" Simple chatbot to use with quantized LlaMa """

import os
import random
import time
import gradio as gr

current_directory = os.path.dirname(os.path.realpath(__file__))

def load_model():
    """
    Loads the model for the chatbot.
    """
    pass

def predict_next_word():
    """
    Predicts the next word based on the given input.
    """
    pass

def predict():
    """
    This function is used to make predictions.
    """
    pass

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = random.choice(["How are you?", "I love you", "I'm very hungry"])
        chat_history.append((message, bot_message))
        time.sleep(2)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()

# from transformers import AutoTokenizer, AutoModelForCausalLM
# 
# # Carica il tokenizer e il modello
# tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
# model = AutoModelForCausalLM.from_pretrained("path_to_your_model")
# 
# # Codifica il testo di input
# input_text = "C'era una volta"
# input_ids = tokenizer.encode(input_text, return_tensors='pt')
# 
# # Genera il testo
# output = model.generate(input_ids, do_sample=True, max_length=50, temperature=0.7)
# 
# # Decodifica il testo generato
# generated_text = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
# 
# print(generated_text)