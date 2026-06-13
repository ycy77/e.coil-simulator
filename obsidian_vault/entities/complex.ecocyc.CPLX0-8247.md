---
entity_id: "complex.ecocyc.CPLX0-8247"
entity_type: "complex"
name: "uracil transporter UraA"
source_database: "EcoCyc"
source_id: "CPLX0-8247"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# uracil transporter UraA

`complex.ecocyc.CPLX0-8247`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8247`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AGM7|protein.P0AGM7]]

## Enriched Summary

UraA is a high affinity uracil transporter that operates as a proton-coupled symporter or possibly a uniporter . In the Transporter Classifcation Database UraA is a member of the NCS2 family of nucleobase:cation symporters. A uraA transposon mutant is defective for uracil uptake but cytosine uptake is not affected; expression of cloned uraA partially complements the uracil uptake defect . Disruption of uraA in a pyrimidine-requiring strain results in a growth defect at low exogenous uracil concentration (9 µM) but not at high uracil concentration (90 µM) uraA forms an operon with upp encoding URACIL-PRIBOSYLTRANS-CPLX . Deletion of upp prevents the uptake of uracil by UraA and by B1006-MONOMER RutG; UPRT activity is rate-limiting for transport by UraA; UPRT activity maintains an inwardly directed electrochemical gradient that sustains UraA-mediated facilitated diffusion of uracil in vivo . Crystal structures of uracil-bound UraA, purified from E. coli O157:H7, in both an inward open and occluded conformation are available . uraA from this strain is identical to E. coli K-12 uraA. UraA contains 14 transmembrane (TM) regions arranged into 2 structural repeats identified as a 'core' domain (TMs 1-4 and 8-11) and a 'gate' domain (TMs 5-7 and 12-14)...

## Biological Role

Catalyzes uracil:proton symport (reaction.ecocyc.TRANS-RXN-132).

## Annotation

UraA is a high affinity uracil transporter that operates as a proton-coupled symporter or possibly a uniporter . In the Transporter Classifcation Database UraA is a member of the NCS2 family of nucleobase:cation symporters. A uraA transposon mutant is defective for uracil uptake but cytosine uptake is not affected; expression of cloned uraA partially complements the uracil uptake defect . Disruption of uraA in a pyrimidine-requiring strain results in a growth defect at low exogenous uracil concentration (9 µM) but not at high uracil concentration (90 µM) uraA forms an operon with upp encoding URACIL-PRIBOSYLTRANS-CPLX . Deletion of upp prevents the uptake of uracil by UraA and by B1006-MONOMER RutG; UPRT activity is rate-limiting for transport by UraA; UPRT activity maintains an inwardly directed electrochemical gradient that sustains UraA-mediated facilitated diffusion of uracil in vivo . Crystal structures of uracil-bound UraA, purified from E. coli O157:H7, in both an inward open and occluded conformation are available . uraA from this strain is identical to E. coli K-12 uraA. UraA contains 14 transmembrane (TM) regions arranged into 2 structural repeats identified as a 'core' domain (TMs 1-4 and 8-11) and a 'gate' domain (TMs 5-7 and 12-14) . UraA may exist in a monomer/dimer equilibrium but a dimer is the functional form for uracil transport; UraA dimerization is mediated through the gate domain; a UraA dimer in which one protomer contains a loss of function mutation is able to mediate uracil uptake in vivo .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-132|reaction.ecocyc.TRANS-RXN-132]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P0AGM7|protein.P0AGM7]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8247`
- `QSPROTEOME:QS00157635`
- `PDB:5XLS`

## Notes

2*protein.P0AGM7
