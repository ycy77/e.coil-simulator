---
entity_id: "complex.ecocyc.CPLX0-8597"
entity_type: "complex"
name: "DNA binding transcriptional dual regulator RcdA"
source_database: "EcoCyc"
source_id: "CPLX0-8597"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "RcdA"
---

# DNA binding transcriptional dual regulator RcdA

`complex.ecocyc.CPLX0-8597`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8597`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P75811|protein.P75811]]

## Enriched Summary

RcdA, also known as YbjK, belongs to the TetR family and is involved in the regulation of a number of stress response genes, biofilm formation, and transcription regulator genes . Genomic SELEX analysis showed that RcdA can bind to the upstream regions of 27 genes. Among these predicted targets of RcdA, six genes correspond to transcription regulators (AppY, CsgD, FimB, RcdA, Sxy, and YcgF). This indicates that a large number of genes must be regulated indirectly by these regulators. Another group of target genes includes membrane-associated stress response proteins (CsgB, NanC, OmpA, PgaA, YbjJ, YehA, and YoeA) and stress response cytoplasmic proteins (Asr and YdeI), among others . RcdA exhibits strong cooperative DNA binding and produces aggregates of RcdA-DNA complexes. In a specific way and with high binding affinity, this regulator recognizes and binds to sites that have closely related sequences. Furthermore, a consensus sequence has been proposed for RcdA sites. This consensus sequence shows a core binding site of 9 bp, TTGTgtACA, with inverted repeat symmetry . According to the analysis performed by the curator, the consensus sequence has a length of 10 bp (TTGTgtACAa).On the other hand, a dimer conformation for RcdA in solution was observed...

## Biological Role

Component of RcdA-trimethylamine N-oxide (complex.ecocyc.CPLX0-8598), RcdA-tris (complex.ecocyc.CPLX0-8599).

## Annotation

RcdA, also known as YbjK, belongs to the TetR family and is involved in the regulation of a number of stress response genes, biofilm formation, and transcription regulator genes . Genomic SELEX analysis showed that RcdA can bind to the upstream regions of 27 genes. Among these predicted targets of RcdA, six genes correspond to transcription regulators (AppY, CsgD, FimB, RcdA, Sxy, and YcgF). This indicates that a large number of genes must be regulated indirectly by these regulators. Another group of target genes includes membrane-associated stress response proteins (CsgB, NanC, OmpA, PgaA, YbjJ, YehA, and YoeA) and stress response cytoplasmic proteins (Asr and YdeI), among others . RcdA exhibits strong cooperative DNA binding and produces aggregates of RcdA-DNA complexes. In a specific way and with high binding affinity, this regulator recognizes and binds to sites that have closely related sequences. Furthermore, a consensus sequence has been proposed for RcdA sites. This consensus sequence shows a core binding site of 9 bp, TTGTgtACA, with inverted repeat symmetry . According to the analysis performed by the curator, the consensus sequence has a length of 10 bp (TTGTgtACAa).On the other hand, a dimer conformation for RcdA in solution was observed . RcdA contains a HTH DNA binding motif located in its N-terminal domain, and in its C-terminal domain it contains a small cavity for ligand binding which is able to bind small molecules like trimethylamine N-oxide (TMAO) and Tris, with TMAO the preferred of these two in solution . The residues involved in the ligand binding are Y110, W126, S130, D147, and E151 . When RcdA is bound to a ligand, its structure is more rigid than when it is not bound to a ligand. It was suggested that in the flexible conformation that is not bo

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8598|complex.ecocyc.CPLX0-8598]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-8599|complex.ecocyc.CPLX0-8599]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P75811|protein.P75811]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8597`
- `QSPROTEOME:QS00190135`

## Notes

2*protein.P75811
