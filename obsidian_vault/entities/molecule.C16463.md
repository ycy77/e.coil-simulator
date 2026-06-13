---
entity_id: "molecule.C16463"
entity_type: "small_molecule"
name: "3',5'-Cyclic diGMP"
source_database: "KEGG"
source_id: "C16463"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "3',5'-Cyclic diGMP"
  - "cdiGMP"
  - "3',5'-Cyclic diguanylic acid"
  - "Bis-(3',5')-cyclic diGMP"
  - "Cyclic di-3',5'-guanylate"
---

# 3',5'-Cyclic diGMP

`molecule.C16463`

## Static

- Type: `small_molecule`
- Source: `KEGG:C16463`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: 3',5'-Cyclic diGMP; cdiGMP; 3',5'-Cyclic diguanylic acid; Bis-(3',5')-cyclic diGMP; Cyclic di-3',5'-guanylate EcoCyc common name: cyclic di-3',5'-guanylate. C-DI-GMP "Cyclic di-3',5'-guanylate" (cyclic di-GMP; c-di-GMP) is an intracellular secondary messenger that is involved in a diverse range of cellular processes in bacteria. It is synthesized by EC-2.7.7.65 (DGC) and degraded by EC-3.1.4.52 (PDE). The ratio of these opposing activities determines the c-di-GMP concentration within a cell. The catalytic activity of DGC enzymes resides in GGDEF domains, and that of PDE enzyme resides in either EAL or HD-GYP domains, which are structurally and evolutionary distinct . The number of these enzyme present in bacteria is unusually high. On average ten GGDEF domain proteins are encoded in a single bacterial genome, though numbers as high as 57 have been reported. Proteins containing EAL and HD-GYP domains are present in bacterial genomes in comparable numbers. Most of these enzymes contain various N-terminal sensor domains that control their activities based on sensing diverse input signals . The most intensively studied process that c-di-GMP participates in is the transition between motile and sessile lifestyles in Gram-negative bacteria...

## Biological Role

Consumed as substrate in 2 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

KEGG compound: 3',5'-Cyclic diGMP; cdiGMP; 3',5'-Cyclic diguanylic acid; Bis-(3',5')-cyclic diGMP; Cyclic di-3',5'-guanylate

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (8)

- `activates` --> [[reaction.ecocyc.CELLULOSE-SYNTHASE-UDP-FORMING-RXN|reaction.ecocyc.CELLULOSE-SYNTHASE-UDP-FORMING-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.RXN0-5413|reaction.ecocyc.RXN0-5413]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `is_product_of` --> [[reaction.ecocyc.RXN0-5359|reaction.ecocyc.RXN0-5359]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R08991|reaction.R08991]] `KEGG` `database` - C16463 + C00001 <=> C18076
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-4181|reaction.ecocyc.RXN0-4181]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.RXN0-5359|reaction.ecocyc.RXN0-5359]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-6445|reaction.ecocyc.RXN0-6445]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.RXN0-7078|reaction.ecocyc.RXN0-7078]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C16463`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
