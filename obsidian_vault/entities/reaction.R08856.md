---
entity_id: "reaction.R08856"
entity_type: "reaction"
name: "UDP-N-acetyl-D-glucosamine:undecaprenyl-phosphate N-acetyl-D-glucosamine phosphotransferase"
source_database: "KEGG"
source_id: "R08856"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R08856"
---

# UDP-N-acetyl-D-glucosamine:undecaprenyl-phosphate N-acetyl-D-glucosamine phosphotransferase

`reaction.R08856`

## Static

- Type: `reaction`
- Source: `KEGG:R08856`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

UDP-N-acetyl-alpha-D-glucosamine + di-trans,poly-cis-Undecaprenyl phosphate N-Acetyl-D-glucosaminyldiphosphoundecaprenol + UMP

## Biological Role

Catalyzed by wecA (protein.P0AC78). Substrates: UDP-N-acetyl-alpha-D-glucosamine (molecule.C00043), di-trans,poly-cis-Undecaprenyl phosphate (molecule.C17556). Products: UMP (molecule.C00105).

## Annotation

UDP-N-acetyl-alpha-D-glucosamine + di-trans,poly-cis-Undecaprenyl phosphate <=> N-Acetyl-D-glucosaminyldiphosphoundecaprenol + UMP

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `catalyzes` <-- [[protein.P0AC78|protein.P0AC78]] `KEGG` `database` - via EC:2.7.8.33
- `is_product_of` <-- [[molecule.C00105|molecule.C00105]] `KEGG` `database` - C00043 + C17556 <=> C01289 + C00105
- `is_substrate_of` <-- [[molecule.C00043|molecule.C00043]] `KEGG` `database` - C00043 + C17556 <=> C01289 + C00105
- `is_substrate_of` <-- [[molecule.C17556|molecule.C17556]] `KEGG` `database` - C00043 + C17556 <=> C01289 + C00105

## External IDs

- `KEGG:R08856`

## Notes

EQUATION: C00043 + C17556 <=> C01289 + C00105
