#!/usr/bin/env python3
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
def read(path):return json.loads((root/path).read_text(encoding="utf-8"))
land=read("data/landing-spec.json")
back=read("data/backlog.json")
snap=read("data/staging-snapshot.json")
sections=land["sections"]
tasks=back["tasks"]
assert len(sections)==19 and land["section_count"]==19
assert [s["order"] for s in sections]==list(range(1,20))
assert len({s["key"] for s in sections})==19
assert len({s["title"] for s in sections})==19
assert all(s["source_confidence"] in {"observado","parcial","solicitado"} for s in sections)
assert all(s["status"]=="pending" and not s["published_to_staging"] for s in sections)
assert len(tasks)==16 and len({t["id"] for t in tasks})==len(tasks)
ids={t["id"] for t in tasks}
assert all(set(t["depends_on"]).issubset(ids) and t["id"] not in t["depends_on"] for t in tasks)
assert all(t["priority"] in {"P0","P1","P2","P3"} for t in tasks)
assert all(s["task"] in ids for s in sections)
assert all(t["issue_url"].endswith("/issues/"+str(t["issue"])) for t in tasks)
assert len({t["issue"] for t in tasks})==16
assert snap["homepage"]["id"]==10625
assert snap["staging_url"]=="https://staging.jbtecnologiamed.com.co"
assert snap["security"]["noindex_detected_in_head"] is False
print(f"OK: {len(sections)} bloques, {len(tasks)} issues enlazadas, staging e integridad de tareas")
