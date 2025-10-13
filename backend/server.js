const express = require("express");
const fs = require("fs");
const app = express();
const PORT = 3000;

app.use(express.json());

app.post("/measure", (req, res) => {
  const { value } = req.body;
  const data = { value, timestamp: new Date().toISOString() };
  fs.appendFileSync("./data/measures.json", JSON.stringify(data) + "\n");
  console.log("Măsurare:", data);
  res.json({ message: "Valoare salvată" });
});

app.get("/data", (req, res) => {
  const content = fs.readFileSync("./data/measures.json", "utf-8");
  const lines = content.trim().split("\n").map(JSON.parse);
  res.json(lines);
});

app.listen(PORT, () => console.log(`Backend pornit pe portul ${PORT}`));