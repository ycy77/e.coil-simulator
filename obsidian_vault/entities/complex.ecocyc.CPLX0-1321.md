---
entity_id: "complex.ecocyc.CPLX0-1321"
entity_type: "complex"
name: "HflK-HflC complex; regulator of FtsH protease"
source_database: "EcoCyc"
source_id: "CPLX0-1321"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "HflA"
---

# HflK-HflC complex; regulator of FtsH protease

`complex.ecocyc.CPLX0-1321`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1321`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0ABC7|protein.P0ABC7]], [[protein.P0ABC3|protein.P0ABC3]]

## Enriched Summary

The HflK-HflC (HflKC) complex interacts with the ATP-dependent protease EG11506-MONOMER "FtsH", regulating the latter's degradation of different substrate proteins such as SecY and the lambda cII protein . HflKC may act as an FtsH specificity factor . HflK and HflC are inner membrane proteins, each containing a single N-terminal transmembrane domain and a large C-terminal domain which is exposed to the periplasm . Both uncomplexed subunits are unstable , but the HflC-HflK complex is stable . The HflKC complex functions in regulation of the EG11367 BarA/EG11140 UvrY two-component signaling system, which mediates adaptive responses to changes in growth stage. The CPLX0-7956 "CsrA regulator", which is present during exponential phase, binds to the EG10436 mRNA and inhibits its translation. Upon the onset of stationary phase, when CsrA concentration drops, expression of EG10436 increases significantly. In addition, the HflKC complex, which is located in discrete foci on cell poles or on the septum region of the cells , interacts with the CPLX0-8302 during the stationary phase, recruiting it to the cell poles and silencing its kinase activity...

## Biological Role

Component of FtsH/HflKC protease complex (complex.ecocyc.CPLX0-2982).

## Annotation

The HflK-HflC (HflKC) complex interacts with the ATP-dependent protease EG11506-MONOMER "FtsH", regulating the latter's degradation of different substrate proteins such as SecY and the lambda cII protein . HflKC may act as an FtsH specificity factor . HflK and HflC are inner membrane proteins, each containing a single N-terminal transmembrane domain and a large C-terminal domain which is exposed to the periplasm . Both uncomplexed subunits are unstable , but the HflC-HflK complex is stable . The HflKC complex functions in regulation of the EG11367 BarA/EG11140 UvrY two-component signaling system, which mediates adaptive responses to changes in growth stage. The CPLX0-7956 "CsrA regulator", which is present during exponential phase, binds to the EG10436 mRNA and inhibits its translation. Upon the onset of stationary phase, when CsrA concentration drops, expression of EG10436 increases significantly. In addition, the HflKC complex, which is located in discrete foci on cell poles or on the septum region of the cells , interacts with the CPLX0-8302 during the stationary phase, recruiting it to the cell poles and silencing its kinase activity . The HflK-HflC complex is important for growth under high aeration; a ΔhflkΔhflC strain has a specific aeration- and medium-dependent growth defect that is associated with reduced levels of the NONMEVIPP-PWY pathway enzyme EG10370-MONOMER IspG . HflK and HflC are prokaryotic members of the stomatin, prohibitin, flotillin, and HflK/C (SPFH) protein superfamily ; SPFH domain proteins localize in eukaryotic lipid rafts and the function and localization of E. coli SPFH proteins, including HflK/C has been investigated . Historically, the hflKC genes were described as part of the hflA class of E. coli mutations which cause high frequency of

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-2982|complex.ecocyc.CPLX0-2982]] `EcoCyc` `database` - EcoCyc component coefficient=6

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P0ABC3|protein.P0ABC3]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0ABC7|protein.P0ABC7]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-1321`
- `PDB:7WI3`
- `PDB:7VHQ`
- `PDB:7VHP`
- `QSPROTEOME:QS00049409`

## Notes

1*protein.P0ABC7|1*protein.P0ABC3
