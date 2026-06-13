---
entity_id: "complex.ecocyc.CPLX0-13749"
entity_type: "complex"
name: "trehalose-6-phosphate synthase"
source_database: "EcoCyc"
source_id: "CPLX0-13749"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# trehalose-6-phosphate synthase

`complex.ecocyc.CPLX0-13749`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-13749`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[complex.ecocyc.CPLX0-13742|complex.ecocyc.CPLX0-13742]]

## Enriched Summary

Under conditions of high osmolarity, E. coli synthesizes high concentrations of internal trehalose. Trehalose-6-phosphate synthase (OtsA) catalyzes the first step in that biosynthetic pathway . Crystal structures of OtsA have been solved to 2.4 Å and 2.0 Å, the latter of which is bound to substrates; the protein exists as a homodimer in equilibrium with its homotetramer form. The catalytic center at the dimer interface has similarity to glycogen phosphorylases and shows conformational changes, providing insight into the catalytic mechanism . Accumulation of trehalose at low temperatures enhances cell viability . otsA mutants are viable, but osmotically sensitive in minimal media and sensitive to cold shock . An otsA mutant produces increased levels of persister cells during early stationary phase and under heat stress conditions . Stability of otsBA mRNA is increased approximately 10-fold at 16°C compared to 37°C . Expression of otsA is induced by high osmolarity , low temperature , and during the transition to stationary phase . Under nutrient-limiting conditions in an RpoS mutant strain background, an adaptive mutation that allows RpoS-independent transcription of otsBA arises spontaneously and increases fitness . Overexpression of otsA improves ethanol tolerance in an engineered strain...

## Biological Role

Catalyzes TREHALOSE6PSYN-RXN (reaction.ecocyc.TREHALOSE6PSYN-RXN).

## Annotation

Under conditions of high osmolarity, E. coli synthesizes high concentrations of internal trehalose. Trehalose-6-phosphate synthase (OtsA) catalyzes the first step in that biosynthetic pathway . Crystal structures of OtsA have been solved to 2.4 Å and 2.0 Å, the latter of which is bound to substrates; the protein exists as a homodimer in equilibrium with its homotetramer form. The catalytic center at the dimer interface has similarity to glycogen phosphorylases and shows conformational changes, providing insight into the catalytic mechanism . Accumulation of trehalose at low temperatures enhances cell viability . otsA mutants are viable, but osmotically sensitive in minimal media and sensitive to cold shock . An otsA mutant produces increased levels of persister cells during early stationary phase and under heat stress conditions . Stability of otsBA mRNA is increased approximately 10-fold at 16°C compared to 37°C . Expression of otsA is induced by high osmolarity , low temperature , and during the transition to stationary phase . Under nutrient-limiting conditions in an RpoS mutant strain background, an adaptive mutation that allows RpoS-independent transcription of otsBA arises spontaneously and increases fitness . Overexpression of otsA improves ethanol tolerance in an engineered strain . OtsA: "osmoregulatory trehalose synthesis A" Reviews:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TREHALOSE6PSYN-RXN|reaction.ecocyc.TREHALOSE6PSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-13742|complex.ecocyc.CPLX0-13742]] `EcoCyc` `database` - EcoCyc component coefficient=2
- `is_component_of` <-- [[protein.P31677|protein.P31677]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-13749`

## Notes

2*complex.ecocyc.CPLX0-13742
