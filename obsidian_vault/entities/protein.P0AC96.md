---
entity_id: "protein.P0AC96"
entity_type: "protein"
name: "gntU"
source_database: "UniProt"
source_id: "P0AC96"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gntU b4476 JW5686"
---

# gntU

`protein.P0AC96`

## Static

- Type: `protein`
- Source: `UniProt:P0AC96`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of the gluconate utilization system Gnt-I; low-affinity intake of gluconate. GntU is one of four known transporters for gluconate in E. coli, the others being the homologous GntT, GntP and IdnT transporters. Whole cell experiments have shown that the cloned gntU gene was able to complement a gluconate transport negative mutant and confers low affinity gluconate transport with a Km of approx 212 μM . Transcriptional analysis has shown that gntU forms a dicistronic operon with the gntK gene encoding a gluconate kinase. Expression of gntU is induced by gluconate and controlled by the GntR repressor. GntU is a member of the Gnt family of gluconate transporters . Gluconate uptake has been reported to occur via a proton-symport mechanism in E. coli . It seems likely that GntU is a low affinity gluconate uptake system that functions via D-gluconate/proton symport.

## Biological Role

Catalyzes D-gluconate:proton symport (reaction.ecocyc.TRANS-RXN0-209).

## Annotation

FUNCTION: Part of the gluconate utilization system Gnt-I; low-affinity intake of gluconate.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-209|reaction.ecocyc.TRANS-RXN0-209]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4476|gene.b4476]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC96`
- `KEGG:ecj:JW5686;eco:b4476;ecoc:C3026_18620;`
- `GeneID:2847760;75173596;75202280;`
- `GO:GO:0005402; GO:0005886; GO:0015128; GO:0019521; GO:0035429`

## Notes

Low-affinity gluconate transporter (Gluconate permease) (Gnt-I system)
