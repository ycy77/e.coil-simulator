---
entity_id: "protein.P69924"
entity_type: "protein"
name: "nrdB"
source_database: "UniProt"
source_id: "P69924"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nrdB ftsB b2235 JW2229"
---

# nrdB

`protein.P69924`

## Static

- Type: `protein`
- Source: `UniProt:P69924`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Provides the precursors necessary for DNA synthesis. Catalyzes the biosynthesis of deoxyribonucleotides from the corresponding ribonucleotides. R2 contains the tyrosyl radical required for catalysis.

## Biological Role

Component of ribonucleoside-diphosphate reductase 1, β subunit dimer (complex.ecocyc.B2-CPLX), ribonucleoside-diphosphate reductase 1 (complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Provides the precursors necessary for DNA synthesis. Catalyzes the biosynthesis of deoxyribonucleotides from the corresponding ribonucleotides. R2 contains the tyrosyl radical required for catalysis.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.B2-CPLX|complex.ecocyc.B2-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX|complex.ecocyc.RIBONUCLEOSIDE-DIP-REDUCTI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2235|gene.b2235]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P69924`
- `KEGG:ecj:JW2229;eco:b2235;ecoc:C3026_12490;`
- `GeneID:75058011;946732;`
- `GO:GO:0004748; GO:0005506; GO:0005737; GO:0005829; GO:0005971; GO:0009185; GO:0009263; GO:0009265; GO:0015949; GO:0042802`
- `EC:1.17.4.1`

## Notes

Ribonucleoside-diphosphate reductase 1 subunit beta (EC 1.17.4.1) (Protein B2) (Protein R2) (Ribonucleotide reductase 1)
