---
entity_id: "complex.ecocyc.CPLX0-253"
entity_type: "complex"
name: "NADPH:quinone oxidoreductase MdaB"
source_database: "EcoCyc"
source_id: "CPLX0-253"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "NADPH dehydrogenase (quinone)"
---

# NADPH:quinone oxidoreductase MdaB

`complex.ecocyc.CPLX0-253`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-253`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P0AEY5|protein.P0AEY5]]

## Enriched Summary

The MdaB quinone reductase is specific for NADPH and is most active with quinone derivatives and ferricyanide as electron acceptors . In vitro, YgiN is able to reoxidize menadiol that has been reduced by MdaB quinone reductase; the two enzymes may form a quinone redox cycle. The biological role of a quinone redox cycle may be to maintain an intracellular pool of menadione and ubiquinone using a catalytic mechanism that avoids the formation of a semiquinone intermediate, and to act as a quinone buffer . Despite the different cofactor and cosubstrate requirements, it was later stated that MdaB is identical to NQOR-CPLX , but no evidence was given. Unlike MdaB, NQOR-CPLX was shown to utilize NADH and to be FMN-dependent . Menadione specifically induces expression of the NADH- and FMN-dependent activity, while 2-methylene-4-butyrolactone (MBL) and other compounds containing a methide group induce expression of the NADPH-dependent MdaB activity . Crystal structures of apo-MdaB and in complex with FAD have been solved . Overexpression of mdaB leads to increased resistance to the tumoricidal agent DMP 840 . A strain adapted for growth in benzalkonium chloride overexpresses MdaB . An mdaB null mutant shows no change in sensitivity to menadione-induced oxidative stress...

## Biological Role

Catalyzes RXN0-271 (reaction.ecocyc.RXN0-271). Bound by FAD (molecule.C00016).

## Annotation

The MdaB quinone reductase is specific for NADPH and is most active with quinone derivatives and ferricyanide as electron acceptors . In vitro, YgiN is able to reoxidize menadiol that has been reduced by MdaB quinone reductase; the two enzymes may form a quinone redox cycle. The biological role of a quinone redox cycle may be to maintain an intracellular pool of menadione and ubiquinone using a catalytic mechanism that avoids the formation of a semiquinone intermediate, and to act as a quinone buffer . Despite the different cofactor and cosubstrate requirements, it was later stated that MdaB is identical to NQOR-CPLX , but no evidence was given. Unlike MdaB, NQOR-CPLX was shown to utilize NADH and to be FMN-dependent . Menadione specifically induces expression of the NADH- and FMN-dependent activity, while 2-methylene-4-butyrolactone (MBL) and other compounds containing a methide group induce expression of the NADPH-dependent MdaB activity . Crystal structures of apo-MdaB and in complex with FAD have been solved . Overexpression of mdaB leads to increased resistance to the tumoricidal agent DMP 840 . A strain adapted for growth in benzalkonium chloride overexpresses MdaB . An mdaB null mutant shows no change in sensitivity to menadione-induced oxidative stress . MdaB: "modulator of drug activity B"

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-271|reaction.ecocyc.RXN0-271]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P0AEY5|protein.P0AEY5]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-253`
- `QSPROTEOME:QS00159897`

## Notes

2*protein.P0AEY5
