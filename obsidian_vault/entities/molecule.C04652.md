---
entity_id: "molecule.C04652"
entity_type: "small_molecule"
name: "UDP-2,3-bis(3-hydroxytetradecanoyl)glucosamine"
source_database: "KEGG"
source_id: "C04652"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "UDP-2,3-bis(3-hydroxytetradecanoyl)glucosamine"
  - "UDP-2,3-bis(beta-hydroxymyristoyl)-D-glucosamine"
  - "UDP-2,3-bis(3-hydroxytetradecanoyl)-D-glucosamine"
  - "UDP-2,3-bis[O-(3R)-3-hydroxymyristoyl]-alpha-D-glucosamine"
---

# UDP-2,3-bis(3-hydroxytetradecanoyl)glucosamine

`molecule.C04652`

## Static

- Type: `small_molecule`
- Source: `KEGG:C04652`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: UDP-2,3-bis(3-hydroxytetradecanoyl)glucosamine; UDP-2,3-bis(beta-hydroxymyristoyl)-D-glucosamine; UDP-2,3-bis(3-hydroxytetradecanoyl)-D-glucosamine; UDP-2,3-bis[O-(3R)-3-hydroxymyristoyl]-alpha-D-glucosamine EcoCyc common name: UDP-2-N,3-O-bis[(3R)-3-hydroxytetradecanoyl]-α-D-glucosamine.

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Annotation

KEGG compound: UDP-2,3-bis(3-hydroxytetradecanoyl)glucosamine; UDP-2,3-bis(beta-hydroxymyristoyl)-D-glucosamine; UDP-2,3-bis(3-hydroxytetradecanoyl)-D-glucosamine; UDP-2,3-bis[O-(3R)-3-hydroxymyristoyl]-alpha-D-glucosamine

## Pathways

- `eco00540` Lipopolysaccharide biosynthesis (KEGG)

## Outgoing Edges (3)

- `is_product_of` --> [[reaction.ecocyc.UDPHYDROXYMYRGLUCOSAMNACETYLTRANS-RXN|reaction.ecocyc.UDPHYDROXYMYRGLUCOSAMNACETYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.LIPIDADISACCHARIDESYNTH-RXN|reaction.ecocyc.LIPIDADISACCHARIDESYNTH-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.LIPIDXSYNTHESIS-RXN|reaction.ecocyc.LIPIDXSYNTHESIS-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C04652`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
