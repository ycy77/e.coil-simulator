---
entity_id: "complex.ecocyc.ACPSUB-CPLX"
entity_type: "complex"
name: "citrate lyase [acyl carrier protein] component"
source_database: "EcoCyc"
source_id: "ACPSUB-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: "CCI-CYTOSOL-GN"
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "CitD acyl carrier protein"
---

# citrate lyase [acyl carrier protein] component

`complex.ecocyc.ACPSUB-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ACPSUB-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Location: CCI-CYTOSOL-GN
- Complex type: `structural`
- Components: [[protein.P69330|protein.P69330]]

## Enriched Summary

This component of the ACECITLY-CPLX is made of 6 copies of the γ subunit, a specialized acyl carrier protein (acp). In the original purification of the enzyme, this subunit was purified with a contaminant and the complex structure was thought to be α-6 β-6 γ-1 . Subsequent work identified the contaminant, and the structure was recognized as α-6 β-6 γ-6 . The [acp] subunit is activated by the covalent binding of an unusual prosthetic group, 2-5-PHOSPHORIBOSYL-3-DEPHOSPHO-COA, which is synthesized from the precursor 2-5-TRIPHOSPHORIBOSYL-3-DEPHOSPHO- (see P2-PWY). This component of the ACECITLY-CPLX is made of 6 copies of the γ subunit, a specialized acyl carrier protein (acp). In the original purification of the enzyme, this subunit was purified with a contaminant and the complex structure was thought to be α-6 β-6 γ-1 . Subsequent work identified the contaminant, and the structure was recognized as α-6 β-6 γ-6 . The [acp] subunit is activated by the covalent binding of an unusual prosthetic group, 2-5-PHOSPHORIBOSYL-3-DEPHOSPHO-COA, which is synthesized from the precursor 2-5-TRIPHOSPHORIBOSYL-3-DEPHOSPHO- (see P2-PWY).

## Biological Role

Component of citrate lyase, inactive (complex.ecocyc.CITLY-CPLX).

## Annotation

This component of the ACECITLY-CPLX is made of 6 copies of the γ subunit, a specialized acyl carrier protein (acp). In the original purification of the enzyme, this subunit was purified with a contaminant and the complex structure was thought to be α-6 β-6 γ-1 . Subsequent work identified the contaminant, and the structure was recognized as α-6 β-6 γ-6 . The [acp] subunit is activated by the covalent binding of an unusual prosthetic group, 2-5-PHOSPHORIBOSYL-3-DEPHOSPHO-COA, which is synthesized from the precursor 2-5-TRIPHOSPHORIBOSYL-3-DEPHOSPHO- (see P2-PWY).

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CITLY-CPLX|complex.ecocyc.CITLY-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P69330|protein.P69330]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:ACPSUB-CPLX`
- `QSPROTEOME:QS00049358`

## Notes

6*protein.P69330
