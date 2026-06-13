---
entity_id: "complex.ecocyc.APORNAP-CPLX"
entity_type: "complex"
name: "RNA polymerase, core enzyme"
source_database: "EcoCyc"
source_id: "APORNAP-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# RNA polymerase, core enzyme

`complex.ecocyc.APORNAP-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:APORNAP-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A7Z4|protein.P0A7Z4]], [[protein.P0A8T7|protein.P0A8T7]], [[protein.P0A8V2|protein.P0A8V2]]

## Enriched Summary

RNA polymerase carries out DNA-dependent RNA synthesis, transcribing genes into RNAs. The core polymerase, consisting of two alpha, one beta and one beta' subunit, binds to one of several sigma factors to form an RNA polymerase holoenzyme that can then initiate transcription at a target promoter. Following initiation, the sigma factor is discarded and the core polymerase transcribes RNA in a step called elongation, which ceases when it reaches a transcription termination site. Initiation of RNA synthesis requires the RNA polymerase core enzyme, an associated sigma factor and a promoter site. RNA polymerase moves along the DNA during its promoter search, stopping to bind initially at one of a number of possible positions in the -55 to -5 position relative to the transcription start site . The promoter search is facilitated by nonspecific DNA interactions and is largely independent of nucleoid organization, growth condition, transcription activity, or promoter class . When a -35 sequence is present, the sigma factor makes first contact there . Following initial contact, the binding interaction spreads to the +20 position and involves the sigma, beta and beta' subunits . Binding appears to involve contact between RNA polymerase and both helix faces as the DNA is wrapped around the protein...

## Biological Role

Catalyzes DNA-DIRECTED-RNA-POLYMERASE-RXN (reaction.ecocyc.DNA-DIRECTED-RNA-POLYMERASE-RXN). Component of RNA polymerase sigma 19 (complex.ecocyc.CPLX0-221), RNA polymerase sigma 28 (complex.ecocyc.CPLX0-222), RNA polymerase sigma 32 (complex.ecocyc.RNAP32-CPLX), RNA polymerase sigma 54 (complex.ecocyc.RNAP54-CPLX), RNA polymerase sigma 70 (complex.ecocyc.RNAP70-CPLX), RNA polymerase sigma 24 (complex.ecocyc.RNAPE-CPLX), RNA polymerase sigma S (complex.ecocyc.RNAPS-CPLX).

## Annotation

RNA polymerase carries out DNA-dependent RNA synthesis, transcribing genes into RNAs. The core polymerase, consisting of two alpha, one beta and one beta' subunit, binds to one of several sigma factors to form an RNA polymerase holoenzyme that can then initiate transcription at a target promoter. Following initiation, the sigma factor is discarded and the core polymerase transcribes RNA in a step called elongation, which ceases when it reaches a transcription termination site. Initiation of RNA synthesis requires the RNA polymerase core enzyme, an associated sigma factor and a promoter site. RNA polymerase moves along the DNA during its promoter search, stopping to bind initially at one of a number of possible positions in the -55 to -5 position relative to the transcription start site . The promoter search is facilitated by nonspecific DNA interactions and is largely independent of nucleoid organization, growth condition, transcription activity, or promoter class . When a -35 sequence is present, the sigma factor makes first contact there . Following initial contact, the binding interaction spreads to the +20 position and involves the sigma, beta and beta' subunits . Binding appears to involve contact between RNA polymerase and both helix faces as the DNA is wrapped around the protein . Once binding is complete, the DNA helix is opened starting at the -12 to -10 positions and proceeding to around the +2 position . Several factors modulate the strength of a promoter. A promoter sequence can affect initiation time and the amount of transcript produced . Both the sequences of the -10 and -35 sites and the distance between them play into activity at a given promoter . Based on results of a genomically encoded multiplexed reporter assay, it was determined that the -35 and -

## Outgoing Edges (8)

- `catalyzes` --> [[reaction.ecocyc.DNA-DIRECTED-RNA-POLYMERASE-RXN|reaction.ecocyc.DNA-DIRECTED-RNA-POLYMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-221|complex.ecocyc.CPLX0-221]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-222|complex.ecocyc.CPLX0-222]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.RNAP32-CPLX|complex.ecocyc.RNAP32-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.RNAP54-CPLX|complex.ecocyc.RNAP54-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.RNAP70-CPLX|complex.ecocyc.RNAP70-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.RNAPE-CPLX|complex.ecocyc.RNAPE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` --> [[complex.ecocyc.RNAPS-CPLX|complex.ecocyc.RNAPS-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0A7Z4|protein.P0A7Z4]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P0A8T7|protein.P0A8T7]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0A8V2|protein.P0A8V2]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:APORNAP-CPLX`
- `PDB:3LU0`
- `PDB:3IYD`
- `PDB:4KN7`
- `PDB:4KN4`
- `PDB:4KMU`
- `PDB:4JK2`
- `PDB:4JK1`
- `PDB:4MEY`
- `QSPROTEOME:QS00182783`

## Notes

2*protein.P0A7Z4|1*protein.P0A8T7|1*protein.P0A8V2
