---
entity_id: "molecule.C00864"
entity_type: "small_molecule"
name: "Pantothenate"
source_database: "KEGG"
source_id: "C00864"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Pantothenate"
  - "Pantothenic acid"
  - "(R)-Pantothenate"
---

# Pantothenate

`molecule.C00864`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00864`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Pantothenate; Pantothenic acid; (R)-Pantothenate EcoCyc common name: (R)-pantothenate. (R)-pantothenate, also called vitamin B5, is the amide between L-PANTOATE and B-ALANINE. It is a precursor for the synthesis of the 4'-phosphopantetheine moiety of CO-A and ACP "acyl carrier protein" in bacteria and eukaryotes. Only plants and microorganisms (including some eukaryotic microbes, such as TAX-4932) can synthesize pantothenate de novo - animals require a dietary supplement.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Annotation

KEGG compound: Pantothenate; Pantothenic acid; (R)-Pantothenate

## Pathways

- `eco00410` beta-Alanine metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.ecocyc.PANTOATE-BETA-ALANINE-LIG-RXN|reaction.ecocyc.PANTOATE-BETA-ALANINE-LIG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-117|reaction.ecocyc.TRANS-RXN-117]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.PANTOTHENATE-KIN-RXN|reaction.ecocyc.PANTOTHENATE-KIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-117|reaction.ecocyc.TRANS-RXN-117]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN|reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P16256|protein.P16256]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00864`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
