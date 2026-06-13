---
entity_id: "protein.P39398"
entity_type: "protein"
name: "lgoT"
source_database: "UniProt"
source_id: "P39398"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lgoT yjiZ yjjL b4356 JW4319"
---

# lgoT

`protein.P39398`

## Static

- Type: `protein`
- Source: `UniProt:P39398`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Probably responsible for the transport of L-galactonate from the periplasm across the inner membrane. Is essential for growth on L-galactonate as the sole carbon source. {ECO:0000269|PubMed:17088549}. The YjjL protein is a member of the major facilitator superfamily (MFS) of transporters . Based on sequence similarity, mutant phenotype in batch growth assays, and expression analyses YjjL is a proton-driven L-galactonate uptake transporter .

## Biological Role

Catalyzes L-galactonate:proton symport (reaction.ecocyc.TRANS-RXN0-227). Transports L-Galactonate (molecule.C15930), hν (molecule.ecocyc.Light).

## Annotation

FUNCTION: Probably responsible for the transport of L-galactonate from the periplasm across the inner membrane. Is essential for growth on L-galactonate as the sole carbon source. {ECO:0000269|PubMed:17088549}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-227|reaction.ecocyc.TRANS-RXN0-227]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.C15930|molecule.C15930]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` --> [[molecule.ecocyc.Light|molecule.ecocyc.Light]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b4356|gene.b4356]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39398`
- `KEGG:ecj:JW4319;eco:b4356;ecoc:C3026_23535;`
- `GeneID:948879;`
- `GO:GO:0005886; GO:0022857; GO:0042873`

## Notes

Probable L-galactonate transporter (Galactonate:H(+) symporter)
