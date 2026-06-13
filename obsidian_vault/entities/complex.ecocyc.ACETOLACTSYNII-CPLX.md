---
entity_id: "complex.ecocyc.ACETOLACTSYNII-CPLX"
entity_type: "complex"
name: "acetohydroxybutanoate synthase / acetolactate synthase"
source_database: "EcoCyc"
source_id: "ACETOLACTSYNII-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "AHAS"
  - "AHAS II"
  - "acetohydroxy acid synthase II"
  - "acetohydroxybutanoate synthase II"
  - "acetolactate synthase II"
---

# acetohydroxybutanoate synthase / acetolactate synthase

`complex.ecocyc.ACETOLACTSYNII-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ACETOLACTSYNII-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0DP89|protein.P0DP89]], [[protein.P0ADG1|protein.P0ADG1]]

## Enriched Summary

Acetohydroxyacid synthase II (AHAS II) encoded by ilvG and ilvM catalyzes the biosynthesis of α-aceto-α-hydroxybutyrate and α-acetolactate. AHAS II is not found in E. coli K-12 due to a mutation in ilvG, although it is found in other E. coli strains. See the entry for G8221-MONOMER for more information. In non-K-12 strains, AHAS II is a bifunctional enzyme that catalyzes the biosynthesis of α-aceto-α-hydroxybutyrate for the isoleucine pathway and of α-acetolactate for the valine pathway . Both the large catalytic subunit IlvG and the small regulatory subunit IlvM are required for this activity, though the exact stoichiometry of the IlvM subunit is unclear . The kinetics of AHAS II have been evaluated . Interactions between the large and small subunits of the three AHAS isozymes have been studied . Review: Acetohydroxyacid synthase II (AHAS II) encoded by ilvG and ilvM catalyzes the biosynthesis of α-aceto-α-hydroxybutyrate and α-acetolactate. AHAS II is not found in E. coli K-12 due to a mutation in ilvG, although it is found in other E. coli strains. See the entry for G8221-MONOMER for more information. In non-K-12 strains, AHAS II is a bifunctional enzyme that catalyzes the biosynthesis of α-aceto-α-hydroxybutyrate for the isoleucine pathway and of α-acetolactate for the valine pathway...

## Biological Role

Catalyzes ACETOLACTSYN-RXN (reaction.ecocyc.ACETOLACTSYN-RXN), 2-aceto-2-hydroxy-butyrate synthase (reaction.ecocyc.ACETOOHBUTSYN-RXN). Bound by FAD (molecule.C00016), Thiamin diphosphate (molecule.C00068).

## Annotation

Acetohydroxyacid synthase II (AHAS II) encoded by ilvG and ilvM catalyzes the biosynthesis of α-aceto-α-hydroxybutyrate and α-acetolactate. AHAS II is not found in E. coli K-12 due to a mutation in ilvG, although it is found in other E. coli strains. See the entry for G8221-MONOMER for more information. In non-K-12 strains, AHAS II is a bifunctional enzyme that catalyzes the biosynthesis of α-aceto-α-hydroxybutyrate for the isoleucine pathway and of α-acetolactate for the valine pathway . Both the large catalytic subunit IlvG and the small regulatory subunit IlvM are required for this activity, though the exact stoichiometry of the IlvM subunit is unclear . The kinetics of AHAS II have been evaluated . Interactions between the large and small subunits of the three AHAS isozymes have been studied . Review:

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.ACETOLACTSYN-RXN|reaction.ecocyc.ACETOLACTSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.ACETOOHBUTSYN-RXN|reaction.ecocyc.ACETOOHBUTSYN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (4)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0ADG1|protein.P0ADG1]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0DP89|protein.P0DP89]] `EcoCyc` `database` - EcoCyc component coefficient=

## External IDs

- `EcoCyc:ACETOLACTSYNII-CPLX`

## Notes

protein.P0DP89|protein.P0ADG1
