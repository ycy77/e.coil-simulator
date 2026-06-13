---
entity_id: "gene.b4388"
entity_type: "gene"
name: "serB"
source_database: "NCBI RefSeq"
source_id: "gene-b4388"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4388"
  - "serB"
---

# serB

`gene.b4388`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4388`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

serB (gene.b4388) is a gene entity. It encodes serB (protein.P0AGB0). Encoded protein function: FUNCTION: Catalyzes the dephosphorylation of phosphoserine (P-Ser). Also catalyzes the hydrolysis of phosphothreonine (P-Thr). {ECO:0000269|PubMed:16990279}. EcoCyc product frame: PSERPHOSPHA-MONOMER. Genomic coordinates: 4624895-4625863. EcoCyc protein note: Phosphoserine phosphatase catalyzes the last step in serine biosynthesis. The enzyme belongs to the superfamily of haloacid dehalogenase (HAD)-like hydrolases . Enzymatic studies were originally performed using partially purified enzyme from E. coli strain W ; assays of the purified enzyme were performed as part of an investigation of the HAD superfamily of enzymes . serB is essential for growth on glycerol minimal medium; the growth defect can be rescued by addition of serine . GPH-MONOMER Gph, IMIDHISTID-CPLX HisB and PGAM2-MONOMER YtjC were identified as multicopy suppressors of the conditional ΔserB phenotype . Directed evolution experiments identified mutations that increased fitness and enzymatic activity of these suppressors . Review:

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGB0|protein.P0AGB0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=serB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0014393,ECOCYC:EG10945,GeneID:948913`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4624895-4625863:+; feature_type=gene
