---
entity_id: "reaction.R06895"
entity_type: "reaction"
name: "coproporphyrinogen-III:S-adenosyl-L-methionine oxidoreductase(decarboxylating)"
source_database: "KEGG"
source_id: "R06895"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R06895"
---

# coproporphyrinogen-III:S-adenosyl-L-methionine oxidoreductase(decarboxylating)

`reaction.R06895`

## Static

- Type: `reaction`
- Source: `KEGG:R06895`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

Coproporphyrinogen III + 2 S-Adenosyl-L-methionine Protoporphyrinogen IX + 2 CO2 + 2 L-Methionine + 2 5'-Deoxyadenosine

## Biological Role

Catalyzed by hemN (protein.P32131). Substrates: S-Adenosyl-L-methionine (molecule.C00019), Coproporphyrinogen III (molecule.C03263). Products: CO2 (molecule.C00011), L-Methionine (molecule.C00073), Protoporphyrinogen IX (molecule.C01079).

## Annotation

Coproporphyrinogen III + 2 S-Adenosyl-L-methionine <=> Protoporphyrinogen IX + 2 CO2 + 2 L-Methionine + 2 5'-Deoxyadenosine

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P32131|protein.P32131]] `KEGG` `database` - via EC:1.3.98.3
- `is_product_of` <-- [[molecule.C00011|molecule.C00011]] `KEGG` `database` - C03263 + 2 C00019 <=> C01079 + 2 C00011 + 2 C00073 + 2 C05198
- `is_product_of` <-- [[molecule.C00073|molecule.C00073]] `KEGG` `database` - C03263 + 2 C00019 <=> C01079 + 2 C00011 + 2 C00073 + 2 C05198
- `is_product_of` <-- [[molecule.C01079|molecule.C01079]] `KEGG` `database` - C03263 + 2 C00019 <=> C01079 + 2 C00011 + 2 C00073 + 2 C05198
- `is_substrate_of` <-- [[molecule.C00019|molecule.C00019]] `KEGG` `database` - C03263 + 2 C00019 <=> C01079 + 2 C00011 + 2 C00073 + 2 C05198
- `is_substrate_of` <-- [[molecule.C03263|molecule.C03263]] `KEGG` `database` - C03263 + 2 C00019 <=> C01079 + 2 C00011 + 2 C00073 + 2 C05198

## External IDs

- `KEGG:R06895`

## Notes

EQUATION: C03263 + 2 C00019 <=> C01079 + 2 C00011 + 2 C00073 + 2 C05198
