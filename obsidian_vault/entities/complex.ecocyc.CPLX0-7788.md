---
entity_id: "complex.ecocyc.CPLX0-7788"
entity_type: "complex"
name: "dihydropyrimidine dehydrogenase (NAD+)"
source_database: "EcoCyc"
source_id: "CPLX0-7788"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "NAD-dependent dihydropyrimidine dehydrogenase"
---

# dihydropyrimidine dehydrogenase (NAD+)

`complex.ecocyc.CPLX0-7788`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7788`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76440|protein.P76440]], [[protein.P25889|protein.P25889]]

## Enriched Summary

The purified and reconstituted PreA/PreT complex was shown to have NAD+-dependent dihydropyrimidine dehydrogenase activity . The enzyme appears to produce dihydrouracil during exponential growth and during stationary phase convert it back to uracil, which can be incorporated into nucleic acids . The enzyme is also active with CPD0-1327 . The purified enzyme contains approximately one molecule each of FAD and FMN and four [4Fe-4S] clusters per PreA-PreT heterodimer . A preTA-deficient mutant has no growth defect in LB medium, but it is not producing dihydrouracil . The purified and reconstituted PreA/PreT complex was shown to have NAD+-dependent dihydropyrimidine dehydrogenase activity . The enzyme appears to produce dihydrouracil during exponential growth and during stationary phase convert it back to uracil, which can be incorporated into nucleic acids . The enzyme is also active with CPD0-1327 . The purified enzyme contains approximately one molecule each of FAD and FMN and four [4Fe-4S] clusters per PreA-PreT heterodimer . A preTA-deficient mutant has no growth defect in LB medium, but it is not producing dihydrouracil .

## Biological Role

Catalyzes DIHYDROURACIL-DEHYDROGENASE-NAD+-RXN (reaction.ecocyc.DIHYDROURACIL-DEHYDROGENASE-NAD_-RXN), RXN-25213 (reaction.ecocyc.RXN-25213), RXN0-6565 (reaction.ecocyc.RXN0-6565).

## Annotation

The purified and reconstituted PreA/PreT complex was shown to have NAD+-dependent dihydropyrimidine dehydrogenase activity . The enzyme appears to produce dihydrouracil during exponential growth and during stationary phase convert it back to uracil, which can be incorporated into nucleic acids . The enzyme is also active with CPD0-1327 . The purified enzyme contains approximately one molecule each of FAD and FMN and four [4Fe-4S] clusters per PreA-PreT heterodimer . A preTA-deficient mutant has no growth defect in LB medium, but it is not producing dihydrouracil .

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.DIHYDROURACIL-DEHYDROGENASE-NAD_-RXN|reaction.ecocyc.DIHYDROURACIL-DEHYDROGENASE-NAD_-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-25213|reaction.ecocyc.RXN-25213]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6565|reaction.ecocyc.RXN0-6565]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P25889|protein.P25889]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` <-- [[protein.P76440|protein.P76440]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-7788`
- `QSPROTEOME:QS00049439`

## Notes

2*protein.P76440|2*protein.P25889
