---
entity_id: "protein.P09163"
entity_type: "protein"
name: "yjaB"
source_database: "UniProt"
source_id: "P09163"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yjaB b4012 JW3972"
---

# yjaB

`protein.P09163`

## Static

- Type: `protein`
- Source: `UniProt:P09163`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: N-epsilon-lysine acetyltransferase that catalyzes acetylation of a large number of proteins (PubMed:30352934). Binds acetyl-CoA (PubMed:19343803). {ECO:0000269|PubMed:19343803, ECO:0000269|PubMed:30352934}. YjaB is an Nε-lysine acetyltransferase that targets 171 unique lysine residues in 128 proteins . Overexpression of YjaB in an acetylation-gutted strain (Δ pta patZ acs cobB) leads to the appearance of acetylated proteins in an anti-acetyllysine Western blot. Mutagenesis of a predicted catalytic residue in YjaB, Y117A, eliminates the acetylation signal observed with the wild-type protein . An NMR solution structure of apo-YjaB has been generated, showing a structure typical for Gcn5-related N-acetyltransferases (GNATs). Addition of acetyl-CoA caused chemical shifts in the NMR structure, indicating that YjaB is able to bind acetyl-CoA . A yjaB insertion mutant is viable . Review:

## Biological Role

Catalyzes RXN0-7160 (reaction.ecocyc.RXN0-7160).

## Annotation

FUNCTION: N-epsilon-lysine acetyltransferase that catalyzes acetylation of a large number of proteins (PubMed:30352934). Binds acetyl-CoA (PubMed:19343803). {ECO:0000269|PubMed:19343803, ECO:0000269|PubMed:30352934}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7160|reaction.ecocyc.RXN0-7160]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4012|gene.b4012]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09163`
- `KEGG:ecj:JW3972;eco:b4012;ecoc:C3026_21675;`
- `GeneID:948514;`
- `GO:GO:0061733`
- `EC:2.3.1.-`

## Notes

Peptidyl-lysine N-acetyltransferase YjaB (EC 2.3.1.-) (KAT)
