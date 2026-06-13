---
entity_id: "protein.P39365"
entity_type: "protein"
name: "sgcC"
source_database: "UniProt"
source_id: "P39365"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sgcC yjhN b4304 JW4266"
---

# sgcC

`protein.P39365`

## Static

- Type: `protein`
- Source: `UniProt:P39365`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. {ECO:0000250}. sgcC is predicted to encode a protein with 9 or 10 transmembrane helices; it shows sequence similarity to the Enzyme IIC domain of the galactitol PTS .

## Biological Role

Component of putative PTS enzyme II SgcBCA (complex.ecocyc.EIISGC).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. {ECO:0000250}.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.EIISGC|complex.ecocyc.EIISGC]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4304|gene.b4304]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39365`
- `KEGG:ecj:JW4266;eco:b4304;ecoc:C3026_23220;`
- `GeneID:946849;`
- `GO:GO:0005886; GO:0008643; GO:0009401; GO:0015577; GO:0015795; GO:1902495`

## Notes

Putative permease IIC component (Putative PTS system EIIC component)
