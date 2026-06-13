---
entity_id: "complex.ecocyc.PII2-CPLX"
entity_type: "complex"
name: "nitrogen regulatory protein PII-2"
source_database: "EcoCyc"
source_id: "PII2-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "PII-2"
  - "nitrogen regulatory protein GlnK"
---

# nitrogen regulatory protein PII-2

`complex.ecocyc.PII2-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:PII2-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AC55|protein.P0AC55]]

## Enriched Summary

The PII proteins play a critical role in the regulation of nitrogen metabolism by controlling the activity of GLUTAMINESYN-OLIGOMER (GS). The main PI protein of E. coli is encoded by the EG10384 gene. However, E. coli possesses a second PII protein encoded by glnK. PII-2, like PIIPROTEIN-CPLX PII-1, can activate the adenylylation of glutamine synthetase in vitro. PII-1 can be modified by the covalent attachment of UMP to tyrosine 51 of each monomer to form uridylylated PII-1 (PII-1-UMP), and PII-2 is uridylylated in vivo as well. In contrast to PII-1, the expression of glnK is regulated by the nitrogen status of the cell in a NtrC (NRI) dependent manner (see also ). GlnK affects viability under conditions of nitrogen starvation and is required for recovery from nitrogen starvation . GlnK and PII-1 are functionally equivalent, but distinct regulation of the genes encoding these products elicits distinct physiological effects . GlnK and AmtB have been shown to directly interact after ammonium shock. This reversible sequestration of GlnK by AmtB is rapidly responsive to μM concentrations of ammonium. The deuridylylated form of GlnK has been shown to be sequestered by AmtB and to inhibit transport of ammonium by AmtB. Deletion or mutation of amtB was shown to prevent deuridylylation of GlnK...

## Annotation

The PII proteins play a critical role in the regulation of nitrogen metabolism by controlling the activity of GLUTAMINESYN-OLIGOMER (GS). The main PI protein of E. coli is encoded by the EG10384 gene. However, E. coli possesses a second PII protein encoded by glnK. PII-2, like PIIPROTEIN-CPLX PII-1, can activate the adenylylation of glutamine synthetase in vitro. PII-1 can be modified by the covalent attachment of UMP to tyrosine 51 of each monomer to form uridylylated PII-1 (PII-1-UMP), and PII-2 is uridylylated in vivo as well. In contrast to PII-1, the expression of glnK is regulated by the nitrogen status of the cell in a NtrC (NRI) dependent manner (see also ). GlnK affects viability under conditions of nitrogen starvation and is required for recovery from nitrogen starvation . GlnK and PII-1 are functionally equivalent, but distinct regulation of the genes encoding these products elicits distinct physiological effects . GlnK and AmtB have been shown to directly interact after ammonium shock. This reversible sequestration of GlnK by AmtB is rapidly responsive to μM concentrations of ammonium. The deuridylylated form of GlnK has been shown to be sequestered by AmtB and to inhibit transport of ammonium by AmtB. Deletion or mutation of amtB was shown to prevent deuridylylation of GlnK. The internal glutamine pool, which is increased upon rapid increases in ammonium availability to nitrogen-limited cells, is responsible for deuridylylation of GlnK due to its interaction with uridylyltransferase . PII-1 and PII-2 can heterotrimerize .

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AC55|protein.P0AC55]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3

## External IDs

- `EcoCyc:PII2-CPLX`
- `QSPROTEOME:QS00168201`

## Notes

3*protein.P0AC55
