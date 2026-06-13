---
entity_id: "complex.ecocyc.CPLX0-8537"
entity_type: "complex"
name: "galactarate dehydratase"
source_database: "EcoCyc"
source_id: "CPLX0-8537"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# galactarate dehydratase

`complex.ecocyc.CPLX0-8537`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8537`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P39829|protein.P39829]]

## Enriched Summary

Galactarate dehydratase catalyzes the dehydration of galactarate, the naturally occurring dicarboxylic acid analogue of D-galactose . Enzymatic activity of galactarate dehydratase is induced by growth on D-glucarate, galactarate, and D-glycerate . A crystal structure of GarD has been solved, revealing a novel combination of three structural domains where the central domain serves as the dimerization interface . A garD deletion mutant in E. coli Nissle 1917 is unable to utilize galactarate or glucarate as the sole source of carbon. The gudDXP and garD genes confer a fitness advantage in the colon of streptomycin pre-treated mice . Galactarate dehydratase catalyzes the dehydration of galactarate, the naturally occurring dicarboxylic acid analogue of D-galactose . Enzymatic activity of galactarate dehydratase is induced by growth on D-glucarate, galactarate, and D-glycerate . A crystal structure of GarD has been solved, revealing a novel combination of three structural domains where the central domain serves as the dimerization interface . A garD deletion mutant in E. coli Nissle 1917 is unable to utilize galactarate or glucarate as the sole source of carbon. The gudDXP and garD genes confer a fitness advantage in the colon of streptomycin pre-treated mice .

## Biological Role

Catalyzes GALACTARDEHYDRA-RXN (reaction.ecocyc.GALACTARDEHYDRA-RXN). Bound by Fe2+ (molecule.C14818).

## Annotation

Galactarate dehydratase catalyzes the dehydration of galactarate, the naturally occurring dicarboxylic acid analogue of D-galactose . Enzymatic activity of galactarate dehydratase is induced by growth on D-glucarate, galactarate, and D-glycerate . A crystal structure of GarD has been solved, revealing a novel combination of three structural domains where the central domain serves as the dimerization interface . A garD deletion mutant in E. coli Nissle 1917 is unable to utilize galactarate or glucarate as the sole source of carbon. The gudDXP and garD genes confer a fitness advantage in the colon of streptomycin pre-treated mice .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GALACTARDEHYDRA-RXN|reaction.ecocyc.GALACTARDEHYDRA-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P39829|protein.P39829]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8537`
- `QSPROTEOME:QS00181911`

## Notes

2*protein.P39829
