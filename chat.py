# %%
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# %%
# initialize an instance 
chat = ChatBot('Skeepers')

trainer = ListTrainer(chat)
# trainer.train([
#     'hi',
#     'Welcome friend!'
#     'Are you gay?'
#     'Well yeah!'
    
# ])

exit_cond = (':q', 'quit', 'exit')

while True:
    query = input('fr3k~$ ')
    if query in exit_cond:
        break
    else:
        print(f' {chat.get_response(query)}')

# %%
## Train 




