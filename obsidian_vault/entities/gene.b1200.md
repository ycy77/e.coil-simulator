---
entity_id: "gene.b1200"
entity_type: "gene"
name: "dhaK"
source_database: "NCBI RefSeq"
source_id: "gene-b1200"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1200"
  - "dhaK"
---

# dhaK

`gene.b1200`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1200`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dhaK (gene.b1200) is a gene entity. It encodes dhaK (protein.P76015). Encoded protein function: FUNCTION: Dihydroxyacetone binding subunit of the dihydroxyacetone kinase, which is responsible for the phosphoenolpyruvate (PEP)-dependent phosphorylation of dihydroxyacetone via a phosphoryl group transfer from DhaL-ATP (PubMed:11350937, PubMed:15476397). Binds covalently dihydroxyacetone in hemiaminal linkage (PubMed:15476397). DhaK also acts as corepressor of the transcription activator DhaR by binding to the sensor domain of DhaR (PubMed:24440518). In the presence of dihydroxyacetone, DhaL-ADP displaces DhaK and stimulates DhaR activity (PubMed:24440518). In the absence of dihydroxyacetone, DhaL-ADP is converted by the PTS to DhaL-ATP, which does not bind to DhaR (PubMed:24440518). {ECO:0000269|PubMed:11350937, ECO:0000269|PubMed:15476397, ECO:0000269|PubMed:24440518}. EcoCyc product frame: G6627-MONOMER. EcoCyc synonyms: ycgT, dhaK1. Genomic coordinates: 1249768-1250838. EcoCyc protein note: DhaK is similar to the N-terminal half of the ATP-dependent dihydroxyacetone kinase of Citrobacter freundii and eukaryotes . Crystal structures of apo-DhaK, DhaK in complex with dihydroxyacetone (DHA) as well as glyceraldehyde or DHA-phosphate , and the DhaK-DhaL complex have been solved...

## Biological Role

Repressed by lrp (protein.P0ACJ0), nac (protein.Q47005). Activated by ygfI (protein.P52044).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76015|protein.P76015]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P52044|protein.P52044]] `RegulonDB` `S` - regulator=SrsR; target=dhaK; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=dhaK; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0004029,ECOCYC:G6627,GeneID:945747`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1249768-1250838:-; feature_type=gene
