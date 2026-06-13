---
entity_id: "protein.P0AEY8"
entity_type: "protein"
name: "mdfA"
source_database: "UniProt"
source_id: "P0AEY8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdfA cmlA cmr b0842 JW0826"
---

# mdfA

`protein.P0AEY8`

## Static

- Type: `protein`
- Source: `UniProt:P0AEY8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Efflux pump driven by the proton motive force. Confers resistance to a broad spectrum of chemically unrelated drugs. Confers resistance to a diverse group of cationic or zwitterionic lipophilic compounds such as ethidium bromide, tetraphenylphosphonium, rhodamine, daunomycin, benzalkonium, rifampicin, tetracycline, puromycin, and to chemically unrelated, clinically important antibiotics such as chloramphenicol, erythromycin, and certain aminoglycosides and fluoroquinolones. Overexpression results in isopropyl-beta-D-thiogalactopyranoside (IPTG) exclusion and spectinomycin sensitivity. Transport of neutral substrates is electrogenic, whereas transport of cationic substrates is electroneutral. In addition to its role in multidrug resistance, confers extreme alkaline pH resistance, allowing the growth under conditions that are close to those used normally by alkaliphiles. This activity requires Na(+) or K(+). {ECO:0000269|PubMed:12578981, ECO:0000269|PubMed:15371593, ECO:0000269|PubMed:9079913, ECO:0000269|PubMed:9644262, ECO:0000269|PubMed:9811673}. The MdfA protein, also known as Cmr, is a multidrug efflux protein belonging to the major facilitator superfamily (MFS)...

## Biological Role

Catalyzes sodium:proton antiport (reaction.ecocyc.TRANS-RXN-101), dequalinium:proton antiport (reaction.ecocyc.TRANS-RXN-337), ethidium:proton antiport (reaction.ecocyc.TRANS-RXN-338), potassium:proton antiport (reaction.ecocyc.TRANS-RXN-42), xenobiotic:proton antiport (reaction.ecocyc.TRANS-RXN-44). Transports Potassium cation (molecule.C00238), Sodium cation (molecule.C01330), dequalinium (molecule.ecocyc.CPD-20894), ethidium (molecule.ecocyc.CPD0-1938), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Efflux pump driven by the proton motive force. Confers resistance to a broad spectrum of chemically unrelated drugs. Confers resistance to a diverse group of cationic or zwitterionic lipophilic compounds such as ethidium bromide, tetraphenylphosphonium, rhodamine, daunomycin, benzalkonium, rifampicin, tetracycline, puromycin, and to chemically unrelated, clinically important antibiotics such as chloramphenicol, erythromycin, and certain aminoglycosides and fluoroquinolones. Overexpression results in isopropyl-beta-D-thiogalactopyranoside (IPTG) exclusion and spectinomycin sensitivity. Transport of neutral substrates is electrogenic, whereas transport of cationic substrates is electroneutral. In addition to its role in multidrug resistance, confers extreme alkaline pH resistance, allowing the growth under conditions that are close to those used normally by alkaliphiles. This activity requires Na(+) or K(+). {ECO:0000269|PubMed:12578981, ECO:0000269|PubMed:15371593, ECO:0000269|PubMed:9079913, ECO:0000269|PubMed:9644262, ECO:0000269|PubMed:9811673}.

## Outgoing Edges (10)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-101|reaction.ecocyc.TRANS-RXN-101]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-337|reaction.ecocyc.TRANS-RXN-337]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-338|reaction.ecocyc.TRANS-RXN-338]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-42|reaction.ecocyc.TRANS-RXN-42]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-44|reaction.ecocyc.TRANS-RXN-44]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD-20894|molecule.ecocyc.CPD-20894]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.CPD0-1938|molecule.ecocyc.CPD0-1938]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0842|gene.b0842]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEY8`
- `KEGG:ag:CAA69997;ecj:JW0826;eco:b0842;ecoc:C3026_05265;`
- `GeneID:945448;`
- `GO:GO:0005886; GO:0015385; GO:0015386; GO:0030641; GO:0046677; GO:1990961`

## Notes

Multidrug transporter MdfA (Chloramphenicol resistance pump Cmr)
