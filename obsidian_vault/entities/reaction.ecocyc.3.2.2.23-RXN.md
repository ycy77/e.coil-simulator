---
entity_id: "reaction.ecocyc.3.2.2.23-RXN"
entity_type: "reaction"
name: "3.2.2.23-RXN"
source_database: "EcoCyc"
source_id: "3.2.2.23-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 3.2.2.23-RXN

`reaction.ecocyc.3.2.2.23-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:3.2.2.23-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

DNA-containing-diamino-hydro-formamidops + WATER -> CPD-16491 + 5-Phospho-terminated-DNAs + 3-Prime-Phosphate-Terminated-DNAs + CPD-21221 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: DNA-containing-diamino-hydro-formamidops + WATER -> CPD-16491 + 5-Phospho-terminated-DNAs + 3-Prime-Phosphate-Terminated-DNAs + CPD-21221 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Catalyzed by mutM (protein.P05523). Substrates: H2O (molecule.C00001), a ring-opened 7-methylguanine in DNA (molecule.ecocyc.DNA-containing-diamino-hydro-formamidops). Products: H+ (molecule.C00080), 2,6-diamino-4-hydroxy-5-(N-methyl)formamidopyrimidine (molecule.ecocyc.CPD-16491), 4-oxo-2-pentenal (molecule.ecocyc.CPD-21221).

## Annotation

DNA-containing-diamino-hydro-formamidops + WATER -> CPD-16491 + 5-Phospho-terminated-DNAs + 3-Prime-Phosphate-Terminated-DNAs + CPD-21221 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P05523|protein.P05523]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-16491|molecule.ecocyc.CPD-16491]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.ecocyc.CPD-21221|molecule.ecocyc.CPD-21221]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.ecocyc.DNA-containing-diamino-hydro-formamidops|molecule.ecocyc.DNA-containing-diamino-hydro-formamidops]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:3.2.2.23-RXN`

## Notes

DNA-containing-diamino-hydro-formamidops + WATER -> CPD-16491 + 5-Phospho-terminated-DNAs + 3-Prime-Phosphate-Terminated-DNAs + CPD-21221 + PROTON; direction=PHYSIOL-LEFT-TO-RIGHT
