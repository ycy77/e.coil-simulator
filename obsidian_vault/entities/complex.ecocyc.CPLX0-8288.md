---
entity_id: "complex.ecocyc.CPLX0-8288"
entity_type: "complex"
name: "sensor histidine kinase CusS"
source_database: "EcoCyc"
source_id: "CPLX0-8288"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# sensor histidine kinase CusS

`complex.ecocyc.CPLX0-8288`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8288`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P77485|protein.P77485]]

## Enriched Summary

CusS is the sensor histidine kinase of the the CusSR two-component system which regulates expression of a CPLX0-1721 in response to elevated copper and silver concentrations (see also and further ). Disruption of cusS results in increased sensitivity to copper(I) and silver(I) - resistance is restored when cusS is expressed from a plasmid (see also ). Disruption of cusS results in Cu(I) accumulation under anaerobic growth conditions . Transcription from the cusCFBA operon is negligible in a cusS deletion strain grown in the presence of Ag(I); CusS is the primary activator for Ag(I) activated expression of the cusCFBA operon . The association and dissociation rates of CusS with Cu(I) in the periplasm have been estimated . CusS contains two transmembrane domains, a periplasmic sensor domain and a catalytic cytoplasmic domain; the purified periplasmic sensor domain (CusS39-187) is a dimer which binds 4 Ag(I) ions - two at the dimer interface and one in each monomer . The periplasmic domain of CusS is required for Cu(I) sensing and Cus-mediated copper resistance under anaereobic conditions . Autophosphorylation of the purifed cytoplasmic domain of CusS and subsequent transfer of the phosphoryl group to its cognate response regulator - the transcription factor CusR, has been demonstrated in vitro...

## Biological Role

Catalyzes 2.7.13.1-RXN (reaction.ecocyc.2.7.13.1-RXN).

## Annotation

CusS is the sensor histidine kinase of the the CusSR two-component system which regulates expression of a CPLX0-1721 in response to elevated copper and silver concentrations (see also and further ). Disruption of cusS results in increased sensitivity to copper(I) and silver(I) - resistance is restored when cusS is expressed from a plasmid (see also ). Disruption of cusS results in Cu(I) accumulation under anaerobic growth conditions . Transcription from the cusCFBA operon is negligible in a cusS deletion strain grown in the presence of Ag(I); CusS is the primary activator for Ag(I) activated expression of the cusCFBA operon . The association and dissociation rates of CusS with Cu(I) in the periplasm have been estimated . CusS contains two transmembrane domains, a periplasmic sensor domain and a catalytic cytoplasmic domain; the purified periplasmic sensor domain (CusS39-187) is a dimer which binds 4 Ag(I) ions - two at the dimer interface and one in each monomer . The periplasmic domain of CusS is required for Cu(I) sensing and Cus-mediated copper resistance under anaereobic conditions . Autophosphorylation of the purifed cytoplasmic domain of CusS and subsequent transfer of the phosphoryl group to its cognate response regulator - the transcription factor CusR, has been demonstrated in vitro . Sensor domain dimerization is driven by Ag(I) ion binding to the interface metal-binding site; CusS autophosphorylates at the pros nitrogen atom (Nδ1) of histidine residue 271 via a cis mechanism (ie. ATP binds to one subunit of the CusS dimer and its γ-phosphate group is transferred to His271 of the same subunit) . In Escherichia coli DH5α, it has been demonstrated that CusS also has phosphatase activity . Rearrangement of helical interactions in the transmembrane domain of CusS

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.13.1-RXN|reaction.ecocyc.2.7.13.1-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P77485|protein.P77485]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8288`
- `QSPROTEOME:QS00197361`

## Notes

2*protein.P77485
