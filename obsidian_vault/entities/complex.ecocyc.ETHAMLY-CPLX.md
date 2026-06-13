---
entity_id: "complex.ecocyc.ETHAMLY-CPLX"
entity_type: "complex"
name: "ethanolamine ammonia-lyase"
source_database: "EcoCyc"
source_id: "ETHAMLY-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ethanolamine ammonia-lyase

`complex.ecocyc.ETHAMLY-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ETHAMLY-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AEJ6|protein.P0AEJ6]], [[protein.P19636|protein.P19636]]

## Enriched Summary

Ethanolamine ammonia-lyase (EAL) allows E. coli to utilize ethanolamine as the sole source of nitrogen and carbon in the presence of external vitamin B12 . EAL is an adenosylcobalamin-dependent enzyme that is spontaneously inactivated by its substrate and can be reactivated by EutA . The enzyme was first studied in the non-K-12 strain NCIB 8114 . Crystal structures of an N-terminally truncated, but active form of the enzyme both in binary and ternary complexes with the cofactor and substrate have been solved . The enzyme is composed of a hexamer of (αβ)2 dimers, with the α subunit holding the active site and the cobalamin cofactor bound at the interface between the α and β subunits . The authors propose a reaction mechanism that is consistent with a previously described mechanism for adenosylcobalamin-dependent rearrangements . The stereochemical course of the reaction has been modeled on the basis of crystal structures, accounting for the apparent lack of stereospecificity of the enzyme . Production of EAL is catabolite repressed and is induced by the simultaneous presence of ethanolamine and the adenosylcobalamin cofactor . Ethanolamine ammonia-lyase (EAL) allows E. coli to utilize ethanolamine as the sole source of nitrogen and carbon in the presence of external vitamin B12...

## Biological Role

Catalyzes ETHAMLY-RXN (reaction.ecocyc.ETHAMLY-RXN). Bound by Cobamide coenzyme (molecule.C00194).

## Annotation

Ethanolamine ammonia-lyase (EAL) allows E. coli to utilize ethanolamine as the sole source of nitrogen and carbon in the presence of external vitamin B12 . EAL is an adenosylcobalamin-dependent enzyme that is spontaneously inactivated by its substrate and can be reactivated by EutA . The enzyme was first studied in the non-K-12 strain NCIB 8114 . Crystal structures of an N-terminally truncated, but active form of the enzyme both in binary and ternary complexes with the cofactor and substrate have been solved . The enzyme is composed of a hexamer of (αβ)2 dimers, with the α subunit holding the active site and the cobalamin cofactor bound at the interface between the α and β subunits . The authors propose a reaction mechanism that is consistent with a previously described mechanism for adenosylcobalamin-dependent rearrangements . The stereochemical course of the reaction has been modeled on the basis of crystal structures, accounting for the apparent lack of stereospecificity of the enzyme . Production of EAL is catabolite repressed and is induced by the simultaneous presence of ethanolamine and the adenosylcobalamin cofactor .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.ETHAMLY-RXN|reaction.ecocyc.ETHAMLY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00194|molecule.C00194]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AEJ6|protein.P0AEJ6]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6
- `is_component_of` <-- [[protein.P19636|protein.P19636]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:ETHAMLY-CPLX`
- `PDB:3ABO`
- `PDB:3ABQ`
- `PDB:3ABR`
- `PDB:3ABS`
- `PDB:3ANY`
- `PDB:3AO0`
- `PDB:5YSR`
- `PDB:5YSN`
- `QSPROTEOME:QS00187837`

## Notes

6*protein.P0AEJ6|6*protein.P19636
