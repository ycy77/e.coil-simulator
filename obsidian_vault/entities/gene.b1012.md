---
entity_id: "gene.b1012"
entity_type: "gene"
name: "rutA"
source_database: "NCBI RefSeq"
source_id: "gene-b1012"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1012"
  - "rutA"
---

# rutA

`gene.b1012`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1012`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rutA (gene.b1012) is a gene entity. It encodes rutA (protein.P75898). Encoded protein function: FUNCTION: Catalyzes the pyrimidine ring opening between N-3 and C-4 by an unusual flavin hydroperoxide-catalyzed mechanism, adding oxygen atoms in the process to yield ureidoacrylate peracid, that immediately reacts with FMN forming ureidoacrylate and FMN-N(5)-oxide. The FMN-N(5)-oxide reacts spontaneously with NADH to produce FMN. Requires the flavin reductase RutF to regenerate FMN in vivo. RutF can be substituted by Fre in vitro. {ECO:0000269|PubMed:16540542, ECO:0000269|PubMed:20400551, ECO:0000269|PubMed:28661684}. EcoCyc product frame: G6523-MONOMER. EcoCyc synonyms: ycdM. Genomic coordinates: 1072863-1074011. EcoCyc protein note: E. coli K-12 contains a previously undescribed pathway for pyrimidine degradation. In the presence of the flavin reductases Fre or RutF, RutA catalyzes the first step in this pathway, the ring opening of uracil at the C4 carbonyl . The reaction was initially thought to produce ureidoacrylate peracid, which would convert to ureidoacrylate either enzymatically or spontaneously . It was later shown that the reaction involves formation of a CPD-22328 intermediate . More recently, used mechanistic and computational studies together with X-ray crystallography to show that flavin-N5-peroxide is the oxygen-transferring species...

## Biological Role

Repressed by rutR (protein.P0ACU2). Activated by arcA (protein.P0A9Q1), glnG (protein.P0AFB8).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75898|protein.P75898]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=rutA; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=rutA; function=+
- `represses` <-- [[protein.P0ACU2|protein.P0ACU2]] `RegulonDB` `C` - regulator=RutR; target=rutA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003416,ECOCYC:G6523,GeneID:945643`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1072863-1074011:-; feature_type=gene
