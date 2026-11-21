const filter = document.querySelector("#filter");
const results = document.querySelector("#results");
function render() {
  const query = filter.value.trim().toLowerCase();
  const matches = projects.filter(project =>
    !query || project.skills.some(skill => skill.toLowerCase().includes(query))
  );
  results.replaceChildren();
  for (const project of matches) {
    const card = document.createElement("article");
    const title = document.createElement("h2");
    title.textContent = project.title;
    card.append(title);
    for (const [label, value] of [
      ["Problem", project.problem], ["Decision", project.decision],
      ["Result", project.result], ["Skills", project.skills.join(", ")]
    ]) {
      const line = document.createElement("p");
      const name = document.createElement("strong");
      name.textContent = label + ": ";
      line.append(name, value);
      card.append(line);
    }
    results.append(card);
  }
  if (!matches.length) results.textContent = projects.length
    ? "No projects match that skill." : "Add your first project in projects.js.";
}
filter.addEventListener("input", render);
render();
