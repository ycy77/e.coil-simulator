---
entity_id: "complex.ecocyc.GLUTATHIONE-REDUCT-NADPH-CPLX"
entity_type: "complex"
name: "glutathione reductase"
source_database: "EcoCyc"
source_id: "GLUTATHIONE-REDUCT-NADPH-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glutathione reductase

`complex.ecocyc.GLUTATHIONE-REDUCT-NADPH-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLUTATHIONE-REDUCT-NADPH-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `structural`
- Components: [[protein.P06715|protein.P06715]]

## Enriched Summary

Glutathione reductase (Gor) is a flavoprotein that reduces oxidized glutathione to form reduced glutathione (GSH), the major nonprotein sulfhydryl in living organisms. Glutathione takes part in many different intracellular processes, including maintenance of reduced thiol groups, protection from oxygen-induced cell damage, and generation of deoxyribonucleotide precursors for DNA synthesis. Glutathione reductase together with NADPH, glutathione, and glutaredoxin make up a second hydrogen donor system in E. coli in addition to the thioredoxin system (see GLUT-REDOX-PWY and THIOREDOX-PWY). Glutathione reductase is a member of the family of flavin-dependent pyridine nucleotide-disulfide oxidoreductases. Other members of this family include THIOREDOXIN-REDUCT-NADPH-CPLX, E3-CPLX, CPLX-4822, CPLX-7455, and CPLX-2803 . In mutants lacking glutathione reductase activity the ratio of reduced to oxidized glutathione is not significantly changed suggesting that either alternative enzymes exist, or the thioredoxin pathway may also participate . These mutations also cause no growth defect, although the activity of glutathione reductase appears to be essential to maintaining a high glutathione content...

## Biological Role

Catalyzes GLUTATHIONE-REDUCT-NADPH-RXN (reaction.ecocyc.GLUTATHIONE-REDUCT-NADPH-RXN). Bound by FAD (molecule.C00016).

## Annotation

Glutathione reductase (Gor) is a flavoprotein that reduces oxidized glutathione to form reduced glutathione (GSH), the major nonprotein sulfhydryl in living organisms. Glutathione takes part in many different intracellular processes, including maintenance of reduced thiol groups, protection from oxygen-induced cell damage, and generation of deoxyribonucleotide precursors for DNA synthesis. Glutathione reductase together with NADPH, glutathione, and glutaredoxin make up a second hydrogen donor system in E. coli in addition to the thioredoxin system (see GLUT-REDOX-PWY and THIOREDOX-PWY). Glutathione reductase is a member of the family of flavin-dependent pyridine nucleotide-disulfide oxidoreductases. Other members of this family include THIOREDOXIN-REDUCT-NADPH-CPLX, E3-CPLX, CPLX-4822, CPLX-7455, and CPLX-2803 . In mutants lacking glutathione reductase activity the ratio of reduced to oxidized glutathione is not significantly changed suggesting that either alternative enzymes exist, or the thioredoxin pathway may also participate . These mutations also cause no growth defect, although the activity of glutathione reductase appears to be essential to maintaining a high glutathione content . Deletion mutant of gor revealed that NI+2 inhibits the Gor complex's ability to resist the antimicrobial oxidation of CPD-26678 (HOSCN); complementation with plasmid-encoded gor restored the HOSCN resistance . The native E. coli enzyme has been purified, characterized, and its redox interconversions studied . The gene was cloned and the recombinant enzyme was also studied . A number of site-directed mutagenesis studies have investigated the structure and catalytic mechanism of Gor . The E. coli enzyme has also been subjected to comparative kinetic analysis with eukaryotic enzymes . Cel

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUTATHIONE-REDUCT-NADPH-RXN|reaction.ecocyc.GLUTATHIONE-REDUCT-NADPH-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P06715|protein.P06715]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GLUTATHIONE-REDUCT-NADPH-CPLX`
- `QSPROTEOME:QS00181741`

## Notes

2*protein.P06715
