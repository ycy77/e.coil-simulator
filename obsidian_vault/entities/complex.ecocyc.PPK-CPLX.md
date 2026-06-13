---
entity_id: "complex.ecocyc.PPK-CPLX"
entity_type: "complex"
name: "polyphosphate kinase"
source_database: "EcoCyc"
source_id: "PPK-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# polyphosphate kinase

`complex.ecocyc.PPK-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PPK-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A7B1|protein.P0A7B1]]

## Enriched Summary

E. coli K-12 has only one polyphosphate kinase (PPK), which is a Type 1 PPK. The enzyme catalyzes several reactions . PPK transfers the γ phosphate of ATP processively to generate inorganic polyphosphate (polyP or polyPi) and ADP. Phosphorylated enzyme (PPK-P) is an intermediate in this reaction. Purified PPK is a tetramer and requires Mg2+ for activity . PPK in which histidine 435 or histidine 454 have been altered to glutamine or alanine results in enzyme that is unable to autophosphorylate and lacks polyphosphate kinase activity. Purified PPK catalyses the synthesis of polyP chains with a uniform length of 750 +/- 50 phosphate groups. No intermediate chain lengths were visualised and polyP chains ranging from 2 - 40 residues in length failed to act as primers for the synthesis reaction in vitro . PPK also catalyses the reverse reaction, which synthesizes ATP from inorganic polyphosphate and ADP . Partially purified PPK from E. coli B is most active in ATP synthesis using polyphosphate molecules with a chain length greater than 132 and its activity decreases with decreasing chain length . Purified PPK can transfer a phosphate from inorganic polyphosphate to nucleotide diphosphates including ADP, GDP, CDP, UDP, dADP, dGDP, dCDP and TDP. It can also transfer a pyrophosphate group to GDP to form guanosine 5' tetraphosphate (ppppG)...

## Biological Role

Catalyzes POLYPHOSPHATE-KINASE-RXN (reaction.ecocyc.POLYPHOSPHATE-KINASE-RXN). Component of degradosome (complex.ecocyc.CPLX0-2381).

## Annotation

E. coli K-12 has only one polyphosphate kinase (PPK), which is a Type 1 PPK. The enzyme catalyzes several reactions . PPK transfers the γ phosphate of ATP processively to generate inorganic polyphosphate (polyP or polyPi) and ADP. Phosphorylated enzyme (PPK-P) is an intermediate in this reaction. Purified PPK is a tetramer and requires Mg2+ for activity . PPK in which histidine 435 or histidine 454 have been altered to glutamine or alanine results in enzyme that is unable to autophosphorylate and lacks polyphosphate kinase activity. Purified PPK catalyses the synthesis of polyP chains with a uniform length of 750 +/- 50 phosphate groups. No intermediate chain lengths were visualised and polyP chains ranging from 2 - 40 residues in length failed to act as primers for the synthesis reaction in vitro . PPK also catalyses the reverse reaction, which synthesizes ATP from inorganic polyphosphate and ADP . Partially purified PPK from E. coli B is most active in ATP synthesis using polyphosphate molecules with a chain length greater than 132 and its activity decreases with decreasing chain length . Purified PPK can transfer a phosphate from inorganic polyphosphate to nucleotide diphosphates including ADP, GDP, CDP, UDP, dADP, dGDP, dCDP and TDP. It can also transfer a pyrophosphate group to GDP to form guanosine 5' tetraphosphate (ppppG) . Purified PPK is also able to phosphorylate thiamine diphosphate in vitro, producing thiamine triphosphate and a small amount of thiamine tetraphosphate . Overproduced PPK results in increased polyPi:AMP phosphotransferase (PAP) activity in E. coli K-12. PPK requires ADENYL-KIN-MONOMER "adenylate kinase" (ADK) for PAP activity. PPK and ADK from a complex in the presence of polyPi in vitro . Overproduced PPK is associated with the outer membran

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.POLYPHOSPHATE-KINASE-RXN|reaction.ecocyc.POLYPHOSPHATE-KINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX0-2381|complex.ecocyc.CPLX0-2381]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A7B1|protein.P0A7B1]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:PPK-CPLX`
- `QSPROTEOME:QS00199535`

## Notes

2*protein.P0A7B1
