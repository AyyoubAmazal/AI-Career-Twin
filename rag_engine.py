import json
import ollama

class RAGEngine:

    def llm(self, prompt):
        response = ollama.generate(
            model="gpt-oss:20b",
            prompt=prompt,
            options={
                "temperature": 0.4
            }
        )

        return response["response"].strip()

    def generate(self, user_profile, retrieved, template):
        prompt = template.format(
            user_profile=json.dumps(user_profile, indent=2),
            retrieved_profiles=json.dumps(retrieved, indent=2)
        )
        return self.llm(prompt)

