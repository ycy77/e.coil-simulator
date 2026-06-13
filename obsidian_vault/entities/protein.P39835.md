---
entity_id: "protein.P39835"
entity_type: "protein"
name: "gntT"
source_database: "UniProt"
source_id: "P39835"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gntT gntM usgA yhgC b3415 JW5690"
---

# gntT

`protein.P39835`

## Static

- Type: `protein`
- Source: `UniProt:P39835`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Part of the gluconate utilization system Gnt-I; high-affinity intake of gluconate. GntT is one of four known transporters for gluconate in E. coli, the others being the homologous GntU, GntP and IdnT transporters. Whole cell experiments have shown that the cloned gntT gene was able to complement a gluconate transport negative mutant and confers high affinity gluconate transport with a Km of approx 6 μM . Transcriptional analysis has shown that gntT constitutes a monocistronic operon. Analysis of gntT-lacZ fusions has indicated that gntT expression is induced at low levels of gluconate, partially repressed by glucose, and increased in early logarithmic phase . Expression of both gntT and gntU is controlled by the GntR repressor and by cyclic AMP-CRP . GntT is a member of the Gnt family of gluconate transporters . Gluconate uptake has been reported to occur via a proton-symport mechanism in E. coli . It seems likely that GntT is a high affinity gluconate uptake system that functions via D-gluconate/proton symport. Imported gluconate is metabolised primarily via the Entner-Douderoff pathway and secondarily via the pentose phosphate pathway.

## Biological Role

Catalyzes D-gluconate:proton symport (reaction.ecocyc.TRANS-RXN0-209).

## Annotation

FUNCTION: Part of the gluconate utilization system Gnt-I; high-affinity intake of gluconate.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-209|reaction.ecocyc.TRANS-RXN0-209]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3415|gene.b3415]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39835`
- `KEGG:ecj:JW5690;eco:b3415;ecoc:C3026_18525;`
- `GeneID:75173572;75202258;947924;`
- `GO:GO:0005886; GO:0015128; GO:0016020; GO:0019521; GO:0035429`

## Notes

High-affinity gluconate transporter (Gluconate permease) (Gnt-I system)
