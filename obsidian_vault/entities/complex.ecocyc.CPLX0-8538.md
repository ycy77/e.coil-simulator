---
entity_id: "complex.ecocyc.CPLX0-8538"
entity_type: "complex"
name: "oxepin-CoA hydrolase [multifunctional]"
source_database: "EcoCyc"
source_id: "CPLX0-8538"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# oxepin-CoA hydrolase [multifunctional]

`complex.ecocyc.CPLX0-8538`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8538`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77455|protein.P77455]]

## Enriched Summary

PaaZ (oxepin-CoA hydrolase/3-oxo-5,6-dehydrosuberyl-CoA semialdehyde dehydrogenase) is a two-domain enzyme that catalyzes the two-step conversion of CPD0-2363 to CPD0-2364 in phenylacetate catabolism. The PaaZ protein consists of an N-terminal NADP-dependent aldehyde dehydrogenase domain and a C-terminal MaoC-like (R)-specific enoyl-CoA hydratase domain . The specific activity of the enzyme for the overall reaction is ~20 µM min-1 mg-1 protein . 3-oxo-5,6-dehydrosuberyl-CoA semialdehyde is a labile intermediate and can undergo spontaneous conversion to the dead-end product CPD0-2558 through a Knoevenagel-type condensation . Avoiding this fate, 3-oxo-5,6-dehydrosuberyl-CoA is transferred between the two PaaZ active sites by electrostatic pivoting of the CoA moiety. The positively charged residues K69, R613 and K636 appear to play a role in channeling Cryo-EM structures of PaaZ show a tri-lobed structure consisting of three domain-swapped homodimers in which the C-terminal hydratase domains form the central core . PaaZ exhibits enoyl-CoA hydratase activity utilizing crotonyl-CoA as a substrate. In a fadB mutant, PaaZ produces (R)-3-hydroxyacyl-CoA for polyhydroxyalkanoate biosynthesis by exogenous Pseudomonas medium-chain-length polyhydroxyalkanoate synthase . A paaZ mutant exhibits a defect in utilization of phenylacetate as a source of carbon...

## Biological Role

Catalyzes 3-HYDROXBUTYRYL-COA-DEHYDRATASE-RXN (reaction.ecocyc.3-HYDROXBUTYRYL-COA-DEHYDRATASE-RXN), RXNMETA-12671 (reaction.ecocyc.RXNMETA-12671), RXNMETA-12672 (reaction.ecocyc.RXNMETA-12672).

## Annotation

PaaZ (oxepin-CoA hydrolase/3-oxo-5,6-dehydrosuberyl-CoA semialdehyde dehydrogenase) is a two-domain enzyme that catalyzes the two-step conversion of CPD0-2363 to CPD0-2364 in phenylacetate catabolism. The PaaZ protein consists of an N-terminal NADP-dependent aldehyde dehydrogenase domain and a C-terminal MaoC-like (R)-specific enoyl-CoA hydratase domain . The specific activity of the enzyme for the overall reaction is ~20 µM min-1 mg-1 protein . 3-oxo-5,6-dehydrosuberyl-CoA semialdehyde is a labile intermediate and can undergo spontaneous conversion to the dead-end product CPD0-2558 through a Knoevenagel-type condensation . Avoiding this fate, 3-oxo-5,6-dehydrosuberyl-CoA is transferred between the two PaaZ active sites by electrostatic pivoting of the CoA moiety. The positively charged residues K69, R613 and K636 appear to play a role in channeling Cryo-EM structures of PaaZ show a tri-lobed structure consisting of three domain-swapped homodimers in which the C-terminal hydratase domains form the central core . PaaZ exhibits enoyl-CoA hydratase activity utilizing crotonyl-CoA as a substrate. In a fadB mutant, PaaZ produces (R)-3-hydroxyacyl-CoA for polyhydroxyalkanoate biosynthesis by exogenous Pseudomonas medium-chain-length polyhydroxyalkanoate synthase . A paaZ mutant exhibits a defect in utilization of phenylacetate as a source of carbon . PaaZ: "phenylacetic acid degradation"

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.3-HYDROXBUTYRYL-COA-DEHYDRATASE-RXN|reaction.ecocyc.3-HYDROXBUTYRYL-COA-DEHYDRATASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXNMETA-12671|reaction.ecocyc.RXNMETA-12671]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXNMETA-12672|reaction.ecocyc.RXNMETA-12672]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P77455|protein.P77455]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-8538`
- `QSPROTEOME:QS00182779`

## Notes

6*protein.P77455
