# AJ

I’m AJ, a petroleum engineering student who builds software for the people doing the work. During an engineering internship, I compared field teams’ accounts of how jobs ran with forecasts and Salesforce records. Those conversations helped me decide which problems were worth automating. Across the summer, the automation tools I built saved an estimated 200 hours.

My projects come from places where I know the work firsthand. Jordan Excavating gave me a reason to build a better contractor website. Student chapter leadership got me thinking about how to tell who an event actually reached. Life Board grew out of a question I kept running into myself: when school, work, and other commitments overlap, what needs my attention today?

## Jordan Excavating website

A contractor’s website has to work for someone looking up a service on a phone at a job site. I rebuilt Jordan Excavating’s site with Next.js and TypeScript, keeping the existing service URLs so customers could still follow a saved link to commercial earthwork or septic systems.

Two small decisions made the site easier to maintain. Contact details and service areas live in one configuration file, so an edit reaches every page that uses it. A contrast check catches hard-to-read brand color combinations before they ship.

[Read the case study](https://github.com/AJORDAN3/AJORDAN3/blob/main/PROJECTS.md#jordan-excavating-website) · [Explore the service-page starter](https://github.com/AJORDAN3/AJORDAN3/blob/main/examples/service-page.html) · [Try the color contrast check](https://github.com/AJORDAN3/AJORDAN3/blob/main/examples/contrast.py)

## Life Board

I built a planner that turns tasks mentioned in chat into cards on a Kanban board. The board and connected assistants share a Neon Postgres database through one API. A task can be due Friday, scheduled for Tuesday, or waiting on someone else. Life Board keeps those details separate so its daily agenda shows what can actually move today.

[Explore the design](https://github.com/AJORDAN3/AJORDAN3/blob/main/PROJECTS.md#life-board) · [Run the agenda query on fictional tasks](https://github.com/AJORDAN3/AJORDAN3/blob/main/examples/agenda.sql)

## Engineering and student leadership

| Project | Engineering decision |
| --- | --- |
| [Event attendance](https://github.com/AJORDAN3/AJORDAN3/blob/main/PROJECTS.md#event-attendance) | As a student chapter leader, I wanted to know both how many people showed up and how many distinct members we reached over a semester. |
| [AI project handoffs](https://github.com/AJORDAN3/AJORDAN3/blob/main/PROJECTS.md#ai-project-handoffs) | Store decisions and next steps by project so another assistant can resume the work. |
| [Pressure drawdown analysis](https://github.com/AJORDAN3/AJORDAN3/blob/main/PROJECTS.md#pressure-drawdown-analysis) | In reservoir engineering coursework, I used Python to measure how quickly well pressure fell during a drawdown test. |

[All eight project walkthroughs and reusable examples](https://github.com/AJORDAN3/AJORDAN3/blob/main/PROJECTS.md) · [Project log template](https://github.com/AJORDAN3/AJORDAN3/blob/main/PROJECT-TEMPLATE.md)

## How I approach engineering work

I start with a concrete case: a customer following an old service link, a volunteer who also checks in at the door, or a task that is overdue while someone else owns the next step. That gives me a requirement I can test. I carry the example through design and release validation, then document it so someone else can understand the decision and reuse the code.

You may copy, modify and redistribute the materials in this portfolio.
