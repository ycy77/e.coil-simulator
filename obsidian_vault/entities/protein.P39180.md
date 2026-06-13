---
entity_id: "protein.P39180"
entity_type: "protein"
name: "flu"
source_database: "UniProt"
source_id: "P39180"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: [Antigen 43]: Periplasm {ECO:0000250}.; SUBCELLULAR LOCATION: [Antigen 43 alpha chain]: Secreted. Cell surface {ECO:0000269|PubMed:22466966}. Note=The cell surface component is about 60 kDa and can be released by mild heat treatment (PubMed:22466966).; SUBCELLULAR LOCATION: [Antigen 43 beta chain]: Cell outer membrane {ECO:0000305|PubMed:25341963}; Multi-pass membrane protein {ECO:0000305}. Note=May form a beta-barrel."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "flu yeeQ yzzX b2000 JW1982"
---

# flu

`protein.P39180`

## Static

- Type: `protein`
- Source: `UniProt:P39180`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: [Antigen 43]: Periplasm {ECO:0000250}.; SUBCELLULAR LOCATION: [Antigen 43 alpha chain]: Secreted. Cell surface {ECO:0000269|PubMed:22466966}. Note=The cell surface component is about 60 kDa and can be released by mild heat treatment (PubMed:22466966).; SUBCELLULAR LOCATION: [Antigen 43 beta chain]: Cell outer membrane {ECO:0000305|PubMed:25341963}; Multi-pass membrane protein {ECO:0000305}. Note=May form a beta-barrel.

## Enriched Summary

FUNCTION: Controls colony form variation and autoaggregation. May function as an adhesin. {ECO:0000269|PubMed:22466966}. agn43 encodes a 1,039 amino acid product with a 52 amino acid N-terminal signal sequence. The mature, peptidase-processed protein is then autocatalytically cleaved to yield two subunits . One is a 60 kDa α43 subunit found peripheral to the outer membrane , extending beyond O-side chains of smooth lipopolysaccharide . The other is a heat modifiable 53 kDa β43 integral membrane protein . Ag43 is an autotransporter as β43 forms an 18 stranded β-barrel through which α43 is translocated . The Ag43 α subunit forms a β-helix structure consisting of 20 rungs, each containing 3 β-strands and 3 turns, which stack in parallel . Both polypeptides are associated with the outer membrane in equal stoichiometry . Immunofluorescence studies of Ag43-producing E. coli showed that the protein is seen evenly distributed over the surface of the entire cell . Based on conserved features, Ag43 can be placed in a group of similar autotransporters that includes AIDA-I and TibA, an adhesin of enterotoxigenic E. coli . Ag43 expression is subject to phase variation with switching frequencies of 2.2 x 10(-3) for Ag43+ to -, and 1 x 10(-3) for Ag43- to + . agn43 expressing variants usually autoaggregate in liquid due to Ag43α- Ag43α interactions, but this is prevented by fimbriation...

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Controls colony form variation and autoaggregation. May function as an adhesin. {ECO:0000269|PubMed:22466966}.

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b2000|gene.b2000]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39180`
- `KEGG:ecj:JW1982;eco:b2000;ecoc:C3026_11280;`
- `GeneID:946540;`
- `GO:GO:0005576; GO:0009279; GO:0009986; GO:0042597`

## Notes

Antigen 43 (AG43) (Fluffing protein) [Cleaved into: Antigen 43 alpha chain; Antigen 43 beta chain]
