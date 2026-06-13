---
entity_id: "molecule.C00244"
entity_type: "small_molecule"
name: "Nitrate"
source_database: "KEGG"
source_id: "C00244"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Nitrate"
  - "Nitric acid"
---

# Nitrate

`molecule.C00244`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00244`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Nitrate; Nitric acid Nitrate is the conjugate base of CPD-15028. It is a common electron acceptor for anaerobic bacteria (see Nitrate-Reduction "nitrate reduction pathways"), and is also the ultimate product of an ammonia oxidation process known as P282-PWY nitrification.

## Biological Role

Consumed as substrate in 8 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

KEGG compound: Nitrate; Nitric acid

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (18)

- `is_product_of` --> [[reaction.R05724|reaction.R05724]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00004 + C00080 <=> 2 C00244 + C00003
- `is_product_of` --> [[reaction.R05725|reaction.R05725]] `KEGG` `database` - 2 C00533 + 2 C00007 + C00005 + C00080 <=> 2 C00244 + C00006
- `is_product_of` --> [[reaction.ecocyc.R621-RXN|reaction.ecocyc.R621-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-12827|reaction.ecocyc.RXN-12827]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN0-239|reaction.ecocyc.TRANS-RXN0-239]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00792|reaction.R00792]] `KEGG` `database` - C00244 + 2 C06259 <=> C00088 + C00001 + 2 C06260
- `is_substrate_of` --> [[reaction.ecocyc.NITRATE-REDUCTASE-CYTOCHROME-RXN|reaction.ecocyc.NITRATE-REDUCTASE-CYTOCHROME-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-3501|reaction.ecocyc.RXN0-3501]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5242|reaction.ecocyc.RXN0-5242]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6369|reaction.ecocyc.RXN0-6369]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-6370|reaction.ecocyc.RXN0-6370]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7124|reaction.ecocyc.RXN0-7124]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN0-239|reaction.ecocyc.TRANS-RXN0-239]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.GLYCOPHOSPHORYL-RXN|reaction.ecocyc.GLYCOPHOSPHORYL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.KDGALDOL-RXN|reaction.ecocyc.KDGALDOL-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.NAPHTHOATE-SYN-RXN|reaction.ecocyc.NAPHTHOATE-SYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.R524-RXN|reaction.ecocyc.R524-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-3281|reaction.ecocyc.RXN0-3281]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `transports` <-- [[protein.P10903|protein.P10903]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00244`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
