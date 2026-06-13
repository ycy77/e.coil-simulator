---
entity_id: "molecule.C00072"
entity_type: "small_molecule"
name: "Ascorbate"
source_database: "KEGG"
source_id: "C00072"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Ascorbate"
  - "Ascorbic acid"
  - "L-Ascorbate"
  - "L-Ascorbic acid"
  - "Vitamin C"
---

# Ascorbate

`molecule.C00072`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00072`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Ascorbate; Ascorbic acid; L-Ascorbate; L-Ascorbic acid; Vitamin C EcoCyc common name: L-ascorbate. ASCORBATE, also known as vitamin C, fulfils multiple essential roles in both plants and animals. Being a strong reducing agent, it functions as the primary water soluble antioxidant in cells, interacting with reactive oxygen species generated during oxidative stress and protecting cell constituents from oxidative damage . Ascorbate is also a cofactor for a number of enzymes, particulariy dioxygenases, in which it maintains the reduced form of the Fe cofactor. Ascorbate-dependent enzymes are involved in many important pathways, including collagen hydroxylation, carnitine biosynthesis, norepinephrine biosynthesis, and hormone and tyrosine metabolism. In plants L-ascorbate is also implicated in defense against pathogens and in control of plant growth and development. A significant proportion of a plants ascorbate is found in the apoplast (the aqueous solution permeating the cell walls) . While most organisms synthesize L-ascorbate, not all do. Examples for organisms that are not able to synthesize L-ascorbate include simians and humans.

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: Ascorbate; Ascorbic acid; L-Ascorbate; L-Ascorbic acid; Vitamin C

## Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (8)

- `activates` --> [[reaction.ecocyc.RXN0-299|reaction.ecocyc.RXN0-299]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.RXN-12440|reaction.ecocyc.RXN-12440]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-3523|reaction.ecocyc.RXN-3523]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10981|reaction.ecocyc.RXN-10981]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12440|reaction.ecocyc.RXN-12440]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12876|reaction.ecocyc.RXN-12876]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-3521|reaction.ecocyc.RXN-3521]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2461|reaction.ecocyc.RXN0-2461]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00072`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
