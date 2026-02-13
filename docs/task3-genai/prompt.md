# Task 3 – GenAI Prompt Record

## Tool Information

| Field         | Value                      |
|---------------|----------------------------|
| **Tool**      | Claude (Anthropic)         |
| **Date**      | 2026-02-13                 |
| **Input Type**| PNG (UML class diagram) + Papyrus-exported XML (`catandomainmodel.uml`) |

---

## Prompt Used

> You are helping me complete "Task 3: Using Generative AI" for a software design assignment.
>
> Context:
> - I have a Papyrus UML model for a simplified Settlers of Catan simulator.
> - I may provide the UML as an image (PNG) or as Papyrus-exported XML.
> - My repo already has Papyrus-generated Java skeleton classes (base code).
> - Your job is to (a) generate code from the UML and (b) critically evaluate the result.
>
> INPUT I WILL PROVIDE:
> - UML model (PNG or XML) attached in this chat.
>
> YOUR TASKS:
> 1) First, repeat back the EXACT prompt you were given (this entire message) under a heading "PROMPT USED".
> 2) Inspect the UML model (PNG/XML) and generate Java code *skeletons* that match the model:
>    - classes/interfaces
>    - fields
>    - method signatures
>    - constructors
>    - relationships (inheritance/associations)
>    - Use encapsulation (private fields). Avoid implementing full logic.
> 3) Compare your generated structure to a typical Papyrus-generated skeleton:
>    - Point out where GenAI commonly makes mistakes (multiplicity, composition vs association, missing classes, invented methods, wrong responsibilities).
>    - If you see any likely mismatches based on the UML, list them explicitly.
> 4) Produce three markdown "files" in your output that I can copy into my GitHub repo:
>
> Output File 1: docs/task3-genai/prompt.md
> - Include tool name ("Claude"), date placeholder, what input type you received (PNG or XML).
> - Under "Prompt Used", paste the full prompt (this message).
>
> Output File 2: docs/task3-genai/genai-output.md
> - Summarize what code you generated.
> - Include a short table: Class | Key fields | Key methods
> - List any assumptions you made.
>
> Output File 3: docs/task3-genai/analysis.md
> Answer these reflection points clearly (bullets + short paragraphs):
> - What did the GenAI tool do well? Strengths.
> - What mistakes did it make? Weaknesses.
> - How would you use GenAI in a large-scale software project? How would you balance strengths/weaknesses?
> - Revenue strategy question: I will paste the table of 4 strategies after. For now, write the decision framework and what data you would need from the table to choose.
>
> FORMATTING REQUIREMENTS:
> - Put each "file" in its own fenced code block labeled as markdown.
> - Use headings and bullet points, keep it concise and professional.
> - Do not invent requirements not present in the UML; when uncertain, clearly label it as an assumption.
