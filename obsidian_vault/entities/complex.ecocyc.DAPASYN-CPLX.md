---
entity_id: "complex.ecocyc.DAPASYN-CPLX"
entity_type: "complex"
name: "adenosylmethionine-8-amino-7-oxononanoate aminotransferase"
source_database: "EcoCyc"
source_id: "DAPASYN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "adenosylmethionine-8-amino-7-oxononanoate transaminase"
---

# adenosylmethionine-8-amino-7-oxononanoate aminotransferase

`complex.ecocyc.DAPASYN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DAPASYN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P12995|protein.P12995]]

## Enriched Summary

bioA encodes 7,8-diaminopelargonic acid synthase of the PWY0-1507 biotin biosynthesis pathway. S-adenosylmethionine acts in the unusual role of amino donor . The enzyme belongs to subclass III of the vitamin B6-dependent aminotransferase family . The kinetic mechanism of the reaction was determined to be of the ping-pong type . Single-turnover reactions were used to determine kinetics of the two half-reactions . Site-directed mutagenesis and kinetic studies of the mutant enzyme have identified residues essential for either or both half-reactions . Crystal structures of wild type and mutant versions of the enzyme have been determined . The PLP cofactor is covalently linked to the Lys274 residue . Transcription of bioA is repressed in the presence of biotin . BioA: "biotin-requiring" Reviews: bioA encodes 7,8-diaminopelargonic acid synthase of the PWY0-1507 biotin biosynthesis pathway. S-adenosylmethionine acts in the unusual role of amino donor . The enzyme belongs to subclass III of the vitamin B6-dependent aminotransferase family . The kinetic mechanism of the reaction was determined to be of the ping-pong type . Single-turnover reactions were used to determine kinetics of the two half-reactions . Site-directed mutagenesis and kinetic studies of the mutant enzyme have identified residues essential for either or both half-reactions...

## Biological Role

Catalyzes DAPASYN-RXN (reaction.ecocyc.DAPASYN-RXN). Bound by Pyridoxal phosphate (molecule.C00018).

## Annotation

bioA encodes 7,8-diaminopelargonic acid synthase of the PWY0-1507 biotin biosynthesis pathway. S-adenosylmethionine acts in the unusual role of amino donor . The enzyme belongs to subclass III of the vitamin B6-dependent aminotransferase family . The kinetic mechanism of the reaction was determined to be of the ping-pong type . Single-turnover reactions were used to determine kinetics of the two half-reactions . Site-directed mutagenesis and kinetic studies of the mutant enzyme have identified residues essential for either or both half-reactions . Crystal structures of wild type and mutant versions of the enzyme have been determined . The PLP cofactor is covalently linked to the Lys274 residue . Transcription of bioA is repressed in the presence of biotin . BioA: "biotin-requiring" Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DAPASYN-RXN|reaction.ecocyc.DAPASYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00018|molecule.C00018]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P12995|protein.P12995]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:DAPASYN-CPLX`
- `QSPROTEOME:QS00196925`

## Notes

2*protein.P12995
