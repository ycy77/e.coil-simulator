---
entity_id: "protein.P77555"
entity_type: "protein"
name: "allD"
source_database: "UniProt"
source_id: "P77555"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "allD glxB8 ylbC b0517 JW0505"
---

# allD

`protein.P77555`

## Static

- Type: `protein`
- Source: `UniProt:P77555`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: AllD plays a pivotal role as a metabolic branch-point enzyme in nitrogen utilization via the assimilation of allantoin (PubMed:10601204). It is able to utilize allantoin as a sole source of nitrogen under anaerobic conditions (PubMed:10601204). Catalyzes the oxidation of ureidoglycolate to oxalurate (PubMed:23284870). {ECO:0000269|PubMed:10601204, ECO:0000269|PubMed:23284870}.

## Biological Role

Component of ureidoglycolate dehydrogenase (complex.ecocyc.CPLX0-7993).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: AllD plays a pivotal role as a metabolic branch-point enzyme in nitrogen utilization via the assimilation of allantoin (PubMed:10601204). It is able to utilize allantoin as a sole source of nitrogen under anaerobic conditions (PubMed:10601204). Catalyzes the oxidation of ureidoglycolate to oxalurate (PubMed:23284870). {ECO:0000269|PubMed:10601204, ECO:0000269|PubMed:23284870}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7993|complex.ecocyc.CPLX0-7993]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0517|gene.b0517]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77555`
- `KEGG:ecj:JW0505;eco:b0517;ecoc:C3026_02535;`
- `GeneID:948342;`
- `GO:GO:0005737; GO:0006144; GO:0009040; GO:0009442`
- `EC:1.1.1.350`

## Notes

Ureidoglycolate dehydrogenase (NAD(+)) (EC 1.1.1.350)
