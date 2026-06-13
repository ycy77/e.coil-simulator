---
entity_id: "molecule.C05235"
entity_type: "small_molecule"
name: "Hydroxyacetone"
source_database: "KEGG"
source_id: "C05235"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Hydroxyacetone"
  - "Acetol"
  - "1-Hydroxy-2-propanone"
  - "2-Ketopropyl alcohol"
  - "Acetone alcohol"
  - "Pyruvinalcohol"
  - "Pyruvic alcohol"
  - "Methylketol"
---

# Hydroxyacetone

`molecule.C05235`

## Static

- Type: `small_molecule`
- Source: `KEGG:C05235`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Hydroxyacetone; Acetol; 1-Hydroxy-2-propanone; 2-Ketopropyl alcohol; Acetone alcohol; Pyruvinalcohol; Pyruvic alcohol; Methylketol

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)

## Annotation

KEGG compound: Hydroxyacetone; Acetol; 1-Hydroxy-2-propanone; 2-Ketopropyl alcohol; Acetone alcohol; Pyruvinalcohol; Pyruvic alcohol; Methylketol

## Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.RXN-8632|reaction.ecocyc.RXN-8632]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-5213|reaction.ecocyc.RXN0-5213]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4281|reaction.ecocyc.RXN0-4281]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C05235`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
