---
entity_id: "reaction.R00177"
entity_type: "reaction"
name: "ATP:L-methionine S-adenosyltransferase"
source_database: "KEGG"
source_id: "R00177"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00177"
---

# ATP:L-methionine S-adenosyltransferase

`reaction.R00177`

## Static

- Type: `reaction`
- Source: `KEGG:R00177`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Orthophosphate + Diphosphate + S-Adenosyl-L-methionine ATP + L-Methionine + H2O

## Biological Role

Catalyzed by metK (protein.P0A817). Substrates: Orthophosphate (molecule.C00009), Diphosphate (molecule.C00013), S-Adenosyl-L-methionine (molecule.C00019). Products: H2O (molecule.C00001), ATP (molecule.C00002), L-Methionine (molecule.C00073).

## Annotation

Orthophosphate + Diphosphate + S-Adenosyl-L-methionine <=> ATP + L-Methionine + H2O

## Outgoing Edges (0)

_None._

## Incoming Edges (7)

- `catalyzes` <-- [[protein.P0A817|protein.P0A817]] `KEGG` `database` - via EC:2.5.1.6
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C00009 + C00013 + C00019 <=> C00002 + C00073 + C00001
- `is_product_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C00009 + C00013 + C00019 <=> C00002 + C00073 + C00001
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `KEGG` `database` - C00009 + C00013 + C00019 <=> C00002 + C00073 + C00001
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C00009 + C00013 + C00019 <=> C00002 + C00073 + C00001
- `is_substrate_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C00009 + C00013 + C00019 <=> C00002 + C00073 + C00001
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - C00009 + C00013 + C00019 <=> C00002 + C00073 + C00001

## External IDs

- `KEGG:R00177`

## Notes

EQUATION: C00009 + C00013 + C00019 <=> C00002 + C00073 + C00001
