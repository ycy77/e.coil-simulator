---
entity_id: "protein.P76641"
entity_type: "protein"
name: "guaD"
source_database: "UniProt"
source_id: "P76641"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "guaD ygfP b2883 JW5466"
---

# guaD

`protein.P76641`

## Static

- Type: `protein`
- Source: `UniProt:P76641`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolytic deamination of guanine, producing xanthine and ammonia. {ECO:0000269|PubMed:10913105}. Guanine deaminase is an aminohydrolase that converts guanine to xanthine and ammonia. This reaction removes guanine from the pool of guanine-containing metabolites, which helps to regulate cellular GTP and the guanylate nucleotide pool. Ammeline is an intermediate in the metabolism of melamine (see the MetaCyc pathway for PWY-5170). E. coli is able to metabolize ammeline to ammelide, but does not metabolize either melamine or ammelide. A guaD deletion mutant is deficient in ammeline deaminase activity .

## Biological Role

Catalyzes GUANINE-DEAMINASE-RXN (reaction.ecocyc.GUANINE-DEAMINASE-RXN). Bound by Zinc cation (molecule.C00038).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolytic deamination of guanine, producing xanthine and ammonia. {ECO:0000269|PubMed:10913105}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.GUANINE-DEAMINASE-RXN|reaction.ecocyc.GUANINE-DEAMINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2883|gene.b2883]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76641`
- `KEGG:ecj:JW5466;eco:b2883;`
- `GeneID:947366;`
- `GO:GO:0005829; GO:0006147; GO:0008270; GO:0008892; GO:0018756; GO:0046098`
- `EC:3.5.4.3`

## Notes

Guanine deaminase (Guanase) (Guanine aminase) (EC 3.5.4.3) (Guanine aminohydrolase) (GAH)
