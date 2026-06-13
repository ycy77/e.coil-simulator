---
entity_id: "protein.Q46927"
entity_type: "protein"
name: "tcdA"
source_database: "UniProt"
source_id: "Q46927"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "tcdA csdL ygdL b2812 JW2783"
---

# tcdA

`protein.Q46927`

## Static

- Type: `protein`
- Source: `UniProt:Q46927`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Membrane {ECO:0000305}; Single-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the ATP-dependent dehydration of threonylcarbamoyladenosine at position 37 (t(6)A37) to form cyclic t(6)A37 (ct(6)A37) in tRNAs that read codons beginning with adenine. TcdA is also part of a sulfur transfer pathway; is able to accept sulfur from CsdA directly in vitro, but CsdE might act as the sulfur donor in vivo. {ECO:0000269|PubMed:20054882, ECO:0000269|PubMed:23242255}.

## Biological Role

Component of tRNA threonylcarbamoyladenosine dehydratase (complex.ecocyc.CPLX0-8176).

## Annotation

FUNCTION: Catalyzes the ATP-dependent dehydration of threonylcarbamoyladenosine at position 37 (t(6)A37) to form cyclic t(6)A37 (ct(6)A37) in tRNAs that read codons beginning with adenine. TcdA is also part of a sulfur transfer pathway; is able to accept sulfur from CsdA directly in vitro, but CsdE might act as the sulfur donor in vivo. {ECO:0000269|PubMed:20054882, ECO:0000269|PubMed:23242255}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8176|complex.ecocyc.CPLX0-8176]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2812|gene.b2812]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46927`
- `KEGG:ecj:JW2783;eco:b2812;ecoc:C3026_15455;`
- `GeneID:93779186;947291;`
- `GO:GO:0005524; GO:0008641; GO:0016020; GO:0030955; GO:0031402; GO:0042803; GO:0061503; GO:0061504`
- `EC:6.1.-.-`

## Notes

tRNA threonylcarbamoyladenosine dehydratase (EC 6.1.-.-) (t(6)A37 dehydratase)
