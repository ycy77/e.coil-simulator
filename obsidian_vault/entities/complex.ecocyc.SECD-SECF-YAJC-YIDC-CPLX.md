---
entity_id: "complex.ecocyc.SECD-SECF-YAJC-YIDC-CPLX"
entity_type: "complex"
name: "Sec translocon accessory complex"
source_database: "EcoCyc"
source_id: "SECD-SECF-YAJC-YIDC-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# Sec translocon accessory complex

`complex.ecocyc.SECD-SECF-YAJC-YIDC-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:SECD-SECF-YAJC-YIDC-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AG90|protein.P0AG90]], [[protein.P0AG93|protein.P0AG93]], [[protein.P0ADZ7|protein.P0ADZ7]]

## Enriched Summary

SecD, SecF and YajC form the Sec translocon accessory complex which is implicated in Sec-dependent translocation pathways. A SecDF-YajC complex can be detected in the solubilized membranes from an over-producing strain . The SecDF-YajC complex, purified from an overproducing strain, also contains YIDC "YidC" . SecDF-YajC stabilizes the CPLX0-8089 "SecA" insertion complex in vitro and inhibits movement of a SecA bound protein precursor in either direction (see also ). SecDF is required for the later, ATP-independent steps of protein translocation driven by the proton motive force (PMF); SecDF comprises 12 transmembrane helices that form the proton-conducting channel, and 3 periplasmic domains (see also ). The periplasmic domains of SecDF mediate the recruitment of the CPLX0-3933 Bam complex to facilitate delivery of outer membrane proteins (OMPs) to the outer membrane; the proton-conducting activity of SecDF, which is not required for SecA-mediated OMP translocation into inner membrane vesicles in vitro, is required for efficient OMP maturation in vivo . SecD, SecF and YajC form the Sec translocon accessory complex which is implicated in Sec-dependent translocation pathways. A SecDF-YajC complex can be detected in the solubilized membranes from an over-producing strain . The SecDF-YajC complex, purified from an overproducing strain, also contains YIDC "YidC"...

## Biological Role

Component of Sec Holo-Translocon (complex.ecocyc.SEC-SECRETION-CPLX).

## Annotation

SecD, SecF and YajC form the Sec translocon accessory complex which is implicated in Sec-dependent translocation pathways. A SecDF-YajC complex can be detected in the solubilized membranes from an over-producing strain . The SecDF-YajC complex, purified from an overproducing strain, also contains YIDC "YidC" . SecDF-YajC stabilizes the CPLX0-8089 "SecA" insertion complex in vitro and inhibits movement of a SecA bound protein precursor in either direction (see also ). SecDF is required for the later, ATP-independent steps of protein translocation driven by the proton motive force (PMF); SecDF comprises 12 transmembrane helices that form the proton-conducting channel, and 3 periplasmic domains (see also ). The periplasmic domains of SecDF mediate the recruitment of the CPLX0-3933 Bam complex to facilitate delivery of outer membrane proteins (OMPs) to the outer membrane; the proton-conducting activity of SecDF, which is not required for SecA-mediated OMP translocation into inner membrane vesicles in vitro, is required for efficient OMP maturation in vivo .

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.SEC-SECRETION-CPLX|complex.ecocyc.SEC-SECRETION-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P0ADZ7|protein.P0ADZ7]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AG90|protein.P0AG90]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AG93|protein.P0AG93]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:SECD-SECF-YAJC-YIDC-CPLX`
- `PDB:5MG3`
- `QSPROTEOME:QS00049526`

## Notes

protein.P0AG90|protein.P0AG93|protein.P0ADZ7
