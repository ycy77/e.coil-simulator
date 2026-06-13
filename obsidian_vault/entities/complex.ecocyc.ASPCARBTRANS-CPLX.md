---
entity_id: "complex.ecocyc.ASPCARBTRANS-CPLX"
entity_type: "complex"
name: "aspartate carbamoyltransferase"
source_database: "EcoCyc"
source_id: "ASPCARBTRANS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# aspartate carbamoyltransferase

`complex.ecocyc.ASPCARBTRANS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ASPCARBTRANS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[complex.ecocyc.ASPCARBCAT-TRIMER|complex.ecocyc.ASPCARBCAT-TRIMER]], [[complex.ecocyc.ASPCARBREG-DIMER|complex.ecocyc.ASPCARBREG-DIMER]]

## Enriched Summary

Aspartate transcarbamylase (ATCase) catalyzes the first reaction unique to the de novo biosynthesis of pyrimidine nucleotides. The enzyme and its mechanism of allosteric regulation has been studied extensively; for details and further references to the primary literature, the reader is referred to the comprehensive reviews cited below. The ATCase holoenzyme consists of two catalytic trimers (encoded by pyrB) and three regulatory dimers (encoded by pyrI) . Numerous crystal structures of the enzyme have been solved (see below). The three regulatory dimers are located at the interface between the two catalytic trimers. Binding of the inhibitor, CTP, causes tightening of the structure, while binding of the activator, ATP, causes opening of the structure. ATCase catalyzes carbamoyl aspartate formation by an ordered sequential reaction between aspartate and carbamoyl phosphate, showing cooperativity for the second substrate, aspartate . Allosteric regulation of the enzyme is achieved by a concerted transition between a low-affinity T state to a high-affinity R state that is induced upon binding of carbamoyl phosphate . The structural transitions of E. coli aspartate transcarbamylase have been analyzed by X-ray crystallography for several decades and this approach represents a large body of work in the field. Some of the work following the review is cited here...

## Biological Role

Catalyzes ASPCARBTRANS-RXN (reaction.ecocyc.ASPCARBTRANS-RXN).

## Annotation

Aspartate transcarbamylase (ATCase) catalyzes the first reaction unique to the de novo biosynthesis of pyrimidine nucleotides. The enzyme and its mechanism of allosteric regulation has been studied extensively; for details and further references to the primary literature, the reader is referred to the comprehensive reviews cited below. The ATCase holoenzyme consists of two catalytic trimers (encoded by pyrB) and three regulatory dimers (encoded by pyrI) . Numerous crystal structures of the enzyme have been solved (see below). The three regulatory dimers are located at the interface between the two catalytic trimers. Binding of the inhibitor, CTP, causes tightening of the structure, while binding of the activator, ATP, causes opening of the structure. ATCase catalyzes carbamoyl aspartate formation by an ordered sequential reaction between aspartate and carbamoyl phosphate, showing cooperativity for the second substrate, aspartate . Allosteric regulation of the enzyme is achieved by a concerted transition between a low-affinity T state to a high-affinity R state that is induced upon binding of carbamoyl phosphate . The structural transitions of E. coli aspartate transcarbamylase have been analyzed by X-ray crystallography for several decades and this approach represents a large body of work in the field. Some of the work following the review is cited here. Structures of unliganded and liganded enzyme have been solved . The structures of mutant enzymes have shown functionally important amino acid residues . Structural studies of the T-state, R-state, and the T to R state transition have also been published . In addition, mutants in the PyrB catalytic subunit have been analyzed crystallographically . Many biophysical , kinetic and modeling , inhibitor , and mutant analysis

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ASPCARBTRANS-RXN|reaction.ecocyc.ASPCARBTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `is_component_of` <-- [[complex.ecocyc.ASPCARBCAT-TRIMER|complex.ecocyc.ASPCARBCAT-TRIMER]] `EcoCyc` `database` - EcoCyc component coefficient=2
- `is_component_of` <-- [[complex.ecocyc.ASPCARBREG-DIMER|complex.ecocyc.ASPCARBREG-DIMER]] `EcoCyc` `database` - EcoCyc component coefficient=3
- `is_component_of` <-- [[protein.P0A786|protein.P0A786]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6
- `is_component_of` <-- [[protein.P0A7F3|protein.P0A7F3]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:ASPCARBTRANS-CPLX`
- `PDB:1RAA`
- `PDB:1RAB`
- `PDB:1RAC`
- `PDB:1RAD`
- `PDB:1RAE`
- `PDB:1RAF`
- `PDB:1RAG`
- `PDB:1RAH`
- `QSPROTEOME:QS00178357`

## Notes

2*complex.ecocyc.ASPCARBCAT-TRIMER|3*complex.ecocyc.ASPCARBREG-DIMER
