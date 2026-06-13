---
entity_id: "gene.b2795"
entity_type: "gene"
name: "ppnN"
source_database: "NCBI RefSeq"
source_id: "gene-b2795"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2795"
  - "ppnN"
---

# ppnN

`gene.b2795`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2795`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ppnN (gene.b2795) is a gene entity. It encodes ppnN (protein.P0ADR8). Encoded protein function: FUNCTION: Catalyzes the hydrolysis of the N-glycosidic bond of diverse pyrimidine and purine nucleotide 5'-monophosphates, to form ribose 5-phosphate and the corresponding free base. Can use AMP, GMP, IMP, CMP, dTMP and UMP as substrates. Cannot catalyze the reverse reactions. Is required for optimal growth in glucose minimal medium, possibly because it contributes to nucleoside pool homeostasis by degrading excess nucleotides and feeding back the ribose moiety to catabolism. {ECO:0000269|PubMed:27941785}. EcoCyc product frame: EG12373-MONOMER. EcoCyc synonyms: ygdH. Genomic coordinates: 2926308-2927672.

## Biological Role

Repressed by nac (protein.Q47005).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADR8|protein.P0ADR8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=ppnN; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009166,ECOCYC:EG12373,GeneID:947266`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2926308-2927672:+; feature_type=gene
