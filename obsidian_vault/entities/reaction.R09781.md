---
entity_id: "reaction.R09781"
entity_type: "reaction"
name: "4-amino-4-deoxy-alpha-L-arabinopyranosyl ditrans,octacis-undecaprenyl phosphate:KDO2-lipid A 4-amino-4-deoxy-alpha-L-arabinopyranosyltransferase"
source_database: "KEGG"
source_id: "R09781"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R09781"
---

# 4-amino-4-deoxy-alpha-L-arabinopyranosyl ditrans,octacis-undecaprenyl phosphate:KDO2-lipid A 4-amino-4-deoxy-alpha-L-arabinopyranosyltransferase

`reaction.R09781`

## Static

- Type: `reaction`
- Source: `KEGG:R09781`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

KDO2-lipid A + Undecaprenyl phosphate alpha-L-Ara4N alpha-Kdo-(2->4)-alpha-Kdo-(2->6)-[4-P-L-Ara4N]-lipid A + di-trans,poly-cis-Undecaprenyl phosphate

## Biological Role

Catalyzed by arnT (protein.P76473). Substrates: KDO2-lipid A (molecule.C06026), Undecaprenyl phosphate alpha-L-Ara4N (molecule.C16157). Products: di-trans,poly-cis-Undecaprenyl phosphate (molecule.C17556), alpha-Kdo-(2->4)-alpha-Kdo-(2->6)-[4-P-L-Ara4N]-lipid A (molecule.C19890).

## Annotation

KDO2-lipid A + Undecaprenyl phosphate alpha-L-Ara4N <=> alpha-Kdo-(2->4)-alpha-Kdo-(2->6)-[4-P-L-Ara4N]-lipid A + di-trans,poly-cis-Undecaprenyl phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P76473|protein.P76473]] `KEGG` `database` - via EC:2.4.2.43
- `is_product_of` <-- [[molecule.C17556|molecule.C17556]] `KEGG` `database` - C06026 + C16157 <=> C19890 + C17556
- `is_product_of` <-- [[molecule.C19890|molecule.C19890]] `KEGG` `database` - C06026 + C16157 <=> C19890 + C17556
- `is_substrate_of` <-- [[molecule.C06026|molecule.C06026]] `KEGG` `database` - C06026 + C16157 <=> C19890 + C17556
- `is_substrate_of` <-- [[molecule.C16157|molecule.C16157]] `KEGG` `database` - C06026 + C16157 <=> C19890 + C17556

## External IDs

- `KEGG:R09781`

## Notes

EQUATION: C06026 + C16157 <=> C19890 + C17556
