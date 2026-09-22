---
name: Comment_Skill
description: Add structured comments to coding problem solutions for better revision understanding
trigger: Use when asked to add comments or documentation to coding challenge/problem solutions
---

# Comment Skill for Coding Problems

## Purpose
This skill defines how to add comprehensive, structured comments to coding problem solutions that help with revision and understanding, without cluttering the actual code.

## When to Use
- When asked to add comments to a coding challenge solution
- When documenting a new problem solution
- When the user mentions "add comments for revision" or similar phrases
- When asked to document the approach or algorithm

## Comment Structure

### Location
- **DO NOT** add inline comments within the code itself
- **DO** create a separate documentation section at the top of the file
- Place documentation after the problem URL/reference and before the code implementation
- Use triple quotes `'''` to create a multi-line comment block

### Required Sections

The documentation should include these sections in order:

#### 1. PROBLEM STATEMENT
```
PROBLEM STATEMENT:
------------------
Brief, clear description of what the problem asks you to solve.
Include input/output format if relevant.
State the goal clearly.
```

#### 2. APPROACH
```
APPROACH - [Algorithm Name]:
---------------------------
Key Insight: Explain the main insight or observation that leads to the solution

Strategy:
- List the main strategy points
- Explain why this approach works
- Mention the technique used (e.g., Sliding Window, Two Pointers, etc.)
```

#### 3. ALGORITHM STEPS
```
ALGORITHM STEPS:
----------------
1. Step-by-step breakdown of the algorithm
2. Each step should be clear and actionable
3. Explain what each major variable/pointer represents
4. Describe the iteration/loop logic
5. Mention the final return value
```

#### 4. EXAMPLE WALKTHROUGH
```
EXAMPLE WALKTHROUGH:
--------------------
Input: [provide concrete example]

Walk through the algorithm step-by-step with this input:
- Show initial state
- Show each iteration with variable values
- Show how the result is built up
- End with the final answer

This section helps visualize how the algorithm works.
```

#### 5. COMPLEXITY ANALYSIS
```
COMPLEXITY ANALYSIS:
--------------------
Time Complexity: O(?) 
- Explain why (number of iterations, nested loops, etc.)

Space Complexity: O(?)
- Explain what extra space is used (or if only constant space)
```

## Formatting Guidelines

### Visual Separation
- Use `#########################################################################################` to separate major sections
- Use `------------------` under section headers for clarity
- Leave blank lines between sections for readability

### Writing Style
- Be concise but complete
- Use bullet points for lists
- Write in clear, simple language
- Avoid jargon unless necessary (and explain it if used)
- Focus on the "why" not just the "what"

### Code Section
- Keep the actual code clean without inline comments
- Let variable names be self-documenting
- Only add inline comments if absolutely necessary for complex logic

## Template

```python
'''
[Problem URL or reference]
'''

# Subarray/Substring = contiguous
# Subsequence = can skip elements
#########################################################################################
##########################  [Algorithm Name] Approach  ##########################

'''
PROBLEM STATEMENT:
------------------
[Clear problem description]
[Input/Output format]
Goal: [What we're trying to achieve]

APPROACH - [TECHNIQUE NAME]:
---------------------------
Key Insight: [Main observation]

Strategy:
- [Point 1]
- [Point 2]
- [Point 3]

ALGORITHM STEPS:
----------------
1. [Step 1]
2. [Step 2]
3. [Step 3]
...

EXAMPLE WALKTHROUGH:
--------------------
Input: [example]

[Step-by-step walkthrough showing how algorithm processes the example]

Answer: [final result with brief explanation]

COMPLEXITY ANALYSIS:
--------------------
Time Complexity: O(?)
- [Explanation]

Space Complexity: O(?)
- [Explanation]
'''

#########################################################################################

class Solution:
    def methodName(self, params):
        # Clean code without inline comments
        pass
        
#########################################################################################
```

## Important Notes

1. **Consistency**: Use this format consistently across all problem solutions
2. **Revision Focus**: Write comments as if you're explaining to your future self
3. **No Code Pollution**: Keep the actual implementation clean and readable
4. **Complete Examples**: Always include a concrete example walkthrough
5. **Complexity**: Always analyze and document time/space complexity

## Examples of Good Comments

✅ "Key Insight: Since we can only pick from ends, we have k+1 combinations"
✅ "Strategy: Start with all k from left, then slide window by swapping left for right"
✅ "Time Complexity: O(k) - We iterate k times for initial sum and k times for sliding"

## Examples of What to Avoid

❌ Inline comments like: `i = 0  # initialize counter`
❌ Vague descriptions: "Use a loop to process the data"
❌ Missing complexity analysis
❌ No concrete example walkthrough
❌ Comments that just repeat what the code does
