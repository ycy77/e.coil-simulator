---
entity_id: "gene.b0912"
entity_type: "gene"
name: "ihfB"
source_database: "NCBI RefSeq"
source_id: "gene-b0912"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0912"
  - "ihfB"
---

# ihfB

`gene.b0912`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0912`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ihfB (gene.b0912) is a gene entity. It encodes ihfB (protein.P0A6Y1). Encoded protein function: FUNCTION: One of the 2 subunits of integration host factor (IHF), a specific DNA-binding protein that functions in genetic recombination as well as in transcriptional and translational control. IHF in combination with the datA locus promotes ATP hydrolysis of ATP-DnaA, called DDAH (datA-dependent DnaA-ATP hydrolysis) (PubMed:23277577). IHF binds oriC as replication initiates, dissociates within minutes and slowly reassociates during the cell cyle; IHF binding to datA is low before initiation, rises after initiation and dissociates during the cell cycle, allowing IHF to coordinate replication initiation (PubMed:23277577). {ECO:0000269|PubMed:23277577}.; FUNCTION: Plays a crucial role in the lysogenic life cycle of bacteriophage lambda, as it is required not only in the recombination reaction, which inserts lambda DNA into the E.coli chromosome, but also for the synthesis of int and cI repressor, two phage proteins necessary for DNA insertion and repression, respectively. The synthesis of int and cI proteins is regulated indirectly by IHF via translational control of the lambda cII protein.; FUNCTION: Has an essential role in conjugative DNA transfer (CDT), the unidirectional transfer of ssDNA plasmid from a donor to a recipient cell...

## Biological Role

Repressed by rseX (gene.b4603). Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6Y1|protein.P0A6Y1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ihfB; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ihfB; function=+
- `represses` <-- [[gene.b4603|gene.b4603]] `RegulonDB` `S` - regulator=RseX; target=ihfB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003107,ECOCYC:EG10441,GeneID:945533`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:963828-964112:+; feature_type=gene
