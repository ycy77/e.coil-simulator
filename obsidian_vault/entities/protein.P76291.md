---
entity_id: "protein.P76291"
entity_type: "protein"
name: "cmoB"
source_database: "UniProt"
source_id: "P76291"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cmoB yecP b1871 JW1860"
---

# cmoB

`protein.P76291`

## Static

- Type: `protein`
- Source: `UniProt:P76291`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes carboxymethyl transfer from carboxy-S-adenosyl-L-methionine (Cx-SAM) to 5-hydroxyuridine (ho5U) to form 5-carboxymethoxyuridine (cmo5U) at position 34 in tRNAs. Can also catalyze the SAM-dependent methylation of ho5U, with much lower efficiency. {ECO:0000269|PubMed:23676670, ECO:0000269|PubMed:25855808}.

## Biological Role

Component of tRNA U34 carboxymethyltransferase (complex.ecocyc.CPLX0-8190).

## Annotation

FUNCTION: Catalyzes carboxymethyl transfer from carboxy-S-adenosyl-L-methionine (Cx-SAM) to 5-hydroxyuridine (ho5U) to form 5-carboxymethoxyuridine (cmo5U) at position 34 in tRNAs. Can also catalyze the SAM-dependent methylation of ho5U, with much lower efficiency. {ECO:0000269|PubMed:23676670, ECO:0000269|PubMed:25855808}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8190|complex.ecocyc.CPLX0-8190]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1871|gene.b1871]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76291`
- `KEGG:ecj:JW1860;eco:b1871;ecoc:C3026_10650;`
- `GeneID:75171943;946387;`
- `GO:GO:0002098; GO:0008168; GO:0016765; GO:0032991; GO:0042802`
- `EC:2.5.1.-`

## Notes

tRNA U34 carboxymethyltransferase (EC 2.5.1.-)
