---
entity_id: "gene.b3298"
entity_type: "gene"
name: "rpsM"
source_database: "NCBI RefSeq"
source_id: "gene-b3298"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3298"
  - "rpsM"
---

# rpsM

`gene.b3298`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3298`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsM (gene.b3298) is a gene entity. It encodes rpsM (protein.P0A7S9). Encoded protein function: FUNCTION: Located at the top of the head of the 30S subunit, it contacts several helices of the 16S rRNA. {ECO:0000269|PubMed:15308780}.; FUNCTION: In the E.coli 70S ribosome in the initiation state (PubMed:12809609) was modeled to contact the 23S rRNA (bridge B1a) and protein L5 of the 50S subunit (bridge B1b), connecting the 2 subunits; bridge B1a is broken in the model with bound EF-G, while the protein-protein contacts between S13 and L5 in B1b change (PubMed:12809609). The 23S rRNA contact site in bridge B1a is modeled to differ in different ribosomal states (PubMed:16272117), contacting alternately S13 or S19. In the two 3.5 angstroms resolved ribosome structures (PubMed:12859903) the contacts between L5, S13 and S19 bridge B1b are different, confirming the dynamic nature of this interaction. Bridge B1a is not visible in the crystallized ribosomes due to 23S rRNA disorder. {ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:12859903, ECO:0000269|PubMed:15308780, ECO:0000269|PubMed:16272117}.; FUNCTION: Contacts the tRNAs in the A and P sites. {ECO:0000269|PubMed:15308780}.; FUNCTION: The C-terminal tail plays a role in the affinity of the 30S P site for different tRNAs. {ECO:0000269|PubMed:15308780}. EcoCyc product frame: EG10912-MONOMER. Genomic coordinates: 3442115-3442471...

## Biological Role

Repressed by rpsD (protein.P0A7V8). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7S9|protein.P0A7S9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=rpsM; function=+
- `represses` <-- [[protein.P0A7V8|protein.P0A7V8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## External IDs

- `Dbxref:ASAP:ABE-0010809,ECOCYC:EG10912,GeneID:947791`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3442115-3442471:-; feature_type=gene
