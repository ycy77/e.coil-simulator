---
entity_id: "protein.P25396"
entity_type: "protein"
name: "tehA"
source_database: "UniProt"
source_id: "P25396"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tehA b1429 JW1425"
---

# tehA

`protein.P25396`

## Static

- Type: `protein`
- Source: `UniProt:P25396`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Responsible for potassium tellurite resistance when present in high copy number. Ion channel involved in potassium tellurite resistance (By similarity). Otherwise, phenotypically silent. {ECO:0000250}. Overexpression of tehAB from a plasmid confers resistance to tellurite through an unknown mechanism that does not appear to involve reduced uptake or increased efflux . Overexpression of tehA results in hypersensitivity to dequalinium and methyl viologen and resistance to tetraphenylarsonium, ethidium, crystal violet and proflavin . Whole cell experiments indicated that TehA confers ethidium resistance via active efflux. Efflux is inhibited by the ionophore carbonyl cyanide m-chlorophenylhydrazone (CCCP). The addition of tellurite has no effect on ethidium transport in vitro . Overexpression of tehAB protects against tellurite induced dissipation of the transmembrane pH gradient and depletion of intracellular ATP levels . TehA is a member of the tellurite resistance/dicarboxylate (TDT) family of transporters which includes malate transporters. The physiological role of tehA remains elusive.

## Biological Role

Catalyzes TRANS-RXN0-539 (reaction.ecocyc.TRANS-RXN0-539).

## Annotation

FUNCTION: Responsible for potassium tellurite resistance when present in high copy number. Ion channel involved in potassium tellurite resistance (By similarity). Otherwise, phenotypically silent. {ECO:0000250}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-539|reaction.ecocyc.TRANS-RXN0-539]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1429|gene.b1429]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25396`
- `KEGG:ecj:JW1425;eco:b1429;`
- `GeneID:945852;`
- `GO:GO:0005886; GO:0006812; GO:0042802; GO:0046583; GO:0046677; GO:0046690; GO:0055085`

## Notes

Tellurite resistance protein TehA
