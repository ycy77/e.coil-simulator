---
entity_id: "gene.b3294"
entity_type: "gene"
name: "rplQ"
source_database: "NCBI RefSeq"
source_id: "gene-b3294"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3294"
  - "rplQ"
---

# rplQ

`gene.b3294`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3294`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rplQ (gene.b3294) is a gene entity. It encodes rplQ (protein.P0AG44). Encoded protein function: FUNCTION: Requires L15 for assembly into the 50S subunit. {ECO:0000269|PubMed:3298242}. EcoCyc product frame: EG10878-MONOMER. Genomic coordinates: 3439616-3439999. EcoCyc protein note: The L17 protein is a component of the 50S subunit of the ribosome. L17 interacts directly with tRNA and can be crosslinked to 23S rRNA . L17 can also be crosslinked to the spiramycin derivative dihydrospiramycin and may thus be located near the peptidyl transferase center .

## Biological Role

Repressed by rpsD (protein.P0A7V8). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG44|protein.P0AG44]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=rplQ; function=+
- `represses` <-- [[protein.P0A7V8|protein.P0A7V8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## External IDs

- `Dbxref:ASAP:ABE-0010799,ECOCYC:EG10878,GeneID:947784`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3439616-3439999:-; feature_type=gene
