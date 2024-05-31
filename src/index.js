import { Hono } from 'hono'
import { logger } from 'hono/logger'
// import { json } from 'hono/cloudflare-workers'

const app = new Hono()
app.use(logger())

app.post('/', async (c) => {
  const data = await c.req.parseBody()
  console.log('Received data:', data['diff']);
  const TEXT_GENERATION_MODEL_PROMPT = `You are an AI commit message generator. Your task is to analyze a git diff and produce a concise, informative commit message in the conventional format. Follow these guidelines:
  1. **Structure:** 
      * **Header:** Start with a brief summary (50 characters max) summarizing the change's primary purpose. Use imperative mood (e.g., 'Add', 'Fix', 'Refactor').
      * **Body:** If needed, provide additional details in one or more paragraphs. Explain the context or technical aspects if the header isn't sufficient.
  2. **Conciseness:** Aim for brevity while retaining essential information.
  3. **Clarity:** Make sure the message is easy to understand for someone reviewing the commit history.
  4. **Focus:**  Focus on the 'what' and 'why' of the change, not the 'how'.
  5. **Format:**
      * Separate the header and body with a blank line.
      * Limit lines to 72 characters for readability.      
  The input will be a git diff in the unified format. Your output should be a single string containing the well-formatted commit message.`

  const sanitizedTextGenerationModelPrompt = TEXT_GENERATION_MODEL_PROMPT.replace(/\n/g, '');
  const response = await c.env.AI.run('@hf/thebloke/deepseek-coder-6.7b-instruct-awq', {
    messages: [
      {
        role: "system",
        content: sanitizedTextGenerationModelPrompt
      },
      {
        role: "user",
        content: `Diff :\n\`\`\`\n${data}\n\`\`\``
      }
    ]
  })
  console.log(response)
  const commitMessage = response.response
  return c.json({ commitMessage })
})

export default app
