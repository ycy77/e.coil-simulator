---
entity_id: "protein.P11551"
entity_type: "protein"
name: "fucP"
source_database: "UniProt"
source_id: "P11551"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:20877283}; Multi-pass membrane protein {ECO:0000269|PubMed:20877283}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fucP b2801 JW2772"
---

# fucP

`protein.P11551`

## Static

- Type: `protein`
- Source: `UniProt:P11551`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:20877283}; Multi-pass membrane protein {ECO:0000269|PubMed:20877283}.

## Enriched Summary

FUNCTION: Mediates the uptake of L-fucose across the boundary membrane with the concomitant transport of protons into the cell (symport system) (PubMed:2829831, PubMed:8052131). Can also transport L-galactose and D-arabinose, but at reduced rates compared with L-fucose. Is not able to transport L-rhamnose and L-arabinose (PubMed:2829831). Binds D-arabinose with the highest affinity, followed by L-fucose, and then by L-galactose (PubMed:9826601). {ECO:0000269|PubMed:2829831, ECO:0000269|PubMed:8052131, ECO:0000269|PubMed:9826601}. FucP is an L-fucose/proton symporter responsible for the uptake of L-fucose. Imported fucose is metabolised to dihydroxyacetone phosphate and L-lactaldehyde by the action of FucI, FucK and FucA. FucP is a member of the major facilitator superfamily (MFS) of transporters . FucP has been overexpressed to a high level and shown in whole cells to mediate L-fucose/proton symport . L-fucose transport in membrane vesicles is inhibited by protonophores and ionophores . L-galactose, D-arabinose, and fructose have also been shown to be substrates, but unlike L-fucose, they do not act as inducers . The fucP gene forms part of a fucose-inducible operon containing fucI and fucK, encoding L-fucose isomerase and fuculose kinase, respectively. Expression of the fucPIK operon is controlled by the FucR regulator...

## Biological Role

Catalyzes D-arabinose:proton symport (reaction.ecocyc.RXN0-7221), L-galactose:proton symport (reaction.ecocyc.RXN0-7222), L-fucose:proton symport (reaction.ecocyc.TRANS-RXN-20). Transports D-Arabinose (molecule.C00216), L-Fucose (molecule.C01019), L-Galactose (molecule.C01825), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Mediates the uptake of L-fucose across the boundary membrane with the concomitant transport of protons into the cell (symport system) (PubMed:2829831, PubMed:8052131). Can also transport L-galactose and D-arabinose, but at reduced rates compared with L-fucose. Is not able to transport L-rhamnose and L-arabinose (PubMed:2829831). Binds D-arabinose with the highest affinity, followed by L-fucose, and then by L-galactose (PubMed:9826601). {ECO:0000269|PubMed:2829831, ECO:0000269|PubMed:8052131, ECO:0000269|PubMed:9826601}.

## Outgoing Edges (7)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7221|reaction.ecocyc.RXN0-7221]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7222|reaction.ecocyc.RXN0-7222]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-20|reaction.ecocyc.TRANS-RXN-20]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00216|molecule.C00216]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C01019|molecule.C01019]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C01825|molecule.C01825]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2801|gene.b2801]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P11551`
- `KEGG:ecj:JW2772;eco:b2801;ecoc:C3026_15400;`
- `GeneID:75172885;75203808;947487;`
- `GO:GO:0005886; GO:0006004; GO:0009679; GO:0015517; GO:0015518; GO:0015535; GO:0015751; GO:0015755; GO:0015756; GO:0015757; GO:0016020`

## Notes

L-fucose-proton symporter (6-deoxy-L-galactose permease) (L-fucose permease) (L-fucose-H(+) symport protein)
