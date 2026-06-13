---
entity_id: "complex.ecocyc.CPLX0-1668"
entity_type: "complex"
name: "anaerobic fatty acid β-oxidation complex"
source_database: "EcoCyc"
source_id: "CPLX0-1668"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "anaerobic trifunctional enzyme"
  - "anEcTFE"
---

# anaerobic fatty acid β-oxidation complex

`complex.ecocyc.CPLX0-1668`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1668`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P76503|protein.P76503]], [[protein.P77399|protein.P77399]]

## Enriched Summary

E. coli has two sets of enzymes involved in fatty acid β-oxidation. One set comprises G6105 FadE, EG10278 FadA, and EG10279 FadB, with the latter two forming a soluble tetrameric FAO-CPLX FadB2FadA2 complex (data from E. coli B in ). The second set of enzymes consists of G6918 YdiO, G7213 FadI and G7212 FadJ, with the latter two forming a membrane-bound octameric CPLX0-1668 [FadJ2FadI2]2 complex . In both complexes the α-subunits are bifunctional and have EC-4.2.1.17 and EC-1.1.1.35 active sites and the β-subunits have EC-2.3.1.16 activity, leading to the name trifunctional enzyme (TFE). However, the two sets do not have high sequence similarity. In fact, the enzymes of the second set are more similar to the human mitochondrial TFE than to the E. coli soluble TFE. In addition, the enzymes have different substrate specificities: the membrane bound [FadJ2FadI2]2 complex has a preference for medium- and long-chain enoyl-CoAs (similar to the human mitochondrial TFE), whereas the FadB2FadA2 complex prefers short chain enoyl-CoA substrates . After noticing that growth of a ΔfadA mutant is more robust in the absence of oxygen, it was proposed that the FadEAB enzymes operate under aerobic conditions, and the YdiO/FadIJ enzymes operate under anaerobic conditions. The complexes became known as the aerobic trifunctional enzyme (EcTFE) and the anaerobic trifunctional enzyme (anEcTFE)...

## Annotation

E. coli has two sets of enzymes involved in fatty acid β-oxidation. One set comprises G6105 FadE, EG10278 FadA, and EG10279 FadB, with the latter two forming a soluble tetrameric FAO-CPLX FadB2FadA2 complex (data from E. coli B in ). The second set of enzymes consists of G6918 YdiO, G7213 FadI and G7212 FadJ, with the latter two forming a membrane-bound octameric CPLX0-1668 [FadJ2FadI2]2 complex . In both complexes the α-subunits are bifunctional and have EC-4.2.1.17 and EC-1.1.1.35 active sites and the β-subunits have EC-2.3.1.16 activity, leading to the name trifunctional enzyme (TFE). However, the two sets do not have high sequence similarity. In fact, the enzymes of the second set are more similar to the human mitochondrial TFE than to the E. coli soluble TFE. In addition, the enzymes have different substrate specificities: the membrane bound [FadJ2FadI2]2 complex has a preference for medium- and long-chain enoyl-CoAs (similar to the human mitochondrial TFE), whereas the FadB2FadA2 complex prefers short chain enoyl-CoA substrates . After noticing that growth of a ΔfadA mutant is more robust in the absence of oxygen, it was proposed that the FadEAB enzymes operate under aerobic conditions, and the YdiO/FadIJ enzymes operate under anaerobic conditions. The complexes became known as the aerobic trifunctional enzyme (EcTFE) and the anaerobic trifunctional enzyme (anEcTFE) . Several observations suggest that the relationship of the two enzyme sets may be more complicated. It was reported that while EcTFE is not expressed under anaerobic conditions, both pathways are active under aerobic conditions . Nonetheless, the ΔfadIJ double mutant grows well on long-chain fatty acids under anaerobic conditions. A more recent proposal suggested that the membrane-bound FadIJ system c

## Outgoing Edges (0)

_None._

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P76503|protein.P76503]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P77399|protein.P77399]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-1668`
- `QSPROTEOME:QS00049411`

## Notes

protein.P76503|protein.P77399
