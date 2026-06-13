---
entity_id: "gene.b3755"
entity_type: "gene"
name: "yieP"
source_database: "NCBI RefSeq"
source_id: "gene-b3755"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3755"
  - "yieP"
---

# yieP

`gene.b3755`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3755`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yieP (gene.b3755) is a gene entity. It encodes yieP (protein.P31475). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YieP EcoCyc product frame: EG11733-MONOMER. Genomic coordinates: 3940635-3941327. EcoCyc protein note: The transcriptional factor YieP appears to regulate genes involved in cellular membrane synthesis or structure, stress responses , and tolerance to 3-HYDROXY-PROPIONATE (3-HP) . YieP appears to belong to the GntR family of transcription factors . The yieP gene and the amino acid residues of its protein are highly conserved among Enterobacteriaceae, particularly in the helix-turn-helix DNA-binding region . The predicted structure of YieP consists of nine alpha helices, seven of which are located in the C-terminus . The helix-turn-helix DNA-binding region is located at the N-terminus, and a signal recognition domain is at the C-terminus . YieP was confirmed as a TF through an integrated workflow comprised of computational prediction, knowledge-based classification, and experimental validation of candidate TFs at the genome scale . Compared to known global transcription factors (TFs), YieP exhibits some interesting regulatory features. First, it binds more frequently to intragenic regions in the genome and less to regions located within putative regulatory regions...

## Biological Role

Repressed by fnrS (gene.b4699), nac (protein.Q47005). Activated by yieP (protein.P31475).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31475|protein.P31475]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P31475|protein.P31475]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4699|gene.b4699]] `RegulonDB` `S` - regulator=FnrS; target=yieP; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yieP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012275,ECOCYC:EG11733,GeneID:948263`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3940635-3941327:-; feature_type=gene
