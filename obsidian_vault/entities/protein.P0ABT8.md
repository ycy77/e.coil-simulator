---
entity_id: "protein.P0ABT8"
entity_type: "protein"
name: "yijE"
source_database: "UniProt"
source_id: "P0ABT8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yijE b3943 JW5557"
---

# yijE

`protein.P0ABT8`

## Static

- Type: `protein`
- Source: `UniProt:P0ABT8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Involved in response to cystine. Overexpression confers tolerance to excess cystine. {ECO:0000269|PubMed:25346166}. YijE belongs to the drug/metabolite exporter (DME) family of inner membrane proteins . The protein has ten predicted transmembrane domains; its C terminus is located in the cytoplasm . The expression of yijE is upregulated in the presence of 10µM cystine; overexpression of yijE from a plasmid confers resistance to the growth inhibitory effects of 80µM cystine; deletion of yijE results in increased sensitivity to 20µM cystine .

## Biological Role

Catalyzes transport of cystine (reaction.ecocyc.TRANS-RXN-267).

## Annotation

FUNCTION: Involved in response to cystine. Overexpression confers tolerance to excess cystine. {ECO:0000269|PubMed:25346166}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-267|reaction.ecocyc.TRANS-RXN-267]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3943|gene.b3943]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABT8`
- `KEGG:ecj:JW5557;eco:b3943;ecoc:C3026_21310;`
- `GeneID:948445;`
- `GO:GO:0000099; GO:0000101; GO:0005886; GO:0016020`

## Notes

Probable cystine transporter YijE
