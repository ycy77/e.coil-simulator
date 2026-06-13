---
entity_id: "protein.P58035"
entity_type: "protein"
name: "sgcB"
source_database: "UniProt"
source_id: "P58035"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sgcB b4565 JW5967"
---

# sgcB

`protein.P58035`

## Static

- Type: `protein`
- Source: `UniProt:P58035`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. {ECO:0000250}. sgcB contains an Enzyme IIB domain with a conserved cysteine residue (Cys8)

## Biological Role

Component of putative PTS enzyme II SgcBCA (complex.ecocyc.EIISGC).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. {ECO:0000250}.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.EIISGC|complex.ecocyc.EIISGC]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4565|gene.b4565]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P58035`
- `KEGG:ecj:JW5967;eco:b4565;`
- `GeneID:1450295;`
- `GO:GO:0005737; GO:0008643; GO:0008982; GO:0009401; GO:0015795; GO:0016301; GO:1902495`
- `EC:2.7.1.-`

## Notes

Putative phosphotransferase enzyme IIB component SgcB (EC 2.7.1.-) (Putative PTS system EIIB component)
