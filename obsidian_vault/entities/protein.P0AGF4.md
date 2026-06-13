---
entity_id: "protein.P0AGF4"
entity_type: "protein"
name: "xylE"
source_database: "UniProt"
source_id: "P0AGF4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:23075985}; Multi-pass membrane protein {ECO:0000269|PubMed:23075985}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xylE b4031 JW3991"
---

# xylE

`protein.P0AGF4`

## Static

- Type: `protein`
- Source: `UniProt:P0AGF4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:23075985}; Multi-pass membrane protein {ECO:0000269|PubMed:23075985}.

## Enriched Summary

FUNCTION: Uptake of D-xylose across the boundary membrane with the concomitant transport of protons into the cell (symport system). Glucose is not transported, but can compete for xylose binding sites and can inhibit xylose transport (in vitro). {ECO:0000269|PubMed:23075985}. XylE is a D-xylose/proton symporter, one of two systems in E. coli K-12 responsible for the uptake of D-xylose - the other being the ATP-dependent ABC transporter XylFGH. The cloned xylE gene has been shown to complement xylE mutants in vivo . XylE-mediated transport in whole cells is inhibited by protonophores and elicits an alkaline pH change . Experiments using xylE and xylF mutants have established that XylE has a Km of 63-169 μM for D-xylose . Crystal structures of XylE bound to the ligands D-xylose, D-glucose and the chemically synthesized glucose derivative, 6-bromo-6-deoxy-D-glucose have been obtained at 2.6 - 2.9 Å. Structures were captured in an outward facing conformation. XylE contains 12 transmembrane (TM) helices organised into two distinct domains with amino and carboxy termini located on the cytosolic side of the membrane. XylE also contains an intracellular domain consisting of 4 helices - 3 of these connect the TM domains, the fourth is located at the C-terminal end of the protein . Crystal structures of XylE in an inward open conformation are also available...

## Biological Role

Catalyzes xylose:proton symport (reaction.ecocyc.TRANS-RXN-30). Transports D-Xylose (molecule.C00181), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Uptake of D-xylose across the boundary membrane with the concomitant transport of protons into the cell (symport system). Glucose is not transported, but can compete for xylose binding sites and can inhibit xylose transport (in vitro). {ECO:0000269|PubMed:23075985}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-30|reaction.ecocyc.TRANS-RXN-30]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00181|molecule.C00181]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b4031|gene.b4031]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGF4`
- `KEGG:ecj:JW3991;eco:b4031;ecoc:C3026_21780;`
- `GeneID:75169486;948529;`
- `GO:GO:0005886; GO:0015519; GO:0015753; GO:0016020; GO:0022857; GO:0055085`

## Notes

D-xylose-proton symporter (D-xylose transporter)
