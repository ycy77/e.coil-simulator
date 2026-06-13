---
entity_id: "protein.P77324"
entity_type: "protein"
name: "paoB"
source_database: "UniProt"
source_id: "P77324"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:19368556}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "paoB yagS b0285 JW0279"
---

# paoB

`protein.P77324`

## Static

- Type: `protein`
- Source: `UniProt:P77324`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:19368556}.

## Enriched Summary

FUNCTION: Oxidizes aldehydes to the corresponding carboxylic acids with a preference for aromatic aldehydes (PubMed:19368556, PubMed:30945846). It might play a role in the detoxification of aldehydes to avoid cell damage (PubMed:19368556). {ECO:0000269|PubMed:19368556, ECO:0000269|PubMed:30945846}. paoB encodes the β subunit of a heterotrimeric periplasmic aldehyde oxidoreductase, PaoABC; PaoB binds a [4Fe-4S] cluster and is the FAD-containing subunit .

## Biological Role

Component of aldehyde dehydrogenase (complex.ecocyc.CPLX0-7805).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Oxidizes aldehydes to the corresponding carboxylic acids with a preference for aromatic aldehydes (PubMed:19368556, PubMed:30945846). It might play a role in the detoxification of aldehydes to avoid cell damage (PubMed:19368556). {ECO:0000269|PubMed:19368556, ECO:0000269|PubMed:30945846}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7805|complex.ecocyc.CPLX0-7805]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0285|gene.b0285]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77324`
- `KEGG:ecj:JW0279;eco:b0285;ecoc:C3026_01390;ecoc:C3026_24025;`
- `GeneID:75204628;945710;`
- `GO:GO:0016903; GO:0030288; GO:0042597; GO:0046872; GO:0047770; GO:0050660; GO:0051539; GO:0071949; GO:0110095; GO:1990204`
- `EC:1.2.99.6`

## Notes

Aldehyde oxidoreductase FAD-binding subunit PaoB (EC 1.2.99.6)
