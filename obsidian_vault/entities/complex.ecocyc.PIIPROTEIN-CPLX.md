---
entity_id: "complex.ecocyc.PIIPROTEIN-CPLX"
entity_type: "complex"
name: "nitrogen regulatory protein PII-1"
source_database: "EcoCyc"
source_id: "PIIPROTEIN-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "PII"
  - "PII-1"
---

# nitrogen regulatory protein PII-1

`complex.ecocyc.PIIPROTEIN-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PIIPROTEIN-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A9Z1|protein.P0A9Z1]]

## Enriched Summary

The PII-1 protein encoded by glnB plays a critical role in the regulation of nitrogen metabolism by controlling the activity of GLUTAMINESYN-OLIGOMER (GS). In its regulatory role, PII-1 can interact with three proteins: the glnE-encoded GLNE-MONOMER "glutamine synthetase adenylyltransferase/deadenylase"; the glnD-encoded GLND-MONOMER "uridylyltransferase/uridylyl removing enzyme" and the GLNL-CPLX "NtrB sensory histidine kinase" (NRII protein); PII-1 undergoes posttranslational uridylylation and can bind the allosteric effectors ATP/ADP and 2-KETOGLUTARATE (reviewed by ). PII-1 is also a regulator of fatty acid biosynthesis via its interaction with the biotin carboxylase/biotin carboxyl carrier protein (BC-BCCP) subcomplex of ACETYL-COA-CARBOXYLMULTI-CPLX "acetyl Co-A carboxylase" . PII-1 regulates the use of amino sugars as a source of nitrogen and carbon and regulates nitrogen assimilation from L-aspartate . Early characterisation was done using an E. coli W strain . PII-1 (often called GlnB) from E. coli K-12 is a homotrimer . PII-1 can be modified by the covalent attachment of UMP to tyrosine 51 of each monomer to form uridylylated PII-1 (PII-1-UMP)...

## Annotation

The PII-1 protein encoded by glnB plays a critical role in the regulation of nitrogen metabolism by controlling the activity of GLUTAMINESYN-OLIGOMER (GS). In its regulatory role, PII-1 can interact with three proteins: the glnE-encoded GLNE-MONOMER "glutamine synthetase adenylyltransferase/deadenylase"; the glnD-encoded GLND-MONOMER "uridylyltransferase/uridylyl removing enzyme" and the GLNL-CPLX "NtrB sensory histidine kinase" (NRII protein); PII-1 undergoes posttranslational uridylylation and can bind the allosteric effectors ATP/ADP and 2-KETOGLUTARATE (reviewed by ). PII-1 is also a regulator of fatty acid biosynthesis via its interaction with the biotin carboxylase/biotin carboxyl carrier protein (BC-BCCP) subcomplex of ACETYL-COA-CARBOXYLMULTI-CPLX "acetyl Co-A carboxylase" . PII-1 regulates the use of amino sugars as a source of nitrogen and carbon and regulates nitrogen assimilation from L-aspartate . Early characterisation was done using an E. coli W strain . PII-1 (often called GlnB) from E. coli K-12 is a homotrimer . PII-1 can be modified by the covalent attachment of UMP to tyrosine 51 of each monomer to form uridylylated PII-1 (PII-1-UMP) . The GlnB monomer adopts an interlocking double βαβ fold and contains three loops - two major loops (the T and C loops) and a smaller C-loop; in the homotrimer the T-loop (which contains Tyr51) protrudes away form the main structure . The T-loop is thought to be the site of interaction with receptor proteins; the clefts formed between the T, B and C-loops are thought to be the sites for interaction with the effector molecules . PII-1 stimulates the adenylyltransferase activity of GLNE-MONOMER GlnE resulting in the addition of AMP to GS and subsequent reduction in GS activity; PII-1-UMP stimulates the deadenylylation rea

## Outgoing Edges (3)

- `activates` --> [[reaction.ecocyc.ASPARTASE-RXN|reaction.ecocyc.ASPARTASE-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.RXN0-7380|reaction.ecocyc.RXN0-7380]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions
- `represses` --> [[reaction.ecocyc.NRIIPHOS-RXN|reaction.ecocyc.NRIIPHOS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Reactions

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A9Z1|protein.P0A9Z1]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:PIIPROTEIN-CPLX`
- `QSPROTEOME:QS00196157`

## Notes

3*protein.P0A9Z1
