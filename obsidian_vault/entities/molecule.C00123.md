---
entity_id: "molecule.C00123"
entity_type: "small_molecule"
name: "L-Leucine"
source_database: "KEGG"
source_id: "C00123"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Leucine"
  - "2-Amino-4-methylvaleric acid"
  - "(2S)-alpha-2-Amino-4-methylvaleric acid"
  - "(2S)-alpha-Leucine"
---

# L-Leucine

`molecule.C00123`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00123`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Leucine; 2-Amino-4-methylvaleric acid; (2S)-alpha-2-Amino-4-methylvaleric acid; (2S)-alpha-Leucine

## Biological Role

Consumed as substrate in 8 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: L-Leucine; 2-Amino-4-methylvaleric acid; (2S)-alpha-2-Amino-4-methylvaleric acid; (2S)-alpha-Leucine

## Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (21)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-155|complex.ecocyc.MONOMER0-155]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.ABC-35-RXN|reaction.ecocyc.ABC-35-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-6979|reaction.ecocyc.RXN0-6979]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-126B|reaction.ecocyc.TRANS-RXN-126B]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-270|reaction.ecocyc.TRANS-RXN0-270]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ABC-35-RXN|reaction.ecocyc.ABC-35-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN|reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.LEUCINE--TRNA-LIGASE-RXN|reaction.ecocyc.LEUCINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22774|reaction.ecocyc.RXN-22774]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23890|reaction.ecocyc.RXN-23890]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-261|reaction.ecocyc.RXN0-261]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-126B|reaction.ecocyc.TRANS-RXN-126B]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-270|reaction.ecocyc.TRANS-RXN0-270]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.2-ISOPROPYLMALATESYN-RXN|reaction.ecocyc.2-ISOPROPYLMALATESYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ACETOLACTSYN-RXN|reaction.ecocyc.ACETOLACTSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ACETOOHBUTSYN-RXN|reaction.ecocyc.ACETOOHBUTSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ASPARTATEKIN-RXN|reaction.ecocyc.ASPARTATEKIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN|reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERLEU-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN-10814|reaction.ecocyc.RXN-10814]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.THREDEHYD-RXN|reaction.ecocyc.THREDEHYD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN|reaction.ecocyc.TYROSINE-AMINOTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (3)

- `transports` <-- [[complex.ecocyc.ABC-15-CPLX|complex.ecocyc.ABC-15-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AD99|protein.P0AD99]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P39277|protein.P39277]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00123`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
