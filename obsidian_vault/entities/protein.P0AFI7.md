---
entity_id: "protein.P0AFI7"
entity_type: "protein"
name: "pdxH"
source_database: "UniProt"
source_id: "P0AFI7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdxH b1638 JW1630"
---

# pdxH

`protein.P0AFI7`

## Static

- Type: `protein`
- Source: `UniProt:P0AFI7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the oxidation of either pyridoxine 5'-phosphate (PNP) or pyridoxamine 5'-phosphate (PMP) into pyridoxal 5'-phosphate (PLP). {ECO:0000269|PubMed:11786019, ECO:0000269|PubMed:7860596, ECO:0000269|PubMed:9693059}.

## Biological Role

Catalyzes pyridoxamine-5'-phosphate:oxygen oxidoreductase (deaminating) (reaction.R00277), pyridoxine 5'-phosphate:oxygen oxidoreductase (reaction.R00278). Component of pyridoxine 5'-phosphate oxidase / pyridoxamine 5'-phosphate oxidase (complex.ecocyc.PDXH-CPLX).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the oxidation of either pyridoxine 5'-phosphate (PNP) or pyridoxamine 5'-phosphate (PMP) into pyridoxal 5'-phosphate (PLP). {ECO:0000269|PubMed:11786019, ECO:0000269|PubMed:7860596, ECO:0000269|PubMed:9693059}.

## Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00277|reaction.R00277]] `KEGG` `database` - via EC:1.4.3.5
- `catalyzes` --> [[reaction.R00278|reaction.R00278]] `KEGG` `database` - via EC:1.4.3.5
- `is_component_of` --> [[complex.ecocyc.PDXH-CPLX|complex.ecocyc.PDXH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1638|gene.b1638]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFI7`
- `KEGG:ecj:JW1630;eco:b1638;ecoc:C3026_09410;`
- `GeneID:75171699;946806;`
- `GO:GO:0004733; GO:0005829; GO:0008615; GO:0010181; GO:0016491; GO:0030170; GO:0032991; GO:0036001; GO:0042301; GO:0042803; GO:0042823; GO:1902444`
- `EC:1.4.3.5`

## Notes

Pyridoxine/pyridoxamine 5'-phosphate oxidase (EC 1.4.3.5) (PNP/PMP oxidase) (PNPOx) (Pyridoxal 5'-phosphate synthase)
