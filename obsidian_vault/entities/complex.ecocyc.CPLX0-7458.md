---
entity_id: "complex.ecocyc.CPLX0-7458"
entity_type: "complex"
name: "glycolate dehydrogenase"
source_database: "EcoCyc"
source_id: "CPLX0-7458"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glycolate dehydrogenase

`complex.ecocyc.CPLX0-7458`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7458`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AEP9|protein.P0AEP9]], [[protein.P52073|protein.P52073]], [[protein.P52074|protein.P52074]]

## Enriched Summary

Glycolate dehydrogenase catalyzes the first step in the utilization of glycolate as the sole source of carbon . The enzyme may be membrane-associated; Sallal and Nimer () isolated a cytoplasmic membrane-associated glycolate oxidoreductase activity from E. coli ATCC11775 (serovar O1:K1:H7), and the GlcF subunit itself could only be detected in the membrane fraction . The physiological electron acceptor is unknown. Crude extracts from an E. coli strain expressing glcDEF from a multicopy plasmid contain glycolate oxidase activity. Insertion mutants in either glcD, glcE, or glcF abolish this activity, suggesting that all three gene products are subunits of a glycolate oxidase complex . Glycolate dehydrogenase activity and expression of the glcDEFGB genes is induced by growth on glycolate . Glycolate dehydrogenase catalyzes the first step in the utilization of glycolate as the sole source of carbon . The enzyme may be membrane-associated; Sallal and Nimer () isolated a cytoplasmic membrane-associated glycolate oxidoreductase activity from E. coli ATCC11775 (serovar O1:K1:H7), and the GlcF subunit itself could only be detected in the membrane fraction . The physiological electron acceptor is unknown. Crude extracts from an E. coli strain expressing glcDEF from a multicopy plasmid contain glycolate oxidase activity...

## Biological Role

Catalyzes GLYCOLATEDEHYDRO-RXN (reaction.ecocyc.GLYCOLATEDEHYDRO-RXN), RXN0-7229 (reaction.ecocyc.RXN0-7229).

## Annotation

Glycolate dehydrogenase catalyzes the first step in the utilization of glycolate as the sole source of carbon . The enzyme may be membrane-associated; Sallal and Nimer () isolated a cytoplasmic membrane-associated glycolate oxidoreductase activity from E. coli ATCC11775 (serovar O1:K1:H7), and the GlcF subunit itself could only be detected in the membrane fraction . The physiological electron acceptor is unknown. Crude extracts from an E. coli strain expressing glcDEF from a multicopy plasmid contain glycolate oxidase activity. Insertion mutants in either glcD, glcE, or glcF abolish this activity, suggesting that all three gene products are subunits of a glycolate oxidase complex . Glycolate dehydrogenase activity and expression of the glcDEFGB genes is induced by growth on glycolate .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GLYCOLATEDEHYDRO-RXN|reaction.ecocyc.GLYCOLATEDEHYDRO-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7229|reaction.ecocyc.RXN0-7229]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0AEP9|protein.P0AEP9]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P52073|protein.P52073]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P52074|protein.P52074]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-7458`
- `QSPROTEOME:QS00049429`

## Notes

protein.P0AEP9|protein.P52073|protein.P52074
