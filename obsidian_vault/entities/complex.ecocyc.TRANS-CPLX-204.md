---
entity_id: "complex.ecocyc.TRANS-CPLX-204"
entity_type: "complex"
name: "multidrug efflux pump MdtEF-TolC"
source_database: "EcoCyc"
source_id: "TRANS-CPLX-204"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# multidrug efflux pump MdtEF-TolC

`complex.ecocyc.TRANS-CPLX-204`

## Static

- Type: `complex`
- Source: `EcoCyc:TRANS-CPLX-204`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CPLX0-7964|complex.ecocyc.CPLX0-7964]], [[protein.P37636|protein.P37636]], [[protein.P37637|protein.P37637]]

## Enriched Summary

MdtEF-TolC is a putative tripartite efflux pump complex; production of the complex (through expression of cloned mdtEF genes) confers some degree of resistance to various toxic compounds in laboratory strains of E. coli K-12. Expression of cloned mdtEF in the K-12 strain KAM3 which lacks AcrB (see ) confers increased resistance to erythromycin, doxorubicin, crystal violet, ethidium bromide, rhodamine 6G, tetraphenylphosphonium (TPP+), benzalkonium, deoxycholate and SDS (compared to the mutant parent) (see also ). Overproduction of MdtEF in the K-12 strain KAM3 confers increased levels of resistance to the antibiotics oxacillin, cloxacillin, nafcillin and erythromycin (compared to the mutant parent) and to deoxycholate, SDS and TPP+ (compared to the mutant parent), MdtEF requires TolC for export function . Deletion of mdtEF in the K-12 strain W3110 does not affect susceptibility to a range of 35 compounds (dyes, detergents, antibiotics and others) . Overexpression of mdtE together with mdtF in E. coli strain HNCE3 (ΔacrA) results in a strong increase in resistance to cholate, taurocholate and erythromycin . MdtEF-TolC is implicated in the efflux of bile acids under extreme acid conditions...

## Biological Role

Catalyzes deoxycholate export (reaction.ecocyc.TRANS-RXN-352), ethidium export (reaction.ecocyc.TRANS-RXN-359), erythromycin export (reaction.ecocyc.TRANS-RXN-367). Transports ethidium (molecule.ecocyc.CPD0-1938), hν (molecule.ecocyc.Light).

## Annotation

MdtEF-TolC is a putative tripartite efflux pump complex; production of the complex (through expression of cloned mdtEF genes) confers some degree of resistance to various toxic compounds in laboratory strains of E. coli K-12. Expression of cloned mdtEF in the K-12 strain KAM3 which lacks AcrB (see ) confers increased resistance to erythromycin, doxorubicin, crystal violet, ethidium bromide, rhodamine 6G, tetraphenylphosphonium (TPP+), benzalkonium, deoxycholate and SDS (compared to the mutant parent) (see also ). Overproduction of MdtEF in the K-12 strain KAM3 confers increased levels of resistance to the antibiotics oxacillin, cloxacillin, nafcillin and erythromycin (compared to the mutant parent) and to deoxycholate, SDS and TPP+ (compared to the mutant parent), MdtEF requires TolC for export function . Deletion of mdtEF in the K-12 strain W3110 does not affect susceptibility to a range of 35 compounds (dyes, detergents, antibiotics and others) . Overexpression of mdtE together with mdtF in E. coli strain HNCE3 (ΔacrA) results in a strong increase in resistance to cholate, taurocholate and erythromycin . MdtEF-TolC is implicated in the efflux of bile acids under extreme acid conditions .

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-352|reaction.ecocyc.TRANS-RXN-352]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-359|reaction.ecocyc.TRANS-RXN-359]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-367|reaction.ecocyc.TRANS-RXN-367]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD0-1938|molecule.ecocyc.CPD0-1938]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-7964|complex.ecocyc.CPLX0-7964]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P02930|protein.P02930]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` <-- [[protein.P37636|protein.P37636]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P37637|protein.P37637]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:TRANS-CPLX-204`
- `QSPROTEOME:QS00195965`

## Notes

1*complex.ecocyc.CPLX0-7964|1*protein.P37636|1*protein.P37637
