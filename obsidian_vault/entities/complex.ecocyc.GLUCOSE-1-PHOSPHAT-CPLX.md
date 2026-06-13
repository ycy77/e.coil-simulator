---
entity_id: "complex.ecocyc.GLUCOSE-1-PHOSPHAT-CPLX"
entity_type: "complex"
name: "glucose-1-phosphatase"
source_database: "EcoCyc"
source_id: "GLUCOSE-1-PHOSPHAT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# glucose-1-phosphatase

`complex.ecocyc.GLUCOSE-1-PHOSPHAT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:GLUCOSE-1-PHOSPHAT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P19926|protein.P19926]]

## Enriched Summary

Glucose-1-phosphatase (Agp) hydrolyzes phosphate from glucose-1-phosphate and from 1D-myo-inositol-hexakisphosphate (phytate), hydrolyzing the former substrate with highest efficiency . Agp functions as a scavenger of glucose from glucose-1-phosphate . Agp is a member of the histidine acid phosphatase family. It is related to CPLX-722 AppA in reaction mechanism and folding architecture, but their specificity for 1D-myo-inositol-hexakisphosphate hydrolysis differs. Agp has been shown to hydrolyze phosphate only at the D-3 position of 1D-myo-inositol-hexakisphosphate. In contrast, AppA sequentially hydrolyzes five of six phosphates beginning with phosphate at the 6 position of the inositol ring . Agp from an E. coli B strain (98% identical to the K-12 protein) also functions as a phosphotransferase, transfering the phosphate group to another sugar molecule instead of water. The reaction proceeds via the canonical phosphomonoester hydrolase mechanism, which involves breakage of the P-O bond, not the C1-O bond . Agp is a homodimeric protein that resides in the periplasm . The enzyme was crystallized, and a crystal structure of an active site H18A mutant in an inactive complex with glucose-1-phosphate has been determined at 2.4 Å resolution...

## Biological Role

Catalyzes GLUCOSE-1-PHOSPHAT-RXN (reaction.ecocyc.GLUCOSE-1-PHOSPHAT-RXN), RXN0-1001 (reaction.ecocyc.RXN0-1001).

## Annotation

Glucose-1-phosphatase (Agp) hydrolyzes phosphate from glucose-1-phosphate and from 1D-myo-inositol-hexakisphosphate (phytate), hydrolyzing the former substrate with highest efficiency . Agp functions as a scavenger of glucose from glucose-1-phosphate . Agp is a member of the histidine acid phosphatase family. It is related to CPLX-722 AppA in reaction mechanism and folding architecture, but their specificity for 1D-myo-inositol-hexakisphosphate hydrolysis differs. Agp has been shown to hydrolyze phosphate only at the D-3 position of 1D-myo-inositol-hexakisphosphate. In contrast, AppA sequentially hydrolyzes five of six phosphates beginning with phosphate at the 6 position of the inositol ring . Agp from an E. coli B strain (98% identical to the K-12 protein) also functions as a phosphotransferase, transfering the phosphate group to another sugar molecule instead of water. The reaction proceeds via the canonical phosphomonoester hydrolase mechanism, which involves breakage of the P-O bond, not the C1-O bond . Agp is a homodimeric protein that resides in the periplasm . The enzyme was crystallized, and a crystal structure of an active site H18A mutant in an inactive complex with glucose-1-phosphate has been determined at 2.4 Å resolution . The structure shows three consecutive disulfide bonds ; enzymatic activity is dependent on DISULFOXRED-MONOMER DsbA, but not on DSBC-MONOMER DsbC . In high-phosphate medium, agp is required for growth on glucose-1-phosphate as the sole source of carbon . Agp: "periplasmic acid glucose-1-phosphatase"

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.GLUCOSE-1-PHOSPHAT-RXN|reaction.ecocyc.GLUCOSE-1-PHOSPHAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-1001|reaction.ecocyc.RXN0-1001]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P19926|protein.P19926]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:GLUCOSE-1-PHOSPHAT-CPLX`
- `QSPROTEOME:QS00188603`

## Notes

2*protein.P19926
