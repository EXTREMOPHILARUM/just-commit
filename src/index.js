import { Hono } from 'hono'
// import { json } from 'hono/cloudflare-workers'

const app = new Hono()

app.post('/', async (c) => {
  const { diff } = c.req.json()

  const response = await c.env.AI.run('@cf/meta/llama-2-7b-chat-int8', {
    messages: [
      {
        role: "system",
        content: `You are a git commit message generator. You will be provided with a git diff and must return only a single concise and informative commit message. The response should conform to the following specifications.
                  type: type of commit
                  scope: Short description of a section of the codebase enclosed in parenthesis followed by a colon and a space. Messages tend to be in the present and imperative.
                  description: Short description of the code changes
                  body: A longer description of the commit, providing additional context about the changes.
                  Must be placed one empty line after the description.
                  footer: Fixes issue #3 //example
                  The footer should only contain additional issue references about the changes.
                  Example:
                  feat(homepage): Add carousel feature to showcase testimonials
                  Implemented a carousel component on the homepage
                  Added client testimonials section for improved user engagement
                  Fixes #12`
      },
      {
        role: "user",
        content: `Diff :\n\`\`\`\n${diff}\n\`\`\``
      }
    ]
  })
  console.log(response)
  const commitMessage = response.response
  return c.json({ commitMessage })
})

export default app
