# Decision · Store event dates as records

**Context.** Chapter officers need to add events after the semester calendar has been published.

**Choice.** Store each event with a date, title, and publication state. Read published records on the calendar page.

**Tradeoff.** An officer can correct a date without a deploy. The application now needs a reliable database and an editing workflow.

**Acceptance check.** Change a draft event's date, publish it, and verify that the calendar shows the corrected date exactly once.

**Reuse.** Replace the context with a decision from your own build. Record who operates the result, what gets easier, what gets harder, and the smallest observation that would make you revisit it.
