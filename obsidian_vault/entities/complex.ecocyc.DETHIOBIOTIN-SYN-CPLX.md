---
entity_id: "complex.ecocyc.DETHIOBIOTIN-SYN-CPLX"
entity_type: "complex"
name: "dethiobiotin synthetase"
source_database: "EcoCyc"
source_id: "DETHIOBIOTIN-SYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# dethiobiotin synthetase

`complex.ecocyc.DETHIOBIOTIN-SYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DETHIOBIOTIN-SYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P13000|protein.P13000]]

## Enriched Summary

Dethiobiotin synthetase (BioD) catalyzes the first ring closure in the biosynthesis of biotin, which is the penultimate step in the biosynthesis pathway. BioD is a functionally unique enzyme which catalyzes a carboxylation reaction that does not require biotin as a prosthetic group . Crystal structures of dethiobiotin synthetase alone and in various binary, ternary and quarternary complexes have been solved . The active form of the enzyme is a homodimer; the active site is located at the dimer interface . The carboxylation site is the N7 amino group of 7,8-diaminopelargonate (DAPA) . A three-step reaction mechanism was proposed : formation of the N7-carbamate of DAPA, activation by ATP to a carbamic-phosphoric acid anhydride, and attack of the anhydride by the N8 amino group, resulting in closure of the ureido ring. Site-directed mutagenesis of active site residues provided further insight into the catalytic mechanism . The mixed carbamic-phosphoric acid anhydride intermediate of the reaction has been isolated and observed by kinetic crystallography . Expression of the bio operon is repressed in the presence of biotin . Under anaerobic conditions on minimal media, a ΔbioD mutant shows weak growth; growth of a double ΔbioD ΔbidA deletion mutant requires supplementation with biotin...

## Biological Role

Catalyzes DETHIOBIOTIN-SYN-RXN (reaction.ecocyc.DETHIOBIOTIN-SYN-RXN). Bound by Magnesium cation (molecule.C00305).

## Annotation

Dethiobiotin synthetase (BioD) catalyzes the first ring closure in the biosynthesis of biotin, which is the penultimate step in the biosynthesis pathway. BioD is a functionally unique enzyme which catalyzes a carboxylation reaction that does not require biotin as a prosthetic group . Crystal structures of dethiobiotin synthetase alone and in various binary, ternary and quarternary complexes have been solved . The active form of the enzyme is a homodimer; the active site is located at the dimer interface . The carboxylation site is the N7 amino group of 7,8-diaminopelargonate (DAPA) . A three-step reaction mechanism was proposed : formation of the N7-carbamate of DAPA, activation by ATP to a carbamic-phosphoric acid anhydride, and attack of the anhydride by the N8 amino group, resulting in closure of the ureido ring. Site-directed mutagenesis of active site residues provided further insight into the catalytic mechanism . The mixed carbamic-phosphoric acid anhydride intermediate of the reaction has been isolated and observed by kinetic crystallography . Expression of the bio operon is repressed in the presence of biotin . Under anaerobic conditions on minimal media, a ΔbioD mutant shows weak growth; growth of a double ΔbioD ΔbidA deletion mutant requires supplementation with biotin . BioD: "biotin-requiring" Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DETHIOBIOTIN-SYN-RXN|reaction.ecocyc.DETHIOBIOTIN-SYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P13000|protein.P13000]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:DETHIOBIOTIN-SYN-CPLX`
- `QSPROTEOME:QS00182759`

## Notes

2*protein.P13000
