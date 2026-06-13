---
entity_id: "protein.P0AE37"
entity_type: "protein"
name: "astA"
source_database: "UniProt"
source_id: "P0AE37"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "astA ydjV b1747 JW1736"
---

# astA

`protein.P0AE37`

## Static

- Type: `protein`
- Source: `UniProt:P0AE37`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the transfer of succinyl-CoA to arginine to produce N(2)-succinylarginine. {ECO:0000269|PubMed:9696779}. Arginine succinyltransferase (AstA) catalyzes the first reaction in the ammonia-producing arginine catabolic pathway, AST-PWY. The activity has only been assayed in crude cell extracts, and thus there is little direct evidence for the function of the astA gene product . AstA is a member of the acyl-CoA N-acyltransferase superfamily . Expression of the enzymes of the AST pathway is regulated by arginine and nitrogen availability via ArgR and NtrC .

## Biological Role

Catalyzes succinyl-CoA:L-arginine N2-succinyltransferase (reaction.R00832), ARGININE-N-SUCCINYLTRANSFERASE-RXN (reaction.ecocyc.ARGININE-N-SUCCINYLTRANSFERASE-RXN).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the transfer of succinyl-CoA to arginine to produce N(2)-succinylarginine. {ECO:0000269|PubMed:9696779}.

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00832|reaction.R00832]] `KEGG` `database` - via EC:2.3.1.109
- `catalyzes` --> [[reaction.ecocyc.ARGININE-N-SUCCINYLTRANSFERASE-RXN|reaction.ecocyc.ARGININE-N-SUCCINYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1747|gene.b1747]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE37`
- `KEGG:ecj:JW1736;eco:b1747;ecoc:C3026_09980;`
- `GeneID:75171814;946261;`
- `GO:GO:0006527; GO:0008791; GO:0009015; GO:0019544; GO:0019545`
- `EC:2.3.1.109`

## Notes

Arginine N-succinyltransferase (AST) (EC 2.3.1.109) (AOST)
