---
entity_id: "protein.P0AC38"
entity_type: "protein"
name: "aspA"
source_database: "UniProt"
source_id: "P0AC38"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aspA b4139 JW4099"
---

# aspA

`protein.P0AC38`

## Static

- Type: `protein`
- Source: `UniProt:P0AC38`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible conversion of L-aspartate to fumarate and ammonia (PubMed:1897995, PubMed:2853974, PubMed:33012071, PubMed:4584395, PubMed:8047016, PubMed:8119980). In the reverse reaction, consumption of fumarate is observed in the presence of not only NH4(+), but also hydroxylamine (NH(2)OH) (PubMed:1897995, PubMed:4584395). Is specific for L-aspartate and cannot use structural analogs of L-aspartate such as D-aspartate, DL-alpha-methylaspartate, DL-beta-methylaspartate, DL-threo-beta-hydroxy-aspartate, DL-erythro-beta-hydroxyaspartate, L-cysteate, L-alpha-aminobutyrate, L-asparagine, L-alanine or L-glutamate (PubMed:4584395). Represents the central enzyme for nitrogen assimilation from L-aspartate in E.coli (PubMed:33012071). {ECO:0000269|PubMed:1897995, ECO:0000269|PubMed:2853974, ECO:0000269|PubMed:33012071, ECO:0000269|PubMed:4584395, ECO:0000269|PubMed:8047016, ECO:0000269|PubMed:8119980}.

## Biological Role

Catalyzes L-aspartate ammonia-lyase (fumarate-forming) (reaction.R00490). Component of aspartate ammonia-lyase (complex.ecocyc.ASPARTASE-CPLX).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible conversion of L-aspartate to fumarate and ammonia (PubMed:1897995, PubMed:2853974, PubMed:33012071, PubMed:4584395, PubMed:8047016, PubMed:8119980). In the reverse reaction, consumption of fumarate is observed in the presence of not only NH4(+), but also hydroxylamine (NH(2)OH) (PubMed:1897995, PubMed:4584395). Is specific for L-aspartate and cannot use structural analogs of L-aspartate such as D-aspartate, DL-alpha-methylaspartate, DL-beta-methylaspartate, DL-threo-beta-hydroxy-aspartate, DL-erythro-beta-hydroxyaspartate, L-cysteate, L-alpha-aminobutyrate, L-asparagine, L-alanine or L-glutamate (PubMed:4584395). Represents the central enzyme for nitrogen assimilation from L-aspartate in E.coli (PubMed:33012071). {ECO:0000269|PubMed:1897995, ECO:0000269|PubMed:2853974, ECO:0000269|PubMed:33012071, ECO:0000269|PubMed:4584395, ECO:0000269|PubMed:8047016, ECO:0000269|PubMed:8119980}.

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00490|reaction.R00490]] `KEGG` `database` - via EC:4.3.1.1
- `is_component_of` --> [[complex.ecocyc.ASPARTASE-CPLX|complex.ecocyc.ASPARTASE-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b4139|gene.b4139]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC38`
- `KEGG:ecj:JW4099;eco:b4139;ecoc:C3026_22370;`
- `GeneID:93777685;948658;`
- `GO:GO:0005829; GO:0006099; GO:0006531; GO:0006533; GO:0006538; GO:0008797; GO:0016020; GO:0019740; GO:0042802; GO:0051289`
- `EC:4.3.1.1`

## Notes

Aspartate ammonia-lyase (Aspartase) (EC 4.3.1.1)
