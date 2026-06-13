---
entity_id: "gene.b3384"
entity_type: "gene"
name: "trpS"
source_database: "NCBI RefSeq"
source_id: "gene-b3384"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3384"
  - "trpS"
---

# trpS

`gene.b3384`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3384`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

trpS (gene.b3384) is a gene entity. It encodes trpS (protein.P00954). Encoded protein function: FUNCTION: Catalyzes the attachment of tryptophan to tRNA(Trp). Amino acylates tRNA(Trp) with both L- and D-tryptophan, although D-tryptophan is a poor substrate (PubMed:10918062). {ECO:0000255|HAMAP-Rule:MF_00140, ECO:0000269|PubMed:10918062}. EcoCyc product frame: TRPS-MONOMER. Genomic coordinates: 3512634-3513638. EcoCyc protein note: Tryptophan-tRNA ligase (TrpRS) is a member of the family of aminoacyl-tRNA synthetases, which interpret the genetic code by covalently linking amino acids to their specific tRNA molecules. The reaction is driven by ATP hydrolysis. TrpRS belongs to the Class I aminoacyl tRNA synthetases . The enzyme purified from E. coli B is a homodimer in solution . The dimer has two binding sites for both tryptophan and tRNATrp . Specificity determinants within tRNATrp that are important for recognition by TrpRS have been identified. The anticodon and the G73 discriminator base are the major identity determinants , and C35 is recognized as well . The apparent affinity of TrpRS for tryptophan appears to be dependent on the tRNA . The identity of tRNATrp predominantly affects the rate of transfer of tryptophan from the TrpRS-tryptophanyl adenylate to the tRNA . TrpRS also aminoacylates tRNATrp with D-tryptophan; the resulting D-Trp-tRNATrp can be hydrolyzed by EC-3.1...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00954|protein.P00954]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=trpS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011056,ECOCYC:EG11030,GeneID:947894`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3512634-3513638:-; feature_type=gene
