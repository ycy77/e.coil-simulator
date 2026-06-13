---
entity_id: "protein.P39386"
entity_type: "protein"
name: "mdtM"
source_database: "UniProt"
source_id: "P39386"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22426385, ECO:0000269|PubMed:23701827, ECO:0000269|PubMed:27025617}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mdtM yjiO b4337 JW4300"
---

# mdtM

`protein.P39386`

## Static

- Type: `protein`
- Source: `UniProt:P39386`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:22426385, ECO:0000269|PubMed:23701827, ECO:0000269|PubMed:27025617}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Proton-dependent efflux pump (PubMed:22426385, PubMed:23221628, PubMed:23701827, PubMed:24684269). Confers resistance to a broad spectrum of chemically unrelated substrates (PubMed:11566977, PubMed:22426385, PubMed:23221628, PubMed:23701827, PubMed:24684269). Overexpression confers resistance to acriflavine, chloramphenicol, norfloxacin, ethidium bromide and tetraphenylphosphonium bromide (TPP) (PubMed:11566977, PubMed:22426385). Can also export a broad range of quaternary ammonium compounds (QACs) and contribute to the intrinsic resistance of E.coli to these antimicrobial compounds (PubMed:23221628). In addition to its role in multidrug resistance, MdtM likely plays a physiological role in alkaline pH homeostasis and in resistance to bile salts (PubMed:23701827, PubMed:24684269, PubMed:28962921). May function in alkaline pH homeostasis when millimolar concentrations of sodium or potassium are present in the growth medium (PubMed:23701827). When overexpressed, can confer a tolerance to alkaline pH values up to 9.75 (PubMed:23701827). Probably acts as a low-affinity antiporter that catalyzes the exchange of internal Na(+) and K(+) cations for extracellular protons to maintain a stable internal pH, acid relative to outside, during exposure to alkaline environments (PubMed:23701827)...

## Biological Role

Catalyzes electrogenic sodium:proton antiport (reaction.ecocyc.TRANS-RXN-129), electrogenic potassium:proton antiport (reaction.ecocyc.TRANS-RXN-336), xenobiotic:proton antiport (reaction.ecocyc.TRANS-RXN-44), cholate:proton antiport (reaction.ecocyc.TRANS-RXN0-588), deoxycholate:proton antiport (reaction.ecocyc.TRANS-RXN0-589). Transports Potassium cation (molecule.C00238), Cholic acid (molecule.C00695), Sodium cation (molecule.C01330), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Proton-dependent efflux pump (PubMed:22426385, PubMed:23221628, PubMed:23701827, PubMed:24684269). Confers resistance to a broad spectrum of chemically unrelated substrates (PubMed:11566977, PubMed:22426385, PubMed:23221628, PubMed:23701827, PubMed:24684269). Overexpression confers resistance to acriflavine, chloramphenicol, norfloxacin, ethidium bromide and tetraphenylphosphonium bromide (TPP) (PubMed:11566977, PubMed:22426385). Can also export a broad range of quaternary ammonium compounds (QACs) and contribute to the intrinsic resistance of E.coli to these antimicrobial compounds (PubMed:23221628). In addition to its role in multidrug resistance, MdtM likely plays a physiological role in alkaline pH homeostasis and in resistance to bile salts (PubMed:23701827, PubMed:24684269, PubMed:28962921). May function in alkaline pH homeostasis when millimolar concentrations of sodium or potassium are present in the growth medium (PubMed:23701827). When overexpressed, can confer a tolerance to alkaline pH values up to 9.75 (PubMed:23701827). Probably acts as a low-affinity antiporter that catalyzes the exchange of internal Na(+) and K(+) cations for extracellular protons to maintain a stable internal pH, acid relative to outside, during exposure to alkaline environments (PubMed:23701827). Can also catalyze Rb(+)/H(+) and Li(+)/H(+) antiport, but not Ca(2+)/H(+) exchange (PubMed:23701827). The exact stoichiometry of antiport is unknown (PubMed:23701827). Finally, it could contribute to bile salt resistance by catalyzing the transport of bile salts out of the cell cytoplasm (PubMed:24684269). Mediates a bile salt/H(+) exchange driven by the electrochemical gradient (PubMed:24684269). Binds to cholate and deoxycholate with micromolar affinity and catalyzes both cholate/H(+) and deoxycholate/H(+) exchange reactions (PubMed:24684269). {ECO:0000269|PubMed:11566977, ECO:0000269|PubMed:22426385, ECO:0000269|PubMed:23221628, ECO:0000269|PubMed:23701827, ECO:0000269|PubMed:24684269, ECO:0000269|PubMed:28962921}.

## Outgoing Edges (9)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-129|reaction.ecocyc.TRANS-RXN-129]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-336|reaction.ecocyc.TRANS-RXN-336]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-44|reaction.ecocyc.TRANS-RXN-44]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-588|reaction.ecocyc.TRANS-RXN0-588]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-589|reaction.ecocyc.TRANS-RXN0-589]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00238|molecule.C00238]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00695|molecule.C00695]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C01330|molecule.C01330]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b4337|gene.b4337]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39386`
- `KEGG:ecj:JW4300;eco:b4337;ecoc:C3026_23445;`
- `GeneID:948861;`
- `GO:GO:0005886; GO:0015125; GO:0015385; GO:0015386; GO:0015721; GO:0030641; GO:0036376; GO:0046677; GO:0097623; GO:1990961`

## Notes

Multidrug resistance protein MdtM (Multidrug resistance transporter MdtM) (MDR transporter MdtM) (Multidrug transporter MdtM)
