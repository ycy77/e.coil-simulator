---
entity_id: "gene.b0391"
entity_type: "gene"
name: "ppnP"
source_database: "NCBI RefSeq"
source_id: "gene-b0391"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0391"
  - "ppnP"
---

# ppnP

`gene.b0391`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0391`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ppnP (gene.b0391) is a gene entity. It encodes ppnP (protein.P0C037). Encoded protein function: FUNCTION: Catalyzes the phosphorolysis of diverse nucleosides, yielding D-ribose 1-phosphate and the respective free bases. Can use uridine, adenosine, guanosine, cytidine, thymidine, inosine and xanthosine as substrates. Also catalyzes the reverse reactions. Is not able to produce D-ribose 1-phosphate from D-ribose and phosphate. {ECO:0000269|PubMed:27941785}. EcoCyc product frame: EG12159-MONOMER. EcoCyc synonyms: yaiE. Genomic coordinates: 408177-408461.

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0C037|protein.P0C037]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0001360,ECOCYC:EG12159,GeneID:945048`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:408177-408461:+; feature_type=gene
