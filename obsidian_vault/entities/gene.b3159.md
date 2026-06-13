---
entity_id: "gene.b3159"
entity_type: "gene"
name: "ubiV"
source_database: "NCBI RefSeq"
source_id: "gene-b3159"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3159"
  - "ubiV"
---

# ubiV

`gene.b3159`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3159`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ubiV (gene.b3159) is a gene entity. It encodes ubiV (protein.P45475). Encoded protein function: FUNCTION: Component of the UbiUV hydroxylase, which is involved in the oxygen-independent ubiquinone (coenzyme Q) biosynthesis (PubMed:31289180, PubMed:37283518, PubMed:38507448). It catalyzes the three hydroxylation steps, using prephenate as the oxygen donor (PubMed:38507448). UbiUV ensures the production of ubiquinone under a range of O(2) levels, from anaerobiosis to microaerobiosis (PubMed:37283518). The UbiUV-dependent ubiquinone biosynthesis is essential for nitrate respiration and uracil biosynthesis under anaerobiosis (PubMed:37283518). When produced at sufficiently high level, UbiUV can also hydroxylate ubiquinone precursors under aerobic conditions (PubMed:37283518). It contributes, though modestly, to bacterial multiplication in the mouse gut (PubMed:37283518). {ECO:0000269|PubMed:31289180, ECO:0000269|PubMed:37283518, ECO:0000269|PubMed:38507448}. EcoCyc product frame: G7653-MONOMER. EcoCyc synonyms: yhbV. Genomic coordinates: 3302489-3303367. EcoCyc protein note: UbiV together with UbiU functions in the three hydroxylation reactions in the oxygen-independent pathway for ubiquinone biosynthesis . UbiV contains a 4Fe-4S iron-sulfur cluster; mutagenesis of the cysteine residues C39, C180, C193, and C197 identified them as the iron-chelating residues...

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45475|protein.P45475]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010382,ECOCYC:G7653,GeneID:949117`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3302489-3303367:+; feature_type=gene
