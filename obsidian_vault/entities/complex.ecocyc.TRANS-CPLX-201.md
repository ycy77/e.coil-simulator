---
entity_id: "complex.ecocyc.TRANS-CPLX-201"
entity_type: "complex"
name: "multidrug efflux pump AcrAB-TolC"
source_database: "EcoCyc"
source_id: "TRANS-CPLX-201"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# multidrug efflux pump AcrAB-TolC

`complex.ecocyc.TRANS-CPLX-201`

## Static

- Type: `complex`
- Source: `EcoCyc:TRANS-CPLX-201`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[complex.ecocyc.CPLX0-7964|complex.ecocyc.CPLX0-7964]], [[protein.P0AE06|protein.P0AE06]], [[protein.P31224|protein.P31224]]

## Enriched Summary

AcrAB-TolC is a tripartite, proton dependent, drug efflux pump complex spanning the cell envelope. The complex consists of a resistance-nodulation-division (RND) family inner membrane transporter AcrB, a membrane fusion protein (MFP) AcrA and a multifunctional outer membrane channel TolC, and is considered to be the major contributor to intrinsic resistance for many compounds (antibiotics, antiseptics, detergents, dyes and others). acrAB null mutants are hypersusceptible to novobiocin, erythromycin, mitomycin C, fusidic acid, ethidium bromide and SDS ; acrAB null mutants are hypersusceptible to the bile salts, sodium cholate and sodium taurodeoxycholate and the C10 fatty acid, n-decanoate (see also ); AcrAB is the major efflux pump for acriflavine ; tetracycline, ampicillin, puromycin, nalidixate, rifampin, and chloramphenicol (see also ). Inactivation of AcrAB increases susceptibility to oxacillin, cloxacillin, mezlocillin, piperacillin, azlocillin, carbenicillin, cefamandole, cefuroxime, and cefoxitin; efflux by AcrAB requires the presence of lipophilic moieties on the substrate molecule (see also ). AcrAB plays a major role in the organic solvent tolerance phenotype of E. coli; deletion of acrAB results in loss of tolerance to the index organic solvent, n-hexane (see also )...

## Biological Role

Catalyzes acriflavine efflux (reaction.ecocyc.TRANS-RXN-354), n-hexane export (reaction.ecocyc.TRANS-RXN-355), decanoate export (reaction.ecocyc.TRANS-RXN-356), enterobactin export (reaction.ecocyc.TRANS-RXN-357), ethidium export (reaction.ecocyc.TRANS-RXN-359), chenodeoxycholate export (reaction.ecocyc.TRANS-RXN0-592). Transports Decanoic acid (molecule.C01571), Chenodeoxycholate (molecule.C02528), Enterochelin (molecule.C05821), hν (molecule.ecocyc.Light).

## Annotation

AcrAB-TolC is a tripartite, proton dependent, drug efflux pump complex spanning the cell envelope. The complex consists of a resistance-nodulation-division (RND) family inner membrane transporter AcrB, a membrane fusion protein (MFP) AcrA and a multifunctional outer membrane channel TolC, and is considered to be the major contributor to intrinsic resistance for many compounds (antibiotics, antiseptics, detergents, dyes and others). acrAB null mutants are hypersusceptible to novobiocin, erythromycin, mitomycin C, fusidic acid, ethidium bromide and SDS ; acrAB null mutants are hypersusceptible to the bile salts, sodium cholate and sodium taurodeoxycholate and the C10 fatty acid, n-decanoate (see also ); AcrAB is the major efflux pump for acriflavine ; tetracycline, ampicillin, puromycin, nalidixate, rifampin, and chloramphenicol (see also ). Inactivation of AcrAB increases susceptibility to oxacillin, cloxacillin, mezlocillin, piperacillin, azlocillin, carbenicillin, cefamandole, cefuroxime, and cefoxitin; efflux by AcrAB requires the presence of lipophilic moieties on the substrate molecule (see also ). AcrAB plays a major role in the organic solvent tolerance phenotype of E. coli; deletion of acrAB results in loss of tolerance to the index organic solvent, n-hexane (see also ). The AcrAB-TolC system also exports enterobactin and the human steroid hormones, progesterone, estradiol and hydrocortisone . Kinetic parameters for AcrAB-TolC mediated drug efflux have been estimated using an artificially optimized system . AcrABTolC provides minimal resistance to ethidium and acriflavine in an emrE mdfA double null background suggesting that tripartite pumps may act cooperatively with single component major facilitator superfamily (MFS) and small multidrug resistance (SMR) trans

## Outgoing Edges (10)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-354|reaction.ecocyc.TRANS-RXN-354]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-355|reaction.ecocyc.TRANS-RXN-355]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-356|reaction.ecocyc.TRANS-RXN-356]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-357|reaction.ecocyc.TRANS-RXN-357]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-359|reaction.ecocyc.TRANS-RXN-359]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-592|reaction.ecocyc.TRANS-RXN0-592]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C01571|molecule.C01571]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C02528|molecule.C02528]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C05821|molecule.C05821]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-7964|complex.ecocyc.CPLX0-7964]] `EcoCyc` `database` - EcoCyc component coefficient=1
- `is_component_of` <-- [[protein.P02930|protein.P02930]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` <-- [[protein.P0AE06|protein.P0AE06]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6 | EcoCyc transporter component coefficient=6
- `is_component_of` <-- [[protein.P31224|protein.P31224]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3

## External IDs

- `EcoCyc:TRANS-CPLX-201`
- `PDB:5V5S`
- `PDB:5O66`
- `PDB:5NG5`
- `PDB:5NG5`
- `PDB:5V78`
- `PDB:5V5S`

## Notes

1*complex.ecocyc.CPLX0-7964|6*protein.P0AE06|3*protein.P31224
