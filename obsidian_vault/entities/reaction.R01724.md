---
entity_id: "reaction.R01724"
entity_type: "reaction"
name: "5-phospho-alpha-D-ribose 1-diphosphate:nicotinate ligase (ADP, diphosphate-forming)"
source_database: "KEGG"
source_id: "R01724"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R01724"
---

# 5-phospho-alpha-D-ribose 1-diphosphate:nicotinate ligase (ADP, diphosphate-forming)

`reaction.R01724`

## Static

- Type: `reaction`
- Source: `KEGG:R01724`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Nicotinate D-ribonucleotide + Diphosphate + ADP + Orthophosphate Nicotinate + 5-Phospho-alpha-D-ribose 1-diphosphate + ATP + H2O + H+

## Biological Role

Catalyzed by pncB (protein.P18133). Substrates: ADP (molecule.C00008), Orthophosphate (molecule.C00009), Diphosphate (molecule.C00013), Nicotinate D-ribonucleotide (molecule.C01185). Products: H2O (molecule.C00001), ATP (molecule.C00002), H+ (molecule.C00080), 5-Phospho-alpha-D-ribose 1-diphosphate (molecule.C00119), Nicotinate (molecule.C00253).

## Annotation

Nicotinate D-ribonucleotide + Diphosphate + ADP + Orthophosphate <=> Nicotinate + 5-Phospho-alpha-D-ribose 1-diphosphate + ATP + H2O + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P18133|protein.P18133]] `KEGG` `database` - via EC:6.3.4.21
- `is_product_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C01185 + C00013 + C00008 + C00009 <=> C00253 + C00119 + C00002 + C00001 + C00080
- `is_product_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - C01185 + C00013 + C00008 + C00009 <=> C00253 + C00119 + C00002 + C00001 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C01185 + C00013 + C00008 + C00009 <=> C00253 + C00119 + C00002 + C00001 + C00080
- `is_product_of` <-- [[molecule.C00119|molecule.C00119]] `KEGG` `database` - C01185 + C00013 + C00008 + C00009 <=> C00253 + C00119 + C00002 + C00001 + C00080
- `is_product_of` <-- [[molecule.C00253|molecule.C00253]] `KEGG` `database` - C01185 + C00013 + C00008 + C00009 <=> C00253 + C00119 + C00002 + C00001 + C00080
- `is_substrate_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - C01185 + C00013 + C00008 + C00009 <=> C00253 + C00119 + C00002 + C00001 + C00080
- `is_substrate_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - C01185 + C00013 + C00008 + C00009 <=> C00253 + C00119 + C00002 + C00001 + C00080
- `is_substrate_of` <-- [[molecule.C00013|molecule.C00013]] `KEGG` `database` - C01185 + C00013 + C00008 + C00009 <=> C00253 + C00119 + C00002 + C00001 + C00080
- `is_substrate_of` <-- [[molecule.C01185|molecule.C01185]] `KEGG` `database` - C01185 + C00013 + C00008 + C00009 <=> C00253 + C00119 + C00002 + C00001 + C00080

## External IDs

- `KEGG:R01724`

## Notes

EQUATION: C01185 + C00013 + C00008 + C00009 <=> C00253 + C00119 + C00002 + C00001 + C00080
