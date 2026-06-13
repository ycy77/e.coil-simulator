---
entity_id: "complex.ecocyc.FRUCBISALD-CLASSI"
entity_type: "complex"
name: "fructose-bisphosphate aldolase class I"
source_database: "EcoCyc"
source_id: "FRUCBISALD-CLASSI"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# fructose-bisphosphate aldolase class I

`complex.ecocyc.FRUCBISALD-CLASSI`

## Static

- Type: `complex`
- Source: `EcoCyc:FRUCBISALD-CLASSI`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0A991|protein.P0A991]]

## Enriched Summary

Fructose 1,6-bisphosphate aldolase catalyzes a reversible aldol cleavage/condensation reaction during glycolysis and gluconeogenesis in E. coli. In the glycolytic direction, fructose 1,6-bisphosphate (FBP) is cleaved to produce glyceraldehyde 3-phosphate and dihydroxyacetone phosphate (glycerone phosphate). Two types of FBP aldolases have been distinguished, Class I and Class II. Class I FBP aldolases utilize an active site lysine residue to form a Schiff-base between the ε-amino group of lysine and the carbonyl group of the substrate. They also vary in subunit stoichiometry. Class II FBP aldolases are dimeric and utilize a divalent metal ion in catalysis via a similar mechanism E. coli is one of a few organisms that expresses both classes of FBP aldolase . The Class I enzyme described here, FbaB, is induced by gluconeogenic substrates, whereas the Class II enzyme encoded by EG10282 is constitutive. When E. coli K-12 is grown on C-3 carbon sources, both classes of aldolase are present, although the Class I enzyme is present only under these conditions. Therefore the Class I enzyme is most likely involved in gluconeogenesis and the Class II enzyme in glycolysis . In earlier work it was thought that FbaB was a tetramer , but later studies showed that it is a homodecamer . A tertiary and quarternary structure was modeled based on small-angle X-ray scattering data...

## Biological Role

Catalyzes F16ALDOLASE-RXN (reaction.ecocyc.F16ALDOLASE-RXN).

## Annotation

Fructose 1,6-bisphosphate aldolase catalyzes a reversible aldol cleavage/condensation reaction during glycolysis and gluconeogenesis in E. coli. In the glycolytic direction, fructose 1,6-bisphosphate (FBP) is cleaved to produce glyceraldehyde 3-phosphate and dihydroxyacetone phosphate (glycerone phosphate). Two types of FBP aldolases have been distinguished, Class I and Class II. Class I FBP aldolases utilize an active site lysine residue to form a Schiff-base between the ε-amino group of lysine and the carbonyl group of the substrate. They also vary in subunit stoichiometry. Class II FBP aldolases are dimeric and utilize a divalent metal ion in catalysis via a similar mechanism E. coli is one of a few organisms that expresses both classes of FBP aldolase . The Class I enzyme described here, FbaB, is induced by gluconeogenic substrates, whereas the Class II enzyme encoded by EG10282 is constitutive. When E. coli K-12 is grown on C-3 carbon sources, both classes of aldolase are present, although the Class I enzyme is present only under these conditions. Therefore the Class I enzyme is most likely involved in gluconeogenesis and the Class II enzyme in glycolysis . In earlier work it was thought that FbaB was a tetramer , but later studies showed that it is a homodecamer . A tertiary and quarternary structure was modeled based on small-angle X-ray scattering data . The enzyme from E. coli BL21 has been crystallized . FbaB shows low amino acid sequence identity with other Class I and Class II FBP aldolases from prokaryotes or eukaryotes. In the active site, Lys236 was identified as the Schiff-base forming residue, and Lys238 is implicated in substrate binding . Using a pull-down assay and stationary phase cells, FbaB was one of five proteins found to form a complex with CPL

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.F16ALDOLASE-RXN|reaction.ecocyc.F16ALDOLASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A991|protein.P0A991]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## External IDs

- `EcoCyc:FRUCBISALD-CLASSI`
- `QSPROTEOME:QS00231927`

## Notes

10*protein.P0A991
