---
entity_id: "molecule.C00407"
entity_type: "small_molecule"
name: "L-Isoleucine"
source_database: "KEGG"
source_id: "C00407"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Isoleucine"
  - "2-Amino-3-methylvaleric acid"
---

# L-Isoleucine

`molecule.C00407`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00407`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Isoleucine; 2-Amino-3-methylvaleric acid

## Biological Role

Consumed as substrate in 6 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: L-Isoleucine; 2-Amino-3-methylvaleric acid

## Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (11)

- `is_product_of` --> [[reaction.ecocyc.ABC-15-RXN|reaction.ecocyc.ABC-15-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-126|reaction.ecocyc.TRANS-RXN-126]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-281|reaction.ecocyc.TRANS-RXN-281]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ABC-15-RXN|reaction.ecocyc.ABC-15-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERILEU-RXN|reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERILEU-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ISOLEUCINE--TRNA-LIGASE-RXN|reaction.ecocyc.ISOLEUCINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23889|reaction.ecocyc.RXN-23889]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-126|reaction.ecocyc.TRANS-RXN-126]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-281|reaction.ecocyc.TRANS-RXN-281]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.ACETOLACTSYN-RXN|reaction.ecocyc.ACETOLACTSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.THREDEHYD-RXN|reaction.ecocyc.THREDEHYD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (3)

- `transports` <-- [[complex.ecocyc.ABC-15-CPLX|complex.ecocyc.ABC-15-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AD99|protein.P0AD99]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P39277|protein.P39277]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00407`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
