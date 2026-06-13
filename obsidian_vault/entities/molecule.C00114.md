---
entity_id: "molecule.C00114"
entity_type: "small_molecule"
name: "Choline"
source_database: "KEGG"
source_id: "C00114"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Choline"
  - "Bilineurine"
---

# Choline

`molecule.C00114`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00114`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Choline; Bilineurine CHOLINE Choline is a quaternary ammonium compound and a fundamental metabolite for eukaryotic organisms, forming the head group of important phospholipids such as PHOSPHATIDYLCHOLINE phosphatidylcholine . Choline is also the precursor for the neurotransmitter ACETYLCHOLINE, and serves as a precursor for the formation of the important osmoprotectant BETAINE (see PWY1F-353 for an example) . Animals cannot synthesize CHOLINE, which must be consumed through the diet, making it a vitamin. It is usually grouped within the B-complex vitamins. Most microbes are also not able to produce choline, although many have transporters for its uptake.

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00552` Teichoic acid biosynthesis (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

KEGG compound: Choline; Bilineurine

## Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00552` Teichoic acid biosynthesis (KEGG)
- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Outgoing Edges (14)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-49|complex.ecocyc.MONOMER0-49]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.RXN-17758|reaction.ecocyc.RXN-17758]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-5647|reaction.ecocyc.RXN-5647]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-99|reaction.ecocyc.TRANS-RXN-99]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-533|reaction.ecocyc.TRANS-RXN0-533]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.CHD-RXN|reaction.ecocyc.CHD-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-18376|reaction.ecocyc.RXN-18376]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-288|reaction.ecocyc.RXN0-288]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7230|reaction.ecocyc.RXN0-7230]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-99|reaction.ecocyc.TRANS-RXN-99]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-533|reaction.ecocyc.TRANS-RXN0-533]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.BADH-RXN|reaction.ecocyc.BADH-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.CROBETREDUCT-RXN|reaction.ecocyc.CROBETREDUCT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TRANS-RXN-29|reaction.ecocyc.TRANS-RXN-29]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P0ABC9|protein.P0ABC9]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00114`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
