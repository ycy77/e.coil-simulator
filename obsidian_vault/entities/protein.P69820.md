---
entity_id: "protein.P69820"
entity_type: "protein"
name: "ulaC"
source_database: "UniProt"
source_id: "P69820"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ulaC ptxA sgaA yjfU b4195 JW4153"
---

# ulaC

`protein.P69820`

## Static

- Type: `protein`
- Source: `UniProt:P69820`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II UlaABC PTS system is involved in ascorbate transport. {ECO:0000269|PubMed:12644495, ECO:0000305|PubMed:11741871}. ulaC contains a PTS Enzyme IIA domain with a predicted active site histidine (his68) that is phosphorylated by the general phosphocarrier protein, HPr . A ulaC deletion mutant is unable to transport or ferment L-ascorbate in vivo or to phosphorylate L-ascorbate in vitro . ulaC: utilization of L-ascorbate .

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

- `encodes` <-- [[gene.b4195|gene.b4195]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69820`
- `KEGG:ecj:JW4153;eco:b4195;ecoc:C3026_22660;`
- `GeneID:948715;`
- `GO:GO:0005737; GO:0009401; GO:0015882; GO:0016301; GO:0090585; GO:1902495`

## Notes

Ascorbate-specific PTS system EIIA component (Ascorbate-specific phosphotransferase enzyme IIA component)
