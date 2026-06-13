---
entity_id: "molecule.C00183"
entity_type: "small_molecule"
name: "L-Valine"
source_database: "KEGG"
source_id: "C00183"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Valine"
  - "2-Amino-3-methylbutyric acid"
---

# L-Valine

`molecule.C00183`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00183`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Valine; 2-Amino-3-methylbutyric acid

## Biological Role

Consumed as substrate in 11 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: L-Valine; 2-Amino-3-methylbutyric acid

## Pathways

- `eco00280` Valine, leucine and isoleucine degradation (KEGG)
- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (20)

- `activates` --> [[reaction.ecocyc.THREDEHYD-RXN|reaction.ecocyc.THREDEHYD-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.ABC-36-RXN|reaction.ecocyc.ABC-36-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-23945|reaction.ecocyc.RXN-23945]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-126A|reaction.ecocyc.TRANS-RXN-126A]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-282|reaction.ecocyc.TRANS-RXN-282]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-269|reaction.ecocyc.TRANS-RXN0-269]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R03665|reaction.R03665]] `KEGG` `database` - C00002 + C00183 + C01653 <=> C00020 + C00013 + C02554
- `is_substrate_of` --> [[reaction.ecocyc.ABC-36-RXN|reaction.ecocyc.ABC-36-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERVAL-RXN|reaction.ecocyc.BRANCHED-CHAINAMINOTRANSFERVAL-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22775|reaction.ecocyc.RXN-22775]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-22838|reaction.ecocyc.RXN-22838]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23944|reaction.ecocyc.RXN-23944]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-126A|reaction.ecocyc.TRANS-RXN-126A]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-282|reaction.ecocyc.TRANS-RXN-282]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-269|reaction.ecocyc.TRANS-RXN0-269]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.VALINE--TRNA-LIGASE-RXN|reaction.ecocyc.VALINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.VALINE-PYRUVATE-AMINOTRANSFER-RXN|reaction.ecocyc.VALINE-PYRUVATE-AMINOTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN|reaction.ecocyc.3-CH3-2-OXOBUTANOATE-OH-CH3-XFER-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ACETOLACTSYN-RXN|reaction.ecocyc.ACETOLACTSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.ACETOOHBUTSYN-RXN|reaction.ecocyc.ACETOOHBUTSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (3)

- `transports` <-- [[complex.ecocyc.ABC-15-CPLX|complex.ecocyc.ABC-15-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P0AD99|protein.P0AD99]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[protein.P39277|protein.P39277]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00183`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
