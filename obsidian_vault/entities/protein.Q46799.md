---
entity_id: "protein.Q46799"
entity_type: "protein"
name: "xdhA"
source_database: "UniProt"
source_id: "Q46799"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xdhA ygeS b2866 JW5462"
---

# xdhA

`protein.Q46799`

## Static

- Type: `protein`
- Source: `UniProt:Q46799`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Presumed to be a dehydrogenase, but possibly an oxidase. Participates in limited purine salvage (requires aspartate) but does not support aerobic growth on purines as the sole carbon source (purine catabolism). Deletion results in increased adenine sensitivity, suggesting that this protein contributes to the conversion of adenine to guanine nucleotides during purine salvage. {ECO:0000269|PubMed:10986234}. XdhA has similarity to the molybdenum cofactor-containing domains of Drosophila melanogaster xanthine dehydrogenase and Desulfovibrio gigas aldehyde oxidoreductase . An xdhA mutant exhibits a defect in an indirect assay of xanthine dehydrogenase activity and exhibits sensitivity to adenine, which is indicative of a defect in purine salvage . The mutant exhibits more rapid growth than wild type utilizing aspartate as the source of nitrogen and growth under these conditions is stimulated by hypoxanthine . The mutant shows wild-type growth utilizing abundant ammonia as the nitrogen source .

## Biological Role

Component of putative xanthine dehydrogenase (complex.ecocyc.CPLX0-761).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Presumed to be a dehydrogenase, but possibly an oxidase. Participates in limited purine salvage (requires aspartate) but does not support aerobic growth on purines as the sole carbon source (purine catabolism). Deletion results in increased adenine sensitivity, suggesting that this protein contributes to the conversion of adenine to guanine nucleotides during purine salvage. {ECO:0000269|PubMed:10986234}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-761|complex.ecocyc.CPLX0-761]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2866|gene.b2866]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46799`
- `KEGG:ecj:JW5462;eco:b2866;`
- `GeneID:947116;`
- `GO:GO:0002197; GO:0004854; GO:0005506; GO:0005737; GO:0006166; GO:0009114; GO:0016491`
- `EC:1.17.1.4`

## Notes

Putative xanthine dehydrogenase molybdenum-binding subunit XdhA (EC 1.17.1.4)
