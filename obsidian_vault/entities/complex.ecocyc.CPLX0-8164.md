---
entity_id: "complex.ecocyc.CPLX0-8164"
entity_type: "complex"
name: "molybdopterin synthase adenylyltransferase"
source_database: "EcoCyc"
source_id: "CPLX0-8164"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# molybdopterin synthase adenylyltransferase

`complex.ecocyc.CPLX0-8164`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8164`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P12282|protein.P12282]]

## Enriched Summary

Molybdenum and tungsten cofactors of all enzymes (except nitrogenase) that require one or the other for activity are present in an oxidized state as molybdate or tungstate ions that are chelated by the cis-dithiolene moiety of a molybdenum cofactor. The cofactor that predominates in E. coli is molybdopterin guanine dinucleotide. In the first segment 5'-GTP is converted in several steps that involve MoaA and MoaC to a sulfur-free pterin named precursor Z (cyclic pyranopterin phosphate); then in a subsequent series of reactions two sulfhydryl groups are added yielding molybdopterin with its cis-dithiolene moiety; finally molybdenum is inserted via chelation into the cis-dithiolene moiety and a guanyl group is added, yielding molybdopterin guanine dinucleotide. Enzymes encoded by the moaABCDE, mobAB, mogA, and moeAB operons all participate in the synthesis of molybdopterin guanine dinucleotide. A mutational block in any of these proteins leads to a loss of function of all molybdenum enzymes. The moeAB (chlEN) operon has been cloned and sequenced . Because MoeB is essential for activation of molybdopterin synthase (MPT synthase), it was initially termed MPT synthase sulfurase and was presumed to catalyze transfer of sulfur atoms to MPT synthase from some unknown donor...

## Biological Role

Catalyzes RXN-11361 (reaction.ecocyc.RXN-11361). Component of molybdopterin synthase adenylyltransferase/sulfur transferase (complex.ecocyc.CPLX0-12611).

## Annotation

Molybdenum and tungsten cofactors of all enzymes (except nitrogenase) that require one or the other for activity are present in an oxidized state as molybdate or tungstate ions that are chelated by the cis-dithiolene moiety of a molybdenum cofactor. The cofactor that predominates in E. coli is molybdopterin guanine dinucleotide. In the first segment 5'-GTP is converted in several steps that involve MoaA and MoaC to a sulfur-free pterin named precursor Z (cyclic pyranopterin phosphate); then in a subsequent series of reactions two sulfhydryl groups are added yielding molybdopterin with its cis-dithiolene moiety; finally molybdenum is inserted via chelation into the cis-dithiolene moiety and a guanyl group is added, yielding molybdopterin guanine dinucleotide. Enzymes encoded by the moaABCDE, mobAB, mogA, and moeAB operons all participate in the synthesis of molybdopterin guanine dinucleotide. A mutational block in any of these proteins leads to a loss of function of all molybdenum enzymes. The moeAB (chlEN) operon has been cloned and sequenced . Because MoeB is essential for activation of molybdopterin synthase (MPT synthase), it was initially termed MPT synthase sulfurase and was presumed to catalyze transfer of sulfur atoms to MPT synthase from some unknown donor . However, other evidence indicates that MoeB is not the actual sulfurase, but rather that it catalyzes the adenylation of the C-terminus of MoaD in an ATP-dependent reaction. MoeB appears to activate sulfurtransferase IscS, and the IscS activity is further enhanced by MoaD . Surface plasmon resonance studies suggested that IscS specifically binds to the putative in vivo MoeB-MoaD complex . It has since been determined that the carboxy-adenylated MoaD is sulfurated by the IscS via TusA or YnjE sulfurtransferas

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-11361|reaction.ecocyc.RXN-11361]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-12611|complex.ecocyc.CPLX0-12611]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P12282|protein.P12282]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8164`
- `QSPROTEOME:QS00188647`

## Notes

2*protein.P12282
