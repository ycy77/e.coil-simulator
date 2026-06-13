---
entity_id: "gene.b2188"
entity_type: "gene"
name: "lapC"
source_database: "NCBI RefSeq"
source_id: "gene-b2188"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2188"
  - "lapC"
---

# lapC

`gene.b2188`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2188`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lapC (gene.b2188) is a gene entity. It encodes pbgA (protein.P0AD27). Encoded protein function: FUNCTION: Essential for outer membrane integrity (PubMed:32788728). Ensures bacterial survival and proliferation by regulating lipopolysaccharide (LPS) assembly (By similarity). Regulates LPS biogenesis by directly sensing LPS levels in the periplasmic leaflet of the inner membrane and controlling the stability of lipid A biosynthesis protein LpxC (PubMed:32540932, PubMed:32788728). Inhibits FtsH-mediated proteolysis of LpxC by competing with FtsH for binding to FtsH adapter protein LapB, resulting in reduced degradation of LpxC (PubMed:32291302, PubMed:32430473, PubMed:32540932, PubMed:33260377, PubMed:35931690). Mediates PhoPQ-regulated outer membrane remodeling and bacterial survival within host tissues by binding to cardiolipin glycerophospholipids near the inner membrane and promoting their trafficking to the outer membrane (By similarity). Has been shown to have Mg(2+)-dependent phosphatase activity (By similarity). {ECO:0000250|UniProtKB:P40709, ECO:0000269|PubMed:32291302, ECO:0000269|PubMed:32430473, ECO:0000269|PubMed:32540932, ECO:0000269|PubMed:32788728, ECO:0000269|PubMed:33260377, ECO:0000269|PubMed:35931690}. EcoCyc product frame: EG12049-MONOMER. EcoCyc synonyms: yejN, pbgA, yejM. Genomic coordinates: 2284376-2286136...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AD27|protein.P0AD27]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=lapC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007240,ECOCYC:EG12049,GeneID:946685`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2284376-2286136:+; feature_type=gene
