---
entity_id: "protein.P02920"
entity_type: "protein"
name: "lacY"
source_database: "UniProt"
source_id: "P02920"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:2164211, ECO:0000269|PubMed:7000781, ECO:0000269|PubMed:7028742}; Multi-pass membrane protein {ECO:0000269|PubMed:2164211}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lacY b0343 JW0334"
---

# lacY

`protein.P02920`

## Static

- Type: `protein`
- Source: `UniProt:P02920`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:2164211, ECO:0000269|PubMed:7000781, ECO:0000269|PubMed:7028742}; Multi-pass membrane protein {ECO:0000269|PubMed:2164211}.

## Enriched Summary

FUNCTION: Responsible for transport of beta-galactosides into the cell, with the concomitant import of a proton (symport system). Can transport lactose, melibiose, the synthetic disaccharide lactulose or the analog methyl-1-thio-beta,D-galactopyranoside (TMG), but not sucrose or fructose (PubMed:18177889, PubMed:1848449, PubMed:22106930, PubMed:7000781, PubMed:7028742). The substrate specificity is directed toward the galactopyranosyl moiety of the substrate (PubMed:22106930). {ECO:0000269|PubMed:18177889, ECO:0000269|PubMed:1848449, ECO:0000269|PubMed:22106930, ECO:0000269|PubMed:7000781, ECO:0000269|PubMed:7028742}. The lactose permease LacY is a galactoside:proton symporter, responsible for the uptake of lactose and other galactosides. LacY is a member of the major facilitator superfamily (MFS) of transporters and is probably the best characterised secondary transporter. β-galactoside transport was first described in the mid twentieth century (reviewed in and studies of lactose transport were instrumental in elucidating and confirming the chemiosmotic theory for energy transfer in cells . The lacY gene was the first transporter gene to be cloned and sequenced . Lactose permease has been solubilised, purified, reconstituted into liposomes, and shown to mediate lactose:proton symport with a 1:1 stoichiometry...

## Biological Role

Catalyzes melibionate:proton symport (reaction.ecocyc.RXN-17755), lactulose:proton symport (reaction.ecocyc.RXN0-7215), 3-O-β-D-galactopyranosyl-D-arabinose:proton symport (reaction.ecocyc.RXN0-7217), lactose:proton symport (reaction.ecocyc.TRANS-RXN-24), melibiose:proton symport (reaction.ecocyc.TRANS-RXN-94). Transports Lactose (molecule.C00243), Melibiose (molecule.C05402), lactulose (molecule.ecocyc.CPD-3561), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Responsible for transport of beta-galactosides into the cell, with the concomitant import of a proton (symport system). Can transport lactose, melibiose, the synthetic disaccharide lactulose or the analog methyl-1-thio-beta,D-galactopyranoside (TMG), but not sucrose or fructose (PubMed:18177889, PubMed:1848449, PubMed:22106930, PubMed:7000781, PubMed:7028742). The substrate specificity is directed toward the galactopyranosyl moiety of the substrate (PubMed:22106930). {ECO:0000269|PubMed:18177889, ECO:0000269|PubMed:1848449, ECO:0000269|PubMed:22106930, ECO:0000269|PubMed:7000781, ECO:0000269|PubMed:7028742}.

## Outgoing Edges (9)

- `catalyzes` --> [[reaction.ecocyc.RXN-17755|reaction.ecocyc.RXN-17755]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7215|reaction.ecocyc.RXN0-7215]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7217|reaction.ecocyc.RXN0-7217]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-24|reaction.ecocyc.TRANS-RXN-24]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-94|reaction.ecocyc.TRANS-RXN-94]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00243|molecule.C00243]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C05402|molecule.C05402]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-3561|molecule.ecocyc.CPD-3561]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0343|gene.b0343]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P02920`
- `KEGG:ecj:JW0334;eco:b0343;ecoc:C3026_01680;ecoc:C3026_24850;`
- `GeneID:75202506;949083;`
- `GO:GO:0005351; GO:0005886; GO:0008643; GO:0015528; GO:0015767; GO:0016020; GO:0030395`

## Notes

Lactose permease (Lactose-proton symport)
