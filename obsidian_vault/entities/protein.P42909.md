---
entity_id: "protein.P42909"
entity_type: "protein"
name: "agaB"
source_database: "UniProt"
source_id: "P42909"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "agaB yraD b3138 JW3107"
---

# agaB

`protein.P42909`

## Static

- Type: `protein`
- Source: `UniProt:P42909`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in N-acetylgalactosamine transport. Sequence analysis indicates that agaB encodes a protein with similarity to the IIB domain of the PTS Enzymes II specific for mannose. agaB has sequence similarity with G7632 "agaV". agaB contains a conserved histidine residue (His17) . agaB encodes the Enzyme IIB domain of a predicted galactosamine (Gam or GalN) transporting PEP-dependent phosphotransferase system. E. coli K-12 cannot transport galactosamine as it is lacking an Enzyme IIA domain for this PTS (encoded by the agaF gene in E. coli strains B and C). Providing agaF on a plasmid results in a Gam+ phenotype .

## Biological Role

Component of galactosamine-specific PTS enzyme II (complex.ecocyc.CPLX-170).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in N-acetylgalactosamine transport.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-170|complex.ecocyc.CPLX-170]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3138|gene.b3138]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P42909`
- `KEGG:ecj:JW3107;eco:b3138;ecoc:C3026_17100;`
- `GeneID:947653;`
- `GO:GO:0005737; GO:0008982; GO:0009401; GO:0016301`
- `EC:2.7.1.-`

## Notes

N-acetylgalactosamine-specific phosphotransferase enzyme IIB component 1 (EC 2.7.1.-) (EIIB-Aga) (PTS system N-acetylgalactosamine-specific EIIB component 1)
