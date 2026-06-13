---
entity_id: "protein.P39363"
entity_type: "protein"
name: "sgcA"
source_database: "UniProt"
source_id: "P39363"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "sgcA yjhL b4302 JW4264"
---

# sgcA

`protein.P39363`

## Static

- Type: `protein`
- Source: `UniProt:P39363`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. {ECO:0000250}. sgcA contains an Enzyme IIA domain . Expression of sgcA is induced by acid stress .

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

- `encodes` <-- [[gene.b4302|gene.b4302]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39363`
- `KEGG:ecj:JW4264;eco:b4302;ecoc:C3026_23210;`
- `GeneID:948831;`
- `GO:GO:0005737; GO:0008643; GO:0009401; GO:0015795; GO:0016301; GO:0090585; GO:1902495`

## Notes

Putative phosphotransferase IIA component SgcA (Putative PTS system EIIA component)
