# Engineering project log

Each entry pairs the original project with a focused exercise. Run commands from the portfolio root with Python 3 or the SQLite CLI. The browser example opens directly from disk.

| Project | Skills practiced | Starter |
| --- | --- | --- |
| Jordan Excavating website | Next.js · TypeScript · content modeling · accessibility | [Service page](examples/service-page.html) · [contrast check](examples/contrast.py) |
| Event attendance | Postgres · data modeling · volunteer workflows | [attendance.sql](examples/attendance.sql) |
| Pressure drawdown analysis | Python · regression · reservoir engineering | [drawdown.py](examples/drawdown.py) |
| AI project handoffs | SQL · API design · Model Context Protocol | [handoffs.sql](examples/handoffs.sql) |
| Daily briefing | Python · service integration · failure handling | [briefing.py](examples/briefing.py) |
| Reusable assistant skills | Workflow design · prompt design · MCP integration | [review-skill.md](examples/review-skill.md) |
| Engineering showcase | Next.js · TypeScript · technical communication | [decision-record.md](examples/decision-record.md) |
| Task board | SQL · task scheduling · state modeling | [agenda.sql](examples/agenda.sql) |

## Jordan Excavating website

The rebuild had two audiences: customers trying to find the right service and the person responsible for keeping business details current. I used Next.js and TypeScript, retained the established service paths, and separated shared business facts from service-specific copy.

| Decision | Why it matters | What to repeat on another site |
| --- | --- | --- |
| Preserve service URLs during the rebuild | A contractor following an old bookmark can still reach the intended service. | Inventory the existing routes before designing navigation. |
| Keep contact information and coverage in one typed configuration | A phone number or service area can change in one place. | Identify facts repeated across pages before building components. |
| Check brand color pairings during the build | Gold lettering that reads clearly on a dark background can disappear on a light one. | Test the actual foreground/background combinations alongside type and lint checks. |

**Try the service catalog.** Open the [standalone page](examples/service-page.html), switch districts, then add a service to the catalog. The selector and results read from the same data. The sample uses fictional districts so it can be adapted for another business.

**Try the accessibility check.** Run `python3 examples/contrast.py 000000 FFFFFF`. It prints `21.00:1` and exits successfully. Run it again with `777777 FFFFFF`: the ratio falls just below the normal-text threshold and the command exits with a failure. That exit code makes the check usable in a build.

[Company website](https://jordanexcavatinginc.com/)

## Event attendance

Event organizers need two counts that answer different questions. Event turnout counts someone each time they attend. Semester reach counts that person once. The event site brings tabling volunteers and attendee check-ins into the same reporting workflow.

**For the next build.** Choose the unit of counting before building the form. Enforce one attendance record per person per event and let both intake paths use it.

**Try the [standalone example](examples/attendance.sql).** `sqlite3 :memory: < examples/attendance.sql`. The fall social has two attendees, the field talk has one, and semester reach is two. Add a third event with an existing member and predict both totals.

## Pressure drawdown analysis

For a reservoir engineering drawdown analysis, I used diagnostic plots to select an infinite-acting radial-flow interval, then fit flowing pressure against log time. The slope is one input to a permeability estimate.

**For the next build.** Identify the flow regime first. Record the interval, pressure units and time convention alongside the slope so the analysis can be repeated.

**Try the [standalone example](examples/drawdown.py).** `python3 examples/drawdown.py`. The synthetic interval falls about 40 psi per tenfold increase in elapsed time. Replace the points with an interval you have independently selected. This example fits the line only.

## AI project handoffs

I built a shared memory service around Neon Postgres so a project decision made in one AI tool could be picked up in another. The original uses a REST API and MCP tools. This example isolates the storage and retrieval step.

**For the next build.** Start with the smallest useful handoff: project, decision and next action. Test retrieval with two interleaved projects before connecting another client.

**Try the [standalone example](examples/handoffs.sql).** `sqlite3 :memory: < examples/handoffs.sql`. The lookup returns the newest demo decision and its next step. Change the project filter to other to see the two threads stay independent.

## Daily briefing

I built a personal dashboard that brings weather and inbox summaries into one view. The backend keeps its data providers separate from the page. The standalone version exercises that boundary with fictional providers.

**For the next build.** Give each provider a small return value and decide what the reader should see when one source times out.

**Try the [standalone example](examples/briefing.py).** `python3 examples/briefing.py`. Weather reports a temporary outage while the calendar and inbox still render. Replace one provider with a function that returns your own local summary.

## Reusable assistant skills

I organized an assistant around a small set of routing instructions and on-demand skills. Each skill gives a recurring activity its own inputs, steps and output. The sample turns a design decision into interview practice.

**For the next build.** Write one narrow trigger, define the expected output, then try the instructions in a fresh conversation where the assistant has no history.

**Try the [standalone example](examples/review-skill.md).** Open examples/review-skill.md and use the trial prompt. The exercise should ask one question at a time and end with evidence from the speaker’s answers. Change the audience and check whether the feedback still fits.

## Engineering showcase

I built an interactive Next.js portfolio for a set of engineering projects, pairing technical decisions with the work that motivated them. A short decision record gives a reviewer a way to inspect the reasoning behind a feature.

**For the next build.** Capture the operational constraint, one choice and its cost while the decision is fresh. Finish with something another person can verify.

**Try the [standalone example](examples/decision-record.md).** Open examples/decision-record.md and copy the headings. The worked example explains why chapter officers benefit from database-backed events. Replace the example with a decision from your build and give it an observable acceptance check.

## Task board

I built a Kanban board on top of the shared-memory API so a task could move from a conversation into a daily agenda. A planned work date and a deadline answer different questions. Status adds a third dimension: a task can be overdue while someone else owns the next action.

**For the next build.** Store the work date, due date and status separately. Test the agenda with a completed item, a blocked item, an overdue item and an item planned for today.

**Try the [agenda query](examples/agenda.sql).** Run `sqlite3 :memory: < examples/agenda.sql`. The abstract appears first because it is overdue. Field notes appear because they are scheduled for the sample date. Change the venue quote to `doing` and run the query again in a fresh database.
