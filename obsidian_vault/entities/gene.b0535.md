---
entity_id: "gene.b0535"
entity_type: "gene"
name: "fimZ"
source_database: "NCBI RefSeq"
source_id: "gene-b0535"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0535"
  - "fimZ"
---

# fimZ

`gene.b0535`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0535`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fimZ (gene.b0535) is a gene entity. It encodes fimZ (protein.P0AEL8). Encoded protein function: FUNCTION: Response regulator that has two active forms, I and II, which are involved in cell surface extension and regulation of pili biosynthesis (PubMed:36057789). The active form I is required for constant cell elongation, possibly by stimulating the ATP synthesis activity of F-type ATPases (PubMed:36057789). The active form II activates expression of the sfmACDHF operon, which is involved in fimbriae formation, by binding directly to the sfmA promoter (PubMed:36057789). {ECO:0000269|PubMed:36057789}. EcoCyc product frame: EG11103-MONOMER. EcoCyc synonyms: ybcA. Genomic coordinates: 563848-564480. EcoCyc protein note: FimZ is a positive DNA-binding transcriptional regulator that belongs to the LuxR/UhpA family of transcriptional regulators. FimZ's role as a regulator of fimbrial gene expression has been studied in Salmonella enterica; see e.g. . FimZ regulates pili biosynthesis and cell surface extension . FimZ has two active forms; active form I includes essential amino acid residues K106 and D109 to bind F-type ATPase, which induces constant cell elongation. The active form II requires the amino acid residue D56, a putative phosphorylation site, to activate the transcription of its targets...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEL8|protein.P0AEL8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001836,ECOCYC:EG11103,GeneID:947079`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:563848-564480:-; feature_type=gene
