---
entity_id: "protein.P39301"
entity_type: "protein"
name: "ulaA"
source_database: "UniProt"
source_id: "P39301"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ulaA sgaT yjfS b4193 JW5744"
---

# ulaA

`protein.P39301`

## Static

- Type: `protein`
- Source: `UniProt:P39301`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II UlaABC PTS system is involved in ascorbate transport. {ECO:0000269|PubMed:12644495, ECO:0000305|PubMed:11741871}. UlaA is the integral membrane component of the ascorbate PTS system. Crystal structures, thought to represent an outward open, substrate bound and an occluded, substrate bound conformation have been reported. The protein crystallises as a dimer; ascorbate is bound, through a mixture of hydrogen and van der Waals intereactions, in a pocket located in the 'core domain' of the dimer; the UlaA protomer contains 11 transmembrane segments, 4 hairpin like structures and three amphipathic helices . A ulaA deletion mutant is unable to transport or ferment L-ascorbate in vivo or to phosphorylate L-ascorbate in vitro . ulaA: utilization of L-ascorbate

## Biological Role

Component of L-ascorbate specific PTS enzyme II (complex.ecocyc.EIISGA).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II UlaABC PTS system is involved in ascorbate transport. {ECO:0000269|PubMed:12644495, ECO:0000305|PubMed:11741871}.

## Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.EIISGA|complex.ecocyc.EIISGA]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4193|gene.b4193]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39301`
- `KEGG:ecj:JW5744;eco:b4193;ecoc:C3026_22650;`
- `GeneID:75169713;948717;`
- `GO:GO:0005886; GO:0009401; GO:0015882; GO:0016020; GO:0042802; GO:0090585; GO:1902495`

## Notes

Ascorbate-specific PTS system EIIC component (Ascorbate-specific permease IIC component UlaA)
