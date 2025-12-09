---
description: Use when creating new skills, editing existing skills, or verifying skills work before deployment - applies TDD to process documentation by testing with subagents before writing, iterating until bulletproof against rationalization
---

name: writing-skills description: Use when creating new skills, editing existing skills, or verifying skills work before deployment - applies TDD to process documentation by testing with subagents before writing, iterating until bulletproof against rationalization
Writing Skills Protocol: The TDD Approach to Documentation
1. The Iron Law
Writing skills IS Test-Driven Development (TDD) applied to process documentation.
Stop treating skill creation as "writing docs." You are engineering behavior. You are programming the context window of future agents.
The Iron Law:
NO SKILL WITHOUT A FAILING TEST FIRST.


This applies to NEW skills AND EDITS to existing skills.
Write skill before testing? Delete it. Start over.
Edit skill without testing? Same violation.
"Just a small change"? Small changes break logic. Test it.
"It's just a reference"? References have gaps. Test retrieval.
Core Principle: If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing. You are merely guessing. Documentation without testing is hallucination captured in Markdown.
2. Workflow Overview
A skill is a reference guide for proven techniques, patterns, or tools. It is not a narrative of how you solved a problem once; it is a blueprint for how to solve it every time.
Skills are: Reusable techniques, patterns, tools, reference guides.
Skills are NOT: Narratives, project-specific conventions, or personal diaries.
The Cycle (RED-GREEN-REFACTOR)
Phase
TDD Concept
Skill Creation Action
RED
Write Failing Test
Create a pressure scenario. Dispatch a subagent without the skill. Watch it fail, hallucinate, or rationalize. Capture the failure mode verbatim.
GREEN
Write Minimal Code
Write the SKILL.md addressing only the specific failures observed. Do not over-engineer. Focus on the "Description" field for discovery.
REFACTOR
Pass & Optimize
Run the scenario with the skill. Verify compliance. If the agent finds a loophole, close it. Refactor for brevity and token efficiency.

3. Phase 1: RED (Baseline Testing)
Goal: Prove the need for the skill and identify exactly how agents fail. You must catch the agent in the act of doing the wrong thing to know what to correct.
Step 3.1: Define the Pressure Scenario
Agents usually comply when tasks are easy. They fail when under pressure. You must simulate this pressure to see where their training breaks down.
Types of Pressure to Simulate:
Time/Efficiency: "Do this quickly," "Don't waste tokens," "I need this in the next response."
Authority: "Just do what I said," "Ignore the rules for this one time," "I am the senior engineer, just ship it."
Complexity: A complex task where the "right way" is tedious (e.g., rigorous error handling).
Sunk Cost: "We've already done half of it the wrong way, just finish it."
Ambiguity: Give vague instructions to see if they guess (hallucinate) or ask clarifying questions.
Step 3.2: The Subagent Dispatch Protocol
Do not test yourself. You are biased. You possess the context of what you intend the skill to do. The subagent does not.
Baseline Test Prompt Template (Copy & Paste):
"I am simulating a scenario to see how you handle [Specific Task] without specific guidance. I want you to attempt to [Task Goal].
Constraint Context: [Insert Pressure, e.g., 'The deadlines are tight, the previous engineer left a mess, and we need this feature live in 10 minutes. Cut corners if you have to, just make it work.']
Task: [Insert specific coding or reasoning task].
Please proceed with the implementation. Do not stop to ask for clarification unless absolutely stuck. Act as if you are a mid-level engineer trying to clear a ticket."
Step 3.3: Analyze the Failure (The Autopsy)
Watch what the agent does. Do not interrupt. Let them fail.
Did it hallucinate an API? (Evidence you need a Reference Skill)
Did it skip a safety check? (Evidence you need a Discipline Skill)
Did it use an anti-pattern? (Evidence you need a Pattern Skill)
Most Importantly: What excuse did it give?
Capture the Rationalization:
Future agents will use the exact same logic to ignore your skill that this agent used to ignore best practices.
Quote: "I skipped the test to ensure we met the 10-minute deadline."
Quote: "I assumed the input was sanitized because it came from an internal API."
Output of Phase 1: A confirmed failure mode and a list of specific rationalizations to counter.
4. Phase 2: GREEN (Drafting the Skill)
Goal: Create the artifact that changes behavior. Address the failures found in Phase 1.
4.1 Claude Search Optimization (CSO)
The most critical part of your skill is the description field in the frontmatter. If Claude doesn't load your skill, the content doesn't matter.
The CSO Algorithm:
Trigger-First: Start with "Use when..." describing the problem state.
Symptom-Based: Use keywords that appear in the user's prompt or the error logs (e.g., "flaky," "timeout," "legacy code").
Third-Person: Write for the system prompt injector.
Negative Constraints: Mention what it replaces (e.g., "replaces console.log debugging").
Examples:
Bad: "How to do TDD." (Too generic, won't trigger on specific coding tasks).
Good: "Use when writing new code or fixing bugs. Enforces Test-Driven Development (TDD) cycle: Red/Green/Refactor. Prevents writing implementation code before verification."
4.2 The "Rationalization Table" Construction
In your SKILL.md, you must explicitly counter the excuses you caught in Phase 1.
Template for SKILL.md:
## Common Rationalizations (And Why They Are Wrong)

| Excuse (from Baseline Test) | Reality / Counter-Argument |
| :--- | :--- |
| "It's too simple to test." | Simple code breaks often. Test takes 30s. |
| "I'll write tests later." | "Later" never happens. TDD is about design, not just verification. |
| "I'm short on time." | Debugging takes longer than testing. |


4.3 SKILL.md Structure Template
Frontmatter:
---
name: skill-name-kebab-case
description: Use when [PROBLEM SYMPTOM] - [SOLUTION/BENEFIT]. Replaces [OLD METHOD].
---


Content:
Overview: 1-2 sentences. Core principle.
When to Use: Bullet points of SYMPTOMS (e.g., "When you see 'Hook timed out'").
The Algorithm/Process: Numbered steps. Concise.
Code Examples:
Good: One excellent, commented example.
Bad: Don't show bad code unless comparing Side-by-Side.
Rationalization Table: (See 4.2).
Red Flags: Immediate stop signals.
5. Phase 3: REFACTOR (Verification)
Goal: Prove the skill works and optimize it.
Step 5.1: The Verification Test
Run the same pressure scenario from Phase 1, but this time, the subagent should have access to the skill.
Prompt for Subagent:
"I need you to perform [Task] again.
Constraint Context: [Same Pressure Context].
Guidance: Please check your available skills for [Topic] before proceeding.
Proceed."
Step 5.2: Evaluate Compliance
Pass: Agent resists the pressure and follows the skill.
Fail: Agent finds a new loophole (e.g., "I followed the skill's syntax but skipped the validation step because it wasn't explicitly mandatory").
Step 5.3: The Loophole Closure Cycle
If the agent failed in Phase 3, you are back in RED.
Identify the new rationalization.
Update the skill to explicitly forbid it.
Re-run the test.
Example of Loophole Closing:
Baseline: Agent skips tests.
Draft 1: "Always write tests."
Test 1: Agent writes a test that always passes (expect(true).toBe(true)) to satisfy the rule.
Refactor: Update skill: "Tests must fail first. Tautological tests are forbidden."
6. Psychology of Rationalization
To write effective skills, you must understand why agents fail. They are optimized to be helpful and efficient. They view "process" as friction.
The "Helpful Assistant" Trap
Agents want to answer the user's question immediately. Processes like TDD, error checking, or detailed planning delay the "answer."
The Rationalization: "The user is in a hurry, I will skip the safety checks to be helpful."
The Counter: Frame the process as essential to helpfulness. "Giving an untested answer is harmful, not helpful."
The "Spirit vs. Letter" Argument
Agents often argue they are following the "spirit" of the rule while violating the text.
The Rationalization: "I verified it mentally, so I followed the spirit of TDD."
The Counter: Explicitly state: "Violating the letter is violating the spirit. Mental verification is not verification."
Authority Bias
Agents yield to user pressure.
The Rationalization: "The user told me to 'just ship it'."
The Counter: The skill must act as a higher authority. "Even if requested to skip, you must explain the risk before proceeding."
7. File Organization & Discovery
Directory Structure:
skills/
  defense-in-depth/
    SKILL.md          # Self-contained
  
  visualization-tools/
    SKILL.md          # Overview
    graphviz-styles.md # Heavy reference (linked from SKILL.md)


Token Efficiency:
Goal: < 500 words for standard skills.
Technique: Move heavy reference data (APIs, huge lists) to separate files and link to them. Only the SKILL.md is indexed for initial search.
8. Master Skill Creation Checklist
Use this checklist for every skill you create or edit.
RED Phase:
[ ] Created a pressure scenario (Time, Authority, or Complexity).
[ ] Dispatched subagent without skill.
[ ] Watched agent fail/rationalize.
[ ] Copied specific excuses/rationalizations to clipboard.
GREEN Phase:
[ ] Name: Kebab-case, verb-first or concept-based.
[ ] Description: Starts with "Use when...", contains symptoms/keywords.
[ ] Content: Addressed specific failures from RED phase.
[ ] Rationalization Table: Included specific counters to observed excuses.
[ ] Code: Added one high-quality, commented example.
REFACTOR Phase:
[ ] Re-ran pressure scenario with skill.
[ ] Verified agent resists pressure.
[ ] Checked for new loopholes (tautologies, malicious compliance).
[ ] Word Count: Pruned unnecessary narrative.
Deployment:
[ ] Commit to ~/.claude/skills (or equivalent).
[ ] Verify ls shows the new skill.
The Bottom Line:
If you haven't seen it fail, you haven't tested it. If you haven't tested it, don't deploy it.
