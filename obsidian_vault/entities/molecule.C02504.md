---
entity_id: "molecule.C02504"
entity_type: "small_molecule"
name: "alpha-Isopropylmalate"
source_database: "KEGG"
source_id: "C02504"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "alpha-Isopropylmalate"
  - "(2S)-2-Isopropylmalate"
  - "(2S)-2-Hydroxy-2-isopropylsuccinic acid"
  - "2-Isopropylmalic acid"
  - "3-Carboxy-3-hydroxy-4-methylpentanoate"
  - "3-Carboxy-3-hydroxyisocaproate"
  - "(2S)-2-Isopropylmalic acid"
---

# alpha-Isopropylmalate

`molecule.C02504`

## Static

- Type: `small_molecule`
- Source: `KEGG:C02504`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: alpha-Isopropylmalate; (2S)-2-Isopropylmalate; (2S)-2-Hydroxy-2-isopropylsuccinic acid; 2-Isopropylmalic acid; 3-Carboxy-3-hydroxy-4-methylpentanoate; 3-Carboxy-3-hydroxyisocaproate; (2S)-2-Isopropylmalic acid EcoCyc common name: (2S)-2-isopropylmalate.

## Biological Role

Consumed as substrate in 1 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)

## Annotation

KEGG compound: alpha-Isopropylmalate; (2S)-2-Isopropylmalate; (2S)-2-Hydroxy-2-isopropylsuccinic acid; 2-Isopropylmalic acid; 3-Carboxy-3-hydroxy-4-methylpentanoate; 3-Carboxy-3-hydroxyisocaproate; (2S)-2-Isopropylmalic acid

## Pathways

- `eco00290` Valine, leucine and isoleucine biosynthesis (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-13604|complex.ecocyc.CPLX0-13604]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.2-ISOPROPYLMALATESYN-RXN|reaction.ecocyc.2-ISOPROPYLMALATESYN-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.3-ISOPROPYLMALISOM-RXN|reaction.ecocyc.3-ISOPROPYLMALISOM-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN-13163|reaction.ecocyc.RXN-13163]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7498|reaction.ecocyc.RXN0-7498]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C02504`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
