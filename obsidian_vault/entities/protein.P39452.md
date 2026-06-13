---
entity_id: "protein.P39452"
entity_type: "protein"
name: "nrdE"
source_database: "UniProt"
source_id: "P39452"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nrdE b2675 JW2650"
---

# nrdE

`protein.P39452`

## Static

- Type: `protein`
- Source: `UniProt:P39452`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Provides the precursors necessary for DNA synthesis. Catalyzes the biosynthesis of deoxyribonucleotides from the corresponding ribonucleotides. R1E contains the binding sites for both substrates and allosteric effectors and carries out the actual reduction of the ribonucleotide.

## Biological Role

Component of ribonucleoside-diphosphate reductase 2, α subunit dimer (complex.ecocyc.NRDE-CPLX), ribonucleoside-diphosphate reductase 2 (complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Provides the precursors necessary for DNA synthesis. Catalyzes the biosynthesis of deoxyribonucleotides from the corresponding ribonucleotides. R1E contains the binding sites for both substrates and allosteric effectors and carries out the actual reduction of the ribonucleotide.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.NRDE-CPLX|complex.ecocyc.NRDE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX|complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2675|gene.b2675]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39452`
- `KEGG:ecj:JW2650;eco:b2675;ecoc:C3026_14740;`
- `GeneID:947155;`
- `GO:GO:0004748; GO:0005524; GO:0005971; GO:0009185; GO:0009263; GO:0009265; GO:0015949`
- `EC:1.17.4.1`

## Notes

Ribonucleoside-diphosphate reductase 2 subunit alpha (EC 1.17.4.1) (R1E protein) (Ribonucleotide reductase 2)
