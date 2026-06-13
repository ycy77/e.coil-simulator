---
entity_id: "protein.P76215"
entity_type: "protein"
name: "astE"
source_database: "UniProt"
source_id: "P76215"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "astE ydjS b1744 JW1733"
---

# astE

`protein.P76215`

## Static

- Type: `protein`
- Source: `UniProt:P76215`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transforms N(2)-succinylglutamate into succinate and glutamate. {ECO:0000269|PubMed:9696779}. Succinylglutamate desuccinylase catalyzes the fifth and final reaction in the ammonia-producing arginine catabolic pathway, AST-PWY. The activity has only been assayed in crude cell extracts, and thus there is little direct evidence for the function of the astE gene product . Deletion of astE enhances tolerance to n-butanol . Expression of the enzymes of the AST pathway is regulated by arginine and nitrogen availability via ArgR and NtrC .

## Biological Role

Catalyzes N-succinyl-L-glutamate amidohydrolase (reaction.R00411), SUCCGLUDESUCC-RXN (reaction.ecocyc.SUCCGLUDESUCC-RXN).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Transforms N(2)-succinylglutamate into succinate and glutamate. {ECO:0000269|PubMed:9696779}.

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00411|reaction.R00411]] `KEGG` `database` - via EC:3.5.1.96
- `catalyzes` --> [[reaction.ecocyc.SUCCGLUDESUCC-RXN|reaction.ecocyc.SUCCGLUDESUCC-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1744|gene.b1744]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76215`
- `KEGG:ecj:JW1733;eco:b1744;ecoc:C3026_09965;`
- `GeneID:946256;`
- `GO:GO:0008270; GO:0009017; GO:0016788; GO:0016811; GO:0019544; GO:0019545`
- `EC:3.5.1.96`

## Notes

Succinylglutamate desuccinylase (EC 3.5.1.96)
