---
entity_id: "molecule.C00212"
entity_type: "small_molecule"
name: "Adenosine"
source_database: "KEGG"
source_id: "C00212"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Adenosine"
---

# Adenosine

`molecule.C00212`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00212`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Adenosine

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: Adenosine

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (14)

- `is_product_of` --> [[reaction.R00183|reaction.R00183]] `KEGG` `database` - C00020 + C00001 <=> C00212 + C00009
- `is_product_of` --> [[reaction.ecocyc.AMP-DEPHOSPHORYLATION-RXN|reaction.ecocyc.AMP-DEPHOSPHORYLATION-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14126|reaction.ecocyc.RXN-14126]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14513|reaction.ecocyc.RXN-14513]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-108A|reaction.ecocyc.TRANS-RXN-108A]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ADENODEAMIN-RXN|reaction.ecocyc.ADENODEAMIN-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ADENOSINE-NUCLEOSIDASE-RXN|reaction.ecocyc.ADENOSINE-NUCLEOSIDASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ADENPHOSPHOR-RXN|reaction.ecocyc.ADENPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-108A|reaction.ecocyc.TRANS-RXN-108A]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.DAPASYN-RXN|reaction.ecocyc.DAPASYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DEOXYGUANPHOSPHOR-RXN|reaction.ecocyc.DEOXYGUANPHOSPHOR-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.GMP-SYN-NH3-RXN|reaction.ecocyc.GMP-SYN-NH3-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-12458|reaction.ecocyc.RXN-12458]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-16165|reaction.ecocyc.RXN-16165]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P0AFF2|protein.P0AFF2]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00212`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
