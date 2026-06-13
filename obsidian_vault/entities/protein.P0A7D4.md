---
entity_id: "protein.P0A7D4"
entity_type: "protein"
name: "purA"
source_database: "UniProt"
source_id: "P0A7D4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "purA adeK b4177 JW4135"
---

# purA

`protein.P0A7D4`

## Static

- Type: `protein`
- Source: `UniProt:P0A7D4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Plays an important role in the de novo pathway of purine nucleotide biosynthesis. Catalyzes the first committed step in the biosynthesis of AMP from IMP. {ECO:0000255|HAMAP-Rule:MF_00011}.

## Biological Role

Catalyzes IMP:L-aspartate ligase (GDP-forming) (reaction.R01135). Component of adenylosuccinate synthetase (complex.ecocyc.ADENYLOSUCCINATE-SYN-DIMER).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Plays an important role in the de novo pathway of purine nucleotide biosynthesis. Catalyzes the first committed step in the biosynthesis of AMP from IMP. {ECO:0000255|HAMAP-Rule:MF_00011}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01135|reaction.R01135]] `KEGG` `database` - via EC:6.3.4.4
- `is_component_of` --> [[complex.ecocyc.ADENYLOSUCCINATE-SYN-DIMER|complex.ecocyc.ADENYLOSUCCINATE-SYN-DIMER]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4177|gene.b4177]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7D4`
- `KEGG:ecj:JW4135;eco:b4177;ecoc:C3026_22570;`
- `GeneID:75169697;75202411;948695;`
- `GO:GO:0000287; GO:0004019; GO:0005525; GO:0005737; GO:0005829; GO:0006164; GO:0006974; GO:0015949; GO:0016020; GO:0044208; GO:0046040; GO:0046086; GO:0097216`
- `EC:6.3.4.4`

## Notes

Adenylosuccinate synthetase (AMPSase) (AdSS) (EC 6.3.4.4) (IMP--aspartate ligase)
