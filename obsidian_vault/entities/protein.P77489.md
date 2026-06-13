---
entity_id: "protein.P77489"
entity_type: "protein"
name: "paoC"
source_database: "UniProt"
source_id: "P77489"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:19368556}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "paoC yagR b0284 JW0278"
---

# paoC

`protein.P77489`

## Static

- Type: `protein`
- Source: `UniProt:P77489`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:19368556}.

## Enriched Summary

FUNCTION: Oxidizes aldehydes to the corresponding carboxylic acids with a preference for aromatic aldehydes (PubMed:19368556, PubMed:30945846). It might play a role in the detoxification of aldehydes to avoid cell damage (PubMed:19368556). {ECO:0000269|PubMed:19368556, ECO:0000269|PubMed:30945846}. paoC encodes the large, molybdenum cofactor-containing subunit of a heterotrimeric periplasmic aldehyde oxidoreductase, PaoABC . A paoC single deletion mutant is unable to grow in the presence of cinnamaldehyde at pH 4.0 .

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

- `encodes` <-- [[gene.b0284|gene.b0284]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77489`
- `KEGG:ecj:JW0278;eco:b0284;ecoc:C3026_01385;ecoc:C3026_24020;`
- `GeneID:944961;`
- `GO:GO:0005506; GO:0006974; GO:0016491; GO:0016903; GO:0030151; GO:0030288; GO:0042597; GO:0047770; GO:0110095; GO:1990204`
- `EC:1.2.99.6`

## Notes

Aldehyde oxidoreductase molybdenum-binding subunit PaoC (EC 1.2.99.6)
