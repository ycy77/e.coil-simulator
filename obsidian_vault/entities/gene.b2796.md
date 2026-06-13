---
entity_id: "gene.b2796"
entity_type: "gene"
name: "sdaC"
source_database: "NCBI RefSeq"
source_id: "gene-b2796"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2796"
  - "sdaC"
---

# sdaC

`gene.b2796`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2796`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sdaC (gene.b2796) is a gene entity. It encodes sdaC (protein.P0AAD6). Encoded protein function: FUNCTION: Mediates the import of L-serine into the cell (PubMed:3129404, PubMed:8026499). Is energized by proton cotransport (PubMed:3129404). Promotes amino acid homeostasis during adaptation to glucose limitation (PubMed:31680488). May also be involved in ampicillin sensitivity (Probable). {ECO:0000269|PubMed:3129404, ECO:0000269|PubMed:31680488, ECO:0000269|PubMed:8026499, ECO:0000305|PubMed:8752353}.; FUNCTION: (Microbial infection) Involved in phage C1 and phage C6 infection (PubMed:12558182, PubMed:8752353). Participates in phage DNA transport pathways in cooperation with different outer membrane receptors, including FhuA and BtuB (PubMed:12558182). Is probably required in the second stage of phage adsorption, the DNA injection process. Participates in the formation or opening of diffusion channels through the outer membrane after phage adsorption (PubMed:12558182). {ECO:0000269|PubMed:12558182, ECO:0000269|PubMed:8752353}.; FUNCTION: (Microbial infection) May function as an inner membrane receptor of colicin V (ColV), a peptide antibiotic secreted by some members of the Enterobacteriaceae to kill closely related bacterial cells. {ECO:0000269|PubMed:15743941}. EcoCyc product frame: SDAC-MONOMER. EcoCyc synonyms: dcrA. Genomic coordinates: 2928229-2929518...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAD6|protein.P0AAD6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=sdaC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009169,ECOCYC:EG12142,GeneID:947264`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2928229-2929518:+; feature_type=gene
