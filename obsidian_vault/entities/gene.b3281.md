---
entity_id: "gene.b3281"
entity_type: "gene"
name: "aroE"
source_database: "NCBI RefSeq"
source_id: "gene-b3281"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3281"
  - "aroE"
---

# aroE

`gene.b3281`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3281`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aroE (gene.b3281) is a gene entity. It encodes aroE (protein.P15770). Encoded protein function: FUNCTION: Involved in the biosynthesis of the chorismate, which leads to the biosynthesis of aromatic amino acids. Catalyzes the reversible NADPH linked reduction of 3-dehydroshikimate (DHSA) to yield shikimate (SA). It displays no activity in the presence of NAD. {ECO:0000255|HAMAP-Rule:MF_00222, ECO:0000269|PubMed:12637497, ECO:0000269|PubMed:3883995}. EcoCyc product frame: AROE-MONOMER. Genomic coordinates: 3430020-3430838. EcoCyc protein note: Shikimate dehydrogenase (AroE) catalyzes the NADPH-linked reduction of 3-dehydroshikimate to shikimate . The reaction is part of the ARO-PWY pathway, which provides the common precursor for the biosynthesis of aromatic amino acids, folate, quinones and enterochelin. Phylogenomic analysis of the shikimate dehydrogenase family showed that the two enzymes encoded in E. coli, AroE and CPLX0-7462 YdiB, belong to different subclasses; the authors suggested that YdiB was acquired by horizontal gene transfer. Common and subclass-specific catalytic residues and substrate binding motifs were identified . AroE is NADP+-specific and has much higher catalytic efficiency than YdiB, which has broader substrate specificity and can use either NADP+ or NAD+ as a co-substrate...

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15770|protein.P15770]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=aroE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010763,ECOCYC:EG10077,GeneID:947776`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3430020-3430838:-; feature_type=gene
