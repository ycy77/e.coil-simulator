---
entity_id: "protein.P77165"
entity_type: "protein"
name: "paoA"
source_database: "UniProt"
source_id: "P77165"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:19368556}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "paoA yagT b0286 JW0280"
---

# paoA

`protein.P77165`

## Static

- Type: `protein`
- Source: `UniProt:P77165`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000305|PubMed:19368556}.

## Enriched Summary

FUNCTION: Oxidizes aldehydes to the corresponding carboxylic acids with a preference for aromatic aldehydes (PubMed:19368556, PubMed:30945846). It might play a role in the detoxification of aldehydes to avoid cell damage (PubMed:19368556). {ECO:0000269|PubMed:19368556, ECO:0000269|PubMed:30945846}. paoA encodes the α subunit of a heterotrimeric periplasmic aldehyde oxidoreductase, PaoABC; PaoA binds two [2Fe-2S] clusters . A paoA single deletion mutant is unable to grow in the presence of cinnamaldehyde at pH 4.0 . PaoA contains a twin arginine signal peptide for translocation to the periplasm .

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

- `encodes` <-- [[gene.b0286|gene.b0286]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77165`
- `KEGG:ecj:JW0280;eco:b0286;ecoc:C3026_01395;ecoc:C3026_24030;`
- `GeneID:945330;`
- `GO:GO:0016903; GO:0030288; GO:0042597; GO:0046872; GO:0047770; GO:0051537; GO:0110095; GO:1990204`
- `EC:1.2.99.6`

## Notes

Aldehyde oxidoreductase iron-sulfur-binding subunit PaoA (EC 1.2.99.6)
