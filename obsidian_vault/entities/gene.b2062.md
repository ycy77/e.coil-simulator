---
entity_id: "gene.b2062"
entity_type: "gene"
name: "wza"
source_database: "NCBI RefSeq"
source_id: "gene-b2062"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2062"
  - "wza"
---

# wza

`gene.b2062`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2062`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

wza (gene.b2062) is a gene entity. It encodes wza (protein.P0A930). Encoded protein function: FUNCTION: Probably involved in the export of the extracellular polysaccharide colanic acid from the cell to medium. EcoCyc product frame: G7107-MONOMER. Genomic coordinates: 2136104-2137243. EcoCyc protein note: wza is located within a cluster of genes that are responsible for production of the extracellular polysaccharide, CPD-21504 "colanic acid" (CA) and based on sequence similarity it may be involved in a CA export system . Wza is a member of the outer membrane auxiliary (OMA) protein family . Much of the information known about Wza comes from experiments characterizing Wza from the group 1 capsule producing strain Escherichia coli serotype K30 (WzaK30); wza from E. coli K-12 can complement a wza defect in E. coli K30 . The Δwza mutant of an EG10820 overexpressing, CA producing strain of E. coli K-12 MG1655 grows as misshapen rods and spheres . WzaK30 is a surface exposed outer membrane lipoprotein that forms a multimeric 'secretin-like' structure . Insertional inactivation of wza in E. coli strain E69 serotype O9a:K30 results in loss of the K30 capsular layer although K30 polysaccharide is still produced . WzaK30 forms ring-like octameric structures arranged as tetramers of dimers...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), rpoE (protein.P0AGB6).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A930|protein.P0A930]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=wza; function=+
- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=wza; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=wza; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006825,ECOCYC:G7107,GeneID:946558`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2136104-2137243:-; feature_type=gene
