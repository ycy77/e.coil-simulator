---
entity_id: "protein.Q47142"
entity_type: "protein"
name: "hcaT"
source_database: "UniProt"
source_id: "Q47142"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hcaT yfhS b2536 JW2520"
---

# hcaT

`protein.Q47142`

## Static

- Type: `protein`
- Source: `UniProt:Q47142`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Probable permease involved in the uptake of 3-phenylpropionic acid. HcaT is a member of the major facilitator superfamily (MFS) of transporters . HcaT is a putative 3-phenylpropionate transporter. The hcaT gene is located immediately downstream of the hcaR gene, whose product regulates expression of the hcaA-D operon responsible for catabolism of 3-phenylpropionic acid . HcaT is predicted to be an inner membrane protein with 12 transmembrane domains; topology analysis suggests the C-terminus is located in the cytoplasm .

## Biological Role

Catalyzes TRANS-RXN0-282 (reaction.ecocyc.TRANS-RXN0-282).

## Annotation

FUNCTION: Probable permease involved in the uptake of 3-phenylpropionic acid.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-282|reaction.ecocyc.TRANS-RXN0-282]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2536|gene.b2536]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q47142`
- `KEGG:ecj:JW2520;eco:b2536;ecoc:C3026_14050;`
- `GeneID:75206229;947007;`
- `GO:GO:0005886; GO:0015528; GO:0030395`

## Notes

Probable 3-phenylpropionic acid transporter
