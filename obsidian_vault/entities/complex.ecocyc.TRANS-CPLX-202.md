---
entity_id: "complex.ecocyc.TRANS-CPLX-202"
entity_type: "complex"
name: "multidrug efflux pump MdtABC-TolC"
source_database: "EcoCyc"
source_id: "TRANS-CPLX-202"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# multidrug efflux pump MdtABC-TolC

`complex.ecocyc.TRANS-CPLX-202`

## Static

- Type: `complex`
- Source: `EcoCyc:TRANS-CPLX-202`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CPLX0-7964|complex.ecocyc.CPLX0-7964]], [[protein.P76399|protein.P76399]], [[protein.P76398|protein.P76398]], [[protein.P76397|protein.P76397]]

## Enriched Summary

MdtABC-TolC is a tripartite efflux system that is implicated in resistance to antibiotics, bile salt derivatives and SDS. The system consists of a heterotrimeric RND (resistance-nodulation-division)-type permease MdtAB, a membrane fusion protein MdtA and an outer membrane channel, TolC. Overexpression of mdtABCD (and separately of mdtABC) in a strain lacking the major multidrug efflux system AcrAB confers increased resistance to deoxycholate, cholate, taurocholate, novobiocin, nalidixic acid, norfloxacin, fosfomycin and SDS but does not impact resistance to a range of other antibiotics and toxic compounds . An E. coli W3110 ΔmdtABC::Kmr strain shows no alteration in susceptibility to a broad range of 35 toxic compounds including antibiotics, dyes, antiseptics and detergents indicating that MdtABC does not contribute to intrinsic resistance for these compounds . MdtABC requires the outer membrane channel TolC for its efflux function; MdtABC contains a unique heteromultimer-type permease (MdtBC); overexpression of mdtA and mdtC confers increased resistance to bile salt derivatives but not to SDS or novobiocin suggesting that in the absence of MdtB, the heteromultimeric permease may be replaced by an MdtC homomultimer of narrower drug specificity...

## Biological Role

Catalyzes deoxycholate export (reaction.ecocyc.TRANS-RXN-352), novobiocin export (reaction.ecocyc.TRANS-RXN-353), dodecyl sulfate export (reaction.ecocyc.TRANS-RXN-92). Transports Novobiocin (molecule.C05080), dodecyl sulfate (molecule.ecocyc.CPD-8876), hν (molecule.ecocyc.Light).

## Annotation

MdtABC-TolC is a tripartite efflux system that is implicated in resistance to antibiotics, bile salt derivatives and SDS. The system consists of a heterotrimeric RND (resistance-nodulation-division)-type permease MdtAB, a membrane fusion protein MdtA and an outer membrane channel, TolC. Overexpression of mdtABCD (and separately of mdtABC) in a strain lacking the major multidrug efflux system AcrAB confers increased resistance to deoxycholate, cholate, taurocholate, novobiocin, nalidixic acid, norfloxacin, fosfomycin and SDS but does not impact resistance to a range of other antibiotics and toxic compounds . An E. coli W3110 ΔmdtABC::Kmr strain shows no alteration in susceptibility to a broad range of 35 toxic compounds including antibiotics, dyes, antiseptics and detergents indicating that MdtABC does not contribute to intrinsic resistance for these compounds . MdtABC requires the outer membrane channel TolC for its efflux function; MdtABC contains a unique heteromultimer-type permease (MdtBC); overexpression of mdtA and mdtC confers increased resistance to bile salt derivatives but not to SDS or novobiocin suggesting that in the absence of MdtB, the heteromultimeric permease may be replaced by an MdtC homomultimer of narrower drug specificity . Purified, active trimers contain MdtB and MdtC in a 2:1 ratio ; mutagenesis assays and modeling suggests these subunits have different functional roles within the permease and that the complex is unlikely to function using a similar mechanism to that proposed for homotrimeric RND type transporters . mdtA, mdtB and mdtC form an operon with the downstream genes mdtD, baeS and baeR; mdtABCD-baeSR is directly regulated by the PWY0-1481 "BaeSR two component system" . Related reviews:

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-352|reaction.ecocyc.TRANS-RXN-352]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-353|reaction.ecocyc.TRANS-RXN-353]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-92|reaction.ecocyc.TRANS-RXN-92]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C05080|molecule.C05080]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-8876|molecule.ecocyc.CPD-8876]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (5)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-7964|complex.ecocyc.CPLX0-7964]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P02930|protein.P02930]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` <-- [[protein.P76397|protein.P76397]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P76398|protein.P76398]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P76399|protein.P76399]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:TRANS-CPLX-202`
- `QSPROTEOME:QS00182949`

## Notes

1*complex.ecocyc.CPLX0-7964|1*protein.P76399|2*protein.P76398|1*protein.P76397
