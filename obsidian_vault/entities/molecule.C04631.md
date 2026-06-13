---
entity_id: "molecule.C04631"
entity_type: "small_molecule"
name: "UDP-N-acetyl-3-(1-carboxyvinyl)-D-glucosamine"
source_database: "KEGG"
source_id: "C04631"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "UDP-N-acetyl-3-(1-carboxyvinyl)-D-glucosamine"
  - "UDP-N-acetyl-3-O-(1-carboxyvinyl)-D-glucosamine"
  - "UDP-N-acetylglucosamine-3-O-pyruvateether"
  - "UDP-N-acetylglucosamine enolpyruvate"
  - "UDP-N-acetyl-3-O-(1-carboxyvinyl)-alpha-D-glucosamine"
---

# UDP-N-acetyl-3-(1-carboxyvinyl)-D-glucosamine

`molecule.C04631`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04631`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: UDP-N-acetyl-3-(1-carboxyvinyl)-D-glucosamine; UDP-N-acetyl-3-O-(1-carboxyvinyl)-D-glucosamine; UDP-N-acetylglucosamine-3-O-pyruvateether; UDP-N-acetylglucosamine enolpyruvate; UDP-N-acetyl-3-O-(1-carboxyvinyl)-alpha-D-glucosamine EcoCyc common name: UDP-N-acetyl-α-D-glucosamine-enolpyruvate.

## Biological Role

Produced in 5 reaction(s).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Annotation

KEGG compound: UDP-N-acetyl-3-(1-carboxyvinyl)-D-glucosamine; UDP-N-acetyl-3-O-(1-carboxyvinyl)-D-glucosamine; UDP-N-acetylglucosamine-3-O-pyruvateether; UDP-N-acetylglucosamine enolpyruvate; UDP-N-acetyl-3-O-(1-carboxyvinyl)-alpha-D-glucosamine

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco00550` Peptidoglycan biosynthesis (KEGG)

## Outgoing Edges (5)

- `is_product_of` --> [[reaction.R00660|reaction.R00660]] `KEGG` `database` - C00074 + C00043 <=> C04631 + C00009
- `is_product_of` --> [[reaction.R03191|reaction.R03191]] `KEGG` `database` - C01050 + C00003 <=> C04631 + C00004 + C00080
- `is_product_of` --> [[reaction.R03192|reaction.R03192]] `KEGG` `database` - C01050 + C00006 <=> C04631 + C00005 + C00080
- `is_product_of` --> [[reaction.ecocyc.UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN|reaction.ecocyc.UDPNACETYLGLUCOSAMENOLPYRTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.UDPNACETYLMURAMATEDEHYDROG-RXN|reaction.ecocyc.UDPNACETYLMURAMATEDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04631`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
