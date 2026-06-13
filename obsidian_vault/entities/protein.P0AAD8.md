---
entity_id: "protein.P0AAD8"
entity_type: "protein"
name: "tdcC"
source_database: "UniProt"
source_id: "P0AAD8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01583, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2115866}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01583}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tdcC b3116 JW3087"
---

# tdcC

`protein.P0AAD8`

## Static

- Type: `protein`
- Source: `UniProt:P0AAD8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01583, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2115866}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01583}.

## Enriched Summary

FUNCTION: Involved in the import of threonine and serine into the cell, with the concomitant import of a proton (symport system). {ECO:0000255|HAMAP-Rule:MF_01583, ECO:0000269|PubMed:2115866, ECO:0000269|PubMed:9498571}. TdcC is a threonine transport system, likely to function as a threonine/proton symporter. Disruption of tdcC reduced threonine uptake under anaerobic conditions, and this defect could be complemented by the cloned tdcC gene . The TdcC transport system displayed a Km of approx 6 μM and threonine transport was inhibited by uncouplers, suggesting it is a high affinity threonine/proton symporter . TdcC has also been shown to be a proton-driven serine transporter . TdcC is a member of the hydroxy/aromatic amino acid permease (HAAAP) family of transporters, and is homologous to the serine transporter SdaC. The tdcC gene is located in the tdcABC operon, which also codes for threonine dehydratase . Expression of tdc-lacZ fusions has indicated that this operon is expressed under anaerobic conditions . Threonine and serine imported under anaerobic conditions are degraded to ammonia and the corresponding α-keto acids.

## Biological Role

Catalyzes L-serine:proton symport (reaction.ecocyc.TRANS-RXN-71), L-threonine:proton symport (reaction.ecocyc.TRANS-RXN-72). Transports L-Serine (molecule.C00065), L-Threonine (molecule.C00188), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Involved in the import of threonine and serine into the cell, with the concomitant import of a proton (symport system). {ECO:0000255|HAMAP-Rule:MF_01583, ECO:0000269|PubMed:2115866, ECO:0000269|PubMed:9498571}.

## Outgoing Edges (5)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-71|reaction.ecocyc.TRANS-RXN-71]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-72|reaction.ecocyc.TRANS-RXN-72]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.C00188|molecule.C00188]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3116|gene.b3116]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAD8`
- `KEGG:ecj:JW3087;eco:b3116;ecoc:C3026_16995;`
- `GeneID:93778869;947629;`
- `GO:GO:0005886; GO:0006865; GO:0015194; GO:0015195; GO:0015295; GO:0015565; GO:0015825; GO:0015826; GO:0022857`

## Notes

Threonine/serine transporter TdcC (H(+)/threonine-serine symporter)
