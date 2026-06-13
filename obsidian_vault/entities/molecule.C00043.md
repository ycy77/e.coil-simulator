---
entity_id: "molecule.C00043"
entity_type: "small_molecule"
name: "UDP-N-acetyl-alpha-D-glucosamine"
source_database: "KEGG"
source_id: "C00043"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "UDP-N-acetyl-alpha-D-glucosamine"
  - "UDP-N-acetyl-D-glucosamine"
  - "UDP-N-acetylglucosamine"
---

# UDP-N-acetyl-alpha-D-glucosamine

`molecule.C00043`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00043`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: UDP-N-acetyl-alpha-D-glucosamine; UDP-N-acetyl-D-glucosamine; UDP-N-acetylglucosamine EcoCyc common name: UDP-N-acetyl-α-D-glucosamine.

## Biological Role

Consumed as substrate in 12 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco00552` Teichoic acid biosynthesis (KEGG)

## Annotation

KEGG compound: UDP-N-acetyl-alpha-D-glucosamine; UDP-N-acetyl-D-glucosamine; UDP-N-acetylglucosamine

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00540` Lipopolysaccharide biosynthesis (KEGG)
- `eco00541` Biosynthesis of various nucleotide sugars (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco00552` Teichoic acid biosynthesis (KEGG)

## Outgoing Edges (16)

- `activates` --> [[reaction.ecocyc.UDPGLCNACEPIM-RXN|reaction.ecocyc.UDPGLCNACEPIM-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.R00416|reaction.R00416]] `KEGG` `database` - C00075 + C04501 <=> C00013 + C00043
- `is_product_of` --> [[reaction.ecocyc.NAG1P-URIDYLTRANS-RXN|reaction.ecocyc.NAG1P-URIDYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00414|reaction.R00414]] `KEGG` `database` - C00043 + C00001 <=> C00645 + C00015
- `is_substrate_of` --> [[reaction.R00418|reaction.R00418]] `KEGG` `database` - C00043 <=> C00203
- `is_substrate_of` --> [[reaction.R00420|reaction.R00420]] `KEGG` `database` - C00043 <=> C01170
- `is_substrate_of` --> [[reaction.R00660|reaction.R00660]] `KEGG` `database` - C00074 + C00043 <=> C04631 + C00009
- `is_substrate_of` --> [[reaction.R08856|reaction.R08856]] `KEGG` `database` - C00043 + C17556 <=> C01289 + C00105
- `is_substrate_of` --> [[reaction.ecocyc.GLCNACPTRANS-RXN|reaction.ecocyc.GLCNACPTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.NACGLCTRANS-RXN|reaction.ecocyc.NACGLCTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19737|reaction.ecocyc.RXN-19737]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5413|reaction.ecocyc.RXN0-5413]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UDPGLCNACEPIM-RXN|reaction.ecocyc.UDPGLCNACEPIM-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UDPNACETYLGLUCOSAMACYLTRANS-RXN|reaction.ecocyc.UDPNACETYLGLUCOSAMACYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN|reaction.ecocyc.UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN|reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00043`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
