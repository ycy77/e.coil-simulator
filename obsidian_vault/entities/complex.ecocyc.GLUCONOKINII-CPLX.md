---
entity_id: "complex.ecocyc.GLUCONOKINII-CPLX"
entity_type: "complex"
name: "D-gluconate kinase, thermostable"
source_database: "EcoCyc"
source_id: "GLUCONOKINII-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "gluconokinase I"
---

# D-gluconate kinase, thermostable

`complex.ecocyc.GLUCONOKINII-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLUCONOKINII-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P46859|protein.P46859]]

## Enriched Summary

E. coli encodes two D-gluconate kinases which can be distinguished by their thermal sensitivity. The gntK-encoded enzyme, described here, is thermostable , and its primary function is in the D-gluconate degradation pathway . The properties of the enzyme purified by differ in several respects from the expected values. Crystal structures of GntK have been solved . Binding of ATP induces a conformational change that opens the active site cavity to the gluconate substrate . Gluconokinase activity is induced by growth on gluconate . Single-cell measurements of gntK expression show that the D-gluconate utilization pathway exhibits a graded response to the presence of D-gluconate at lower concentrations; at higher concentrations, the cell population splits into induced and uninduced subpopulations . Review: E. coli encodes two D-gluconate kinases which can be distinguished by their thermal sensitivity. The gntK-encoded enzyme, described here, is thermostable , and its primary function is in the D-gluconate degradation pathway . The properties of the enzyme purified by differ in several respects from the expected values. Crystal structures of GntK have been solved . Binding of ATP induces a conformational change that opens the active site cavity to the gluconate substrate . Gluconokinase activity is induced by growth on gluconate...

## Biological Role

Catalyzes GLUCONOKIN-RXN (reaction.ecocyc.GLUCONOKIN-RXN).

## Annotation

E. coli encodes two D-gluconate kinases which can be distinguished by their thermal sensitivity. The gntK-encoded enzyme, described here, is thermostable , and its primary function is in the D-gluconate degradation pathway . The properties of the enzyme purified by differ in several respects from the expected values. Crystal structures of GntK have been solved . Binding of ATP induces a conformational change that opens the active site cavity to the gluconate substrate . Gluconokinase activity is induced by growth on gluconate . Single-cell measurements of gntK expression show that the D-gluconate utilization pathway exhibits a graded response to the presence of D-gluconate at lower concentrations; at higher concentrations, the cell population splits into induced and uninduced subpopulations . Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GLUCONOKIN-RXN|reaction.ecocyc.GLUCONOKIN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P46859|protein.P46859]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GLUCONOKINII-CPLX`
- `QSPROTEOME:QS00049499`

## Notes

2*protein.P46859
