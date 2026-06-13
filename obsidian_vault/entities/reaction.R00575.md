---
entity_id: "reaction.R00575"
entity_type: "reaction"
name: "HCO3-:L-glutamine amido-ligase (ADP-forming, carbamate-phosphorylating)"
source_database: "KEGG"
source_id: "R00575"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00575"
---

# HCO3-:L-glutamine amido-ligase (ADP-forming, carbamate-phosphorylating)

`reaction.R00575`

## Static

- Type: `reaction`
- Source: `KEGG:R00575`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2 ATP + L-Glutamine + HCO3- + H2O 2 ADP + Orthophosphate + L-Glutamate + Carbamoyl phosphate

## Biological Role

Catalyzed by carB (protein.P00968), carA (protein.P0A6F1). Substrates: H2O (molecule.C00001), ATP (molecule.C00002), L-Glutamine (molecule.C00064), HCO3- (molecule.C00288). Products: ADP (molecule.C00008), Orthophosphate (molecule.C00009), L-Glutamate (molecule.C00025), Carbamoyl phosphate (molecule.C00169).

## Annotation

2 ATP + L-Glutamine + HCO3- + H2O <=> 2 ADP + Orthophosphate + L-Glutamate + Carbamoyl phosphate

## Outgoing Edges (0)

_None._

## Incoming Edges (10)

- `catalyzes` <-- [[protein.P00968|protein.P00968]] `KEGG` `database` - via EC:6.3.5.5
- `catalyzes` <-- [[protein.P0A6F1|protein.P0A6F1]] `KEGG` `database` - via EC:6.3.5.5
- `is_product_of` <-- [[molecule.C00008|molecule.C00008]] `KEGG` `database` - 2 C00002 + C00064 + C00288 + C00001 <=> 2 C00008 + C00009 + C00025 + C00169
- `is_product_of` <-- [[molecule.C00009|molecule.C00009]] `KEGG` `database` - 2 C00002 + C00064 + C00288 + C00001 <=> 2 C00008 + C00009 + C00025 + C00169
- `is_product_of` <-- [[molecule.C00025|molecule.C00025]] `KEGG` `database` - 2 C00002 + C00064 + C00288 + C00001 <=> 2 C00008 + C00009 + C00025 + C00169
- `is_product_of` <-- [[molecule.C00169|molecule.C00169]] `KEGG` `database` - 2 C00002 + C00064 + C00288 + C00001 <=> 2 C00008 + C00009 + C00025 + C00169
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - 2 C00002 + C00064 + C00288 + C00001 <=> 2 C00008 + C00009 + C00025 + C00169
- `is_substrate_of` <-- [[molecule.C00002|molecule.C00002]] `KEGG` `database` - 2 C00002 + C00064 + C00288 + C00001 <=> 2 C00008 + C00009 + C00025 + C00169
- `is_substrate_of` <-- [[molecule.C00064|molecule.C00064]] `KEGG` `database` - 2 C00002 + C00064 + C00288 + C00001 <=> 2 C00008 + C00009 + C00025 + C00169
- `is_substrate_of` <-- [[molecule.C00288|molecule.C00288]] `KEGG` `database` - 2 C00002 + C00064 + C00288 + C00001 <=> 2 C00008 + C00009 + C00025 + C00169

## External IDs

- `KEGG:R00575`

## Notes

EQUATION: 2 C00002 + C00064 + C00288 + C00001 <=> 2 C00008 + C00009 + C00025 + C00169
