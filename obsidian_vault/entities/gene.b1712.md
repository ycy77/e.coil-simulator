---
entity_id: "gene.b1712"
entity_type: "gene"
name: "ihfA"
source_database: "NCBI RefSeq"
source_id: "gene-b1712"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1712"
  - "ihfA"
---

# ihfA

`gene.b1712`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1712`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ihfA (gene.b1712) is a gene entity. It encodes ihfA (protein.P0A6X7). Encoded protein function: FUNCTION: One of the 2 subunits of integration host factor (IHF), a specific DNA-binding protein that functions in genetic recombination as well as in transcriptional and translational control. Binds to hundreds of transcriptionally inactive, AT-rich DNA sites, approximately half its binding sites are in non-coding DNA, which only accounts for about 10% of the genome (PubMed:16963779). IHF in combination with the datA locus promotes ATP hydrolysis of ATP-DnaA, called DDAH (datA-dependent DnaA-ATP hydrolysis) (PubMed:23277577). IHF binds oriC as replication initiates, dissociates within minutes and slowly reassociates during the cell cyle; IHF binding to datA is low before initiation, rises after initiation and dissociates during the cell cycle, allowing IHF to coordinate replication initiation (PubMed:23277577). {ECO:0000269|PubMed:16963779, ECO:0000269|PubMed:23277577}.; FUNCTION: Plays a crucial role in the lysogenic life cycle of bacteriophage lambda, as it is required not only in the recombination reaction, which inserts lambda DNA into the E.coli chromosome, but also for the synthesis of int and cI repressor, two phage proteins necessary for DNA insertion and repression, respectively...

## Biological Role

Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6X7|protein.P0A6X7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ihfA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005715,ECOCYC:EG10440,GeneID:945472`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1795253-1795552:-; feature_type=gene
