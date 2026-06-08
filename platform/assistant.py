"""GenAI customer service assistant with tool use."""
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_google_vertexai import ChatVertexAI
from langchain.tools import tool
from langchain.memory import ConversationBufferWindowMemory
from langchain_core.prompts import ChatPromptTemplate

SYSTEM_PROMPT = """You are a helpful, empathetic customer service assistant.
Always be polite, concise and solution-focused. If you cannot solve the issue,
offer to escalate to a human agent. Respond in the same language as the customer."""

@tool
def get_order_status(order_id: str) -> str:
    """Get the current status of a customer order."""
    return f"Order {order_id}: In transit, expected delivery in 2 business days."

@tool
def process_refund(order_id: str, reason: str) -> str:
    """Process a refund request for a customer order."""
    return f"Refund initiated for order {order_id}. Processing in 3-5 business days."

@tool
def escalate_to_human(reason: str, priority: str = "normal") -> str:
    """Escalate conversation to a human agent."""
    return f"Escalated to human agent (priority: {priority}). Wait time: ~5 min."

def create_assistant(session_id: str) -> AgentExecutor:
    llm = ChatVertexAI(model_name="gemini-1.5-flash-002", temperature=0.1)
    tools = [get_order_status, process_refund, escalate_to_human]
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT), ("placeholder", "{chat_history}"),
        ("human", "{input}"), ("placeholder", "{agent_scratchpad}")])
    agent = create_tool_calling_agent(llm, tools, prompt)
    memory = ConversationBufferWindowMemory(k=10, return_messages=True, memory_key="chat_history")
    return AgentExecutor(agent=agent, tools=tools, memory=memory, verbose=False, max_iterations=5)
