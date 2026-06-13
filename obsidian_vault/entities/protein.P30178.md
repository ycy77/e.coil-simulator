---
entity_id: "protein.P30178"
entity_type: "protein"
name: "hcxB"
source_database: "UniProt"
source_id: "P30178"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hcxB ybiC b0801 JW0786"
---

# hcxB

`protein.P30178`

## Static

- Type: `protein`
- Source: `UniProt:P30178`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the NAD(P)H-dependent reduction of 2-oxoglutarate, phenylpyruvate and (4-hydroxyphenyl)pyruvate, leading to the respective 2-hydroxycarboxylate in vitro. Shows a preference for NADPH over NADH as a redox partner. Do not catalyze the reverse reactions. {ECO:0000269|PubMed:27941785}. The hydroxycarboxylate dehydrogenase activity of HcxB was discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . HcxB: "hydroxycarboxylic acid dehydrogenase B"

## Biological Role

Catalyzes RXN-7632 (reaction.ecocyc.RXN-7632).

## Enriched Pathways

- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the NAD(P)H-dependent reduction of 2-oxoglutarate, phenylpyruvate and (4-hydroxyphenyl)pyruvate, leading to the respective 2-hydroxycarboxylate in vitro. Shows a preference for NADPH over NADH as a redox partner. Do not catalyze the reverse reactions. {ECO:0000269|PubMed:27941785}.

## Pathways

- `eco00350` Tyrosine metabolism (KEGG)
- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-7632|reaction.ecocyc.RXN-7632]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0801|gene.b0801]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30178`
- `KEGG:ecj:JW0786;eco:b0801;ecoc:C3026_05055;`
- `GeneID:93776629;945412;`
- `GO:GO:0005829; GO:0047029; GO:0047995`
- `EC:1.1.1.-; 1.1.1.237`

## Notes

Hydroxycarboxylate dehydrogenase B (EC 1.1.1.-) (2-oxoglutarate reductase) (Hydroxyphenylpyruvate reductase) (EC 1.1.1.237) (Phenylpyruvate reductase)
