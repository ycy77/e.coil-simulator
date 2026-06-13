---
entity_id: "reaction.R06942"
entity_type: "reaction"
name: "(3S)-3-hydroxyacyl-CoA hydro-lyase"
source_database: "KEGG"
source_id: "R06942"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/KEGG
aliases:
  - "R06942"
---

# (3S)-3-hydroxyacyl-CoA hydro-lyase

`reaction.R06942`

## Static

- Type: `reaction`
- Source: `KEGG:R06942`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

5-Carboxy-2-pentenoyl-CoA + H2O (3S)-3-Hydroxyadipyl-CoA

## Biological Role

Catalyzed by fadB (protein.P21177), paaF (protein.P76082), fadJ (protein.P77399). Substrates: H2O (molecule.C00001), 5-Carboxy-2-pentenoyl-CoA (molecule.C14144). Products: (3S)-3-Hydroxyadipyl-CoA (molecule.C14145).

## Annotation

5-Carboxy-2-pentenoyl-CoA + H2O <=> (3S)-3-Hydroxyadipyl-CoA

## Outgoing Edges (0)

_None._

## Incoming Edges (6)

- `catalyzes` <-- [[protein.P21177|protein.P21177]] `KEGG` `database` - via EC:4.2.1.17
- `catalyzes` <-- [[protein.P76082|protein.P76082]] `KEGG` `database` - via EC:4.2.1.17
- `catalyzes` <-- [[protein.P77399|protein.P77399]] `KEGG` `database` - via EC:4.2.1.17
- `is_product_of` <-- [[molecule.C14145|molecule.C14145]] `KEGG` `database` - C14144 + C00001 <=> C14145
- `is_substrate_of` <-- [[molecule.C00001|molecule.C00001]] `KEGG` `database` - C14144 + C00001 <=> C14145
- `is_substrate_of` <-- [[molecule.C14144|molecule.C14144]] `KEGG` `database` - C14144 + C00001 <=> C14145

## External IDs

- `KEGG:R06942`

## Notes

EQUATION: C14144 + C00001 <=> C14145
