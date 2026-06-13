---
entity_id: "complex.ecocyc.CPLX0-8200"
entity_type: "complex"
name: "cyclic di-GMP phosphodiesterase PdeF"
source_database: "EcoCyc"
source_id: "CPLX0-8200"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cyclic di-GMP phosphodiesterase PdeF

`complex.ecocyc.CPLX0-8200`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8200`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P77172|protein.P77172]]

## Enriched Summary

PdeF is an anaerobic cyclic di-GMP phosphodiesterase that is involved in biofilm formation and response to hydrogen peroxide stress . PdeF is an inner membrane protein with an N-terminal MASE1 (Membrane-Associated SEnsor) domain containing nine predicted transmembrane domains, followed by a degenerate GGDEF domain and a C-terminal EAL domain . The C terminus is located in the cytoplasm . pdeF is expressed in stationary phase under anaerobic conditions. Transcription is regulated from a class II FNR-dependent promoter . Under anaerobic conditions, a pdeF mutant shows enhanced biofilm formation and increased sensitivity to hydrogen peroxide stress. Overexpression of PdeF may be toxic . PdeF: "phosphodiesterase F" PdeF is an anaerobic cyclic di-GMP phosphodiesterase that is involved in biofilm formation and response to hydrogen peroxide stress . PdeF is an inner membrane protein with an N-terminal MASE1 (Membrane-Associated SEnsor) domain containing nine predicted transmembrane domains, followed by a degenerate GGDEF domain and a C-terminal EAL domain . The C terminus is located in the cytoplasm . pdeF is expressed in stationary phase under anaerobic conditions. Transcription is regulated from a class II FNR-dependent promoter . Under anaerobic conditions, a pdeF mutant shows enhanced biofilm formation and increased sensitivity to hydrogen peroxide stress...

## Biological Role

Catalyzes RXN0-4181 (reaction.ecocyc.RXN0-4181).

## Annotation

PdeF is an anaerobic cyclic di-GMP phosphodiesterase that is involved in biofilm formation and response to hydrogen peroxide stress . PdeF is an inner membrane protein with an N-terminal MASE1 (Membrane-Associated SEnsor) domain containing nine predicted transmembrane domains, followed by a degenerate GGDEF domain and a C-terminal EAL domain . The C terminus is located in the cytoplasm . pdeF is expressed in stationary phase under anaerobic conditions. Transcription is regulated from a class II FNR-dependent promoter . Under anaerobic conditions, a pdeF mutant shows enhanced biofilm formation and increased sensitivity to hydrogen peroxide stress. Overexpression of PdeF may be toxic . PdeF: "phosphodiesterase F"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4181|reaction.ecocyc.RXN0-4181]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P77172|protein.P77172]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8200`
- `QSPROTEOME:QS00196469`

## Notes

2*protein.P77172
