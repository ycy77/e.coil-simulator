---
entity_id: "complex.ecocyc.CPLX0-1721"
entity_type: "complex"
name: "copper/silver export system"
source_database: "EcoCyc"
source_id: "CPLX0-1721"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "CusCFBA"
---

# copper/silver export system

`complex.ecocyc.CPLX0-1721`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-1721`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P77211|protein.P77211]], [[protein.P77239|protein.P77239]], [[protein.P77214|protein.P77214]], [[protein.P38054|protein.P38054]]

## Enriched Summary

The cusCFBA operon in E. coli K-12 encodes proteins that function together as a copper/silver efflux system. CusCBA is a tripartite complex that spans both the inner and outer membrane and, along with the periplasmic chaperone CusF, functions to export copper and silver ions from both the the cytoplasm and the periplasm to the extracellular environment. CusC forms a channel in the outer membrane, CusB is a member of the membrane fusion protein (MFP) family and CusA is a resistance-nodulation-division (RND) permease. CusF is the periplasmic copper binding protein . Through its efflux function, CusCFBA helps to protect E. coli K-12 from high levels of exogenous copper and silver however its primary physiological role may be to export endogenous copper(I) ions that accumulate in the periplasm under anaerobic amino acid limitation (a host-relevant environment). Free Cu(I) accumulates in the periplasmic space of E. coli grown under anaerobic amino acid limitation largely due to lack of methionine which is the principal intracellular Cu(I) chelator, although anaerobiosis will also favor the accumulation of Cu(I) over Cu(II). ΔcopA and/or ΔcusC mutants show compromised growth during fumarate respiration under anaerobic and amino acid-limited conditions possibly due to Cu(I) induced damage to the Fe-S clusters of fumarate reductase...

## Biological Role

Catalyzes Ag+ export (reaction.ecocyc.TRANS-RXN-90), Cu+ export (reaction.ecocyc.TRANS-RXN0-280). Transports Ag2+ (molecule.ecocyc.CPD-1486), Cu+ (molecule.ecocyc.CU_), hν (molecule.ecocyc.Light).

## Annotation

The cusCFBA operon in E. coli K-12 encodes proteins that function together as a copper/silver efflux system. CusCBA is a tripartite complex that spans both the inner and outer membrane and, along with the periplasmic chaperone CusF, functions to export copper and silver ions from both the the cytoplasm and the periplasm to the extracellular environment. CusC forms a channel in the outer membrane, CusB is a member of the membrane fusion protein (MFP) family and CusA is a resistance-nodulation-division (RND) permease. CusF is the periplasmic copper binding protein . Through its efflux function, CusCFBA helps to protect E. coli K-12 from high levels of exogenous copper and silver however its primary physiological role may be to export endogenous copper(I) ions that accumulate in the periplasm under anaerobic amino acid limitation (a host-relevant environment). Free Cu(I) accumulates in the periplasmic space of E. coli grown under anaerobic amino acid limitation largely due to lack of methionine which is the principal intracellular Cu(I) chelator, although anaerobiosis will also favor the accumulation of Cu(I) over Cu(II). ΔcopA and/or ΔcusC mutants show compromised growth during fumarate respiration under anaerobic and amino acid-limited conditions possibly due to Cu(I) induced damage to the Fe-S clusters of fumarate reductase . A co-crystal structure of the CusBA complex has been resolved at 2.9Å. The trimeric CusA permease directly contacts with 6 CusB molecules which form a hexameric funnel-like structure . Crystal structures of CusBA in complex with copper(I) are also available . Copper and silver extrusion through CusCFBA is dependent upon the proton-motive-force . Selectable silver resistance is mediated by the CusCFBA system . An in-frame chromosomal deletion mutant

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-90|reaction.ecocyc.TRANS-RXN-90]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-280|reaction.ecocyc.TRANS-RXN0-280]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD-1486|molecule.ecocyc.CPD-1486]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CU|molecule.ecocyc.CU_]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[protein.P38054|protein.P38054]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` <-- [[protein.P77211|protein.P77211]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` <-- [[protein.P77214|protein.P77214]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P77239|protein.P77239]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6 | EcoCyc transporter component coefficient=6

## External IDs

- `EcoCyc:CPLX0-1721`
- `PDB:3NE5`

## Notes

3*protein.P77211|6*protein.P77239|1*protein.P77214|3*protein.P38054
