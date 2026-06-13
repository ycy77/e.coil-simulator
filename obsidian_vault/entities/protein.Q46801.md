---
entity_id: "protein.Q46801"
entity_type: "protein"
name: "xdhC"
source_database: "UniProt"
source_id: "Q46801"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xdhC ygeU b2868 JW2836"
---

# xdhC

`protein.Q46801`

## Static

- Type: `protein`
- Source: `UniProt:Q46801`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Iron-sulfur subunit of the xanthine dehydrogenase complex. XdhC has similarity to the iron-binding regions of Drosophila melanogaster xanthine dehydrogenase and Desulfovibrio gigas aldehyde oxidoreductase .

## Biological Role

Component of putative xanthine dehydrogenase (complex.ecocyc.CPLX0-761).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Iron-sulfur subunit of the xanthine dehydrogenase complex.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-761|complex.ecocyc.CPLX0-761]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2868|gene.b2868]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46801`
- `KEGG:ecj:JW2836;eco:b2868;ecoc:C3026_15735;`
- `GeneID:93779134;945148;`
- `GO:GO:0002197; GO:0005737; GO:0006166; GO:0009114; GO:0016491; GO:0046872; GO:0051537`

## Notes

Putative xanthine dehydrogenase iron-sulfur-binding subunit XdhC
