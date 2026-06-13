---
entity_id: "gene.b3288"
entity_type: "gene"
name: "fmt"
source_database: "NCBI RefSeq"
source_id: "gene-b3288"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3288"
  - "fmt"
---

# fmt

`gene.b3288`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3288`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fmt (gene.b3288) is a gene entity. It encodes fmt (protein.P23882). Encoded protein function: FUNCTION: Attaches a formyl group to the free amino group of methionyl-tRNA(fMet). The formyl group appears to play a dual role in the initiator identity of N-formylmethionyl-tRNA by promoting its recognition by IF2 and preventing the misappropriation of this tRNA by the elongation apparatus. {ECO:0000255|HAMAP-Rule:MF_00182, ECO:0000269|PubMed:6989606, ECO:0000269|PubMed:8331078, ECO:0000269|PubMed:9843487}. EcoCyc product frame: EG11268-MONOMER. EcoCyc synonyms: ftm, yhdD. Genomic coordinates: 3434214-3435161. EcoCyc protein note: 10-formyltetrahydrofolate:L-methionyl-tRNAfMet N-formyltransferase (Fmt) attaches a formyl group to the free amino group of methionyl-tRNAfMet . There are two types of methionine-specific tRNAs in E. coli; the Initiation-tRNAmet is used in the initiation of translation, while Elongation-tRNAMet is used during peptide chain elongation. The timely formylation of the methionine-charged initiator tRNA that is catalyzed by Fmt is important in restricting the use of the methionylated initiator tRNA specifically for initiation, rather than chain elongation...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P23882|protein.P23882]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fmt; function=+

## External IDs

- `Dbxref:ASAP:ABE-0010781,ECOCYC:EG11268,GeneID:947779`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3434214-3435161:+; feature_type=gene
