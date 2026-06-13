---
entity_id: "complex.ecocyc.TRANS-200-CPLX"
entity_type: "complex"
name: "ABC-type tripartite efflux pump"
source_database: "EcoCyc"
source_id: "TRANS-200-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "MacAB-TolC"
  - "macrolide ABC exporter"
---

# ABC-type tripartite efflux pump

`complex.ecocyc.TRANS-200-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:TRANS-200-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CPLX0-7964|complex.ecocyc.CPLX0-7964]], [[protein.P75831|protein.P75831]], [[protein.P75830|protein.P75830]]

## Enriched Summary

MacAB-TolC is an ABC-type tripartite efflux transporter. In E. coli K-12 drug hypersensitive strains, the MacAB-TolC complex confers a significant protective effect against macrolide antibiotics such as erythromycin and cyclic peptide antibiotics such as bacitracin and colistin; MacAB-TolC has been implicated in export of the heme precursor, PROTOPORPHYRIN_IX (PPIX) and suggested to export rough-LPS or similar glycolipids. The macAB genes form an operon with a single promoter; sequence analysis suggests that MacA is a peripheral membrane protein of the MFP (membrane fusion protein) family and MacB is a half-type ABC protein with four putative TM segments and one nucleotide-binding cassette . Multicopy expression of macAB in an E. coli strain lacking the major drug efflux system AcrAB, confers erythromycin specific resistance; similar macAB mediated resistance was found to other macrolides with 14-and 15- membered rings, though not for 16-membered lactones . macAB mediated macrolide resistance is dependent on the outer membrane channel TolC . MacAB mediates secretion of heat-stable enterotoxin STII in E. coli strains engineered to produce STII . Multicopy expression of macAB in an E. coli strain lacking the major drug efflux system AcrAB confers increased resistance to colistin and bacitracin...

## Biological Role

Catalyzes TRANS-RXN-377 (reaction.ecocyc.TRANS-RXN-377), TRANS-RXN-378 (reaction.ecocyc.TRANS-RXN-378), TRANS-RXN0-224 (reaction.ecocyc.TRANS-RXN0-224). Transports Bacitracin (molecule.C01667), hν (molecule.ecocyc.Light), a macrolide antibiotic (molecule.ecocyc.Macrolide-Antibiotics), a polymyxin (molecule.ecocyc.Polymyxins).

## Annotation

MacAB-TolC is an ABC-type tripartite efflux transporter. In E. coli K-12 drug hypersensitive strains, the MacAB-TolC complex confers a significant protective effect against macrolide antibiotics such as erythromycin and cyclic peptide antibiotics such as bacitracin and colistin; MacAB-TolC has been implicated in export of the heme precursor, PROTOPORPHYRIN_IX (PPIX) and suggested to export rough-LPS or similar glycolipids. The macAB genes form an operon with a single promoter; sequence analysis suggests that MacA is a peripheral membrane protein of the MFP (membrane fusion protein) family and MacB is a half-type ABC protein with four putative TM segments and one nucleotide-binding cassette . Multicopy expression of macAB in an E. coli strain lacking the major drug efflux system AcrAB, confers erythromycin specific resistance; similar macAB mediated resistance was found to other macrolides with 14-and 15- membered rings, though not for 16-membered lactones . macAB mediated macrolide resistance is dependent on the outer membrane channel TolC . MacAB mediates secretion of heat-stable enterotoxin STII in E. coli strains engineered to produce STII . Multicopy expression of macAB in an E. coli strain lacking the major drug efflux system AcrAB confers increased resistance to colistin and bacitracin . Overproduction of PPIX interferes with MacAB-dependent antibiotic efflux; tolC and macAB null mutants accumulate more PPIX than the isogenic parental strain when G7266-MONOMER "YfeX" is induced or when intracellular iron is limiting; PPIX may be the endogenous substrate of the MacAB-TolC efflux pump Cryo-EM structures of stabilized MacAB-TolC complexes have been reported; the structures, which are functionally active for drug efflux, have a MacA:MacB:TolC ratio of 6:2:3 . Related

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-377|reaction.ecocyc.TRANS-RXN-377]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-378|reaction.ecocyc.TRANS-RXN-378]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-224|reaction.ecocyc.TRANS-RXN0-224]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C01667|molecule.C01667]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Macrolide-Antibiotics|molecule.ecocyc.Macrolide-Antibiotics]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Polymyxins|molecule.ecocyc.Polymyxins]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-7964|complex.ecocyc.CPLX0-7964]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P02930|protein.P02930]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` <-- [[protein.P75830|protein.P75830]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6 | EcoCyc transporter component coefficient=6
- `is_component_of` <-- [[protein.P75831|protein.P75831]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:TRANS-200-CPLX`
- `PDB:5NIL`
- `PDB:5NIK`
- `PDB:5NIK`
- `PDB:5NIL`
- `QSPROTEOME:QS00143533`

## Notes

1*complex.ecocyc.CPLX0-7964|2*protein.P75831|6*protein.P75830
