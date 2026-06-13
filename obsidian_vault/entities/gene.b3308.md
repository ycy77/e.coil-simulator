---
entity_id: "gene.b3308"
entity_type: "gene"
name: "rplE"
source_database: "NCBI RefSeq"
source_id: "gene-b3308"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3308"
  - "rplE"
---

# rplE

`gene.b3308`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3308`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplE (gene.b3308) is a gene entity. It encodes rplE (protein.P62399). Encoded protein function: FUNCTION: This is one of the proteins that bind and probably mediate the attachment of the 5S RNA into the large ribosomal subunit, where it forms part of the central protuberance. Its 5S rRNA binding is significantly enhanced in the presence of L18. {ECO:0000269|PubMed:354687, ECO:0000269|PubMed:7038683, ECO:0000269|PubMed:8925931}.; FUNCTION: In the 70S ribosome in the initiation state (PubMed:12809609) was modeled to contact protein S13 of the 30S subunit (bridge B1b), connecting the 2 subunits; the protein-protein contacts between S13 and L5 in B1b change in the model with bound EF-G implicating this bridge in subunit movement (PubMed:12809609, PubMed:18723842). In the two 3.5 A resolved ribosome structures (PubMed:16272117) the contacts between L5, S13 and S19 are different, confirming the dynamic nature of this interaction. {ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:12859903, ECO:0000269|PubMed:16272117}.; FUNCTION: Contacts the P site tRNA; the 5S rRNA and some of its associated proteins might help stabilize positioning of ribosome-bound tRNAs. {ECO:0000269|PubMed:8524654}. EcoCyc product frame: EG10868-MONOMER. Genomic coordinates: 3446899-3447438. EcoCyc protein note: The L5 protein is a component of the 50S subunit of the ribosome...

## Biological Role

Repressed by rpsH (protein.P0A7W7).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P62399|protein.P62399]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A7W7|protein.P0A7W7]] `RegulonDB` `S` - regulator=RpsH; target=rplE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010833,ECOCYC:EG10868,GeneID:947800`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3446899-3447438:-; feature_type=gene
