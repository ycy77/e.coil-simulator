---
entity_id: "gene.b4384"
entity_type: "gene"
name: "deoD"
source_database: "NCBI RefSeq"
source_id: "gene-b4384"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4384"
  - "deoD"
---

# deoD

`gene.b4384`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4384`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

deoD (gene.b4384) is a gene entity. It encodes deoD (protein.P0ABP8). Encoded protein function: FUNCTION: Catalyzes the reversible phosphorolytic breakdown of the N-glycosidic bond in the beta-(deoxy)ribonucleoside molecules, with the formation of the corresponding free purine bases and pentose-1-phosphate (PubMed:11786017, PubMed:21672603, PubMed:235429, PubMed:30337572). Acts on 6-amino and 6-oxopurines including deoxyinosine, deoxyguanosine, deoxyadenosine, adenosine, guanosine, and inosine (PubMed:11786017, PubMed:21672603, PubMed:235429, PubMed:30337572). Does not act on xanthosine (Probable). May also catalyze a phosphate-dependent transfer of the pentose moiety from one purine base to another (PubMed:235429). {ECO:0000269|PubMed:11786017, ECO:0000269|PubMed:21672603, ECO:0000269|PubMed:235429, ECO:0000269|PubMed:30337572, ECO:0000305|PubMed:235429}. EcoCyc product frame: DEOD-MONOMER. EcoCyc synonyms: pup. Genomic coordinates: 4620883-4621602.

## Biological Role

Repressed by modE (protein.P0A9G8), crp (protein.P0ACJ8), deoR (protein.P0ACK5), cytR (protein.P0ACN7). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABP8|protein.P0ABP8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=deoD; function=-+
- `represses` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=deoD; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `C` - regulator=CRP; target=deoD; function=-+
- `represses` <-- [[protein.P0ACK5|protein.P0ACK5]] `RegulonDB` `S` - regulator=DeoR; target=deoD; function=-
- `represses` <-- [[protein.P0ACN7|protein.P0ACN7]] `RegulonDB` `C` - regulator=CytR; target=deoD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014379,ECOCYC:EG10222,GeneID:945654`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4620883-4621602:+; feature_type=gene
