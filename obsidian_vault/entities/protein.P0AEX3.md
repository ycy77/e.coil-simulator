---
entity_id: "protein.P0AEX3"
entity_type: "protein"
name: "kgtP"
source_database: "UniProt"
source_id: "P0AEX3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kgtP witA b2587 JW2571"
---

# kgtP

`protein.P0AEX3`

## Static

- Type: `protein`
- Source: `UniProt:P0AEX3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Uptake of alpha-ketoglutarate across the boundary membrane with the concomitant import of a cation (symport system). {ECO:0000269|PubMed:2053984}. KgtP is a proton-driven transporter for α-ketoglutarate. kgtP mutants show greatly impaired growth on α-ketoglutarate which can be complemented by the cloned kgtP gene . KgtP-dependent α-ketoglutarate/proton symport activity has been demonstrated in membrane vesicles . KgtP displays a Km for α-ketoglutarate of 13-46 μM. KgtP-mediated α-ketoglutarate transport could be partially inhibited by fumarate, malate and succinate . Consistent with its function as an α-ketoglutarate/proton symport, KgtP is a member of the major facilitator superfamily . Alkaline phosphatase fusions have demonstrated that KgtP consists of twelve transmembrane spanning segments . Arg-92 and Asp-88 have been shown to be essential residues in the KgtP transporter . kgtP appears to be constitutively expressed . KgtP has been implicated in arabinose efflux .

## Biological Role

Catalyzes 2-oxoglutarate:proton symport (reaction.ecocyc.TRANS-RXN-23). Transports 2-Oxoglutarate (molecule.C00026), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Uptake of alpha-ketoglutarate across the boundary membrane with the concomitant import of a cation (symport system). {ECO:0000269|PubMed:2053984}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-23|reaction.ecocyc.TRANS-RXN-23]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00026|molecule.C00026]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b2587|gene.b2587]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEX3`
- `KEGG:ecj:JW2571;eco:b2587;ecoc:C3026_14335;`
- `GeneID:75172703;75206281;947069;`
- `GO:GO:0005886; GO:0015294`

## Notes

Alpha-ketoglutarate permease
