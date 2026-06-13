---
entity_id: "protein.P39377"
entity_type: "protein"
name: "iadA"
source_database: "UniProt"
source_id: "P39377"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:7876157}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "iadA yjiF b4328 JW4291"
---

# iadA

`protein.P39377`

## Static

- Type: `protein`
- Source: `UniProt:P39377`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:7876157}.

## Enriched Summary

FUNCTION: Catalyzes the hydrolytic cleavage of a subset of L-isoaspartyl (L-beta-aspartyl) dipeptides. Used to degrade proteins damaged by L-isoaspartyl residues formation. The best substrate for the enzyme reported thus far is iso-Asp-Leu. {ECO:0000269|PubMed:12718528, ECO:0000269|PubMed:15882050, ECO:0000269|PubMed:4880759, ECO:0000269|PubMed:7876157}.

## Biological Role

Component of isoaspartyl dipeptidase (complex.ecocyc.CPLX0-3021).

## Annotation

FUNCTION: Catalyzes the hydrolytic cleavage of a subset of L-isoaspartyl (L-beta-aspartyl) dipeptides. Used to degrade proteins damaged by L-isoaspartyl residues formation. The best substrate for the enzyme reported thus far is iso-Asp-Leu. {ECO:0000269|PubMed:12718528, ECO:0000269|PubMed:15882050, ECO:0000269|PubMed:4880759, ECO:0000269|PubMed:7876157}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3021|complex.ecocyc.CPLX0-3021]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## Incoming Edges (1)

- `encodes` <-- [[gene.b4328|gene.b4328]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P39377`
- `KEGG:ecj:JW4291;eco:b4328;ecoc:C3026_23395;`
- `GeneID:948853;`
- `GO:GO:0005737; GO:0005829; GO:0006508; GO:0008237; GO:0008270; GO:0008798; GO:0016810; GO:0042802`
- `EC:3.4.19.-`

## Notes

Isoaspartyl dipeptidase (EC 3.4.19.-)
