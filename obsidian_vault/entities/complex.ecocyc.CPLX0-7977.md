---
entity_id: "complex.ecocyc.CPLX0-7977"
entity_type: "complex"
name: "16S rRNA m4C1402 methyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-7977"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "ribosomal RNA small subunit methyltransferase H"
---

# 16S rRNA m4C1402 methyltransferase

`complex.ecocyc.CPLX0-7977`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7977`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P60390|protein.P60390]]

## Enriched Summary

RsmH is the methyltransferase responsible for methylation of 16S rRNA at the N4 position of the C1402 nucleotide within the P site of the ribosome. In vitro, the enzyme is active on the assembled 30S ribosomal subunit, but not naked 16S rRNA or 70S ribosomes . Dimethylation of the C1402 nucleotide is involved in decoding fidelity and translation initiation at non-AUG start codons . The methylation of a 20 kDa protein was seen to depend on the amount of overexpressed RsmH (MraW) in crude extracts; thus, RsmH may also be able to methylate a protein . A crystal structure of RsmH has been solved at 2.25 Å resolution. Although the protein is monomeric in the crystal structure, the His-tagged protein behaves like a dimer during gel filtration . An rsmH null mutant was reported to have no growth defect or a slightly reduced growth rate . An rsmH rsmI double mutant has a more pronounced growth defect . While polar insertion mutants are not viable , non-polar insertion mutations can be generated . MraW: "murein region a" RsmH: "rRNA small subunit methyltransferase H" RsmH is the methyltransferase responsible for methylation of 16S rRNA at the N4 position of the C1402 nucleotide within the P site of the ribosome. In vitro, the enzyme is active on the assembled 30S ribosomal subunit, but not naked 16S rRNA or 70S ribosomes...

## Biological Role

Catalyzes RXN-11638 (reaction.ecocyc.RXN-11638).

## Annotation

RsmH is the methyltransferase responsible for methylation of 16S rRNA at the N4 position of the C1402 nucleotide within the P site of the ribosome. In vitro, the enzyme is active on the assembled 30S ribosomal subunit, but not naked 16S rRNA or 70S ribosomes . Dimethylation of the C1402 nucleotide is involved in decoding fidelity and translation initiation at non-AUG start codons . The methylation of a 20 kDa protein was seen to depend on the amount of overexpressed RsmH (MraW) in crude extracts; thus, RsmH may also be able to methylate a protein . A crystal structure of RsmH has been solved at 2.25 Å resolution. Although the protein is monomeric in the crystal structure, the His-tagged protein behaves like a dimer during gel filtration . An rsmH null mutant was reported to have no growth defect or a slightly reduced growth rate . An rsmH rsmI double mutant has a more pronounced growth defect . While polar insertion mutants are not viable , non-polar insertion mutations can be generated . MraW: "murein region a" RsmH: "rRNA small subunit methyltransferase H"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11638|reaction.ecocyc.RXN-11638]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P60390|protein.P60390]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7977`
- `QSPROTEOME:QS00182769`

## Notes

2*protein.P60390
