import openai
import pyttsx3
engine = pyttsx3.init()
openai.api_key = "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"
messages = [
 {"role": "system", "content" : "You’re a kind helpful assistant"}
]

def main():
  print("Hola! Esta es un pequenio programa para hablar con ChatGPT. Escribe algo:")
  while True:
    txt_input = input()
    if len(str(txt_input)) > 0:
        st = str(txt_input)
        if st == 'exit':
            quit()
        else:
            messages.append({"role": "user", "content": st + '. Responde en pocas palabras por favor.'})
            completion = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=messages
            )
            resp = completion.choices[0].message.content
            engine.say(resp)
            engine.runAndWait()
            messages.append({"role": "assistant", "content": resp})
            print("Escribe algo:")

main()