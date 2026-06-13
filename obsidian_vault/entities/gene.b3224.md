---
entity_id: "gene.b3224"
entity_type: "gene"
name: "nanT"
source_database: "NCBI RefSeq"
source_id: "gene-b3224"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3224"
  - "nanT"
---

# nanT

`gene.b3224`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3224`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nanT (gene.b3224) is a gene entity. It encodes nanT (protein.P41036). Encoded protein function: FUNCTION: Catalyzes the proton-dependent transport of sialic acid (PubMed:22167185, PubMed:23848303). Can transport the common sialic acid N-acetylneuraminic acid (Neu5Ac) and the related sialic acids N-glycolylneuraminic acid (Neu5Gc) and 3-keto-3-deoxy-D-glycero-D-galactonononic acid (KDN) (PubMed:23848303). Functions as a bidirectional transporter in vitro (PubMed:22167185). {ECO:0000269|PubMed:22167185, ECO:0000269|PubMed:23848303}. EcoCyc product frame: NANT-MONOMER. Genomic coordinates: 3371084-3372574. EcoCyc protein note: E. coli K-12 is able to use the common sialic acid, N-acetylneuramic acid, as a carbon source and possesses a transporter, NanT, with high specificity for this sugar acid . NanT recognizes the abundant β-anomer of N-acetylneuramic acid; expression of a periplasmic CPLX0-7658 supports the ability to use the less abundant α-anomer in vivo . Purified NanT, reconstituted into liposomes, mediates the uptake of labeled N-acetylneuraminate in vitro and transport is energised by the proton gradient alone . NanT facilitates both substrate counterflow and substrate exchange in vitro (see also ). NanT transports the related sialic acids, CPD-273 and CPD-21259 "3-deoxy-D-glycero-D-galactonononate" (KDN) and the anhydro-sialic acid CPD-23638...

## Biological Role

Repressed by spf (gene.b3864), fis (protein.P0A6R3), nanR (protein.P0A8W0), nac (protein.Q47005). Activated by crp (protein.P0ACJ8), nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P41036|protein.P41036]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=nanT; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=nanT; function=-+
- `represses` <-- [[gene.b3864|gene.b3864]] `RegulonDB` `S` - regulator=Spf; target=nanT; function=-
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=nanT; function=-
- `represses` <-- [[protein.P0A8W0|protein.P0A8W0]] `RegulonDB` `C` - regulator=NanR; target=nanT; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=nanT; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0010577,ECOCYC:G436,GeneID:947740`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3371084-3372574:-; feature_type=gene
