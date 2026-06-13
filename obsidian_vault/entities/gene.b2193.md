---
entity_id: "gene.b2193"
entity_type: "gene"
name: "narP"
source_database: "NCBI RefSeq"
source_id: "gene-b2193"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2193"
  - "narP"
---

# narP

`gene.b2193`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2193`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

narP (gene.b2193) is a gene entity. It encodes narP (protein.P31802). Encoded protein function: FUNCTION: This protein activates the expression of the nitrate reductase (narGHJI) and formate dehydrogenase-N (fdnGHI) operons and represses the transcription of the fumarate reductase (frdABCD) operon in response to a nitrate/nitrite induction signal transmitted by either the NarX or NarQ proteins. EcoCyc product frame: PHOSPHO-NARP. Genomic coordinates: 2290500-2291147. EcoCyc protein note: NarP, "nitrate/nitrite response regulator NarP," is a transcriptional dual regulator of many anaerobic electron transport and fermentation-related genes in the response to the availability of high concentrations of nitrate or nitrite . A microarray analysis suggests that NarP activates 14 operons and represses 37 operons . The response regulator NarP belongs to the LuxR/UhpA family and is part of the two-component system NarQ-NarP. There is intensive cross-regulation with the paralogous two-component system NarX-NarL . Each of the sensors, NarQ and NarX, phosphorylates both NarP and NarL, leading to the activation of both proteins. In the absence of nitrate and nitrite, NarX and NarQ stimulate the dephosphorylation of NarL-P and NarP-P . This reaction is specific, that is, NarP-P is only dephosphorylated by NarQ. The system discriminates between nitrate and nitrite...

## Biological Role

Repressed by rprA (gene.b4431), sdsN (gene.b4719). Activated by rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31802|protein.P31802]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=narP; function=+
- `represses` <-- [[gene.b4431|gene.b4431]] `RegulonDB` `S` - regulator=RprA; target=narP; function=-
- `represses` <-- [[gene.b4719|gene.b4719]] `RegulonDB` `S` - regulator=SdsN; target=narP; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007259,ECOCYC:EG11527,GeneID:949081`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2290500-2291147:+; feature_type=gene
