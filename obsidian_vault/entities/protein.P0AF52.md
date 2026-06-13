---
entity_id: "protein.P0AF52"
entity_type: "protein"
name: "ghxP"
source_database: "UniProt"
source_id: "P0AF52"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:24214977}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:24214977}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ghxP yjcD b4064 JW4025"
---

# ghxP

`protein.P0AF52`

## Static

- Type: `protein`
- Source: `UniProt:P0AF52`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:24214977}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:24214977}.

## Enriched Summary

FUNCTION: High-affinity transporter for guanine and hypoxanthine. {ECO:0000269|PubMed:24214977}. Cloned and overexpressed GhxP transports labelled guanine and hypoxanthine, but not adenine, xanthine, uric acid or uracil in E. coli K-12 . GhxP has been implicated in transport of the purine base analogs CPD-15922, CPD-15921, CPD-15916, CPD-5721 and CPD-15920 . GhxP is a member of the nucleobase-cation symporter-2 (NCS2) family of transporters . A ghxP transposon mutation suppresses the sensitivity of a ΔG6487 "ycbX" strain to the purine analogues, 6-hydroxyaminopurine and 2-amino-6-hydroxyaminopurine. A ΔghxP strain is also less sensitive to 6-mercaptopurine and 6-thioguanine than wild type . ghxP contains a PurR binding motif and PurR dependent repression of ghxP is induced by exogenous adenine . Membrane topology predictions using experimentally determined C terminus locations indicate that GhxP has 13 transmembrane helices and the C-terminus is located in the periplasm .

## Biological Role

Catalyzes TRANS-RXN0-562 (reaction.ecocyc.TRANS-RXN0-562), TRANS-RXN0-578 (reaction.ecocyc.TRANS-RXN0-578).

## Annotation

FUNCTION: High-affinity transporter for guanine and hypoxanthine. {ECO:0000269|PubMed:24214977}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-562|reaction.ecocyc.TRANS-RXN0-562]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-578|reaction.ecocyc.TRANS-RXN0-578]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4064|gene.b4064]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AF52`
- `KEGG:ecj:JW4025;eco:b4064;ecoc:C3026_21960;`
- `GeneID:93777765;948565;`
- `GO:GO:0005345; GO:0005886; GO:0006863; GO:0015208; GO:0035344; GO:0098710`

## Notes

Guanine/hypoxanthine permease GhxP
