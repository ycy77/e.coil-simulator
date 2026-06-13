---
entity_id: "complex.ecocyc.DHPDIOXYGEN-CPLX"
entity_type: "complex"
name: "3-carboxyethylcatechol 2,3-dioxygenase"
source_database: "EcoCyc"
source_id: "DHPDIOXYGEN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "2,3-dihydroxyphenylpropionate/2,3-dihydroxycinnamate 1,2-dioxygenase"
---

# 3-carboxyethylcatechol 2,3-dioxygenase

`complex.ecocyc.DHPDIOXYGEN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DHPDIOXYGEN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ABR9|protein.P0ABR9]]

## Enriched Summary

3-(2,3-dihydroxyphenyl)propionate dioxygenase (MhpB) is a non-heme-iron(II)-dependent extradiol catechol dioxygenase; it catalyzes the meta cleavage of the phenolic ring structure of 3-(2,3-dihydroxyphenyl)propionate. This compound is a common catabolic intermediate of both 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate degradation . The catalytic mechanism of MhpB is based on acid-base catalysis involving the His115 and His179 residues assisting direct 1,2-alkenyl migration to form a lactone intermediate . A H115Y mutant catalyzes lactonization of the substrate . Directed evolution of MhpB yields enzymes that are able to catalyze the intradiol catechol dioxygenase reaction . MhpB can also catalyze the formation of a 2-tropolone ring-expansion product through a pinacol-type rearrangement . An mhpB mutant does not grow with m-hydroxyphenylpropionate (MHP) or hydroxycinnamate (HCA) as the sole source of carbon . Examination of the potential role of MhpB for degradation of aromatic pollutants has been examined . 3-(2,3-dihydroxyphenyl)propionate dioxygenase (MhpB) is a non-heme-iron(II)-dependent extradiol catechol dioxygenase; it catalyzes the meta cleavage of the phenolic ring structure of 3-(2,3-dihydroxyphenyl)propionate. This compound is a common catabolic intermediate of both 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate degradation...

## Biological Role

Catalyzes 1.13.11.16-RXN (reaction.ecocyc.1.13.11.16-RXN), RXN-12073 (reaction.ecocyc.RXN-12073). Bound by Fe2+ (molecule.C14818).

## Annotation

3-(2,3-dihydroxyphenyl)propionate dioxygenase (MhpB) is a non-heme-iron(II)-dependent extradiol catechol dioxygenase; it catalyzes the meta cleavage of the phenolic ring structure of 3-(2,3-dihydroxyphenyl)propionate. This compound is a common catabolic intermediate of both 3-phenylpropionate and 3-(3-hydroxyphenyl)propionate degradation . The catalytic mechanism of MhpB is based on acid-base catalysis involving the His115 and His179 residues assisting direct 1,2-alkenyl migration to form a lactone intermediate . A H115Y mutant catalyzes lactonization of the substrate . Directed evolution of MhpB yields enzymes that are able to catalyze the intradiol catechol dioxygenase reaction . MhpB can also catalyze the formation of a 2-tropolone ring-expansion product through a pinacol-type rearrangement . An mhpB mutant does not grow with m-hydroxyphenylpropionate (MHP) or hydroxycinnamate (HCA) as the sole source of carbon . Examination of the potential role of MhpB for degradation of aromatic pollutants has been examined .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.1.13.11.16-RXN|reaction.ecocyc.1.13.11.16-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-12073|reaction.ecocyc.RXN-12073]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0ABR9|protein.P0ABR9]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:DHPDIOXYGEN-CPLX`
- `QSPROTEOME:QS00049698`

## Notes

4*protein.P0ABR9
