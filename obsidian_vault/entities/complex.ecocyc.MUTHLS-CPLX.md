---
entity_id: "complex.ecocyc.MUTHLS-CPLX"
entity_type: "complex"
name: "methyl-directed mismatch repair system"
source_database: "EcoCyc"
source_id: "MUTHLS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "MMR"
---

# methyl-directed mismatch repair system

`complex.ecocyc.MUTHLS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:MUTHLS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P23367|protein.P23367]], [[protein.P23909|protein.P23909]], [[protein.P06722|protein.P06722]]

## Enriched Summary

mutH, mutL and mutS encode the key proteins of a post-replicative, methyl-directed mismatch repair (MMR) system. Early studies characterizing this repair system in E. coli include . mutS, mutH (formerly mutR) and mutL mutators (see ) show high mutability by bromouracil and appear to be defective in the repair of mismatched bases . The in vitro repair of a DNA mismatch on the unmethylated strand of a circular heteroduplex DNA requires the products of mutH, mutL, mutS and uvrD (and further ). Methyl-directed DNA mismatch correction has been reconstituted in a purified system consisting of MutH, MutL, and MutS proteins, EG11064-MONOMER, CPLX0-8165, CPLX0-3803 DNA polymerase III holoenzyme, EG10926-MONOMER, DNA ligase, ATP and dNTPs . Bidirectional excision capability depends on both 3' to 5' and 5' to 3' exonucleases and simultaneous inactivation of EG10830-MONOMER exonuclease RecJ, EG10926-MONOMER, CPLX-3946, and G7016-MONOMER abolishes normal mismatch repair in vitro . Reviews: Nobel lecture: mutH, mutL and mutS encode the key proteins of a post-replicative, methyl-directed mismatch repair (MMR) system. Early studies characterizing this repair system in E. coli include . mutS, mutH (formerly mutR) and mutL mutators (see ) show high mutability by bromouracil and appear to be defective in the repair of mismatched bases...

## Annotation

mutH, mutL and mutS encode the key proteins of a post-replicative, methyl-directed mismatch repair (MMR) system. Early studies characterizing this repair system in E. coli include . mutS, mutH (formerly mutR) and mutL mutators (see ) show high mutability by bromouracil and appear to be defective in the repair of mismatched bases . The in vitro repair of a DNA mismatch on the unmethylated strand of a circular heteroduplex DNA requires the products of mutH, mutL, mutS and uvrD (and further ). Methyl-directed DNA mismatch correction has been reconstituted in a purified system consisting of MutH, MutL, and MutS proteins, EG11064-MONOMER, CPLX0-8165, CPLX0-3803 DNA polymerase III holoenzyme, EG10926-MONOMER, DNA ligase, ATP and dNTPs . Bidirectional excision capability depends on both 3' to 5' and 5' to 3' exonucleases and simultaneous inactivation of EG10830-MONOMER exonuclease RecJ, EG10926-MONOMER, CPLX-3946, and G7016-MONOMER abolishes normal mismatch repair in vitro . Reviews: Nobel lecture:

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P06722|protein.P06722]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P23367|protein.P23367]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P23909|protein.P23909]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:MUTHLS-CPLX`
- `PDB:5AKD`
- `PDB:5AKC`
- `PDB:5AKB`
- `PDB:7AIC`
- `PDB:7AIB`
- `QSPROTEOME:QS00182007`

## Notes

2*protein.P23367|protein.P23909|protein.P06722
