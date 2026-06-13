---
entity_id: "molecule.C00140"
entity_type: "small_molecule"
name: "N-Acetyl-D-glucosamine"
source_database: "KEGG"
source_id: "C00140"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "N-Acetyl-D-glucosamine"
  - "N-Acetylchitosamine"
  - "2-Acetamido-2-deoxy-D-glucose"
  - "GlcNAc"
---

# N-Acetyl-D-glucosamine

`molecule.C00140`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00140`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: N-Acetyl-D-glucosamine; N-Acetylchitosamine; 2-Acetamido-2-deoxy-D-glucose; GlcNAc

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 4 reaction(s).

## Enriched Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

KEGG compound: N-Acetyl-D-glucosamine; N-Acetylchitosamine; 2-Acetamido-2-deoxy-D-glucose; GlcNAc

## Pathways

- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco02010` ABC transporters (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.R00022|reaction.R00022]] `KEGG` `database` - C01674 + C00001 <=> 2 C00140
- `is_product_of` --> [[reaction.R07809|reaction.R07809]] `KEGG` `database` - G13074 + C00001 <=> G01391 + C00140
- `is_product_of` --> [[reaction.ecocyc.RXN0-5226|reaction.ecocyc.RXN0-5226]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7392|reaction.ecocyc.RXN0-7392]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.ecocyc.N-ACETYLGLUCOSAMINE-KINASE-RXN|reaction.ecocyc.N-ACETYLGLUCOSAMINE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5413|reaction.ecocyc.RXN0-5413]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-167|reaction.ecocyc.TRANS-RXN-167]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00140`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
