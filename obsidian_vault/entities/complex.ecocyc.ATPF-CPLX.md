---
entity_id: "complex.ecocyc.ATPF-CPLX"
entity_type: "complex"
name: "ATP synthase Fo complex - subunit b"
source_database: "EcoCyc"
source_id: "ATPF-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# ATP synthase Fo complex - subunit b

`complex.ecocyc.ATPF-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ATPF-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0ABA0|protein.P0ABA0]]

## Enriched Summary

The b subunit complex is involved in binding the F1 complex to the Fo complex and is necessary for the assembly of the Fo complex. Most of the subunit complex is exposed to the cytoplasm with only the short hydrophobic amino terminus embedded in the membrane . Results from cross-linking studies and molecular modeling suggest that this subunit can stably exist as a left-handed coiled coil although results from other studies have not supported this . A chimera approach has been used to investigate the tolerance of regions of the ATP synthase stator stalk to change, providing insight into the structural and sequential requirements for the function of this subunit . Small-angle X-ray scattering (SAXS) has determined the structure of the soluble domain of this subunit (b22-156) to low resolution . Fluorescence correlation spectroscopy (FCS) titration experiments have allowed assignment of the segments involved in δ–b assembly . The b subunit complex is involved in binding the F1 complex to the Fo complex and is necessary for the assembly of the Fo complex. Most of the subunit complex is exposed to the cytoplasm with only the short hydrophobic amino terminus embedded in the membrane . Results from cross-linking studies and molecular modeling suggest that this subunit can stably exist as a left-handed coiled coil although results from other studies have not supported this...

## Biological Role

Component of ATP synthase Fo complex (complex.ecocyc.F-O-CPLX).

## Annotation

The b subunit complex is involved in binding the F1 complex to the Fo complex and is necessary for the assembly of the Fo complex. Most of the subunit complex is exposed to the cytoplasm with only the short hydrophobic amino terminus embedded in the membrane . Results from cross-linking studies and molecular modeling suggest that this subunit can stably exist as a left-handed coiled coil although results from other studies have not supported this . A chimera approach has been used to investigate the tolerance of regions of the ATP synthase stator stalk to change, providing insight into the structural and sequential requirements for the function of this subunit . Small-angle X-ray scattering (SAXS) has determined the structure of the soluble domain of this subunit (b22-156) to low resolution . Fluorescence correlation spectroscopy (FCS) titration experiments have allowed assignment of the segments involved in δ–b assembly .

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.F-O-CPLX|complex.ecocyc.F-O-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0ABA0|protein.P0ABA0]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:ATPF-CPLX`
- `QSPROTEOME:QS00049576`

## Notes

2*protein.P0ABA0
