---
entity_id: "gene.b0911"
entity_type: "gene"
name: "rpsA"
source_database: "NCBI RefSeq"
source_id: "gene-b0911"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0911"
  - "rpsA"
---

# rpsA

`gene.b0911`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0911`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsA (gene.b0911) is a gene entity. It encodes rpsA (protein.P0AG67). Encoded protein function: FUNCTION: Required for translation of most natural mRNAs except for leaderless mRNA (PubMed:12068815, PubMed:17376482, PubMed:24339747, PubMed:7003157, PubMed:9677288). Binds mRNA upstream of the Shine-Dalgarno (SD) sequence and helps it bind to the 30S ribosomal subunit; acts as an RNA chaperone to unfold structured mRNA on the ribosome but is not essential for mRNAs with strong SDs and little 5'-UTR structure, thus it may help fine-tune which mRNAs that are translated (PubMed:24339747). Unwinds dsRNA by binding to transiently formed ssRNA regions; binds about 10 nucleotides (PubMed:22908248). Has a preference for polypyrimidine tracts (PubMed:778845). Negatively autoregulates its own translation (PubMed:2120211). {ECO:0000269|PubMed:12068815, ECO:0000269|PubMed:15340139, ECO:0000269|PubMed:1712292, ECO:0000269|PubMed:17376482, ECO:0000269|PubMed:2120211, ECO:0000269|PubMed:22908248, ECO:0000269|PubMed:24339747, ECO:0000269|PubMed:7003157, ECO:0000269|PubMed:778845, ECO:0000269|PubMed:9677288}.; FUNCTION: It is not clear if it plays a role in trans-translation (a process which rescues stalled ribosomes). Evidence for its role; binds to tmRNA with very high affinity, is required for binding of tmRNA to 30S subunit (PubMed:11101533, PubMed:15340139)...

## Biological Role

Repressed by rpsA (protein.P0AG67). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG67|protein.P0AG67]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rpsA; function=+
- `represses` <-- [[protein.P0AG67|protein.P0AG67]] `RegulonDB|EcoCyc` `S` - regulator=RpsA; target=rpsA; function=- | EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## External IDs

- `Dbxref:ECOCYC:EG10900,GeneID:945536`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:961995-963668:+; feature_type=gene
