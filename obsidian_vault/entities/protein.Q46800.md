---
entity_id: "protein.Q46800"
entity_type: "protein"
name: "xdhB"
source_database: "UniProt"
source_id: "Q46800"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xdhB ygeT b2867 JW2835"
---

# xdhB

`protein.Q46800`

## Static

- Type: `protein`
- Source: `UniProt:Q46800`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Presumed to be a dehydrogenase, but possibly an oxidase. Participates in limited purine salvage (requires aspartate) but does not support aerobic growth on purines as the sole carbon source (purine catabolism). XdhB has similarity to YagS . XdhB has sequence similarity to the FAD-binding domain of Drosophila melanogaster xanthine dehydrogenase .

## Biological Role

Component of putative xanthine dehydrogenase (complex.ecocyc.CPLX0-761).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Presumed to be a dehydrogenase, but possibly an oxidase. Participates in limited purine salvage (requires aspartate) but does not support aerobic growth on purines as the sole carbon source (purine catabolism).

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-761|complex.ecocyc.CPLX0-761]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2867|gene.b2867]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46800`
- `KEGG:ecj:JW2835;eco:b2867;ecoc:C3026_15730;`
- `GeneID:75205296;947205;`
- `GO:GO:0002197; GO:0004854; GO:0005737; GO:0006166; GO:0009114; GO:0016903; GO:0071949`
- `EC:1.17.1.4`

## Notes

Putative xanthine dehydrogenase FAD-binding subunit XdhB (EC 1.17.1.4)
