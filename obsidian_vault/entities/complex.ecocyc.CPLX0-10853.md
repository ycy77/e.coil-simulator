---
entity_id: "complex.ecocyc.CPLX0-10853"
entity_type: "complex"
name: "SoxR [2Fe-2S] reducing system"
source_database: "EcoCyc"
source_id: "CPLX0-10853"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# SoxR [2Fe-2S] reducing system

`complex.ecocyc.CPLX0-10853`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-10853`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P0AB85|protein.P0AB85]], [[protein.P46187|protein.P46187]], [[complex.ecocyc.CPLX0-10852|complex.ecocyc.CPLX0-10852]]

## Enriched Summary

Products of the rsxABCDGE cluster and G7347 rseC are implicated in a pathway that functions to reduce the PD04132 SoxR iron-sulfur cluster; in-frame deletion of any gene within the cluster results in SoxR-mediated constitutive activation of EG10958 soxS transcription in the absence of oxidative stress . SoxR exists in a more oxidized form in rsx and rseC mutants . The periplasmic flavin transferase EG12073-MONOMER ApbE (renamed Ftp ) is also a component of this system; the RsxABCDGE, RseC and AbpE proteins likely form a complex that uses NAD(P)H to reduce SoxR . The rsxABCDGE gene cluster has similarity to the TAX-1061 rnf cluster (rnfABCDGEH ), which plays a role in nitrogenase reduction (see further ). Proton-motive force (PMF) driven Rnf complexes are one mechanism by which diazotrophs can maintain reduced ferredoxin production from NAD(P)H (see ); the Rsx complex of E. coli may couple periplasmic redox signals to ion transport and reduction of the SoxR iron-sulfur cluster . Products of the rsxABCDGE cluster and G7347 rseC are implicated in a pathway that functions to reduce the PD04132 SoxR iron-sulfur cluster; in-frame deletion of any gene within the cluster results in SoxR-mediated constitutive activation of EG10958 soxS transcription in the absence of oxidative stress . SoxR exists in a more oxidized form in rsx and rseC mutants...

## Biological Role

Catalyzes RXN0-7453 (reaction.ecocyc.RXN0-7453). Bound by FMN (molecule.C00061), a [2Fe-2S] iron-sulfur cluster (molecule.ecocyc.CPD-6), a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

Products of the rsxABCDGE cluster and G7347 rseC are implicated in a pathway that functions to reduce the PD04132 SoxR iron-sulfur cluster; in-frame deletion of any gene within the cluster results in SoxR-mediated constitutive activation of EG10958 soxS transcription in the absence of oxidative stress . SoxR exists in a more oxidized form in rsx and rseC mutants . The periplasmic flavin transferase EG12073-MONOMER ApbE (renamed Ftp ) is also a component of this system; the RsxABCDGE, RseC and AbpE proteins likely form a complex that uses NAD(P)H to reduce SoxR . The rsxABCDGE gene cluster has similarity to the TAX-1061 rnf cluster (rnfABCDGEH ), which plays a role in nitrogenase reduction (see further ). Proton-motive force (PMF) driven Rnf complexes are one mechanism by which diazotrophs can maintain reduced ferredoxin production from NAD(P)H (see ); the Rsx complex of E. coli may couple periplasmic redox signals to ion transport and reduction of the SoxR iron-sulfur cluster .

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7453|reaction.ecocyc.RXN0-7453]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (12)

- `binds` <-- [[molecule.C00061|molecule.C00061]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-6|molecule.ecocyc.CPD-6]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[complex.ecocyc.CPLX0-10852|complex.ecocyc.CPLX0-10852]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P0A766|protein.P0A766]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P0AB85|protein.P0AB85]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P46187|protein.P46187]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P76182|protein.P76182]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P77179|protein.P77179]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P77223|protein.P77223]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P77285|protein.P77285]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` <-- [[protein.P77611|protein.P77611]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1

## External IDs

- `EcoCyc:CPLX0-10853`
- `QSPROTEOME:QS00196437`

## Notes

protein.P0AB85|protein.P46187|complex.ecocyc.CPLX0-10852
