---
entity_id: "protein.P37617"
entity_type: "protein"
name: "zntA"
source_database: "UniProt"
source_id: "P37617"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:10660539, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16411752, ECO:0000269|PubMed:16890908}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "zntA yhhO b3469 JW3434"
---

# zntA

`protein.P37617`

## Static

- Type: `protein`
- Source: `UniProt:P37617`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:10660539, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:16411752, ECO:0000269|PubMed:16890908}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Confers resistance to zinc, cadmium and lead (PubMed:10660539, PubMed:17326661, PubMed:9364914, PubMed:9405611, PubMed:9830000). Couples the hydrolysis of ATP with the export of zinc, cadmium or lead, with highest activity when the metals are present as metal-thiolate complexes (PubMed:10660539, PubMed:17326661, PubMed:9405611). Can also bind nickel, copper, cobalt and mercury (PubMed:10660539, PubMed:17326661). {ECO:0000269|PubMed:10660539, ECO:0000269|PubMed:17326661, ECO:0000269|PubMed:9364914, ECO:0000269|PubMed:9405611, ECO:0000269|PubMed:9830000}. zntA encodes a P-type ATPase that mediates export of the divalent metal ions Zn2+, Cd2+ and Pb2+ . ZntA mediated metal ion export contributes to Zn2+ homeostasis and confers resistance to Cd2+ and Pb2+ (see ). The enzyme has low activity with Ni2+, Co2+, and Cu2+ in vitro but these metal ions are not physiologically relevant substrates . Purified ZntA has metal (Pb2+, Zn2+, Cd2+)-induced ATPase activity; metal-thiolates may be the true substrate in vivo . In the solution NMR structure of a ZntA fragment (ZntA26-118) reported by mononunuclear Zn is bound through Cys-59, Cys-62 and Asp-58 side-chains. Asp-436 is the site of phosphorylation (see also )...

## Biological Role

Catalyzes 3.6.3.3-RXN (reaction.ecocyc.3.6.3.3-RXN), RXN0-5205 (reaction.ecocyc.RXN0-5205), TRANS-RXN-452 (reaction.ecocyc.TRANS-RXN-452). Transports Zinc cation (molecule.C00038), Lead (molecule.C06696), Cd2+ (molecule.ecocyc.CD_2), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Confers resistance to zinc, cadmium and lead (PubMed:10660539, PubMed:17326661, PubMed:9364914, PubMed:9405611, PubMed:9830000). Couples the hydrolysis of ATP with the export of zinc, cadmium or lead, with highest activity when the metals are present as metal-thiolate complexes (PubMed:10660539, PubMed:17326661, PubMed:9405611). Can also bind nickel, copper, cobalt and mercury (PubMed:10660539, PubMed:17326661). {ECO:0000269|PubMed:10660539, ECO:0000269|PubMed:17326661, ECO:0000269|PubMed:9364914, ECO:0000269|PubMed:9405611, ECO:0000269|PubMed:9830000}.

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.ecocyc.3.6.3.3-RXN|reaction.ecocyc.3.6.3.3-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-5205|reaction.ecocyc.RXN0-5205]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-452|reaction.ecocyc.TRANS-RXN-452]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C06696|molecule.C06696]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CD_2|molecule.ecocyc.CD_2]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3469|gene.b3469]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37617`
- `KEGG:ecj:JW3434;eco:b3469;ecoc:C3026_18790;`
- `GeneID:947972;`
- `GO:GO:0005524; GO:0005886; GO:0006829; GO:0006882; GO:0008551; GO:0010043; GO:0010288; GO:0010312; GO:0015086; GO:0015094; GO:0015692; GO:0016020; GO:0016463; GO:0016887; GO:0030001; GO:0046686; GO:0046872; GO:0055085; GO:0070574; GO:0071577`
- `EC:7.2.2.-; 7.2.2.12; 7.2.2.21`

## Notes

Zinc/cadmium/lead-transporting P-type ATPase (EC 7.2.2.-) (EC 7.2.2.12) (EC 7.2.2.21) (Pb(II)/Cd(II)/Zn(II)-translocating ATPase) (Zn(2+)/Cd(2+)/Pb(2+) export ATPase)
