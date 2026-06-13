---
entity_id: "protein.P37146"
entity_type: "protein"
name: "nrdF"
source_database: "UniProt"
source_id: "P37146"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nrdF ygaD b2676 JW2651"
---

# nrdF

`protein.P37146`

## Static

- Type: `protein`
- Source: `UniProt:P37146`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Provides the precursors necessary for DNA synthesis. Catalyzes the biosynthesis of deoxyribonucleotides from the corresponding ribonucleotides. R2F contains the tyrosyl radical required for catalysis.

## Biological Role

Component of ribonucleoside-diphosphate reductase 2, β subunit dimer (complex.ecocyc.NRDF-CPLX), ribonucleoside-diphosphate reductase 2 (complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Provides the precursors necessary for DNA synthesis. Catalyzes the biosynthesis of deoxyribonucleotides from the corresponding ribonucleotides. R2F contains the tyrosyl radical required for catalysis.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.NRDF-CPLX|complex.ecocyc.NRDF-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX|complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTII-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2676|gene.b2676]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37146`
- `KEGG:ecj:JW2651;eco:b2676;ecoc:C3026_14745;`
- `GeneID:93779334;947149;`
- `GO:GO:0004748; GO:0005971; GO:0009185; GO:0009263; GO:0009265; GO:0030145`
- `EC:1.17.4.1`

## Notes

Ribonucleoside-diphosphate reductase 2 subunit beta (EC 1.17.4.1) (R2F protein) (Ribonucleotide reductase 2)
