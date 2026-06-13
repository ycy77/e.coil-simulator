---
entity_id: "complex.ecocyc.TRANS-CPLX-203"
entity_type: "complex"
name: "2,3-diketo-L-gulonate:Na+ symporter"
source_database: "EcoCyc"
source_id: "TRANS-CPLX-203"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "YiaMNO binding protein-dependent secondary (TRAP) transporter"
---

# 2,3-diketo-L-gulonate:Na+ symporter

`complex.ecocyc.TRANS-CPLX-203`

## Static

- Type: `complex`
- Source: `EcoCyc:TRANS-CPLX-203`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P37676|protein.P37676]], [[protein.P37675|protein.P37675]], [[protein.P37674|protein.P37674]]

## Enriched Summary

Based on sequence similarity, the yiaMNO genes encode the only tri-partite ATP-independent periplasmic (TRAP) transporter in Escherichia coli. The TRAP transporters share characteristics of both the ATP-binding cassette (ABC) and secondary families of transporters . Like the ABC transporters TRAP transporters use an extracytoplasmic solute-binding protein, but, rather than ATP hydrolysis, the driving force is provided by either proton-(pmf) and/or sodium ion motive force (smf) . Based on sequence similarity, YiaO is the periplasmic solute-binding protein and YiaM and YiaN are the large and small membrane-spanning proteins, respectively . The YiaMNO TRAP transporter is responsible for the uptake of 2,3-diketo-L-gulonate which is known to form spontaneously in aqueous solutions from oxidation of ascorbic acid and dehydroascorbic acid . Binding experiments with purified YiaO revealed that YiaO binds 2,3-diketo-L-gulonate with high affinity but does not bind L- or D-xylulose . These newer experiments refute the results of prior experiments which suggested L-xylulose might be the natural substrate of the transporter . Deletion of yiaMNO resulted in a delay of entry into stationary phase of cells grown in LB with glucose, or minimal medium with glucose or other compounds. These cultures obtained a higher stationary phase OD660 and higher c.f.u. numbers...

## Biological Role

Catalyzes 2,3-dioxo-L-gulonate:Na+ symport (reaction.ecocyc.TRANS-RXN0-235). Transports Sodium cation (molecule.C01330), 2,3-didehydro-L-gulonate (molecule.ecocyc.CPD-334).

## Annotation

Based on sequence similarity, the yiaMNO genes encode the only tri-partite ATP-independent periplasmic (TRAP) transporter in Escherichia coli. The TRAP transporters share characteristics of both the ATP-binding cassette (ABC) and secondary families of transporters . Like the ABC transporters TRAP transporters use an extracytoplasmic solute-binding protein, but, rather than ATP hydrolysis, the driving force is provided by either proton-(pmf) and/or sodium ion motive force (smf) . Based on sequence similarity, YiaO is the periplasmic solute-binding protein and YiaM and YiaN are the large and small membrane-spanning proteins, respectively . The YiaMNO TRAP transporter is responsible for the uptake of 2,3-diketo-L-gulonate which is known to form spontaneously in aqueous solutions from oxidation of ascorbic acid and dehydroascorbic acid . Binding experiments with purified YiaO revealed that YiaO binds 2,3-diketo-L-gulonate with high affinity but does not bind L- or D-xylulose . These newer experiments refute the results of prior experiments which suggested L-xylulose might be the natural substrate of the transporter . Deletion of yiaMNO resulted in a delay of entry into stationary phase of cells grown in LB with glucose, or minimal medium with glucose or other compounds. These cultures obtained a higher stationary phase OD660 and higher c.f.u. numbers. Deletion of yiaMNO also resulted in an increased lag time in cultures with high NaCl concentrations, and a reduction in biofilm formation in minimal medium with glucose . Expression of the yiaKLMNO-lyxK-sgbHUE operon increased moderately in response to L-ascorbate .

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-235|reaction.ecocyc.TRANS-RXN0-235]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-334|molecule.ecocyc.CPD-334]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P37674|protein.P37674]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P37675|protein.P37675]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P37676|protein.P37676]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:TRANS-CPLX-203`
- `QSPROTEOME:QS00170441`

## Notes

1*protein.P37676|1*protein.P37675|1*protein.P37674
