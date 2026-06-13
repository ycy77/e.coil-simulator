---
entity_id: "complex.ecocyc.ABC-56-CPLX"
entity_type: "complex"
name: "aliphatic sulfonate ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-56-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "YcbE/YcbM ABC transporter"
  - "alkanesulfonate ABC transporter"
---

# aliphatic sulfonate ABC transporter

`complex.ecocyc.ABC-56-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-56-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P75853|protein.P75853]], [[protein.P75851|protein.P75851]], [[protein.P0AAI1|protein.P0AAI1]]

## Enriched Summary

SsuA, SsuC and SsuB are the protein components of an ATP-dependent uptake system for a broad range of aliphatic sulfonates which E. coli K-12 can use as a source of sulfur under aerobic condtions. ssuA, ssuC and ssuB are part of a larger gene cluster (ssuEADCB) which is required for the utilization of a broad range of aliphatic sulfonates as a source of sulfur; a strain lacking the chromosomal ssuEADBC gene cluster is unable to use a broad range of aliphatic sulfonates as sulfur source including CPD-10434 ethanesulfonate, CPD-10435 propanesulfonate, CPD-3744 butanesulfonate, CPD0-2075 pentanesulfonate, CPD0-2074 hexanesulfonate, CPD-10431 ethanedisulfonate, CPD0-2547 octanesulfonate, CPD0-2546 decanesulfonate, CPD-3745 isethionate, CPD-10246 sulfoacetate, and the buffer substances CPD0-1958 MOPS, HEPES HEPES, CPD0-1958 MES, and CPD-19809 PIPES; the mutant strain is able to obtain sulfur from sulfate, cysteine, cystine, lanthionine, methionine, glutathione and taurine |CITS [10506196]|. Sequence analysis suggests that ssuA, ssuC and ssuB encode a periplasmic substrate-binding protein, a membrane protein and an ATP-binding protein, respectively, of a putative ATP-binding cassette (ABC) family transporter . E...

## Biological Role

Catalyzes ABC-56-RXN (reaction.ecocyc.ABC-56-RXN). Transports an aliphatic sulfonate (molecule.ecocyc.Aliphatic-Sulfonates), hν (molecule.ecocyc.Light).

## Annotation

SsuA, SsuC and SsuB are the protein components of an ATP-dependent uptake system for a broad range of aliphatic sulfonates which E. coli K-12 can use as a source of sulfur under aerobic condtions. ssuA, ssuC and ssuB are part of a larger gene cluster (ssuEADCB) which is required for the utilization of a broad range of aliphatic sulfonates as a source of sulfur; a strain lacking the chromosomal ssuEADBC gene cluster is unable to use a broad range of aliphatic sulfonates as sulfur source including CPD-10434 ethanesulfonate, CPD-10435 propanesulfonate, CPD-3744 butanesulfonate, CPD0-2075 pentanesulfonate, CPD0-2074 hexanesulfonate, CPD-10431 ethanedisulfonate, CPD0-2547 octanesulfonate, CPD0-2546 decanesulfonate, CPD-3745 isethionate, CPD-10246 sulfoacetate, and the buffer substances CPD0-1958 MOPS, HEPES HEPES, CPD0-1958 MES, and CPD-19809 PIPES; the mutant strain is able to obtain sulfur from sulfate, cysteine, cystine, lanthionine, methionine, glutathione and taurine |CITS [10506196]|. Sequence analysis suggests that ssuA, ssuC and ssuB encode a periplasmic substrate-binding protein, a membrane protein and an ATP-binding protein, respectively, of a putative ATP-binding cassette (ABC) family transporter . E. coli K-12 contains a second ABC transporter (ABC-64-CPLX "TauABC") for the uptake of taurine and other sulfonates; the two systems appear to complement each other with respect to the range of substrates transported . A ΔssuA ΔssuCB mutant strain is unable to grow with ethanesulfonate, hexanesulfonate, octanesulfonate, decanesulfonate, CPD0-2543 N-phenyltaurine, sulfoacetate, CPD0-2545 4-phenyl-1-butanesulfonate, HEPES or MOPS as sulfur source and has significantly reduced growth with CPD0-2544 2-(4-pyridyl)ethanesulfonate, propanesulfonate, pentanesulfonate or PIPES

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.ABC-56-RXN|reaction.ecocyc.ABC-56-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.Aliphatic-Sulfonates|molecule.ecocyc.Aliphatic-Sulfonates]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0AAI1|protein.P0AAI1]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P75851|protein.P75851]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P75853|protein.P75853]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-56-CPLX`
- `QSPROTEOME:QS00173827`

## Notes

1*protein.P75853|2*protein.P75851|2*protein.P0AAI1
