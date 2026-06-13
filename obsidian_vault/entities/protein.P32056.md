---
entity_id: "protein.P32056"
entity_type: "protein"
name: "gmm"
source_database: "UniProt"
source_id: "P32056"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gmm nudD wcaH yefC b2051 JW5335"
---

# gmm

`protein.P32056`

## Static

- Type: `protein`
- Source: `UniProt:P32056`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Hydrolyzes both GDP-mannose and GDP-glucose (PubMed:10913267, PubMed:23481913, PubMed:7592609). Could participate in the regulation of cell wall biosynthesis by influencing the concentration of GDP-mannose or GDP-glucose in the cell. Might also be involved in the biosynthesis of the slime polysaccharide colanic acid (PubMed:10913267, PubMed:7592609). {ECO:0000269|PubMed:10913267, ECO:0000269|PubMed:23481913, ECO:0000269|PubMed:7592609}. GDP-mannose mannosyl hydrolase (GDPMH) is able to hydrolyze both GDP-mannose and GDP-glucose. Its biological role is as yet unknown, though it may participate in the regulation of cell wall biosynthesis by influencing the cell concentration of GDP-mannose or GDP-glucose . The enzyme was first identified as a member of the Nudix hydrolase family . However, unlike other Nudix hydrolases, GDPMH catalyzes the nucleophilic substitution at C1' rather than phosphorus and requires one divalent cation per active site to facilitate the departure of GMP . The divalent cation binding site, the general base catalyst, and other residues important for catalytic activity were identified by site-directed mutagenesis . Crystal structures of GDPMH have been solved, and a reaction mechanism with a four-stage catalytic cycle was suggested . Review:

## Biological Role

Component of GDP-mannose mannosyl hydrolase (complex.ecocyc.CPLX0-7712).

## Annotation

FUNCTION: Hydrolyzes both GDP-mannose and GDP-glucose (PubMed:10913267, PubMed:23481913, PubMed:7592609). Could participate in the regulation of cell wall biosynthesis by influencing the concentration of GDP-mannose or GDP-glucose in the cell. Might also be involved in the biosynthesis of the slime polysaccharide colanic acid (PubMed:10913267, PubMed:7592609). {ECO:0000269|PubMed:10913267, ECO:0000269|PubMed:23481913, ECO:0000269|PubMed:7592609}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7712|complex.ecocyc.CPLX0-7712]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2051|gene.b2051]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32056`
- `KEGG:ecj:JW5335;eco:b2051;ecoc:C3026_11545;`
- `GeneID:946559;`
- `GO:GO:0000287; GO:0008727; GO:0009103; GO:0030145; GO:0042802; GO:0042803; GO:0047917`
- `EC:3.6.1.-`

## Notes

GDP-mannose mannosyl hydrolase (GDPMH) (EC 3.6.1.-) (Colanic acid biosynthesis protein WcaH)
