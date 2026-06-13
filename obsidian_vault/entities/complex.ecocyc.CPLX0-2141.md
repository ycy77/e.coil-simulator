---
entity_id: "complex.ecocyc.CPLX0-2141"
entity_type: "complex"
name: "multidrug efflux pump AcrEF-TolC"
source_database: "EcoCyc"
source_id: "CPLX0-2141"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# multidrug efflux pump AcrEF-TolC

`complex.ecocyc.CPLX0-2141`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-2141`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CPLX0-7964|complex.ecocyc.CPLX0-7964]], [[protein.P24180|protein.P24180]], [[protein.P24181|protein.P24181]]

## Enriched Summary

AcrEF-TolC is a putative tripartite efflux pump complex. The AcrEF proteins share high amino acid sequence identity with the AcrAB efflux pump proteins . AcrEF is implicated in indole excretion however its contribution to this process is not significant as indole can rapidly diffuse across the inner membrane without protein mediated assistance . Deletion of acrEF does not affect the drug sensitivity of E. coli K-12 C600 to a range of substances (antibiotics, dyes, detergents); overexpression of acrEF restores resistance to acriflavine, erythromycin, novobiocin and crystal violet in acrAB deletion mutants (see also ). Overexpression of cloned acrEF in the K-12 strain KAM3 which lacks AcrB (see ) confers increased resistance to doxorubicin, chloramphenicol, tetracycline, minocycline, erythromycin, nalidixic acid, norfloxacin, enoxacin, novobiocin, trimethoprim, acriflavine, ethidium bromide, rhodamine 6G, deoxycholate, SDS, crystal violet, methyl viologen, TPP, and benzalkonium (compared to the mutant parent)...

## Biological Role

Catalyzes deoxycholate export (reaction.ecocyc.TRANS-RXN-352), acriflavine efflux (reaction.ecocyc.TRANS-RXN-354), n-hexane export (reaction.ecocyc.TRANS-RXN-355), erythromycin export (reaction.ecocyc.TRANS-RXN-367). Transports Deoxycholic acid (molecule.C04483), 3,6-diamino-10-methylacridinium (molecule.ecocyc.CPD-21070), hexane (molecule.ecocyc.CPD-9288), an erythromycin (molecule.ecocyc.Erythromycins), hν (molecule.ecocyc.Light).

## Annotation

AcrEF-TolC is a putative tripartite efflux pump complex. The AcrEF proteins share high amino acid sequence identity with the AcrAB efflux pump proteins . AcrEF is implicated in indole excretion however its contribution to this process is not significant as indole can rapidly diffuse across the inner membrane without protein mediated assistance . Deletion of acrEF does not affect the drug sensitivity of E. coli K-12 C600 to a range of substances (antibiotics, dyes, detergents); overexpression of acrEF restores resistance to acriflavine, erythromycin, novobiocin and crystal violet in acrAB deletion mutants (see also ). Overexpression of cloned acrEF in the K-12 strain KAM3 which lacks AcrB (see ) confers increased resistance to doxorubicin, chloramphenicol, tetracycline, minocycline, erythromycin, nalidixic acid, norfloxacin, enoxacin, novobiocin, trimethoprim, acriflavine, ethidium bromide, rhodamine 6G, deoxycholate, SDS, crystal violet, methyl viologen, TPP, and benzalkonium (compared to the mutant parent) . Overproduction of AcrEF in the K-12 strain KAM3 confers increased levels of resistance to the antibiotics novobiocin, oxacillin, cloxacillin, nafcillin, cefuroxime, cefamandole and erythromycin (compared to the mutant parent) and restores wild-type levels of resistance to deoxycholate, SDS and tetraphenylphosphonium; AcrD requires TolC for β-lactam export acrEF is not expressed at significant levels in wild-type K-12 strains (see ). acrEF is expressed at high level upon integration of IS1 or IS2 into the upstream region of the operon and this increased expression suppresses the solvent hypersensitivity of an E. coli strain (OST5500) in which AcrB is defective; overexpression of acrA and acrF or of acrE and acrF improves the solvent resistance of a ΔacrAB::cat ΔacrE

## Outgoing Edges (9)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-352|reaction.ecocyc.TRANS-RXN-352]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-354|reaction.ecocyc.TRANS-RXN-354]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-355|reaction.ecocyc.TRANS-RXN-355]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-367|reaction.ecocyc.TRANS-RXN-367]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C04483|molecule.C04483]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-21070|molecule.ecocyc.CPD-21070]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-9288|molecule.ecocyc.CPD-9288]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Erythromycins|molecule.ecocyc.Erythromycins]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-7964|complex.ecocyc.CPLX0-7964]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P02930|protein.P02930]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` <-- [[protein.P24180|protein.P24180]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6 | EcoCyc transporter component coefficient=6
- `is_component_of` <-- [[protein.P24181|protein.P24181]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## External IDs

- `EcoCyc:CPLX0-2141`

## Notes

1*complex.ecocyc.CPLX0-7964|6*protein.P24180|3*protein.P24181
