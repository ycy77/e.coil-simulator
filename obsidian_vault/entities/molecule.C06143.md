---
entity_id: "molecule.C06143"
entity_type: "small_molecule"
name: "Poly-beta-hydroxybutyrate"
source_database: "KEGG"
source_id: "C06143"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Poly-beta-hydroxybutyrate"
---

# Poly-beta-hydroxybutyrate

`molecule.C06143`

## Static

- Type: `small_molecule`
- Source: `KEGG:C06143`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Poly-beta-hydroxybutyrate EcoCyc common name: poly-[(R)-3-hydroxybutanoate]. During enzymatic polymerization the ester bond in this polymer is derived from the hydroxyl group of the (R)-3-hydroxybutanoyl moiety of CPD-650 .

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00650` Butanoate metabolism (KEGG)

## Annotation

KEGG compound: Poly-beta-hydroxybutyrate

## Pathways

- `eco00650` Butanoate metabolism (KEGG)

## Outgoing Edges (2)

- `is_product_of` --> [[reaction.ecocyc.RXN1-42|reaction.ecocyc.RXN1-42]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN1-42|reaction.ecocyc.RXN1-42]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C06143`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
