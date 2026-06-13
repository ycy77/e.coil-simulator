---
entity_id: "protein.P75712"
entity_type: "protein"
name: "ybbW"
source_database: "UniProt"
source_id: "P75712"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ybbW glxB2 b0511 JW0499"
---

# ybbW

`protein.P75712`

## Static

- Type: `protein`
- Source: `UniProt:P75712`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Uptake of allantoin into the cell. {ECO:0000250|UniProtKB:P94575}. E. coli is able to utilize allantoin as a source of nitrogen under anaerobic conditions . allW, located within an allantoin utilization gene cluster, encodes an allantoin transporter that relies on binding to allB-encoded CPLX-64 for activity; AllW-AllB physical association is enhanced in the presence of glyoxylate . AllW and AllB constitute a functional 'membrane transport metabolon' . AllW (formerly YbbW) has sequence similarity to the allantoin permease of Saccharomyces cerevisiae . Accumulation of the cationic fluorescent dye 3,3'-dipropylthiadicarbocyanine iodide (diS-C3) is greater in ybbW knockout cells compared to wild type . In the Transporter Classification Database AllW is a member of the Nucleobase:Cation Symporter-1 (NCS1) family within the Amino Acid-Polyamine-Organocation (APC) superfamily.

## Biological Role

Catalyzes TRANS-RXN0-444 (reaction.ecocyc.TRANS-RXN0-444). Transports L-Serine (molecule.C00065), allantoin (molecule.ecocyc.ALLANTOIN), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Uptake of allantoin into the cell. {ECO:0000250|UniProtKB:P94575}.

## Outgoing Edges (4)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-444|reaction.ecocyc.TRANS-RXN0-444]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C00065|molecule.C00065]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.ALLANTOIN|molecule.ecocyc.ALLANTOIN]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b0511|gene.b0511]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75712`
- `KEGG:ecj:JW0499;eco:b0511;ecoc:C3026_02505;`
- `GeneID:945138;`
- `GO:GO:0005886; GO:0006144; GO:0015205; GO:0015293; GO:0015720; GO:0015851`

## Notes

Putative allantoin permease (Allantoin transport protein) (Allantoin transporter)
