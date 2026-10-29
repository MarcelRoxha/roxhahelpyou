from google.adk.agents import LlmAgent
from google.adk.skills import load_skill_from_dir
from google.adk.tools.skill_toolset import SkillToolset
from google.adk.integrations.environment_toolset import EnvironmentToolset, LocalEnvironment
import os
from datetime import datetime

# Caminho para as skills
skills_dir = os.path.join(os.path.dirname(__file__), "skills")

# Carrega a skill financeira
skill_toolset = SkillToolset(
    skills=[
        load_skill_from_dir(os.path.join(skills_dir, "gestao-financeira"))
    ]
)

# Ferramentas de arquivo (apenas Read e Write)
class FerramentasDeArquivo(EnvironmentToolset):
    async def get_tools(self, readonly_context=None):
        tools = await super().get_tools(readonly_context)
        return [t for t in tools if t.name in ("ReadFile", "WriteFile")]

# O working_dir aponta para a pasta 'planos' na raiz do projeto
working_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "planos"))
env_toolset = FerramentasDeArquivo(environment=LocalEnvironment(working_dir=working_dir))

# Instrução principal com a data atual
data_hoje = datetime.now().strftime("%d/%m/%Y")

instrucoes = f"""
Você é o Harness Financeiro Pessoal do usuário. Hoje é {data_hoje}.
Sua missão é ajudar o usuário a sair do vermelho, organizar o fluxo de caixa e tomar decisões inteligentes sobre dívidas.

Sempre que o assunto for dinheiro, finanças, dívidas ou planejamento, você DEVE usar a skill 'gestao-financeira'.
Siga estritamente o workflow da skill.
Seja empático, direto e matemático. Não julgue os gastos, apenas apresente os números e as melhores rotas de saída.
Ao ler os arquivos CSV do usuário, lembre-se que eles podem estar desorganizados. Leia o cabeçalho de cada um para entender o que ele contém antes de fazer cálculos.
"""

# Define o agente raiz
root_agent = LlmAgent(
    name="harness_financeiro",
    model=os.environ.get("MODEL", "gemini-3.8-flash"),
    instruction=instrucoes,
    tools=[skill_toolset, env_toolset]
)