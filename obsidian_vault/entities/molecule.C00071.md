---
entity_id: "molecule.C00071"
entity_type: "small_molecule"
name: "Aldehyde"
source_database: "KEGG"
source_id: "C00071"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "Aldehyde"
  - "RCHO"
---

# Aldehyde

`molecule.C00071`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00071`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: Aldehyde; RCHO EcoCyc common name: an aldehyde. An aldehyde is an organic compound containing a formyl group (CHO). This functional group consists of a carbonyl centre bonded to hydrogen and an R group. Aldehydes differ from LONG-CHAIN-KETONE ketones in that the carbonyl is placed at the end of a carbon skeleton rather than between two carbon atoms.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 8 reaction(s).

## Enriched Pathways

- `eco00071` Fatty acid degradation (KEGG)

## Annotation

KEGG compound: Aldehyde; RCHO

## Pathways

- `eco00071` Fatty acid degradation (KEGG)

## Outgoing Edges (11)

- `is_product_of` --> [[reaction.R00623|reaction.R00623]] `KEGG` `database` - C00226 + C00003 <=> C00071 + C00004 + C00080
- `is_product_of` --> [[reaction.R00625|reaction.R00625]] `KEGG` `database` - C00226 + C00006 <=> C00071 + C00005 + C00080
- `is_product_of` --> [[reaction.ecocyc.ALCOHOL-DEHYDROG-GENERIC-RXN|reaction.ecocyc.ALCOHOL-DEHYDROG-GENERIC-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN|reaction.ecocyc.ALCOHOL-DEHYDROGENASE-NADPORNOP_-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.AMINEOXID-RXN|reaction.ecocyc.AMINEOXID-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-9597|reaction.ecocyc.RXN-9597]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-280|reaction.ecocyc.RXN0-280]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7247|reaction.ecocyc.RXN0-7247]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.ALDEHYDE-DEHYDROGENASE-NADP_-RXN|reaction.ecocyc.ALDEHYDE-DEHYDROGENASE-NADP_-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.CARBOXYLATE-REDUCTASE-RXN|reaction.ecocyc.CARBOXYLATE-REDUCTASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7247|reaction.ecocyc.RXN0-7247]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00071`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
