---
entity_id: "gene.b0388"
entity_type: "gene"
name: "aroL"
source_database: "NCBI RefSeq"
source_id: "gene-b0388"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0388"
  - "aroL"
---

# aroL

`gene.b0388`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0388`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aroL (gene.b0388) is a gene entity. It encodes aroL (protein.P0A6E1). Encoded protein function: FUNCTION: Catalyzes the specific phosphorylation of the 3-hydroxyl group of shikimic acid using ATP as a cosubstrate. {ECO:0000269|PubMed:3001029, ECO:0000269|PubMed:3026317}. EcoCyc product frame: AROL-MONOMER. Genomic coordinates: 406405-406929. EcoCyc protein note: Shikimate kinase is involved in the fifth step of the chorismate pathway, which leads to the biosynthesis of aromatic amino acids. Shikimate kinase catalyzes the formation of shikimate 3-phosphate from shikimate and ATP. There are two shikimate kinase enzymes, I (AroK) and II (AroL). The isoenzymes are separable and presumably monofunctional . The amino acid sequences of shikimate kinase I and II shows 30% homology over the entire length of both proteins . Shikimate kinase I is encoded by aroK and shikimate kinase II is encoded by aroL. The expression of aroK unlike that of aroL, which is controlled by the TyrR and TrpR repressors, appears to be constitutive . Expression of aroL is regulated by the tyrR gene product protein with tyrosine or tryptophan as a co-repressor . Shikimate kinase I has a much lower affinity (approximately 100-fold) for shikimate than shikimate kinase II. Shikimate II seems to be the dominant enzyme of the pathway with shikimate I playing a secondary role...

## Biological Role

Repressed by tyrR (protein.P07604), trpR (protein.P0A881). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6E1|protein.P0A6E1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=aroL; function=+
- `represses` <-- [[protein.P07604|protein.P07604]] `RegulonDB` `C` - regulator=TyrR; target=aroL; function=-
- `represses` <-- [[protein.P0A881|protein.P0A881]] `RegulonDB` `C` - regulator=TrpR; target=aroL; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001353,ECOCYC:EG10082,GeneID:945031`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:406405-406929:+; feature_type=gene
