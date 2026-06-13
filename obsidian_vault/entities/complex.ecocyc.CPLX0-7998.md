---
entity_id: "complex.ecocyc.CPLX0-7998"
entity_type: "complex"
name: "RNase adaptor protein RapZ"
source_database: "EcoCyc"
source_id: "CPLX0-7998"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# RNase adaptor protein RapZ

`complex.ecocyc.CPLX0-7998`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7998`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0A894|protein.P0A894]]

## Enriched Summary

RapZ is involved in regulation of the expression of the metabolic enzyme L-GLN-FRUCT-6-P-AMINOTRANS-MONOMER (GlmS). It binds the small RNA regulators TKE1-RNA GlmY and SRAJ-RNA GlmZ as well as glucosamine-6-phosphate (GlcN6P), the product of the GlmS-catalyzed reaction, and interacts with the PWY0-1503. RapZ controls the processing and stability of the small regulatory RNA GlmZ ; it acts as an adaptor protein that guides processing of GlmZ by RNase E via a direct-entry mechanism that is independent of the 5' phosphorylation status of GlmZ . In vivo, both the RNase E-binding and GlmZ-binding functions of RapZ are required for cleavage of GlmZ . The "decoy" small RNA GlmY binds and sequesters RapZ, thereby inhibiting GlmZ processing . RapZ binds both GlmY and GlmZ likely via its C terminus . Because the GlmZ* cleavage product retains the ability to bind RapZ, it competes with full-length GlmZ for RapZ binding and thereby counteracts processing . Complex formation of GlmZ-RapZ-Rnase E has been demonstrated . The SLI and SLII stem-loop structures of GlmZ are bound by two molecules of two RapZ tetramers, and the region near the intersection of SLI and SLII is bound by one tetramer of RNAse E . The amino acids H190, G249, R253, K170, and C247 are essential for RapZ to promote GlmZ cleavage. The L279, Q273, N271, Y240, and T161 amino acids of RapZ appear to interact with RNAse E...

## Biological Role

Component of RapZ-GlmZ-RnaseE (complex.ecocyc.CPLX0-10097).

## Annotation

RapZ is involved in regulation of the expression of the metabolic enzyme L-GLN-FRUCT-6-P-AMINOTRANS-MONOMER (GlmS). It binds the small RNA regulators TKE1-RNA GlmY and SRAJ-RNA GlmZ as well as glucosamine-6-phosphate (GlcN6P), the product of the GlmS-catalyzed reaction, and interacts with the PWY0-1503. RapZ controls the processing and stability of the small regulatory RNA GlmZ ; it acts as an adaptor protein that guides processing of GlmZ by RNase E via a direct-entry mechanism that is independent of the 5' phosphorylation status of GlmZ . In vivo, both the RNase E-binding and GlmZ-binding functions of RapZ are required for cleavage of GlmZ . The "decoy" small RNA GlmY binds and sequesters RapZ, thereby inhibiting GlmZ processing . RapZ binds both GlmY and GlmZ likely via its C terminus . Because the GlmZ* cleavage product retains the ability to bind RapZ, it competes with full-length GlmZ for RapZ binding and thereby counteracts processing . Complex formation of GlmZ-RapZ-Rnase E has been demonstrated . The SLI and SLII stem-loop structures of GlmZ are bound by two molecules of two RapZ tetramers, and the region near the intersection of SLI and SLII is bound by one tetramer of RNAse E . The amino acids H190, G249, R253, K170, and C247 are essential for RapZ to promote GlmZ cleavage. The L279, Q273, N271, Y240, and T161 amino acids of RapZ appear to interact with RNAse E . RapZ also binds GlcN6P. In the GlcN6P-free form, RapZ stimulates phosphorylation of the two-component system kinase CPLX0-8275 GlrK, which subsequently causes increased expression of glmY. Both GlmY and GlmZ can counteract RapZ's effect on GlrK, resulting in a negative feedback loop. Under GlcN6P-limiting conditions, RapZ binding also protects GlmY* from degradation . RapZ was purified and crystalliz

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-10097|complex.ecocyc.CPLX0-10097]] `EcoCyc` `database` - EcoCyc component coefficient=2

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0A894|protein.P0A894]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## External IDs

- `EcoCyc:CPLX0-7998`
- `QSPROTEOME:QS00188919`

## Notes

4*protein.P0A894
