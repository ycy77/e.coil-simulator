---
entity_id: "gene.b2266"
entity_type: "gene"
name: "elaB"
source_database: "NCBI RefSeq"
source_id: "gene-b2266"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2266"
  - "elaB"
---

# elaB

`gene.b2266`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2266`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

elaB (gene.b2266) is a gene entity. It encodes elaB (protein.P0AEH5). Encoded protein function: Protein ElaB EcoCyc product frame: G7173-MONOMER. EcoCyc synonyms: yfbD. Genomic coordinates: 2380722-2381027. EcoCyc protein note: ElaB is a C-tail anchored inner membrane protein that is implicated in various stress reponses; deletion of elaB reduces cell survival under heat and oxidative stress; deletion of elaB also increases persister cell formation . Overexpressed ElaB is present in the ribosome fraction . ElaB is predicted to be a bitopic inner membrane protein . An ElaB-YFP fusion protein localizes mainly at the cell poles; the tail anchor domain of ElaB localizes to regions enriched in phosphatidic acid . elaB is a member of the RpoS regulon; transcription is induced during stationary phase and when cells are grown in nutrient limited minimal medium . EG11447-MONOMER CsrA regulates elaB expression both transcriptionally and post-transcriptionally; CsrA mediates the direct translational repression of elaB during exponential growth . ElaB, G7612-MONOMER "YqjD" and B0899-MONOMER "YgaM" are paralogs ; ElaB, YqjD and YgaM contain similar C-terminal transmembrane domains ; E. coli K-12 contains 11 chromosomally encoded C-tail anchored proteins . ElaB, YqjD, and YgaM are ribosome associated factors implicated in stress-associated translation modulation (see )

## Biological Role

Repressed by oxyR (protein.P0ACQ4). Activated by oxyR (protein.P0ACQ4), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEH5|protein.P0AEH5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=elaB; function=-+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=elaB; function=+
- `represses` <-- [[protein.P0ACQ4|protein.P0ACQ4]] `RegulonDB` `C` - regulator=OxyR; target=elaB; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0007487,ECOCYC:G7173,GeneID:946751`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2380722-2381027:-; feature_type=gene
