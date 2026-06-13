---
entity_id: "reaction.ecocyc.UDPNACETYLGLUCOSAMACYLTRANS-RXN"
entity_type: "reaction"
name: "UDPNACETYLGLUCOSAMACYLTRANS-RXN"
source_database: "EcoCyc"
source_id: "UDPNACETYLGLUCOSAMACYLTRANS-RXN"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# UDPNACETYLGLUCOSAMACYLTRANS-RXN

`reaction.ecocyc.UDPNACETYLGLUCOSAMACYLTRANS-RXN`

## Static

- Type: `reaction`
- Source: `EcoCyc:UDPNACETYLGLUCOSAMACYLTRANS-RXN`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

This is the first unique reaction in the biosynthesis of the phosphorylated glycolipid, lipid A, in the outer membrane of E.coli. EcoCyc reaction equation: R-3-hydroxymyristoyl-ACPs + UDP-N-ACETYL-D-GLUCOSAMINE -> UDP-OHMYR-ACETYLGLUCOSAMINE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT. This is the first unique reaction in the biosynthesis of the phosphorylated glycolipid, lipid A, in the outer membrane of E.coli.

## Biological Role

Catalyzed by acyl-[acyl-carrier-protein]—UDP-N-acetylglucosamine O-acyltransferase (complex.ecocyc.UDPNACETYLGLUCOSAMACYLTRANS-CPLX). Substrates: UDP-N-acetyl-alpha-D-glucosamine (molecule.C00043). Products: UDP-3-O-(3-hydroxytetradecanoyl)-N-acetylglucosamine (molecule.C04738).

## Enriched Pathways

- `ecocyc.NAGLIPASYN-PWY` lipid IVA biosynthesis (E. coli) (EcoCyc)

## Annotation

This is the first unique reaction in the biosynthesis of the phosphorylated glycolipid, lipid A, in the outer membrane of E.coli.

## Pathways

- `ecocyc.NAGLIPASYN-PWY` lipid IVA biosynthesis (E. coli) (EcoCyc)

## Outgoing Edges (0)

_None._

## Incoming Edges (3)

- `catalyzes` <-- [[complex.ecocyc.UDPNACETYLGLUCOSAMACYLTRANS-CPLX|complex.ecocyc.UDPNACETYLGLUCOSAMACYLTRANS-CPLX]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_product_of` <-- [[molecule.C04738|molecule.C04738]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C00043|molecule.C00043]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:UDPNACETYLGLUCOSAMACYLTRANS-RXN`

## Notes

R-3-hydroxymyristoyl-ACPs + UDP-N-ACETYL-D-GLUCOSAMINE -> UDP-OHMYR-ACETYLGLUCOSAMINE + ACP; direction=PHYSIOL-LEFT-TO-RIGHT
