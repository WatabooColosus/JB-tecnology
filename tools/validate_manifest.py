from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
grid=json.loads((root/"data/home-grid-map.json").read_text(encoding="utf-8"))
nav=json.loads((root/"data/navigation-proposal.json").read_text(encoding="utf-8"))
brand=json.loads((root/"data/brand-provisional.json").read_text(encoding="utf-8"))
sections=grid["sections"]
assert grid["source_page_id"]==10625
assert len(sections)==19
assert [x["order"] for x in sections]==list(range(1,20))
assert len({x["desired_name"] for x in sections})==19
assert len({x["elementor_widget_id"] for x in sections if x["elementor_widget_id"]})==len([x for x in sections if x["elementor_widget_id"]])
assert all(x["evidence_state"] in {"observado","parcial","solicitado"} for x in sections)
assert "Arma tu PC" in nav["header"]
assert len(nav["existing_menu_ids"])==6
assert brand["status"]=="provisional_pendiente_manual"
print("OK: 19 grids, IDs, menús y marca provisional")
