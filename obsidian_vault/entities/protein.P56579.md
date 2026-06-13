---
entity_id: "protein.P56579"
entity_type: "protein"
name: "srlA"
source_database: "UniProt"
source_id: "P56579"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00430, ECO:0000305|PubMed:3553176}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00430, ECO:0000305|PubMed:3553176}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "srlA gutA sbl b2702 JW5429"
---

# srlA

`protein.P56579`

## Static

- Type: `protein`
- Source: `UniProt:P56579`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00430, ECO:0000305|PubMed:3553176}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00430, ECO:0000305|PubMed:3553176}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. The enzyme II complex composed of SrlA, SrlB and SrlE is involved in glucitol/sorbitol transport. It can also use D-mannitol. {ECO:0000269|PubMed:1100608}. Contains PTS enzyme IIC2 (IIC-N) domain . SrlA is predicted to contain 3 transmembrane helices; the C-terminus is located in the cytoplasm . srlA belongs to a network of genes which facilitate stress-induced mutagenesis (SIM) in E. coli K-12 .

## Biological Role

Component of sorbitol-specific PTS enzyme II (complex.ecocyc.CPLX-169).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. The enzyme II complex composed of SrlA, SrlB and SrlE is involved in glucitol/sorbitol transport. It can also use D-mannitol. {ECO:0000269|PubMed:1100608}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-169|complex.ecocyc.CPLX-169]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2702|gene.b2702]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P56579`
- `KEGG:ecj:JW5429;eco:b2702;ecoc:C3026_14875;`
- `GeneID:93779309;947575;`
- `GO:GO:0005886; GO:0009401; GO:0015795; GO:1902495`

## Notes

PTS system glucitol/sorbitol-specific EIIC component (EIIC-Gut) (Glucitol/sorbitol permease IIC component)
