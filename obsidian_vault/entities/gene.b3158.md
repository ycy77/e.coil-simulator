---
entity_id: "gene.b3158"
entity_type: "gene"
name: "ubiU"
source_database: "NCBI RefSeq"
source_id: "gene-b3158"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3158"
  - "ubiU"
---

# ubiU

`gene.b3158`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3158`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ubiU (gene.b3158) is a gene entity. It encodes ubiU (protein.P45527). Encoded protein function: FUNCTION: Component of the UbiUV hydroxylase, which is involved in the oxygen-independent ubiquinone (coenzyme Q) biosynthesis (PubMed:31289180, PubMed:37283518, PubMed:38507448). It catalyzes the three hydroxylation steps, using prephenate as the oxygen donor (PubMed:38507448). UbiUV ensures the production of ubiquinone under a range of O(2) levels, from anaerobiosis to microaerobiosis (PubMed:37283518). The UbiUV-dependent ubiquinone biosynthesis is essential for nitrate respiration and uracil biosynthesis under anaerobiosis (PubMed:37283518). When produced at sufficiently high level, UbiUV can also hydroxylate ubiquinone precursors under aerobic conditions (PubMed:37283518). It contributes, though modestly, to bacterial multiplication in the mouse gut (PubMed:37283518). {ECO:0000269|PubMed:31289180, ECO:0000269|PubMed:37283518, ECO:0000269|PubMed:38507448}. EcoCyc product frame: G7652-MONOMER. EcoCyc synonyms: yhbU. Genomic coordinates: 3301485-3302480. EcoCyc protein note: UbiU together with UbiV functions in the three hydroxylation reactions in the oxygen-independent pathway for ubiquinone biosynthesis . UbiU contains a 4Fe-4S iron-sulfur cluster; mutagenesis of the cysteine residues C169, C176, C193, and C232 identified them as the iron-chelating residues...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P45527|protein.P45527]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ubiU; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010380,ECOCYC:G7652,GeneID:949115`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3301485-3302480:+; feature_type=gene
