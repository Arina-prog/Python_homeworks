# Create a list of sentences, create 1 extra process, that should transfer random sentence by word to main
# process, main process should read sentence and reply to it 10 times.

# Создайте список предложений, создайте 1 дополнительный процесс, который должен передавать случайное
# предложение за словом в основной процесс, основной процесс должен прочитать предложение и ответить на него 10 раз.


import multiprocessing

def strings_list(list,queue):
