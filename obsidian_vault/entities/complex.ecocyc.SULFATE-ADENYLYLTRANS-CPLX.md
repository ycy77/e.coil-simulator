---
entity_id: "complex.ecocyc.SULFATE-ADENYLYLTRANS-CPLX"
entity_type: "complex"
name: "sulfate adenylyltransferase"
source_database: "EcoCyc"
source_id: "SULFATE-ADENYLYLTRANS-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sulfate adenylyltransferase

`complex.ecocyc.SULFATE-ADENYLYLTRANS-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:SULFATE-ADENYLYLTRANS-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P21156|protein.P21156]], [[protein.P23845|protein.P23845]]

## Enriched Summary

Sulfate adenylyltransferase is composed of two types of subunits, CysN (53 kDa) and CysD (35 kDa) . The native (390 kDa) molecular weight suggests that the enzyme is a tetramer of CysD-CysN heterodimers . The enzyme catalyzes the activation of intracellular sulfate to APS (APS), a reaction that generates a sulfate-phosphate anhydride linkage. This linkage facilitates an energetically-downhill entry into the subsequent metabolic fates of reduction and group transfer. The rate of APS formation is enhanced by both a protein activator and by GTP hydrolysis . The intrinsic GTPase Is believed to be the CysN subunit . Sulfate adenylyltransferase is composed of two types of subunits, CysN (53 kDa) and CysD (35 kDa) . The native (390 kDa) molecular weight suggests that the enzyme is a tetramer of CysD-CysN heterodimers . The enzyme catalyzes the activation of intracellular sulfate to APS (APS), a reaction that generates a sulfate-phosphate anhydride linkage. This linkage facilitates an energetically-downhill entry into the subsequent metabolic fates of reduction and group transfer. The rate of APS formation is enhanced by both a protein activator and by GTP hydrolysis . The intrinsic GTPase Is believed to be the CysN subunit .

## Biological Role

Catalyzes SULFATE-ADENYLYLTRANS-RXN (reaction.ecocyc.SULFATE-ADENYLYLTRANS-RXN).

## Annotation

Sulfate adenylyltransferase is composed of two types of subunits, CysN (53 kDa) and CysD (35 kDa) . The native (390 kDa) molecular weight suggests that the enzyme is a tetramer of CysD-CysN heterodimers . The enzyme catalyzes the activation of intracellular sulfate to APS (APS), a reaction that generates a sulfate-phosphate anhydride linkage. This linkage facilitates an energetically-downhill entry into the subsequent metabolic fates of reduction and group transfer. The rate of APS formation is enhanced by both a protein activator and by GTP hydrolysis . The intrinsic GTPase Is believed to be the CysN subunit .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.SULFATE-ADENYLYLTRANS-RXN|reaction.ecocyc.SULFATE-ADENYLYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P21156|protein.P21156]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `is_component_of` <-- [[protein.P23845|protein.P23845]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:SULFATE-ADENYLYLTRANS-CPLX`
- `QSPROTEOME:QS00195507`

## Notes

4*protein.P21156|4*protein.P23845
