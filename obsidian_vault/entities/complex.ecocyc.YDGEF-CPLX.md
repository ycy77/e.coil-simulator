---
entity_id: "complex.ecocyc.YDGEF-CPLX"
entity_type: "complex"
name: "multidrug/spermidine efflux pump"
source_database: "EcoCyc"
source_id: "YDGEF-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "MdtJI spermidine SMR transporter"
---

# multidrug/spermidine efflux pump

`complex.ecocyc.YDGEF-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:YDGEF-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P69212|protein.P69212]], [[protein.P69210|protein.P69210]]

## Enriched Summary

mdtJ and mdtI encode two components of a multidrug / spermidine / deoxycholate efflux transporter. Overexpression of mdtJI in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) confers increased resistance to deoxycholate (4-fold), nalidixic acid (2-fold), fosfomycin (2-fold), and SDS (2-fold) but does not impact resistance to a range of other antibiotics and toxic compounds (see also ). Expression of mdtJI (from a low-copy-number vector) in a strain lacking spermidine acetyltransferase increases cell viability when cultures are grown in the presence of 12mM spermidine; MdtJI enhances cell viability and growth through excretion of spermidine when spermidine over-accumulates in cells; both proteins are required for rescue . MdtJ and MdtI are homologous integral membrane proteins; the C-terminus of MdtI is locted in the periplasm while the C-terminus of MdtJ is located in the cytoplasm and they are predicted to form antiparallel heterodimers or higher oligomers in vivo . A parallel arrangement of the subunits has also been postulated . MdtI is predicted to contain 4 transmembrane segments; the N- and C-terminus are located in the periplasm . MdtJ and MdtI belong to the 4 Transmembrane (TM) Small Multidrug Resistance (SMR) Family within the Drug/Metabolite Transporter (DMT) Superfamily...

## Biological Role

Catalyzes nalidixate:proton antiport (reaction.ecocyc.TRANS-RXN-350), spermidine:proton antiport (reaction.ecocyc.TRANS-RXN0-266). Transports Spermidine (molecule.C00315), nalidixic acid (molecule.ecocyc.CPD-21025), hν (molecule.ecocyc.Light).

## Annotation

mdtJ and mdtI encode two components of a multidrug / spermidine / deoxycholate efflux transporter. Overexpression of mdtJI in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) confers increased resistance to deoxycholate (4-fold), nalidixic acid (2-fold), fosfomycin (2-fold), and SDS (2-fold) but does not impact resistance to a range of other antibiotics and toxic compounds (see also ). Expression of mdtJI (from a low-copy-number vector) in a strain lacking spermidine acetyltransferase increases cell viability when cultures are grown in the presence of 12mM spermidine; MdtJI enhances cell viability and growth through excretion of spermidine when spermidine over-accumulates in cells; both proteins are required for rescue . MdtJ and MdtI are homologous integral membrane proteins; the C-terminus of MdtI is locted in the periplasm while the C-terminus of MdtJ is located in the cytoplasm and they are predicted to form antiparallel heterodimers or higher oligomers in vivo . A parallel arrangement of the subunits has also been postulated . MdtI is predicted to contain 4 transmembrane segments; the N- and C-terminus are located in the periplasm . MdtJ and MdtI belong to the 4 Transmembrane (TM) Small Multidrug Resistance (SMR) Family within the Drug/Metabolite Transporter (DMT) Superfamily . Expression of chromosomal mdtJI is very low in both the presence and absence of spermidine . Expression of mdtJ increases upon exposure of wild-type E. coli strain CF1943 (W3110) to puromycin , during growth in L-idonate , during growth at pH 5.7 or 7.0 compared to 8.5 , and is growth-phase independent in complex media . Expression of mdtJI is increased in a strain lacking PD00288 "H-NS" . EG12116-MONOMER AcrR directly regulates expression of the MdtJI efflu

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-350|reaction.ecocyc.TRANS-RXN-350]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-266|reaction.ecocyc.TRANS-RXN0-266]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00315|molecule.C00315]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-21025|molecule.ecocyc.CPD-21025]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (2)

- `is_component_of` <-- [[protein.P69210|protein.P69210]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P69212|protein.P69212]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:YDGEF-CPLX`
- `QSPROTEOME:QS00049534`

## Notes

protein.P69212|protein.P69210
