---
entity_id: "complex.ecocyc.CPLX0-8031"
entity_type: "complex"
name: "pyridoxal kinase 2"
source_database: "EcoCyc"
source_id: "CPLX0-8031"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# pyridoxal kinase 2

`complex.ecocyc.CPLX0-8031`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8031`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77150|protein.P77150]]

## Enriched Summary

PdxY was first identified by its sequence homology to PDXK-MONOMER PdxK, the major pyridoxal (PL) kinase activity in the cell , and is a member of the ribokinase superfamily of enzymes . The physiological role of PdxY is still unclear. Purified PdxY has very low catalytic activity compared to PdxK . Assaying overexpressed PdxY in cell lysate results in significantly increased PL kinase activity, suggesting a requirement for a cellular component that the purified enzyme lacks . PdxY binds PL and PLP tightly, apparently via a covalent bond to Cys122 . A C122A mutant shows reduced catalytic activity compared to wild type . PdxY activity appears to be sufficient to allow mutants blocked in both pdxK and the PLP biosynthetic pathway to grow with pyridoxal supplementation . Crystal structures of PdxY has been determined . PdxY is a homodimer, with each monomer forming a separate active site . PdxY: PdxY was first identified by its sequence homology to PDXK-MONOMER PdxK, the major pyridoxal (PL) kinase activity in the cell , and is a member of the ribokinase superfamily of enzymes . The physiological role of PdxY is still unclear. Purified PdxY has very low catalytic activity compared to PdxK . Assaying overexpressed PdxY in cell lysate results in significantly increased PL kinase activity, suggesting a requirement for a cellular component that the purified enzyme lacks...

## Biological Role

Catalyzes PYRIDOXKIN-RXN (reaction.ecocyc.PYRIDOXKIN-RXN).

## Annotation

PdxY was first identified by its sequence homology to PDXK-MONOMER PdxK, the major pyridoxal (PL) kinase activity in the cell , and is a member of the ribokinase superfamily of enzymes . The physiological role of PdxY is still unclear. Purified PdxY has very low catalytic activity compared to PdxK . Assaying overexpressed PdxY in cell lysate results in significantly increased PL kinase activity, suggesting a requirement for a cellular component that the purified enzyme lacks . PdxY binds PL and PLP tightly, apparently via a covalent bond to Cys122 . A C122A mutant shows reduced catalytic activity compared to wild type . PdxY activity appears to be sufficient to allow mutants blocked in both pdxK and the PLP biosynthetic pathway to grow with pyridoxal supplementation . Crystal structures of PdxY has been determined . PdxY is a homodimer, with each monomer forming a separate active site . PdxY:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PYRIDOXKIN-RXN|reaction.ecocyc.PYRIDOXKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P77150|protein.P77150]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8031`
- `QSPROTEOME:QS00183277`

## Notes

2*protein.P77150
