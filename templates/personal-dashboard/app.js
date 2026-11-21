const results = document.querySelector("#results");
const sections = { schedule: "Schedule", tasks: "Tasks", inbox: "Inbox" };

function render(data) {
  const cards = [];
  for (const [key, title] of Object.entries(sections)) {
    const entries = data?.[key];
    if (!Array.isArray(entries) || entries.some(item => typeof item !== "string")) {
      throw new Error(key + " must be a list of text entries.");
    }
    const card = document.createElement("article");
    const heading = document.createElement("h2");
    heading.textContent = title;
    const list = document.createElement("ul");
    for (const entry of entries) {
      const row = document.createElement("li");
      row.textContent = entry;
      list.append(row);
    }
    card.append(heading, entries.length ? list : "No entries.");
    cards.push(card);
  }
  results.replaceChildren(...cards);
}

render({ schedule: [], tasks: [], inbox: [] });
document.querySelector("#source").addEventListener("change", async event => {
  const file = event.target.files[0];
  if (!file) return;
  try {
    render(JSON.parse(await file.text()));
  } catch (error) {
    results.textContent = "Could not load briefing. " + error.message;
  }
});
