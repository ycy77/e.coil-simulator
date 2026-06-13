---
entity_id: "protein.P32143"
entity_type: "protein"
name: "yihV"
source_database: "UniProt"
source_id: "P32143"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yihV b3883 JW5568"
---

# yihV

`protein.P32143`

## Static

- Type: `protein`
- Source: `UniProt:P32143`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Phosphorylates 6-deoxy-6-sulfo-D-fructose (SF) to 6-deoxy-6-sulfo-D-fructose 1-phosphate (SFP) (PubMed:24463506, PubMed:33791429). Cannot phosphorylate fructose 6-phosphate (PubMed:33791429). {ECO:0000269|PubMed:24463506, ECO:0000269|PubMed:33791429}. 6-Deoxy-6-sulfofructose kinase (YihV) catalyzes the ATP-dependent phosphorylation of CPD-16501 to CPD-16502 , a part of the PWY-7446 pathway. Expression of YihV is induced by growth on sulfoquinovose , lactose and galactose . A yihV mutant is unable to grow on sulfoquinovose as the sole source of carbon .

## Biological Role

Catalyzes RXN-15297 (reaction.ecocyc.RXN-15297).

## Enriched Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Phosphorylates 6-deoxy-6-sulfo-D-fructose (SF) to 6-deoxy-6-sulfo-D-fructose 1-phosphate (SFP) (PubMed:24463506, PubMed:33791429). Cannot phosphorylate fructose 6-phosphate (PubMed:33791429). {ECO:0000269|PubMed:24463506, ECO:0000269|PubMed:33791429}.

## Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-15297|reaction.ecocyc.RXN-15297]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3883|gene.b3883]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32143`
- `KEGG:ecj:JW5568;eco:b3883;ecoc:C3026_20990;`
- `GeneID:75204554;948382;`
- `GO:GO:0005524; GO:0005829; GO:0016301; GO:0046835; GO:0061594; GO:0061720; GO:1902777`
- `EC:2.7.1.184`

## Notes

Sulfofructose kinase (SF kinase) (EC 2.7.1.184)
