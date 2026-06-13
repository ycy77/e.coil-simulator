---
entity_id: "protein.P42910"
entity_type: "protein"
name: "agaC"
source_database: "UniProt"
source_id: "P42910"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "agaC yraE b3139 JW3108"
---

# agaC

`protein.P42910`

## Static

- Type: `protein`
- Source: `UniProt:P42910`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. This system is involved in N-acetylgalactosamine transport. Sequence analysis indicates that agaC encodes a protein with similarity to the IIC domain of the PTS Enzymes II specific for mannose. agaC is predicted to encode a hydrophobic protein containing 7 transmembrane regions agaC encodes the Enzyme IIC domain of a predicted galactosamine (Gam or GalN) transporting PEP-dependent phosphotransferase system. E. coli K-12 cannot transport galactosamine as it is lacking an Enzyme IIA domain for this PTS (encoded by the agaF gene in E. coli strains B and C). Providing agaF on a plasmid results in a Gam+ phenotype .

## Biological Role

Component of galactosamine-specific PTS enzyme II (complex.ecocyc.CPLX-170).

## Enriched Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. This system is involved in N-acetylgalactosamine transport.

## Pathways

- `eco00052` Galactose metabolism (KEGG)
- `eco00520` Amino sugar and nucleotide sugar metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-170|complex.ecocyc.CPLX-170]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3139|gene.b3139]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P42910`
- `KEGG:ecj:JW3108;eco:b3139;ecoc:C3026_17105;`
- `GeneID:75173312;75203743;947652;`
- `GO:GO:0005886; GO:0009401`

## Notes

N-acetylgalactosamine permease IIC component 1 (EIIC-Aga) (PTS system N-acetylgalactosamine-specific EIIC component 1)
