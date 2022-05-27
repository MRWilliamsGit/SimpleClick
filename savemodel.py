#save and load, works but only one word
model = GPT2Model.from_pretrained('gpt2', return_dict=True)
pickle.dump(model, open('model.pkl', 'wb'))

back = pickle.load(open('model.pkl', 'rb'))
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
indexed_tokens = tokenizer.encode(text)
tokens_tensor = torch.tensor([indexed_tokens])
outputs = back(tokens_tensor)
predictions = outputs[0]
predicted_index = torch.argmax(predictions[0, -1, :]).item()
output = tokenizer.decode(indexed_tokens + [predicted_index])

print(f'{output}')