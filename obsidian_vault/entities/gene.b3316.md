---
entity_id: "gene.b3316"
entity_type: "gene"
name: "rpsS"
source_database: "NCBI RefSeq"
source_id: "gene-b3316"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3316"
  - "rpsS"
---

# rpsS

`gene.b3316`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3316`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsS (gene.b3316) is a gene entity. It encodes rpsS (protein.P0A7U3). Encoded protein function: FUNCTION: In the E.coli 70S ribosome in the initiation state (PubMed:12809609) it has been modeled to contact the 23S rRNA of the 50S subunit forming part of bridge B1a; this bridge is broken in the model with bound EF-G. The 23S rRNA contact site in bridge B1a is modeled to differ in different ribosomal states (PubMed:12859903), contacting alternately S13 or S19. In the 3.5 angstroms resolved ribosome structures (PubMed:16272117) the contacts between L5, S13 and S19 bridge B1b are different, confirming the dynamic nature of this interaction. Bridge B1a is not visible in the crystallized ribosomes due to 23S rRNA disorder. {ECO:0000269|PubMed:12809609, ECO:0000269|PubMed:12859903, ECO:0000269|PubMed:16272117}.; FUNCTION: Protein S19 forms a complex with S13 that binds strongly to the 16S ribosomal RNA. Contacts the A site tRNA. EcoCyc product frame: EG10918-MONOMER. Genomic coordinates: 3450248-3450526. EcoCyc protein note: The S19 protein is a component of the 30S subunit of the ribosome. S19 interacts with 16S rRNA . S13 forms a complex with S19 in order to bind to 16S rRNA at its specific site . Binding of S19 to 16S rRNA is necessary and sufficient for converting 16S rRNA into a substrate for EG10343-MONOMER, while it abolishes activity of EG12163-MONOMER...

## Biological Role

Repressed by fliX (gene.b4827). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7U3|protein.P0A7U3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=rpsS; function=+
- `represses` <-- [[gene.b4827|gene.b4827]] `RegulonDB` `S` - regulator=FliX; target=rpsS; function=-

## External IDs

- `Dbxref:ASAP:ABE-0010852,ECOCYC:EG10918,GeneID:947811`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3450248-3450526:-; feature_type=gene
