from google import genai

class ScriptEngine:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
        self.model_id = "gemini-2.5-flash" # Use a versão estável que funcionou para você

    def generate_script(self, produto, publico, tom, estilo):
        # Adicionamos uma instrução restritiva para a formatação
        prompt = f"""
        Atue como copywriter sênior. 
        Gere 3 roteiros distintos para o produto: {produto}. 
        Público: {publico}. Tom: {tom}. Formato: {estilo}.

        IMPORTANTE: Separe estritamente cada roteiro usando exatamente o marcador: ###SEPARADOR###
        Não escreva introduções antes do primeiro roteiro.
        """
        try:
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=prompt
            )
            return response.text
        except Exception as e:
            return f"Erro na API: {str(e)}"