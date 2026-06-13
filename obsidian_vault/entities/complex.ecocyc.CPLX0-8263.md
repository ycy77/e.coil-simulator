---
entity_id: "complex.ecocyc.CPLX0-8263"
entity_type: "complex"
name: "guanidinium exporter"
source_database: "EcoCyc"
source_id: "CPLX0-8263"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "Gdx-Eco"
  - "Gdx"
---

# guanidinium exporter

`complex.ecocyc.CPLX0-8263`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8263`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P69937|protein.P69937]]

## Enriched Summary

SugE/Gdx is a member of the small multidrug resistance (SMR) family of proton-dependent drug efflux transporters within the Drug/Metabolite Transporter (DMT) superfamily . Gdx is a proton-coupled guanidinium (Gdm+) transporter . Purified Gdx reconstituted into liposomes, mediates the uptake of labeled Gdm+ in the presence of an outward directed Gdm+ gradient (Gdm+ exchange) and in the presence of an outward directed H+ gradient (Gdm+:H+ antiport); Gdm+:H+ antiport occurs with a 1:2 stoichiometry; Gdx is selective for Gdm+; the role of Gdm+ in bacteria is not known . Gdx mRNA contains a guanidine II (mini-ykkC) riboswitch; the Gdx guanidine II riboswitch aptamer binds guanidine (guanidinium) in vitro and undergoes guanidine-mediated structural modulation; the Gdx guanidine II riboswitch responds co-operatively to guanidine . The Gdx guanidine II riboswitch comprises two putative stem loops (P1 and P2) connected by a spacer; the crystal structure of the P1 stem loop bound to guanidine has been solved; the Gdx guanidine II riboswitch is predicted to act as a translation 'on' switch . Overexpression of cloned sugE in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) does not impact resistance to a range of toxic compounds (dyes, detergents, antibiotics and others) compared to the mutant parent...

## Biological Role

Catalyzes cetylpyridinium:H+ antiport (reaction.ecocyc.TRANS-RXN-368), guanidinium:proton antiport (reaction.ecocyc.TRANS-RXN-369). Transports cetylpyridinium (molecule.ecocyc.CPD-20888), guanidinium (molecule.ecocyc.CPD0-1470), hν (molecule.ecocyc.Light).

## Annotation

SugE/Gdx is a member of the small multidrug resistance (SMR) family of proton-dependent drug efflux transporters within the Drug/Metabolite Transporter (DMT) superfamily . Gdx is a proton-coupled guanidinium (Gdm+) transporter . Purified Gdx reconstituted into liposomes, mediates the uptake of labeled Gdm+ in the presence of an outward directed Gdm+ gradient (Gdm+ exchange) and in the presence of an outward directed H+ gradient (Gdm+:H+ antiport); Gdm+:H+ antiport occurs with a 1:2 stoichiometry; Gdx is selective for Gdm+; the role of Gdm+ in bacteria is not known . Gdx mRNA contains a guanidine II (mini-ykkC) riboswitch; the Gdx guanidine II riboswitch aptamer binds guanidine (guanidinium) in vitro and undergoes guanidine-mediated structural modulation; the Gdx guanidine II riboswitch responds co-operatively to guanidine . The Gdx guanidine II riboswitch comprises two putative stem loops (P1 and P2) connected by a spacer; the crystal structure of the P1 stem loop bound to guanidine has been solved; the Gdx guanidine II riboswitch is predicted to act as a translation 'on' switch . Overexpression of cloned sugE in a K-12 strain which lacks the major efflux pump permease AcrB (E. coli KAM3; see ) does not impact resistance to a range of toxic compounds (dyes, detergents, antibiotics and others) compared to the mutant parent . Expression of cloned sugE (under control of its native promoter) results in increased resistance to cetrimide cations (hexadecyltrimethyl ammonium), cetylpyridinium and cetyldimethylethyl ammonium (compared to wild type) but does not affect resistance to a number of other structurally related compounds or cationic dyes . Purified SugE in membrane mimetic environments binds various compounds (methyl viologen, proflavin, tetraphenylphosphonium and ethi

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-368|reaction.ecocyc.TRANS-RXN-368]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-369|reaction.ecocyc.TRANS-RXN-369]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CPD-20888|molecule.ecocyc.CPD-20888]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD0-1470|molecule.ecocyc.CPD0-1470]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P69937|protein.P69937]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## External IDs

- `EcoCyc:CPLX0-8263`
- `QSPROTEOME:QS00157827`

## Notes

2*protein.P69937
