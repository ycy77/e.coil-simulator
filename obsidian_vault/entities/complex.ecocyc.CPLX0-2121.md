---
entity_id: "complex.ecocyc.CPLX0-2121"
entity_type: "complex"
name: "multidrug efflux pump EmrAB-TolC"
source_database: "EcoCyc"
source_id: "CPLX0-2121"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# multidrug efflux pump EmrAB-TolC

`complex.ecocyc.CPLX0-2121`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-2121`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[complex.ecocyc.CPLX0-7964|complex.ecocyc.CPLX0-7964]], [[protein.P27303|protein.P27303]], [[protein.P0AEJ0|protein.P0AEJ0]]

## Enriched Summary

EmrAB-TolC is an efflux pump complex which contributes to E. coli's intrinsic resistance to a variety of mainly hydrophobic compounds. Expression of cloned emrAB confers increased resistance to the uncoupler, carbonylcyanide m-chlorophenylhydrazone (CCCP) and its analog 2-chlorophenylhydrazine hydrochloride, to the uncoupler tetrachlorosalicylanilide (TSA), to nalidixate and to phenylmercury acetate (but not to a number of other compounds including norfloxacin, tetracycline and chloramphenicol); EmrAB substrates appear to be hydrophobic compounds . Expression of cloned emrAB in the K-12 strain KAM3 which lacks AcrB (see ) confers increased resistance to rhodamine 6G, methyl viologen, CCCP, deoxycholate and SDS (compared to the mutant parent) (see also ). Deletion of emrAB in the K-12 strain W3110 does not affect susceptibility to a range of 35 compounds (dyes, detergents, antibiotics and others) . EmrAB is implicated in the efflux of bile acids and the steroid hormones, progesterone and estradiol . Increased expression of EmrAB confers resistance to the antibiotic thiolactomycin . EmrA and EmrB form a stable complex in vitro; the EmrAB complex can be reconstituted in the absence of TolC; the reconstituted complex likely forms a dimer...

## Biological Role

Catalyzes nalidixate export (reaction.ecocyc.TRANS-RXN-363), carbonylcyanide m-chlorophenylhydrazone export (reaction.ecocyc.TRANS-RXN-364), deoxycholate export (reaction.ecocyc.TRANS-RXN-365). Transports nalidixic acid (molecule.ecocyc.CPD-21025), carbonylcyanide m-chlorophenylhydrazone (molecule.ecocyc.CPD-7970), hν (molecule.ecocyc.Light).

## Annotation

EmrAB-TolC is an efflux pump complex which contributes to E. coli's intrinsic resistance to a variety of mainly hydrophobic compounds. Expression of cloned emrAB confers increased resistance to the uncoupler, carbonylcyanide m-chlorophenylhydrazone (CCCP) and its analog 2-chlorophenylhydrazine hydrochloride, to the uncoupler tetrachlorosalicylanilide (TSA), to nalidixate and to phenylmercury acetate (but not to a number of other compounds including norfloxacin, tetracycline and chloramphenicol); EmrAB substrates appear to be hydrophobic compounds . Expression of cloned emrAB in the K-12 strain KAM3 which lacks AcrB (see ) confers increased resistance to rhodamine 6G, methyl viologen, CCCP, deoxycholate and SDS (compared to the mutant parent) (see also ). Deletion of emrAB in the K-12 strain W3110 does not affect susceptibility to a range of 35 compounds (dyes, detergents, antibiotics and others) . EmrAB is implicated in the efflux of bile acids and the steroid hormones, progesterone and estradiol . Increased expression of EmrAB confers resistance to the antibiotic thiolactomycin . EmrA and EmrB form a stable complex in vitro; the EmrAB complex can be reconstituted in the absence of TolC; the reconstituted complex likely forms a dimer . The tripartite EmrAB-TolC complex has been purified (from a strain co-expressing cloned emrB and emrA-tolC) and the structure analysed by electron microscopy . Expression of emrAB is controlled by the negative regulator CPLX0-7418 "MprA" (also called EmrR); expression is induced by a number of unrelated compounds including CCCP, TSA, nalidixate, salicylate, 2,4-dinitrophenol and ethidium bromide . Selected related reviews: Please note: stoichiometry of the EmrAB-TolC efflux pump complex is not known

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-363|reaction.ecocyc.TRANS-RXN-363]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-364|reaction.ecocyc.TRANS-RXN-364]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-365|reaction.ecocyc.TRANS-RXN-365]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD-21025|molecule.ecocyc.CPD-21025]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-7970|molecule.ecocyc.CPD-7970]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (4)

- `is_component_of` <-- [[complex.ecocyc.CPLX0-7964|complex.ecocyc.CPLX0-7964]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` <-- [[protein.P02930|protein.P02930]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3 | EcoCyc transporter component coefficient=3
- `is_component_of` <-- [[protein.P0AEJ0|protein.P0AEJ0]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1
- `is_component_of` <-- [[protein.P27303|protein.P27303]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## External IDs

- `EcoCyc:CPLX0-2121`
- `QSPROTEOME:QS00093452`

## Notes

complex.ecocyc.CPLX0-7964|protein.P27303|protein.P0AEJ0
