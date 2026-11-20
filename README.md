# AJ

I build websites, automate everyday workflows, and write tools for engineering analysis.

## Jordan Excavating website

A contractor’s website has to work for someone looking up a service on a phone at a job site. I rebuilt Jordan Excavating’s site with Next.js and TypeScript, keeping the existing service URLs so customers could still follow a saved link to commercial earthwork or septic systems.

Two small decisions made the site easier to maintain. Contact details and service areas live in one configuration file, so an edit reaches every page that uses it. A contrast check catches hard-to-read brand color combinations before they ship.

[Read the case study](https://github.com/ashleigh24jordan-ops/ashleigh24jordan-ops/blob/main/PROJECTS.md#jordan-excavating-website) · [Explore the service-page starter](https://github.com/ashleigh24jordan-ops/ashleigh24jordan-ops/blob/main/examples/service-page.html) · [Try the color contrast check](https://github.com/ashleigh24jordan-ops/ashleigh24jordan-ops/blob/main/examples/contrast.py)

## Life Board

I built a planner that turns tasks mentioned in chat into cards on a Kanban board. The board and connected assistants share a Neon Postgres database through one API. A task can be due Friday, scheduled for Tuesday, or waiting on someone else. Life Board keeps those details separate so its daily agenda shows what can actually move today.

[Explore the design](https://github.com/ashleigh24jordan-ops/ashleigh24jordan-ops/blob/main/PROJECTS.md#life-board) · [Run the agenda query on fictional tasks](https://github.com/ashleigh24jordan-ops/ashleigh24jordan-ops/blob/main/examples/agenda.sql)

## More selected work

| Project | Engineering decision |
| --- | --- |
| [Event attendance](https://github.com/ashleigh24jordan-ops/ashleigh24jordan-ops/blob/main/PROJECTS.md#event-attendance) | Combine volunteer rosters and check-ins while counting each person once per event. |
| [AI project handoffs](https://github.com/ashleigh24jordan-ops/ashleigh24jordan-ops/blob/main/PROJECTS.md#ai-project-handoffs) | Store decisions and next steps by project so another assistant can resume the work. |
| [Pressure drawdown analysis](https://github.com/ashleigh24jordan-ops/ashleigh24jordan-ops/blob/main/PROJECTS.md#pressure-drawdown-analysis) | Fit a line over a selected flow interval and report the pressure change per tenfold increase in elapsed time. |

[All eight project walkthroughs and reusable examples](https://github.com/ashleigh24jordan-ops/ashleigh24jordan-ops/blob/main/PROJECTS.md) · [Project log template](https://github.com/ashleigh24jordan-ops/ashleigh24jordan-ops/blob/main/PROJECT-TEMPLATE.md)

## How I approach engineering work

I start by tracing how people do the job today. I compare operational forecasts and Salesforce records with what field teams describe, then turn the gaps into requirements I can test. I carry those checks through release validation with the people who use the workflow.

You may copy, modify and redistribute the materials in this portfolio.
