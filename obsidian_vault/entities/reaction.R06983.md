---
entity_id: "reaction.R06983"
entity_type: "reaction"
name: "S-(hydroxymethyl)glutathione dehydrogenase"
source_database: "KEGG"
source_id: "R06983"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R06983"
---

# S-(hydroxymethyl)glutathione dehydrogenase

`reaction.R06983`

## Static

- Type: `reaction`
- Source: `KEGG:R06983`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

S-(Hydroxymethyl)glutathione + NAD+ S-Formylglutathione + NADH + H+

## Biological Role

Catalyzed by frmA (protein.P25437). Substrates: NAD+ (molecule.C00003), S-(Hydroxymethyl)glutathione (molecule.C14180). Products: NADH (molecule.C00004), H+ (molecule.C00080), S-Formylglutathione (molecule.C01031).

## Annotation

S-(Hydroxymethyl)glutathione + NAD+ <=> S-Formylglutathione + NADH + H+

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P25437|protein.P25437]] `KEGG` `database` - via EC:1.1.1.284
- `is_product_of` <-- [[molecule.C00004|molecule.C00004]] `KEGG` `database` - C14180 + C00003 <=> C01031 + C00004 + C00080
- `is_product_of` <-- [[molecule.C00080|molecule.C00080]] `KEGG` `database` - C14180 + C00003 <=> C01031 + C00004 + C00080
- `is_product_of` <-- [[molecule.C01031|molecule.C01031]] `KEGG` `database` - C14180 + C00003 <=> C01031 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C00003|molecule.C00003]] `KEGG` `database` - C14180 + C00003 <=> C01031 + C00004 + C00080
- `is_substrate_of` <-- [[molecule.C14180|molecule.C14180]] `KEGG` `database` - C14180 + C00003 <=> C01031 + C00004 + C00080

## External IDs

- `KEGG:R06983`

## Notes

EQUATION: C14180 + C00003 <=> C01031 + C00004 + C00080
