---
entity_id: "protein.P77231"
entity_type: "protein"
name: "citG"
source_database: "UniProt"
source_id: "P77231"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "citG ybdT b0613 JW0605"
---

# citG

`protein.P77231`

## Static

- Type: `protein`
- Source: `UniProt:P77231`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the formation of 2-(5''-triphosphoribosyl)-3'-dephosphocoenzyme-A, the precursor of the prosthetic group of the holo-acyl carrier protein (gamma chain) of citrate lyase, from ATP and dephospho-CoA. {ECO:0000269|PubMed:10924139, ECO:0000269|PubMed:11042274}. CitG catalyzes the synthesis of the citrate lyase prosthetic group precursor, 2'-(5''-triphosphoribosyl)-3'-dephospho-CoA, from dephospho-CoA and ATP. The enzyme does not catalyze the conversion of AMP-ACP to holo-ACP . Overexpression of citG from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hydrogen peroxide .

## Biological Role

Catalyzes 2.7.8.25-RXN (reaction.ecocyc.2.7.8.25-RXN).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of 2-(5''-triphosphoribosyl)-3'-dephosphocoenzyme-A, the precursor of the prosthetic group of the holo-acyl carrier protein (gamma chain) of citrate lyase, from ATP and dephospho-CoA. {ECO:0000269|PubMed:10924139, ECO:0000269|PubMed:11042274}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2.7.8.25-RXN|reaction.ecocyc.2.7.8.25-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0613|gene.b0613]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77231`
- `KEGG:ecj:JW0605;eco:b0613;ecoc:C3026_03065;`
- `GeneID:946395;`
- `GO:GO:0005524; GO:0046917; GO:0051191`
- `EC:2.4.2.52`

## Notes

2-(5''-triphosphoribosyl)-3'-dephosphocoenzyme-A synthase (2-(5''-triphosphoribosyl)-3'-dephospho-CoA synthase) (EC 2.4.2.52)
