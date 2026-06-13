---
entity_id: "gene.b0232"
entity_type: "gene"
name: "yafN"
source_database: "NCBI RefSeq"
source_id: "gene-b0232"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0232"
  - "yafN"
---

# yafN

`gene.b0232`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0232`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yafN (gene.b0232) is a gene entity. It encodes yafN (protein.Q47156). Encoded protein function: FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Functions as an mRNA interferase antitoxin; overexpression prevents YafO-mediated cessation of cell growth and inhibition of cell proliferation. {ECO:0000269|PubMed:19617347, ECO:0000269|PubMed:19943910}. EcoCyc product frame: G6116-MONOMER. Genomic coordinates: 252005-252298. EcoCyc protein note: YafN is the antitoxin for the ribosome-associated mRNA interferase toxin YafO . yafN is essential when yafO is present. The yafN mutant strain of the Keio collection, JW0222 , also contains a frameshift mutation in yafO, thus making it viable . Expression of yafN is increased by UV irradiation ; the dinB promoter is SOS-regulated . The promoter upstream of yafN appears to be autorepressed by YafN; Lon protease is required for activation of transcription. Transcription is induced by chloramphenicol treatment, amino acid starvation induced by serine hydroxamate, and glucose starvation . Polar dinB mutations affecting the dinB-yafNOP operon reduce spontaneous mutagenesis ; however, only DinB is required for stress-induced mutagenesis...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.Q47156|protein.Q47156]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yafN; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000793,ECOCYC:G6116,GeneID:944920`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:252005-252298:+; feature_type=gene
