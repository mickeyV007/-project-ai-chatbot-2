import ollama

class ChatbotBackend:
    def __init__(self, model_name):
        self.model_name = model_name
    
    def get_response(self, user_message):
        try:
            response = ollama.chat(
                model=self.model_name,
                messages=[
                    {'role': 'user', 'content': user_message},
                    {'role': 'user', 'contents': "you are assistant speak english language and Thai"},
                ]
            )
            ai_response = response['message']['content'].replace('<think>', '').replace('</think>', '').strip()
            
            
            return ai_response
        
        
        except Exception as e:
            return f"Error: {str(e)}"
