---
entity_id: "protein.P0A9J4"
entity_type: "protein"
name: "panE"
source_database: "UniProt"
source_id: "P0A9J4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "panE apbA b0425 JW0415"
---

# panE

`protein.P0A9J4`

## Static

- Type: `protein`
- Source: `UniProt:P0A9J4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the NADPH-dependent reduction of ketopantoate into pantoic acid. {ECO:0000269|PubMed:10736170, ECO:0000269|PubMed:11123955}. 2-Dehydropantoate 2-reductase catalyzes the NADPH-dependent reduction of ketopantoate to pantoate. The enzyme does not require added divalent metal ions . Kinetic data is consistent with an ordered sequential reaction mechanism, with NADPH binding followed by ketopantoate binding . Residues involved in catalysis and substrate binding were identified by site-directed mutagenesis . The enzyme has relatively high substrate specificity . Crystal structures of the enzyme have been solved . The enzyme is a monomer in solution and is comprised of an N-terminal Rossmann fold domain and a C-terminal α-helical domain . The enzyme was used as a target for fragment-based drug discovery . A panE mutant alone is not auxotrophic for pantothenate, because in both E. coli and S. typhimurium, the reaction can also be carried out by IlvC (CPLX0-7643) . ApbA: "alternative pyrimidine biosynthetic pathway" (Salmonella typhimurium) PanE: "pantothenate"

## Biological Role

Catalyzes 2-DEHYDROPANTOATE-REDUCT-RXN (reaction.ecocyc.2-DEHYDROPANTOATE-REDUCT-RXN).

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the NADPH-dependent reduction of ketopantoate into pantoic acid. {ECO:0000269|PubMed:10736170, ECO:0000269|PubMed:11123955}.

## Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.2-DEHYDROPANTOATE-REDUCT-RXN|reaction.ecocyc.2-DEHYDROPANTOATE-REDUCT-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0425|gene.b0425]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9J4`
- `KEGG:ecj:JW0415;eco:b0425;ecoc:C3026_02075;`
- `GeneID:93777035;945065;`
- `GO:GO:0005737; GO:0008677; GO:0015940; GO:0050661`
- `EC:1.1.1.169`

## Notes

2-dehydropantoate 2-reductase (EC 1.1.1.169) (Ketopantoate reductase) (KPA reductase) (KPR)
