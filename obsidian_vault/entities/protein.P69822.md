---
entity_id: "protein.P69822"
entity_type: "protein"
name: "ulaB"
source_database: "UniProt"
source_id: "P69822"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ulaB sgaB yjfT b4194 JW4152"
---

# ulaB

`protein.P69822`

## Static

- Type: `protein`
- Source: `UniProt:P69822`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II UlaABC PTS system is involved in ascorbate transport. {ECO:0000269|PubMed:12644495, ECO:0000305|PubMed:11741871}. ulaB encodes a hydrohilic protein that contains a PTS Enzyme IIB domain and a putative cysteine phosphorylation site (Cys9) . A ulaB deletion mutant is unable to transport or ferment L-ascorbate in vivo or to phosphorylate L-ascorbate in vitro . ulaB utilization of L-ascorbate

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

- `is_component_of` --> [[complex.ecocyc.EIISGA|complex.ecocyc.EIISGA]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4194|gene.b4194]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69822`
- `KEGG:ecj:JW4152;eco:b4194;ecoc:C3026_22655;`
- `GeneID:86861412;89519181;948716;`
- `GO:GO:0005737; GO:0008982; GO:0009401; GO:0015882; GO:0016301; GO:0090585; GO:1902495`
- `EC:2.7.1.194`

## Notes

Ascorbate-specific PTS system EIIB component (EC 2.7.1.194) (Ascorbate-specific phosphotransferase enzyme IIB component)
