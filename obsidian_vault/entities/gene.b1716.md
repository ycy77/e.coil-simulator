---
entity_id: "gene.b1716"
entity_type: "gene"
name: "rplT"
source_database: "NCBI RefSeq"
source_id: "gene-b1716"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1716"
  - "rplT"
---

# rplT

`gene.b1716`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1716`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplT (gene.b1716) is a gene entity. It encodes rplT (protein.P0A7L3). Encoded protein function: FUNCTION: One of the primary rRNA binding proteins, it binds close to the 5'-end of the 23S rRNA. It is important during the early stages of 50S assembly. {ECO:0000269|PubMed:3298242}. EcoCyc product frame: EG10881-MONOMER. EcoCyc synonyms: pdzA. Genomic coordinates: 1799393-1799749. EcoCyc protein note: The L20 protein is a component of the 50S subunit of the ribosome and autoregulates its own expression and that of L35 at the posttranscriptional level. The N-terminal domain of L20 is required for ribosome assembly, and the C-terminal domain is required for its regulatory function . L20 binds to the 5' terminal third of 23S rRNA . The C-terminal domain of L20 interacts with both 23S rRNA (H40-41) and the translational regulatory region. Proper folding of the L20 binding sites within RNA is required for interaction with L20, and binding of L20 stabilizes their structure . L20 is required for early assembly of the 4.3c core particle, but is not required for function of the mature 50S ribosomal subunit . L20 can replace L24 for the initiation of assembly of the 50S subunit at permissive temperatures in an L24 mutant . L20 can be crosslinked to L13 and L21 . L20 might be required for maintaining the 50S subunit in the correct conformation for binding of aminoacyl-tRNAs...

## Biological Role

Repressed by rplT (protein.P0A7L3). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7L3|protein.P0A7L3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rplT; function=+
- `represses` <-- [[protein.P0A7L3|protein.P0A7L3]] `RegulonDB` `S` - regulator=RplT; target=rplT; function=-

## External IDs

- `Dbxref:ASAP:ABE-0005729,ECOCYC:EG10881,GeneID:945152`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1799393-1799749:-; feature_type=gene
