---
entity_id: "gene.b4203"
entity_type: "gene"
name: "rplI"
source_database: "NCBI RefSeq"
source_id: "gene-b4203"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4203"
  - "rplI"
---

# rplI

`gene.b4203`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4203`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplI (gene.b4203) is a gene entity. It encodes rplI (protein.P0A7R1). Encoded protein function: FUNCTION: One of the primary rRNA binding proteins, it binds very close to the 3' end of the 23S rRNA (PubMed:3298242). {ECO:0000269|PubMed:3298242}. EcoCyc product frame: EG10870-MONOMER. Genomic coordinates: 4426108-4426557. EcoCyc protein note: The L9 protein is a component of the 50S subunit of the ribosome. L9 is universally conserved in eubacteria, but not in other domains of life; surprisingly, it is not essential. L9 appears to be involved in maintenance of the reading frame during translational pauses . A model for the physiological function of L9 has been proposed . L9 is part of the first reconstitution intermediate of the 50S subunit . L9 can be crosslinked to L2 and L28 and is exposed on the ribosome surface . A solution structure determined by cryo-EM showed that the L9 protein consists of N-terminal and C-terminal domains connected by a long α helical domain that is wrapped around the L1 stalk . An atomic model of L9 within the ribosome was obtained in a cryo-EM structure, revealing contacts with the 30S subunit . The binding region of L9 on domain V of 23S rRNA was mapped . The N- and C-terminal domains of L9 interact with two separate sites in domain V of 23S rRNA . Crosslinking of tRNA in the A site of the ribosome to L9 depends on the state of the tRNA...

## Biological Role

Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7R1|protein.P0A7R1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rplI; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013746,ECOCYC:EG10870,GeneID:948720`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4426108-4426557:+; feature_type=gene
