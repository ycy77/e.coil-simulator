---
entity_id: "complex.ecocyc.ABC-5-CPLX"
entity_type: "complex"
name: "vitamin B12 ABC transporter"
source_database: "EcoCyc"
source_id: "ABC-5-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# vitamin B12 ABC transporter

`complex.ecocyc.ABC-5-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:ABC-5-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P06611|protein.P06611]], [[protein.P06609|protein.P06609]], [[protein.P37028|protein.P37028]]

## Enriched Summary

BtuCD-F is a high-affinity vitamin B12 uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. Early studies in E. coli K-12 and B strains using labeled cyanocobalamin and cobinamide cyanide characterized an effective, binding protein dependent uptake system for these compounds and implicated the product of btuC in transport across the inner membrane . Based on sequence analysis btuB and btuC encode the ATP-binding and integral membrane subunit, respectively of the transporter complex; BtuF is the periplasmic cyanocobalamin-binding protein of the system . Strains with null mutations in any of the three genes show impaired utilization of cyanocobalamin in growth assays and are defective for cyanocobalamin transport across the inner membrane; suppressor variants which are able to use cyanocobalamin (in methionine assay plates) arise frequently . Transport of labeled Vitamin B12 into BtuCD containing proteoliposomes is dependent on external BtuF and internal ATP . BtuCD containing proteoliposomes also transport labeled cobinamide (14C-labeled CPD-22316 "cyano-aquo-cob(III)inamide") in an ATP and BtuF dependent manner . Crystal structures of BtuCD and BtuCD-F at medium resolution (3.2 Å and 2.6 Å respectively) are available...

## Biological Role

Catalyzes ABC-5-RXN (reaction.ecocyc.ABC-5-RXN), TRANS-RXN-296 (reaction.ecocyc.TRANS-RXN-296). Transports Cob(I)alamin (molecule.C00853), cob(II)inamide (molecule.ecocyc.CPD-20903), hν (molecule.ecocyc.Light).

## Annotation

BtuCD-F is a high-affinity vitamin B12 uptake system that is a member of the ATP-Binding Cassette (ABC) Superfamily of transporters. Early studies in E. coli K-12 and B strains using labeled cyanocobalamin and cobinamide cyanide characterized an effective, binding protein dependent uptake system for these compounds and implicated the product of btuC in transport across the inner membrane . Based on sequence analysis btuB and btuC encode the ATP-binding and integral membrane subunit, respectively of the transporter complex; BtuF is the periplasmic cyanocobalamin-binding protein of the system . Strains with null mutations in any of the three genes show impaired utilization of cyanocobalamin in growth assays and are defective for cyanocobalamin transport across the inner membrane; suppressor variants which are able to use cyanocobalamin (in methionine assay plates) arise frequently . Transport of labeled Vitamin B12 into BtuCD containing proteoliposomes is dependent on external BtuF and internal ATP . BtuCD containing proteoliposomes also transport labeled cobinamide (14C-labeled CPD-22316 "cyano-aquo-cob(III)inamide") in an ATP and BtuF dependent manner . Crystal structures of BtuCD and BtuCD-F at medium resolution (3.2 Å and 2.6 Å respectively) are available. Structures of disulphide stabilized BtuCD and BtuCD-F in complex with with the non-hydrolysable ATP analogue AMP-PNP have also been reported . Two BtuC subunits are in close contact and provide 20 transmembrane helices that form a translocation pathway wide enough to accomodate a vitamin B12 molecule. A short helical region in each BtuC subunit forms a cytoplasmic loop (the L-loop) which interacts with the BtuD subunits that constitute the nucleotide binding domain. The membrane spanning BtuC subunits form an enclos

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.ABC-5-RXN|reaction.ecocyc.ABC-5-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-296|reaction.ecocyc.TRANS-RXN-296]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00853|molecule.C00853]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-20903|molecule.ecocyc.CPD-20903]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (3)

- `is_component_of` <-- [[protein.P06609|protein.P06609]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P06611|protein.P06611]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2
- `is_component_of` <-- [[protein.P37028|protein.P37028]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:ABC-5-CPLX`
- `PDB:1L7V`
- `PDB:2QI9`
- `PDB:4DBL`
- `PDB:4FI3`
- `PDB:4R9U`
- `PDB:4R9U`
- `PDB:4FI3`
- `PDB:4DBL`
- `QSPROTEOME:QS00093847`

## Notes

2*protein.P06611|2*protein.P06609|1*protein.P37028
