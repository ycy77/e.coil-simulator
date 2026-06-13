---
entity_id: "complex.ecocyc.CPLX0-8176"
entity_type: "complex"
name: "tRNA threonylcarbamoyladenosine dehydratase"
source_database: "EcoCyc"
source_id: "CPLX0-8176"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# tRNA threonylcarbamoyladenosine dehydratase

`complex.ecocyc.CPLX0-8176`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8176`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.Q46927|protein.Q46927]]

## Enriched Summary

tRNA threonylcarbamoyladenosine dehydratase (TcdA) catalyzes the ATP-dependent dehydration of threonylcarbamoyladenosine to form the cyclic threonylcarbamoyladenosine (ct6A) residue at position 37 of ANN-decoding tRNAs. ct6A helps tRNALys decode noncognate codons . TcdA is able to accept sulfur from CsdA in vitro. CsdE interacts with TcdA and thus might act as the sulfur donor in vivo ; transient interactions between TcdA and both CsdE and CsdA can be detected in vitro . CsdA and CsdE appear to support the function of TcdA in the biosynthesis of ct6A . TcdA has been crystallized , and a crystal structure of the enzyme in complex with AMP and ATP has been solved . A solution structure of the TcdA-tRNALys(UUU) complex was reconstructed from SAXS data . A tcdA mutant does not contain the ct6A modification in tRNAs and has lower decoding efficiency than wild type . In growth competition experiments, a tcdA mutant shows reduced fitness compared to wild type, but outcompetes a csdA mutant . An mnmA tcdA double mutant has a synthetic growth defect . CsdL: "cysteine sulfinate desulfinase" TcdA: "tRNA threonylcarbamoyladenosine dehydratase A" tRNA threonylcarbamoyladenosine dehydratase (TcdA) catalyzes the ATP-dependent dehydration of threonylcarbamoyladenosine to form the cyclic threonylcarbamoyladenosine (ct6A) residue at position 37 of ANN-decoding tRNAs...

## Biological Role

Catalyzes RXN0-7115 (reaction.ecocyc.RXN0-7115).

## Annotation

tRNA threonylcarbamoyladenosine dehydratase (TcdA) catalyzes the ATP-dependent dehydration of threonylcarbamoyladenosine to form the cyclic threonylcarbamoyladenosine (ct6A) residue at position 37 of ANN-decoding tRNAs. ct6A helps tRNALys decode noncognate codons . TcdA is able to accept sulfur from CsdA in vitro. CsdE interacts with TcdA and thus might act as the sulfur donor in vivo ; transient interactions between TcdA and both CsdE and CsdA can be detected in vitro . CsdA and CsdE appear to support the function of TcdA in the biosynthesis of ct6A . TcdA has been crystallized , and a crystal structure of the enzyme in complex with AMP and ATP has been solved . A solution structure of the TcdA-tRNALys(UUU) complex was reconstructed from SAXS data . A tcdA mutant does not contain the ct6A modification in tRNAs and has lower decoding efficiency than wild type . In growth competition experiments, a tcdA mutant shows reduced fitness compared to wild type, but outcompetes a csdA mutant . An mnmA tcdA double mutant has a synthetic growth defect . CsdL: "cysteine sulfinate desulfinase" TcdA: "tRNA threonylcarbamoyladenosine dehydratase A"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7115|reaction.ecocyc.RXN0-7115]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.Q46927|protein.Q46927]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8176`
- `QSPROTEOME:QS00196981`

## Notes

2*protein.Q46927
