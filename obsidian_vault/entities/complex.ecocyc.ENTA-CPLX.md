---
entity_id: "complex.ecocyc.ENTA-CPLX"
entity_type: "complex"
name: "2,3-dihydro-2,3-dihydroxybenzoate dehydrogenase"
source_database: "EcoCyc"
source_id: "ENTA-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# 2,3-dihydro-2,3-dihydroxybenzoate dehydrogenase

`complex.ecocyc.ENTA-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ENTA-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P15047|protein.P15047]]

## Enriched Summary

2,3-Dihydro-2,3-dihydroxybenzoate dehydrogenase catalyzes the formation of 2,3-dihydroxybenzoate (DHB), an intermediate in the enterobactin biosynthesis pathway. Subsequent condensation of DHB with serine and cyclization comprise the remainder of the pathway. Due to the aromatization of the 2,3-dihydro-2,3-dihydroxybenzoate, the reaction is irreversible . EntA specifically oxidizes the C3-hydroxyl group of 2,3-dihydro-2,3-dihydroxybenzoate, producing the transient intermediate 2-hydroxy-3-oxo-4,6-cyclohexadiene-1-carboxylate, which undergoes rapid aromatization to the final product, 2,3-dihydroxybenzoate . A crystal structure of the enzyme has been solved at 2.0 Å resolution . Based on gel filtration data, EntA was originally thought to be a homooctamer in solution . However, EntA is homotetrameric in the crystal structure , and later experiments showed that it undergoes a concentration-dependent transition from a homodimer to a homotetramer . EntA directly interacts with EntE both in vitro and in vivo, enhancing EntE's DHB-AMP ligase activity . The α4 helix, and specifically Gln64, of EntA is involved in the interaction with EntE and in EntA homotetramerization . EntA also directly interacts with EntB. Computational docking studies are consistent with experimental evidence and support the existence of a ternary EntA-EntB-EntE complex...

## Biological Role

Catalyzes DHBDEHYD-RXN (reaction.ecocyc.DHBDEHYD-RXN).

## Annotation

2,3-Dihydro-2,3-dihydroxybenzoate dehydrogenase catalyzes the formation of 2,3-dihydroxybenzoate (DHB), an intermediate in the enterobactin biosynthesis pathway. Subsequent condensation of DHB with serine and cyclization comprise the remainder of the pathway. Due to the aromatization of the 2,3-dihydro-2,3-dihydroxybenzoate, the reaction is irreversible . EntA specifically oxidizes the C3-hydroxyl group of 2,3-dihydro-2,3-dihydroxybenzoate, producing the transient intermediate 2-hydroxy-3-oxo-4,6-cyclohexadiene-1-carboxylate, which undergoes rapid aromatization to the final product, 2,3-dihydroxybenzoate . A crystal structure of the enzyme has been solved at 2.0 Å resolution . Based on gel filtration data, EntA was originally thought to be a homooctamer in solution . However, EntA is homotetrameric in the crystal structure , and later experiments showed that it undergoes a concentration-dependent transition from a homodimer to a homotetramer . EntA directly interacts with EntE both in vitro and in vivo, enhancing EntE's DHB-AMP ligase activity . The α4 helix, and specifically Gln64, of EntA is involved in the interaction with EntE and in EntA homotetramerization . EntA also directly interacts with EntB. Computational docking studies are consistent with experimental evidence and support the existence of a ternary EntA-EntB-EntE complex . Cultivation with nTiO2 resulted in increased production of proteins involved in siderophore biosynthesis (EntA, EntB, EntC, and EntE), siderophore recognition (FepA, CirA) and transport (FepB) . Review:

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.DHBDEHYD-RXN|reaction.ecocyc.DHBDEHYD-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P15047|protein.P15047]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:ENTA-CPLX`
- `QSPROTEOME:QS00188859`

## Notes

4*protein.P15047
