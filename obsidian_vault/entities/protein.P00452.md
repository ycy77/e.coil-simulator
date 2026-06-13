---
entity_id: "protein.P00452"
entity_type: "protein"
name: "nrdA"
source_database: "UniProt"
source_id: "P00452"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nrdA dnaF b2234 JW2228"
---

# nrdA

`protein.P00452`

## Static

- Type: `protein`
- Source: `UniProt:P00452`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Provides the precursors necessary for DNA synthesis. Catalyzes the biosynthesis of deoxyribonucleotides from the corresponding ribonucleotides. R1 contains the binding sites for both substrates and allosteric effectors and carries out the actual reduction of the ribonucleotide. It also provides redox-active cysteines.

## Biological Role

Component of ribonucleoside-diphosphate reductase 1, α subunit dimer (complex.ecocyc.B1-CPLX), ribonucleoside-diphosphate reductase 1 (complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Provides the precursors necessary for DNA synthesis. Catalyzes the biosynthesis of deoxyribonucleotides from the corresponding ribonucleotides. R1 contains the binding sites for both substrates and allosteric effectors and carries out the actual reduction of the ribonucleotide. It also provides redox-active cysteines.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.B1-CPLX|complex.ecocyc.B1-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX|complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2234|gene.b2234]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P00452`
- `KEGG:ecj:JW2228;eco:b2234;ecoc:C3026_12485;`
- `GeneID:93774941;946612;`
- `GO:GO:0004748; GO:0005524; GO:0005829; GO:0005971; GO:0009185; GO:0009263; GO:0009265; GO:0015949; GO:0042802; GO:0044183`
- `EC:1.17.4.1`

## Notes

Ribonucleoside-diphosphate reductase 1 subunit alpha (EC 1.17.4.1) (Protein B1) (Ribonucleoside-diphosphate reductase 1 R1 subunit) (Ribonucleotide reductase 1)
