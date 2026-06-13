---
entity_id: "gene.b3319"
entity_type: "gene"
name: "rplD"
source_database: "NCBI RefSeq"
source_id: "gene-b3319"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3319"
  - "rplD"
---

# rplD

`gene.b3319`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3319`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplD (gene.b3319) is a gene entity. It encodes rplD (protein.P60723). Encoded protein function: FUNCTION: One of the primary rRNA binding proteins, this protein initially binds near the 5'-end of the 23S rRNA (PubMed:3298242). It is important during the early stages of 50S assembly (PubMed:3298242). It makes multiple contacts with different domains of the 23S rRNA in the assembled 50S subunit and ribosome (PubMed:6170935, PubMed:7556101). {ECO:0000269|PubMed:13130133, ECO:0000269|PubMed:2442760, ECO:0000269|PubMed:3298242, ECO:0000269|PubMed:6170935, ECO:0000269|PubMed:7556101}.; FUNCTION: Protein uL4 is a both a transcriptional repressor and a translational repressor protein; these two functions are independent of each other. It regulates transcription of the S10 operon (to which uL4 belongs) by causing premature termination of transcription within the S10 leader; termination absolutely requires the NusA protein. uL4 controls the translation of the S10 operon by binding to its mRNA. The regions of uL4 that control regulation (residues 131-210) are different from those required for ribosome assembly (residues 89-103). {ECO:0000269|PubMed:13130133, ECO:0000269|PubMed:1692593, ECO:0000269|PubMed:2157208, ECO:0000269|PubMed:2442760}.; FUNCTION: Forms part of the polypeptide exit tunnel...

## Biological Role

Repressed by fliX (gene.b4827). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P60723|protein.P60723]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rplD; function=+
- `represses` <-- [[gene.b4827|gene.b4827]] `RegulonDB` `S` - regulator=FliX; target=rplD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010858,ECOCYC:EG10867,GeneID:947818`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3451681-3452286:-; feature_type=gene
