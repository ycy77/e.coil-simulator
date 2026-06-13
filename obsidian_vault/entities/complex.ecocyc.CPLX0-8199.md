---
entity_id: "complex.ecocyc.CPLX0-8199"
entity_type: "complex"
name: "oxygen-sensing cyclic di-GMP phosphodiesterase DosP"
source_database: "EcoCyc"
source_id: "CPLX0-8199"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# oxygen-sensing cyclic di-GMP phosphodiesterase DosP

`complex.ecocyc.CPLX0-8199`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8199`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P76129|protein.P76129]]

## Enriched Summary

DosP acts a direct sensor of oxygen; the protein has an N-terminal heme-binding PAS domain and a C-terminal phosphodiesterase domain . DosP, together with the oxygen-sensing diguanylate cyclase DosC, appears to control production and removal of the second messenger molecule c-di-GMP in response to oxygen . Conformational changes within the N-terminal domain of DosP regulate the enzymatic activity of the C-terminal domain . Binding of O2 or CO to the reduced heme ligand and cyanide or imidazole to the oxidized heme ligand enhances c-di-GMP phosphodiesterase activity. It is proposed that the heme sensor domain inhibits phosphodiesterase catalytic activity, and ligand binding to the heme releases catalytic suppression . O2-dependent catalytic activity is allosterically regulated . Hydrogen sulfide stimulates catalytic activity of DosP under aerobic conditions ; the effect can be attributed to changes in the coordination of the heme iron complex . Dos was initially shown to exhibit cAMP phosphodiesterase activity using a fluorescent substrate; the ferrous form was enzymatically active and the ferric form was not . Under different assay conditions using c-di-GMP and cAMP, the C-terminal EAL domain of Dos exhibits c-di-GMP-specific phosphodiesterase activity, but no cAMP-dependent phosphodiesterase activity...

## Biological Role

Catalyzes RXN0-4181 (reaction.ecocyc.RXN0-4181). Bound by Magnesium cation (molecule.C00305).

## Annotation

DosP acts a direct sensor of oxygen; the protein has an N-terminal heme-binding PAS domain and a C-terminal phosphodiesterase domain . DosP, together with the oxygen-sensing diguanylate cyclase DosC, appears to control production and removal of the second messenger molecule c-di-GMP in response to oxygen . Conformational changes within the N-terminal domain of DosP regulate the enzymatic activity of the C-terminal domain . Binding of O2 or CO to the reduced heme ligand and cyanide or imidazole to the oxidized heme ligand enhances c-di-GMP phosphodiesterase activity. It is proposed that the heme sensor domain inhibits phosphodiesterase catalytic activity, and ligand binding to the heme releases catalytic suppression . O2-dependent catalytic activity is allosterically regulated . Hydrogen sulfide stimulates catalytic activity of DosP under aerobic conditions ; the effect can be attributed to changes in the coordination of the heme iron complex . Dos was initially shown to exhibit cAMP phosphodiesterase activity using a fluorescent substrate; the ferrous form was enzymatically active and the ferric form was not . Under different assay conditions using c-di-GMP and cAMP, the C-terminal EAL domain of Dos exhibits c-di-GMP-specific phosphodiesterase activity, but no cAMP-dependent phosphodiesterase activity . The rate of cAMP hydrolysis reported in is three orders of magnitude lower than the rate of c-di-GMP hydrolysis; thus, c-di-GMP appears to be the physiological substrate . However, overexpressed DosP appears to cleave cAMP, thereby reducing transcription of tnaA and synthesis of indole and leading to increased persistence . Dos forms a homotetramer , with the C-terminal region responsible for tetramerization . In contrast, later experiments indicate that the full-length

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-4181|reaction.ecocyc.RXN0-4181]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P76129|protein.P76129]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8199`
- `QSPROTEOME:QS00049686`

## Notes

2*protein.P76129
