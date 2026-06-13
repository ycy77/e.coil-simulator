---
entity_id: "complex.ecocyc.CPLX0-1242"
entity_type: "complex"
name: "MazE-MazF antitoxin/toxin complex / DNA-binding transcriptional repressor"
source_database: "EcoCyc"
source_id: "CPLX0-1242"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "MazE-MazF \"addiction module\""
  - "MazFE"
  - "MazEF"
  - "MazE-MazF"
---

# MazE-MazF antitoxin/toxin complex / DNA-binding transcriptional repressor

`complex.ecocyc.CPLX0-1242`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1242`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[complex.ecocyc.CPLX0-1241|complex.ecocyc.CPLX0-1241]], [[complex.ecocyc.CPLX0-841|complex.ecocyc.CPLX0-841]]

## Enriched Summary

MazF is a toxin that is counteracted by the MazE antitoxin . The mazEF system causes a "programmed cell death" response to stresses including starvation antibiotics and quaternary ammonium compounds (QAC) . The response to QAC depends on the density of the bacterial population, through the autoinducer, the extracellular death factor . The antitoxin, MazE, is subject to degradation by ClpP-ClpA protease complex and exhibits a short (30 minute) half life, whereas the toxin, MazF, is much more stable . The structure of the MazE-MazF complex is presented at 1.7 A resolution . The complex is hexameric and is comprised of a MazE homodimer sandwiched between MazF homodimers . It has been shown that the C terminus of the MazE TF plays an important role for MazE by increasing its binding affinity for the palindromic single-site operator . Review: . MazF is a toxin that is counteracted by the MazE antitoxin . The mazEF system causes a "programmed cell death" response to stresses including starvation antibiotics and quaternary ammonium compounds (QAC) . The response to QAC depends on the density of the bacterial population, through the autoinducer, the extracellular death factor . The antitoxin, MazE, is subject to degradation by ClpP-ClpA protease complex and exhibits a short (30 minute) half life, whereas the toxin, MazF, is much more stable...

## Annotation

MazF is a toxin that is counteracted by the MazE antitoxin . The mazEF system causes a "programmed cell death" response to stresses including starvation antibiotics and quaternary ammonium compounds (QAC) . The response to QAC depends on the density of the bacterial population, through the autoinducer, the extracellular death factor . The antitoxin, MazE, is subject to degradation by ClpP-ClpA protease complex and exhibits a short (30 minute) half life, whereas the toxin, MazF, is much more stable . The structure of the MazE-MazF complex is presented at 1.7 A resolution . The complex is hexameric and is comprised of a MazE homodimer sandwiched between MazF homodimers . It has been shown that the C terminus of the MazE TF plays an important role for MazE by increasing its binding affinity for the palindromic single-site operator . Review: .

## Outgoing Edges (1)

- `represses` --> [[reaction.ecocyc.NUCLEOTIDE-PYROPHOSPHATASE-RXN|reaction.ecocyc.NUCLEOTIDE-PYROPHOSPHATASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (4)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-1241|complex.ecocyc.CPLX0-1241]] `EcoCyc` `database` - EcoCyc component coefficient=2
- `is_component_of` <-- [[complex.ecocyc.CPLX0-841|complex.ecocyc.CPLX0-841]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P0AE70|protein.P0AE70]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=4
- `is_component_of` <-- [[protein.P0AE72|protein.P0AE72]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-1242`
- `PDB:1UB4`
- `PDB:5CQY`
- `PDB:5CQX`
- `QSPROTEOME:QS00247040`

## Notes

2*complex.ecocyc.CPLX0-1241|1*complex.ecocyc.CPLX0-841
