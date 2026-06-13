---
entity_id: "molecule.C01050"
entity_type: "small_molecule"
name: "UDP-N-acetylmuramate"
source_database: "KEGG"
source_id: "C01050"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "UDP-N-acetylmuramate"
  - "UDP-N-acetyl-alpha-D-muramate"
  - "UDP-N-acetylmuramic acid"
  - "UDP-MurNAc"
---

# UDP-N-acetylmuramate

`molecule.C01050`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01050`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: UDP-N-acetylmuramate; UDP-N-acetyl-alpha-D-muramate; UDP-N-acetylmuramic acid; UDP-MurNAc EcoCyc common name: UDP-N-acetyl-α-D-muramate.

## Biological Role

Consumed as substrate in 8 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Annotation

KEGG compound: UDP-N-acetylmuramate; UDP-N-acetyl-alpha-D-muramate; UDP-N-acetylmuramic acid; UDP-MurNAc

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Outgoing Edges (12)

- `is_product_of` --> [[reaction.ecocyc.RXN-25001|reaction.ecocyc.RXN-25001]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R03191|reaction.R03191]] `KEGG` `database` - C01050 + C00003 <=> C04631 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R03192|reaction.R03192]] `KEGG` `database` - C01050 + C00006 <=> C04631 + C00005 + C00080
- `is_substrate_of` --> [[reaction.R03193|reaction.R03193]] `KEGG` `database` - C00002 + C01050 + C00041 <=> C00008 + C00009 + C01212
- `is_substrate_of` --> [[reaction.R10901|reaction.R10901]] `KEGG` `database` - C00002 + C01050 + C20925 <=> C00008 + C00009 + C04877
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2361|reaction.ecocyc.RXN0-2361]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7022|reaction.ecocyc.RXN0-7022]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UDP-NACMUR-ALA-LIG-RXN|reaction.ecocyc.UDP-NACMUR-ALA-LIG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.UDPNACETYLMURAMATEDEHYDROG-RXN|reaction.ecocyc.UDPNACETYLMURAMATEDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.2.3.1.157-RXN|reaction.ecocyc.2.3.1.157-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN|reaction.ecocyc.UDP-NACMURALGLDAPLIG-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN|reaction.ecocyc.UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01050`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
