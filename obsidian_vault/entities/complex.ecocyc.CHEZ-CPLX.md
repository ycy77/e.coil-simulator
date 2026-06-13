---
entity_id: "complex.ecocyc.CHEZ-CPLX"
entity_type: "complex"
name: "chemotaxis protein CheZ"
source_database: "EcoCyc"
source_id: "CHEZ-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "protein phosphatase CheZ"
  - "CheZ"
  - "chemotaxis accessory protein CheZ"
  - "CheY-P phosphatase"
---

# chemotaxis protein CheZ

`complex.ecocyc.CHEZ-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:CHEZ-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A9H9|protein.P0A9H9]]

## Enriched Summary

CheZ mediates dephosphorylation of the response regulator CheY-phosphate (CheY-P) in chemotactic two component signaling pathways; the proposed mechanism of CheZ mediated dephosphorylation includes elements of both allosteric activation of CheY-P autodephosphorylation and direct CheY-P phosphatase activity ( (see also ). cheZ mutants are 'tumbly' swimmers . Overproduction of CheZ counteracts CheY-induced tumbling . E. coli exhibits an optimal tumble-bias for swarming; swarmer cells have a low tumble bias and elevated levels of CheZ relative to liquid-grown cells; CheZ levels are elevated post-transcriptionally in swarming cells by increasing protein stability Purified CheZ dephosphorylates CheA-phosphate in vitro . CheZ accelerates the dephosphorylation of CheA-phosphate in the presence of CheY ; CheZ does not act directly on CheA-phosphate, it may act to accelerate the dephosphorylation of CheY-P . CheZ binds to CheY and binds better to CheY-P; Mg2+ increases binding of CheZ to both CheY and CheY-P . CheZ is a dimer which undergoes further oligomerization in the presence of CheY-P . Reduced CheAS interacts physically with CheZ in situ and this complex has enhanced CheY-P dephosphorylating activity in vitro . Localization of labeled CheZ to chemoreceptor patches requires CheAS but not CheAL...

## Biological Role

Catalyzes CHEYDEPHOS-RXN (reaction.ecocyc.CHEYDEPHOS-RXN).

## Annotation

CheZ mediates dephosphorylation of the response regulator CheY-phosphate (CheY-P) in chemotactic two component signaling pathways; the proposed mechanism of CheZ mediated dephosphorylation includes elements of both allosteric activation of CheY-P autodephosphorylation and direct CheY-P phosphatase activity ( (see also ). cheZ mutants are 'tumbly' swimmers . Overproduction of CheZ counteracts CheY-induced tumbling . E. coli exhibits an optimal tumble-bias for swarming; swarmer cells have a low tumble bias and elevated levels of CheZ relative to liquid-grown cells; CheZ levels are elevated post-transcriptionally in swarming cells by increasing protein stability Purified CheZ dephosphorylates CheA-phosphate in vitro . CheZ accelerates the dephosphorylation of CheA-phosphate in the presence of CheY ; CheZ does not act directly on CheA-phosphate, it may act to accelerate the dephosphorylation of CheY-P . CheZ binds to CheY and binds better to CheY-P; Mg2+ increases binding of CheZ to both CheY and CheY-P . CheZ is a dimer which undergoes further oligomerization in the presence of CheY-P . Reduced CheAS interacts physically with CheZ in situ and this complex has enhanced CheY-P dephosphorylating activity in vitro . Localization of labeled CheZ to chemoreceptor patches requires CheAS but not CheAL . A co-crystal structure of CheZ and CheY-BeF3--Mg2+ has been determined; CheZ is a homodimer which forms a long four-helix bundle; each CheZ monomer binds one CheY molecule; Gln147 from CheZ inserts into the CheY active site and an essential catalytic role for this residue is proposed Comments:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.CHEYDEPHOS-RXN|reaction.ecocyc.CHEYDEPHOS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9H9|protein.P0A9H9]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CHEZ-CPLX`
- `QSPROTEOME:QS00049580`

## Notes

2*protein.P0A9H9
