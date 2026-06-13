---
entity_id: "complex.ecocyc.DIHYDROXYACIDDEHYDRAT-CPLX"
entity_type: "complex"
name: "dihydroxy-acid dehydratase"
source_database: "EcoCyc"
source_id: "DIHYDROXYACIDDEHYDRAT-CPLX"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
  - "2,3-dihydroxy-acid hydro-lyase"
---

# dihydroxy-acid dehydratase

`complex.ecocyc.DIHYDROXYACIDDEHYDRAT-CPLX`

## Static

- Type: `complex`
- Source: `EcoCyc:DIHYDROXYACIDDEHYDRAT-CPLX`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `structural`
- Components: [[protein.P05791|protein.P05791]]

## Enriched Summary

Dihydroxy-acid dehydratase carries out the penultimate step in both the isoleucine and valine biosynthesis pathways. It is also the target for NO-induced bacteriostasis in E. coli. IlvD catalyzes two similar dehydration reactions that convert 2,3-dihydroxy-isovalerate into 2-keto-isovalerate and 2,3-dihydroxy-3-methylvalerate into 2-keto-3-methyl-valerate . IlvD has an Fe-S cluster that is both critical for its activity and is a primary target for NO-induced bacteriostasis. The native, homodimeric protein contains a [4Fe-4S] cluster that is subject to oxidative degradation and inactivation in the presence of molecular oxygen . This inactivation does not lead to the degradation of IlvD. In fact, upon removal of the oxidizing agent, the [4Fe-4S] cluster can be rebuilt by the cluster synthesis system, reactivating the enzyme. This synthesis system is known to include ACSERLYA-CPLX, ACSERLYB-CPLX, CYSTATHIONINE-BETA-LYASE-CPLX, and THII-MONOMER . Most significantly, IlvD is inactivated by exposure to NITRIC-OXIDE. The NO-inactivated IlvD remains inactive in anaerobic growth conditions, but is repaired in aerobic growth conditions. This inactivation, in turn, leads to bacteriostasis, and is the basis of NITRIC-OXIDE's general bacteriostatic effect on E. coli . The kinetic characterization of the reaction between NO and the [4Fe-4S] cluster of IlvD has been investigated...

## Biological Role

Catalyzes DIHYDROXYISOVALDEHYDRAT-RXN (reaction.ecocyc.DIHYDROXYISOVALDEHYDRAT-RXN), 2,3-Dihydroxy-3-methylvalerate dehydratase (reaction.ecocyc.DIHYDROXYMETVALDEHYDRAT-RXN). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Annotation

Dihydroxy-acid dehydratase carries out the penultimate step in both the isoleucine and valine biosynthesis pathways. It is also the target for NO-induced bacteriostasis in E. coli. IlvD catalyzes two similar dehydration reactions that convert 2,3-dihydroxy-isovalerate into 2-keto-isovalerate and 2,3-dihydroxy-3-methylvalerate into 2-keto-3-methyl-valerate . IlvD has an Fe-S cluster that is both critical for its activity and is a primary target for NO-induced bacteriostasis. The native, homodimeric protein contains a [4Fe-4S] cluster that is subject to oxidative degradation and inactivation in the presence of molecular oxygen . This inactivation does not lead to the degradation of IlvD. In fact, upon removal of the oxidizing agent, the [4Fe-4S] cluster can be rebuilt by the cluster synthesis system, reactivating the enzyme. This synthesis system is known to include ACSERLYA-CPLX, ACSERLYB-CPLX, CYSTATHIONINE-BETA-LYASE-CPLX, and THII-MONOMER . Most significantly, IlvD is inactivated by exposure to NITRIC-OXIDE. The NO-inactivated IlvD remains inactive in anaerobic growth conditions, but is repaired in aerobic growth conditions. This inactivation, in turn, leads to bacteriostasis, and is the basis of NITRIC-OXIDE's general bacteriostatic effect on E. coli . The kinetic characterization of the reaction between NO and the [4Fe-4S] cluster of IlvD has been investigated . IlvD is contranslated with IlvA, the threonine deaminase that carries out the first step in the isoleucine biosynthesis pathway .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.DIHYDROXYISOVALDEHYDRAT-RXN|reaction.ecocyc.DIHYDROXYISOVALDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.DIHYDROXYMETVALDEHYDRAT-RXN|reaction.ecocyc.DIHYDROXYMETVALDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P05791|protein.P05791]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:DIHYDROXYACIDDEHYDRAT-CPLX`
- `QSPROTEOME:QS00049699`

## Notes

2*protein.P05791
