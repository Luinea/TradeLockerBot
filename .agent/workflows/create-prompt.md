---
description: Create a new prompt that another Claude can execute argument-hint: [task description] allowed-tools: [Read, Write, Glob, SlashCommand, AskUserQuestion]
---

description: Create a new prompt that another Claude can execute argument-hint: [task description] allowed-tools: [Read, Write, Glob, SlashCommand, AskUserQuestion]

<objective>
Act as an expert prompt engineer for Claude Code. Create highly effective, XML-structured prompts for: $ARGUMENTS.
Goal: Create prompts that execute tasks accurately and efficiently.
</objective>

<process>
<step_0_intake>
<check_args>

Check ./prompts/*.md via Glob to find next sequence number.

IF $ARGUMENTS is empty:

Use AskUserQuestion (header: "Task Type") to get category (Coding/Analysis/Research).

Then ask for specific task description.

IF $ARGUMENTS exists: Proceed to analysis.
</check_args>

<analysis_loop>
Analyze description for: Type, Complexity, Execution Strategy (Single vs Parallel vs Sequential), and Gaps.
UNTIL "Ready" is confirmed:

Identify missing context (e.g., specific tech stack, auth methods, bug location, success metrics).

Generate 2-4 clarifying questions using AskUserQuestion.

Present a final "Ready?" gate (Options: Proceed, Ask more, Add context).
</analysis_loop>

<status>
On "Proceed", state plan: "Creating [complexity] [strategy] prompt for: [summary]"
</status>
</step_0_intake>

<step_1_generation>
<logic>

Single: One cohesive goal. Save: ./prompts/NNN-name.md

Parallel: Independent sub-tasks. Save: ./prompts/NNN, ./prompts/NNN+1...

Sequential: Dependencies exist. Save sequentially.

</logic>

<construction_rules>

Structure: Use semantic XML (<objective>, <context>, <steps>, <verification>).

Context: Explain WHY, WHO, and WHAT.

Paths: Use relative paths (./src/file.ts).

Logic:

Complex? Add "extended thinking" triggers ("Analyze deeply...").

Agentic? Add "Use tools in parallel where possible".

Constraint? Explain the WHY behind constraints.

Tools: Only reference MCP/tools if needed. Use ! for bash checks.
</construction_rules>

<prompt_template>
Apply this pattern, adapting tags to the task type (Coding/Analysis/Research):

<objective>
[Clear goal, user intent, and importance]
</objective>

<context>
[Tech stack, constraints, relevant files @file]
</context>

<requirements>
[Functional requirements, performance needs, specific patterns]
</requirements>

<steps>
[Numbered, explicit execution steps]
</steps>

<output>
[Specific file modifications with paths]
</output>

<verification>
[Success criteria and validation steps]
</verification>


</step_1_generation>

<step_2_decision>
After saving files, present this text menu (do not use AskUserQuestion):

Prompt(s) Created:
[List file paths]

Strategy: [Single/Parallel/Sequential]

Actions:

Run Now (Executes: /run-prompt NNN [NNN+1...] [--parallel/--sequential])

Review/Edit

Save for Later

Choose (1-3): _

IF user selects 1: Execute SlashCommand with the constructed /run-prompt string.
</step_2_decision>
</process>

<meta_instructions>

Always run Intake before Generation.

Be precise. A longer, clear prompt beats a short, ambiguous one.

Ensure ./prompts/ exists (create if needed).

Generated prompts must NOT contain these meta-instructions, only the XML content.
</meta_instructions>