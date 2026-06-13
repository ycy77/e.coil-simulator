---
entity_id: "reaction.R00178"
entity_type: "reaction"
name: "S-adenosyl-L-methionine carboxy-lyase [S-adenosyl 3-(methylsulfanyl)propylamine-forming]"
source_database: "KEGG"
source_id: "R00178"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R00178"
---

# S-adenosyl-L-methionine carboxy-lyase [S-adenosyl 3-(methylsulfanyl)propylamine-forming]

`reaction.R00178`

## Static

- Type: `reaction`
- Source: `KEGG:R00178`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-Adenosyl-L-methionine + H+ S-Adenosylmethioninamine + CO2

## Biological Role

Catalyzed by speD (protein.P0A7F6). Substrates: S-Adenosyl-L-methionine (molecule.C00019), H+ (molecule.C00080). Products: CO2 (molecule.C00011), S-Adenosylmethioninamine (molecule.C01137).

## Annotation

S-Adenosyl-L-methionine + H+ <=> S-Adenosylmethioninamine + CO2

## Outgoing Edges (0)

_None._

## Incoming Edges (5)

- `catalyzes` <-- [[protein.P0A7F6|protein.P0A7F6]] `KEGG` `database` - via EC:4.1.1.50
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C00019 + C00080 <=> C01137 + C00011
- `is_product_of` <-- [[molecule.C01137|molecule.C01137]] `KEGG` `database` - C00019 + C00080 <=> C01137 + C00011
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - C00019 + C00080 <=> C01137 + C00011
- `is_substrate_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C00019 + C00080 <=> C01137 + C00011

## External IDs

- `KEGG:R00178`

## Notes

EQUATION: C00019 + C00080 <=> C01137 + C00011
