---
entity_id: "protein.P39199"
entity_type: "protein"
name: "prmB"
source_database: "UniProt"
source_id: "P39199"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "prmB yfcB b2330 JW5841"
---

# prmB

`protein.P39199`

## Static

- Type: `protein`
- Source: `UniProt:P39199`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Specifically methylates ribosomal protein uL3 on 'Gln-150' (PubMed:11847124, PubMed:372746). Does not methylate the translation termination release factors RF1 or RF2 (PubMed:11847124). {ECO:0000269|PubMed:11847124, ECO:0000269|PubMed:372746}. PrmB is an N5-glutamine methyltransferase that specifically methylates EG10866-MONOMER ribosomal protein L3 . PrmB and PrmC have sequence similarity to each other; PrmB is active toward ribosomal protein L3, whereas PrmC is active toward polypeptide chain release factors RF1 and RF2 . A prmB mutant lacks methylation of L3, has a cold-sensitive growth phenotype and accumulates abnormal ribosomal particles, indicating a defect in ribosome assembly . PrmB: "protein methylation B"

## Biological Role

Catalyzes RXN0-1241 (reaction.ecocyc.RXN0-1241).

## Annotation

FUNCTION: Specifically methylates ribosomal protein uL3 on 'Gln-150' (PubMed:11847124, PubMed:372746). Does not methylate the translation termination release factors RF1 or RF2 (PubMed:11847124). {ECO:0000269|PubMed:11847124, ECO:0000269|PubMed:372746}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-1241|reaction.ecocyc.RXN0-1241]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2330|gene.b2330]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39199`
- `KEGG:ecj:JW5841;eco:b2330;ecoc:C3026_12980;`
- `GeneID:946805;`
- `GO:GO:0003676; GO:0005829; GO:0006479; GO:0008276; GO:0008757; GO:0036009`
- `EC:2.1.1.298`

## Notes

Ribosomal protein uL3 glutamine methyltransferase (L3 MTase) (uL3 MTase) (EC 2.1.1.298) (N5-glutamine methyltransferase PrmB)
