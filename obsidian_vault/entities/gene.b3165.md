---
entity_id: "gene.b3165"
entity_type: "gene"
name: "rpsO"
source_database: "NCBI RefSeq"
source_id: "gene-b3165"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3165"
  - "rpsO"
---

# rpsO

`gene.b3165`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3165`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsO (gene.b3165) is a gene entity. It encodes rpsO (protein.P0ADZ4). Encoded protein function: FUNCTION: One of the primary rRNA binding proteins, it binds directly to 16S rRNA where it helps nucleate assembly of the platform of the 30S subunit by binding and bridging several RNA helices of the 16S rRNA (PubMed:12809609, PubMed:16272117). Binds to its own mRNA, stabilizing it 5-UTR and preventing its translation (PubMed:24339747). {ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:16272117, ECO:0000269|PubMed:24339747}.; FUNCTION: In the E.coli 70S ribosome it has been modeled (PubMed:12809609) to contact the 23S rRNA of the 50S subunit forming part of bridge B4. In the two 3.5 A resolved ribosome structures (PubMed:16272117) there are minor differences between side-chain conformations. {ECO:0000269|PubMed:12244297, ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:16272117}. EcoCyc product frame: EG10914-MONOMER. EcoCyc synonyms: secC. Genomic coordinates: 3311415-3311684. EcoCyc protein note: The S15 protein is a component of the 30S subunit of the ribosome and also functions in the post-transcriptional regulation of its own expression. The S15 protein binds to 16S rRNA in the absence of other ribosomal proteins . Nucleotides essential for the S15-16S rRNA interaction have been determined by mutagenesis and nuclease protection . S15 appears to depend on S4 for assembly...

## Biological Role

Repressed by argR (protein.P0A6D0), crp (protein.P0ACJ8), rpsO (protein.P0ADZ4). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADZ4|protein.P0ADZ4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rpsO; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=rpsO; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=rpsO; function=-
- `represses` <-- [[protein.P0ADZ4|protein.P0ADZ4]] `RegulonDB` `C` - regulator=RpsO; target=rpsO; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010401,ECOCYC:EG10914,GeneID:947686`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3311415-3311684:-; feature_type=gene
