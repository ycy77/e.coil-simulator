---
entity_id: "gene.b2606"
entity_type: "gene"
name: "rplS"
source_database: "NCBI RefSeq"
source_id: "gene-b2606"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2606"
  - "rplS"
---

# rplS

`gene.b2606`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2606`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplS (gene.b2606) is a gene entity. It encodes rplS (protein.P0A7K6). Encoded protein function: FUNCTION: This protein is located at the 30S-50S ribosomal subunit interface and may play a role in the structure and function of the aminoacyl-tRNA binding site. {ECO:0000255|HAMAP-Rule:MF_00402}.; FUNCTION: In the 70S ribosome it has been modeled to make two contacts with the 16S rRNA of the 30S subunit forming part of bridges B6 and B8 (PubMed:12809609). In the 3.5 A resolved structures L14 and L19 interact and together make contact with the 16S rRNA (PubMed:16272117). The protein conformation is quite different between the 50S and 70S structures, which may be necessary for translocation (PubMed:16272117). {ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:16272117}. EcoCyc product frame: EG10880-MONOMER. Genomic coordinates: 2744183-2744530. EcoCyc protein note: The L19 protein is a component of the 50S subunit of the ribosome. Depending on the method used, L19 does or does not appear to be essential for viability. L19 can be crosslinked to 23S rRNA , mRNA , and ribosomal proteins S9 and L18 , L3 , L14 , L6 , and L25 . L19 has RNA chaperone-like activity in an in vitro trans splicing assay as well as protein chaperone activity . L19 is photoaffinity labeled by dyhydrorosaramyicin . L19 appears to be phosphorylated at residues Ser18 and Ser82...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7K6|protein.P0A7K6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rplS; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008574,ECOCYC:EG10880,GeneID:947096`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2744183-2744530:-; feature_type=gene
