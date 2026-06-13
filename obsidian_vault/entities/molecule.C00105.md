---
entity_id: "molecule.C00105"
entity_type: "small_molecule"
name: "UMP"
source_database: "KEGG"
source_id: "C00105"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "UMP"
  - "Uridylic acid"
  - "Uridine monophosphate"
  - "Uridine 5'-monophosphate"
  - "5'Uridylic acid"
  - "Uridylate"
---

# UMP

`molecule.C00105`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00105`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: UMP; Uridylic acid; Uridine monophosphate; Uridine 5'-monophosphate; 5'Uridylic acid; Uridylate

## Biological Role

Consumed as substrate in 4 reaction(s). Produced in 15 reaction(s).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Annotation

KEGG compound: UMP; Uridylic acid; Uridine monophosphate; Uridine 5'-monophosphate; 5'Uridylic acid; Uridylate

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)

## Outgoing Edges (21)

- `is_product_of` --> [[reaction.R00287|reaction.R00287]] `KEGG` `database` - C00029 + C00001 <=> C00105 + C00103
- `is_product_of` --> [[reaction.R00662|reaction.R00662]] `KEGG` `database` - C00075 + C00001 <=> C00105 + C00013
- `is_product_of` --> [[reaction.R08856|reaction.R08856]] `KEGG` `database` - C00043 + C17556 <=> C01289 + C00105
- `is_product_of` --> [[reaction.R12075|reaction.R12075]] `KEGG` `database` - G10610 + C02970 <=> C00105 + G13118
- `is_product_of` --> [[reaction.ecocyc.GLCNACPTRANS-RXN|reaction.ecocyc.GLCNACPTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.LIPIDXSYNTHESIS-RXN|reaction.ecocyc.LIPIDXSYNTHESIS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.OROTPDECARB-RXN|reaction.ecocyc.OROTPDECARB-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.PHOSNACMURPENTATRANS-RXN|reaction.ecocyc.PHOSNACMURPENTATRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-11791|reaction.ecocyc.RXN-11791]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-14139|reaction.ecocyc.RXN-14139]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-16381|reaction.ecocyc.RXN-16381]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.UDPSUGARHYDRO-RXN|reaction.ecocyc.UDPSUGARHYDRO-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.URIDINEKIN-RXN|reaction.ecocyc.URIDINEKIN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.URIDYLREM-RXN|reaction.ecocyc.URIDYLREM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.URKI-RXN|reaction.ecocyc.URKI-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00158|reaction.R00158]] `KEGG` `database` - C00002 + C00105 <=> C00008 + C00015
- `is_substrate_of` --> [[reaction.ecocyc.RXN-12002|reaction.ecocyc.RXN-12002]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14025|reaction.ecocyc.RXN-14025]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.URACIL-PRIBOSYLTRANS-RXN|reaction.ecocyc.URACIL-PRIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.CARBPSYN-RXN|reaction.ecocyc.CARBPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.UDPGLUCEPIM-RXN|reaction.ecocyc.UDPGLUCEPIM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00105`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
