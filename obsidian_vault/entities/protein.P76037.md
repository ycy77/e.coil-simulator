---
entity_id: "protein.P76037"
entity_type: "protein"
name: "puuP"
source_database: "UniProt"
source_id: "P76037"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "puuP ycjJ b1296 JW1289"
---

# puuP

`protein.P76037`

## Static

- Type: `protein`
- Source: `UniProt:P76037`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Involved in the uptake of putrescine (PubMed:15590624, PubMed:19181795, PubMed:23719730, PubMed:27803167). Imports putrescine for its utilization as an energy source in the absence of glucose (PubMed:23719730). {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:19181795, ECO:0000269|PubMed:23719730, ECO:0000269|PubMed:27803167}. PuuP is a proton dependent putrescine transporter which functions in the exponential growth phase . Mutational experiments show that among all the genes for putrescine transport (potFGHI, potABCD, potE and puuP) only puuP is essential to utilise putrescine as a sole carbon or nitrogen source . The level of puuP expression increases at low concentrations of glucose (0.04%). The expression of puuP is not inhibited by the intracellular accumulation of putrescine . PuuP and YEEF-MONOMER PlaP are receptors for the group 5 CDI ionophore toxins .

## Biological Role

Catalyzes putrescine:proton symport (reaction.ecocyc.TRANS-RXN-69).

## Annotation

FUNCTION: Involved in the uptake of putrescine (PubMed:15590624, PubMed:19181795, PubMed:23719730, PubMed:27803167). Imports putrescine for its utilization as an energy source in the absence of glucose (PubMed:23719730). {ECO:0000269|PubMed:15590624, ECO:0000269|PubMed:19181795, ECO:0000269|PubMed:23719730, ECO:0000269|PubMed:27803167}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-69|reaction.ecocyc.TRANS-RXN-69]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1296|gene.b1296]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76037`
- `KEGG:ecj:JW1289;eco:b1296;`
- `GeneID:946287;`
- `GO:GO:0005886; GO:0006865; GO:0006974; GO:0009447; GO:0015295; GO:0015489; GO:0015847; GO:0022857`

## Notes

Putrescine importer PuuP
