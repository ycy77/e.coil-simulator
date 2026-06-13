---
entity_id: "complex.ecocyc.CPLX0-8111"
entity_type: "complex"
name: "DNA helicase II"
source_database: "EcoCyc"
source_id: "CPLX0-8111"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# DNA helicase II

`complex.ecocyc.CPLX0-8111`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8111`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P03018|protein.P03018]]

## Enriched Summary

UvrD, also known as DNA helicase II, is an ATP-dependent ssDNA translocase and dsDNA helicase which functions in methyl-directed mismatch repair ( and reviewed in ), and UVRABC-CPLX nucleotide excision repair (NER) . Helicases have been classified into 6 superfamilies (SF) ; UvrD belongs to SFI, as do EG10826-MONOMER "RecD helicase" and CPLX0-3931 "Rep helicase". UvrD may also have a role in replication restart - different modes of action at inactivated replication forks have been characterised, some of which do not require ATPase activity . UvrD does not function in clearing and processing of UV induced blocked replication forks in vivo . UvrD may act as a 'protein remover' while tracking on its DNA substrate . UvrD is required for replication of rolling circle plasmids in E. coli . UvrD is implicated in conjugative plasmid transfer; plasmid transfer frequency is significantly decreased in a ΔuvrD recipient strain . UvrD is a second transcription coupling repair factor; UvrD binds to RNA polymerase and promotes backtracking at stalled elongation complexes in vitro and in vivo, allowing the NER proteins UvrA, UvrB and UvrC access to sites of damage. UvrD binds near the upstream fork of the transcription bubble. Backtracking of RNA polymerase from lesion sites by UvrD, is the first step in a UvrD-dependent transcription coupled repair pathway (and see )...

## Biological Role

Catalyzes RXN-11135 (reaction.ecocyc.RXN-11135).

## Annotation

UvrD, also known as DNA helicase II, is an ATP-dependent ssDNA translocase and dsDNA helicase which functions in methyl-directed mismatch repair ( and reviewed in ), and UVRABC-CPLX nucleotide excision repair (NER) . Helicases have been classified into 6 superfamilies (SF) ; UvrD belongs to SFI, as do EG10826-MONOMER "RecD helicase" and CPLX0-3931 "Rep helicase". UvrD may also have a role in replication restart - different modes of action at inactivated replication forks have been characterised, some of which do not require ATPase activity . UvrD does not function in clearing and processing of UV induced blocked replication forks in vivo . UvrD may act as a 'protein remover' while tracking on its DNA substrate . UvrD is required for replication of rolling circle plasmids in E. coli . UvrD is implicated in conjugative plasmid transfer; plasmid transfer frequency is significantly decreased in a ΔuvrD recipient strain . UvrD is a second transcription coupling repair factor; UvrD binds to RNA polymerase and promotes backtracking at stalled elongation complexes in vitro and in vivo, allowing the NER proteins UvrA, UvrB and UvrC access to sites of damage. UvrD binds near the upstream fork of the transcription bubble. Backtracking of RNA polymerase from lesion sites by UvrD, is the first step in a UvrD-dependent transcription coupled repair pathway (and see ). UvrD and the small molecule alarmone GUANOSINE-5DP-3DP act together to promote RNA polymerase backtracking during transcription coupled NER . UvrD colocates with the replisome at replication blocks; unlike CPLX0-3931 DNA helicase Rep, it does not interact directly with a specific replisome component; UvrD appears to self-associate into tetramers . Purified UvrD has single strand DNA-dependent, ATPase activity, and ATP-de

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11135|reaction.ecocyc.RXN-11135]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P03018|protein.P03018]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8111`
- `QSPROTEOME:QS00191653`

## Notes

2*protein.P03018
